import os
import datetime
import time
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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


timestamp = datetime.datetime.now()
createdon = timestamp.strftime("%d/%m/%Y, %H:%M:%S")
createdondate = timestamp.strftime("%d/%m/%Y")



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
            "membersince": createdondate,
            "profilecomplete": False
        }
        mongo.db.users.insert_one(register)

        # put user in session cookie and go to complete profile page
        session["user"] = request.form.get("email").lower()
        flash("Please fill out the form below so we can provide you with an optimal application experience.", "completeprofilemessage")
        return redirect(url_for("edit_profile", user=session["user"]))
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
    return render_template("map.html", isMap=True)


@app.route("/get_runs")
def get_runs():
    runs = mongo.db.runs.find().sort("formdate", 1)
    return render_template("upcomingruns.html", runs=runs, isRuns=True)


@app.route("/add_run", methods=["GET", "POST"])
def add_run():
    if request.method == "POST":
        crewrun = "on" if request.form.get("crewrun") else "off"
        samegender = "on" if request.form.get("samegender") else "off"
        formdate = request.form.get("date")
        date = datetime.datetime.strptime(formdate, "%Y-%m-%d").strftime("%d/%m/%Y")
        run = {
            "runtype": request.form.get("runtype"),
            "level": request.form.get("level"),
            "date": date,
            "formdate": formdate,
            "time": request.form.get("time"),
            "location": request.form.get("location"),
            "city": request.form.get("city"),
            "distance": request.form.get("distance"),
            "crewrun": crewrun,
            "samegender": samegender,
            "createdby": session["user"],  
            "createdon": createdon
        }
        mongo.db.runs.insert_one(run)
        return redirect(url_for("get_runs"))

    runs = mongo.db.runs.find().sort("formdate", 1)
    runtypes = mongo.db.runtypes.find().sort("runtype", 1)
    levels = mongo.db.levels.find().sort("level", 1)
    return render_template("addrun.html", runs=runs, runtypes=runtypes, levels=levels, isAddRun=True)


@app.route("/edit_run/<run_id>", methods=["GET", "POST"])
def edit_run(run_id):
    if request.method == "POST":
        crewrun = "on" if request.form.get("crewrun") else "off"
        samegender = "on" if request.form.get("samegender") else "off"
        formdate = request.form.get("date")
        date = datetime.datetime.strptime(formdate, "%Y-%m-%d").strftime("%d/%m/%Y")
        submit = {
            "runtype": request.form.get("runtype"),
            "level": request.form.get("level"),
            "date": date,
            "formdate": formdate,
            "time": request.form.get("time"),
            "location": request.form.get("location"),
            "city": request.form.get("city"),
            "distance": request.form.get("distance"),
            "crewrun": crewrun,
            "samegender": samegender,
            "createdby": session["user"],  
            "createdon": createdon
        }
        mongo.db.runs.update({"_id": ObjectId(run_id)} , submit)
        return redirect(url_for("get_runs"))

    run = mongo.db.runs.find_one({"_id": ObjectId(run_id)})
    runs = mongo.db.runs.find().sort("formdate", 1)
    runtypes = mongo.db.runtypes.find().sort("runtype", 1)
    levels = mongo.db.levels.find().sort("level", 1)
    return render_template("editrun.html", run=run, runs=runs, runtypes=runtypes, levels=levels, isEditRun=True)


@app.route("/delete_run/<run_id>")
def delete_run(run_id):
    run = mongo.db.runs.find_one({"_id": ObjectId(run_id)})
    runs = mongo.db.runs.find().sort("formdate", 1)
    return render_template("deleterun.html", run=run, runs=runs, isDeleteRun=True)


@app.route("/permanently_delete_run/<run_id>")
def permanently_delete_run(run_id):
    mongo.db.runs.remove({"_id": ObjectId(run_id)})
    return redirect(url_for("get_runs")) 


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    genders = mongo.db.genders.find()    
    user = mongo.db.users.find_one({"email": user})
            
    return render_template("profile.html", 
                            user=user, genders=genders, isProfileComplete=True)


def determine_user_level(age, besttime):
    if int(age) < 30:
        if besttime > datetime.datetime.strptime("01:05:39", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:05:39", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:54:42", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:54:42", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:47:01", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:47:01", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:41:20", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    elif int(age) > 30 & int(age) < 35:
        if besttime > datetime.datetime.strptime("01:06:15", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:06:15", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:55:13", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:55:13", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:47:27", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:47:27", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:41:42", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    elif int(age) > 35 & int(age) < 40:
        if besttime > datetime.datetime.strptime("01:08:08", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:08:08", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:56:46", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:56:46", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:48:48", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:48:48", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:42:53", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    else:
        if besttime > datetime.datetime.strptime("01:10:53", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:10:53", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:59:04", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:59:04", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:50:46", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:50:46", "%H:%M:%S") & besttime > datetime.datetime.strptime("00:44:37", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    return userlevel


@app.route("/edit_profile/<user>", methods=["GET", "POST"])
def edit_profile(user):
    if request.method == "POST":
        formdob = request.form.get("dateofbirth")
        dob = datetime.datetime.strptime(formdob, "%Y-%m-%d").date()
        print("date of birth: ", dob)
        delta = timestamp.date() - dob
        print("delta: ", delta)
        age = str(delta / 365.25)
        print("age: ", age)
        formbesttime = request.form.get("besttime")
        besttime = datetime.datetime.strptime(formbesttime, "%H:%M:%S")
        print("besttime: ", besttime)
        # print(strformbesttime)
        # besttime = datetime.datetime.strptime(formbesttime, "%H:%M:%S").time()
        # print("Hour: ", besttime.hour)
        # print("Minute: ", besttime.minute)
        # print("Second: ", besttime.second)
        # print(besttime)
        # userlevel = determine_user_level(age, besttime)
        completeprofile = {
            "firstname": request.form.get("firstname"),
            "lastname": request.form.get("lastname"),
            "dateofbirth": request.form.get("dateofbirth"),
            "gender": request.form.get("gender"),
            "location": request.form.get("location"),
            "besttime": request.form.get("besttime"),
            # "userlevel": userlevel,
            "profilecomplete": True
        }
        mongo.db.users.update({"email": user}, {"$set": completeprofile})
        flash("Profile Succesfulyy Updated.")
        return redirect(url_for("get_runs"))
    
    genders = mongo.db.genders.find()    
    user = mongo.db.users.find_one({"email": user})
    return render_template("edit_profile.html", 
                            user=user, genders=genders, isEditProfile=True)


@app.route("/logout")
def logout():
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)