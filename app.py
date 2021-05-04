import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from datetime import date
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


now = date.today()
membersince = now.strftime("%d %B, %Y")



@app.route("/")
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        # check if the email is already registered in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("That e-mail address is already in use!", "registeremailerror")
            return redirect(url_for("register"))

        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Passwords do not match!", "registerpassworderror")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password1")),
            "membersince": membersince
        }
        mongo.db.users.insert_one(register)

        # put user in session cookie and go to activity page
        session["user"] = request.form.get("email").lower()
        return redirect(url_for("show_map"))
    return render_template("register.html", isRegister=True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        
        if existing_user:
            # check password
            if check_password_hash(
                existing_user["password"], request.form.get("password1")):
                    session["user"] = request.form.get("email").lower()
                    return redirect(url_for("show_map"))
            else:
                # invalid password
                flash("The password is not correct!", "loginpassworderror")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("This e-mail address has not been registered yet!", "loginemailerror")
            return redirect(url_for("login"))

    return render_template("login.html", isLogin=True)


@app.route("/map")
def show_map():
    return render_template("map.html")


@app.route("/get_runs")
def get_runs():
    runs = mongo.db.runs.find()
    return render_template("upcomingruns.html", runs=runs, isRuns=True)


@app.route("/add_run")
def add_run():
    runs = mongo.db.runs.find()
    run_types = mongo.db.run_types.find().sort("run_type", 1)
    levels = mongo.db.levels.find()
    return render_template("addrun.html", runs=runs, run_types=run_types, levels=levels, isAddRun=True)


@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    # get the session user by registered email address
    email = mongo.db.users.find_one(
        {"email": session["user"]})["email"]

    return render_template("profile.html", 
                            email=email,
                            isProfile=True)


@app.route("/logout")
def logout():
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)