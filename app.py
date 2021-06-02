import os
import datetime
import googlemaps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from datetime import datetime
from datetime import timedelta
from helpers import determine_user_level
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
gmaps = googlemaps.Client(key="AIzaSyAh2mLYzYzAmAWbN_OUY9CksCHUJm82WWg")


timestamp = datetime.now()
createdon = timestamp.strftime("%d/%m/%Y, %H:%M:%S")
createdondate = timestamp.strftime("%d/%m/%Y")
days_in_year = 365.2425



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
            "membersince": createdondate
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
                    return redirect(url_for("show_map", user=session["user"]))
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
    try:
        if session["user"]:
            user = mongo.db.users.find_one({"email": session['user']})
            runs = list(mongo.db.runs.find({
                                            "$and": [
                                                    {"city": user['location']},
                                                    {"timestamp": {"$gte": datetime.today()}}
                                                ]
                                            }).sort("timestamp", 1))
            for run in runs:
                for participant in run['participants']:
                    if session['user'] == participant['email']:
                        run['isCurrentUser'] = True
                if not 'isCurrentUser' in run:
                    run['isCurrentUser'] = False

            return render_template("map.html", runs=runs, user=user, isGetRuns=True)
    except:
        return render_template("login.html", isLogin=True)
    
    return render_template("login.html", isLogin=True)


@app.route("/search", methods=["GET", "POST"])
def search():
    try:
        if session["user"]:
            if request.method == "POST":
                querylocation = request.form.get("location")
                formmindate = request.form.get("mindate")
                querymindate = datetime.strptime(formmindate, "%Y-%m-%d") 
                formmaxdate = request.form.get("maxdate")
                querymaxdate = datetime.strptime(formmaxdate, "%Y-%m-%d") + timedelta(days=1)
                querymindistance = int(request.form.get("mindistance"))
                querymaxdistance = int(request.form.get("maxdistance"))

                runs = list(mongo.db.runs.find({
                                            "$and": [
                                                    {"city": querylocation},
                                                    {"$and": [{"timestamp": {"$gte": querymindate}} , {"timestamp": {"$lte": querymaxdate}}]},
                                                    {"$and": [{"intdistance": {"$gte": querymindistance}} , {"intdistance": {"$lte": querymaxdistance}}]}
                                                ]   
                                            }).sort("timestamp", 1))
                
                if len(runs) == 0:
                    flash("No runs found with such criteria", "mainwindowmessage")
                    return redirect(url_for("show_map", user=session["user"]))
                else:
                    user = mongo.db.users.find_one({"email": session['user']})
                    flash("Filter Active", "mainwindowmessage")
                    return render_template("searchresults.html", runs=runs, user=user, isActiveFilter=True)
            
            user = mongo.db.users.find_one({"email": session['user']})
            runs = list(mongo.db.runs.find({
                                            "$and": [
                                                    {"city": user['location']},
                                                    {"timestamp": {"$gte": datetime.today()}}
                                                ]
                                            }).sort("timestamp", 1))
            
            return render_template("search.html", runs=runs, user=user, isActiveFilter=False)
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)


@app.route("/add_run", methods=["GET", "POST"])
def add_run():
    try:
        if session["user"]:
            if request.method == "POST":
                levelrestriction = "on" if request.form.get(
                    "levelrestriction") else "off"

                formrundate = request.form.get("date")
                rundate = datetime.strptime(formrundate, "%Y-%m-%d")
                rundatestring = rundate.strftime("%d-%m-%Y")
                formruntime = "{}:{}".format(request.form.get(
                            "hour"), request.form.get("minute"))

                runtime = datetime.strptime(formruntime, "%H:%M")
                runtimestring = runtime.strftime("%H:%M")
                runtimestamp = datetime.strptime(
                rundatestring + ", " + runtimestring, "%d-%m-%Y, %H:%M")

                runcity = request.form.get("city")
                runcity_geocode_result = gmaps.geocode(runcity)
                runcitylat = runcity_geocode_result[0]["geometry"]["location"]["lat"]
                runcitylng = runcity_geocode_result[0]["geometry"]["location"]["lng"]

                meetingpoint = request.form.get(
                            "location") + ", " + request.form.get("city")
                meetingpoint_geocode_result = gmaps.geocode(meetingpoint)
                meetingpointlat = meetingpoint_geocode_result[0]["geometry"]["location"]["lat"]
                meetingpointlng = meetingpoint_geocode_result[0]["geometry"]["location"]["lng"]

                participant = mongo.db.users.find_one({"email": session['user']}, {
                                                            "_id": 1, "firstname": 1, "lastname": 1, "initials": 1, "email": 1})
                creatorrunninglevel = mongo.db.users.find_one(
                            {"email": session['user']}).get('userlevel')

                distance = int(request.form.get("distance")[:2])

                run = {
                    "level": creatorrunninglevel,
                    "formrundate": formrundate,
                    "date": rundatestring,
                    "time": runtimestring,
                    "hour": request.form.get("hour"),
                    "minute": request.form.get("minute"),
                    "timestamp": runtimestamp,
                    "location": request.form.get("location"),
                    "city": request.form.get("city"),
                    "runcitylat": runcitylat,
                    "runcitylng": runcitylng,
                    "meetingpointlat": meetingpointlat,
                    "meetingpointlng": meetingpointlng,
                    "distance": request.form.get("distance"),
                    "intdistance": distance,
                    "levelrestriction": levelrestriction,
                    "createdby": session["user"],
                    "createdon": createdon,
                    "participants": [participant]
                }
                if runtimestamp.date() < date.today():
                    flash("Please make sure your run is in the future", "mainwindowmessage")
                    return redirect(url_for("add_run"))

                mongo.db.runs.insert_one(run)
                flash("Run added succesfully", "mainwindowmessage")
                return redirect(url_for("show_map"))

            user = mongo.db.users.find_one({"email": session['user']})
            runs = list(mongo.db.runs.find({
                                            "$and": [
                                                    {"city": user['location']},
                                                    {"timestamp": {"$gte": datetime.today()}}
                                                ]
                                                }).sort("timestamp", 1))
            return render_template("addrun.html", runs=runs, user=user)
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)

    
@app.route("/join_run/<run_id>", methods=["GET", "POST"])
def join_run(run_id):
    try:
        if session["user"]:
            participant = mongo.db.users.find_one({"email": session['user']}, {"_id": 1, "firstname": 1, "lastname": 1, "initials": 1, "email": 1, "userlevel": 1})
            run = mongo.db.runs.find_one({"_id": ObjectId(run_id)})
            print(participant['userlevel'])
            print(run['level'])
            print(run['levelrestriction'])
            
            if run['levelrestriction'] == "on":
                if run['level'] == participant['userlevel']:
                    flash("You have been added to the participtantslist", "mainwindowmessage")
                    mongo.db.runs.update_one(
                        {"_id": ObjectId(run_id)},
                        {"$push": {"participants": participant}})
                else:
                    flash("Only people from the same level can attend this run", "mainwindowmessage")
                    return redirect(url_for("show_map"))
            else:
                flash("You have been added to the participtantslist", "mainwindowmessage")
                mongo.db.runs.update_one(
                    {"_id": ObjectId(run_id)},
                    {"$push": {"participants": participant}})

            return redirect(url_for("show_map"))
    except:
        return render_template("login.html", isLogin=True)
    
    return render_template("login.html", isLogin=True)


@app.route("/leave_run/<run_id>", methods=["GET", "POST"])
def leave_run(run_id):
    try:
        if session["user"]:
            participant = mongo.db.users.find_one({"email": session['user']}, {"_id": 1, "firstname": 1, "lastname": 1, "initials": 1, "email": 1})
            mongo.db.runs.update_one(
                {"_id": ObjectId(run_id)},
                {"$pull": {"participants": participant}} 
            )
            
            return redirect(url_for("show_map"))
    except:
        return render_template("login.html", isLogin=True)
    
    return render_template("login.html", isLogin=True)


@app.route("/edit_run/<run_id>", methods=["GET", "POST"])
def edit_run(run_id):
    try:
        if session["user"]:
            if request.method == "POST":
                levelrestriction = "on" if request.form.get("levelrestriction") else "off"

                formrundate = request.form.get("date")
                rundate = datetime.strptime(formrundate, "%Y-%m-%d")
                rundatestring = rundate.strftime("%d-%m-%Y")
                formruntime = "{}:{}".format(request.form.get("hour"), request.form.get("minute"))

                runtime = datetime.strptime(formruntime, "%H:%M")
                runtimestring = runtime.strftime("%H:%M")
                runtimestamp = datetime.strptime(rundatestring + ", " + runtimestring, "%d-%m-%Y, %H:%M")

                runcity = request.form.get("city")
                runcity_geocode_result = gmaps.geocode(runcity)
                runcitylat = runcity_geocode_result[0]["geometry"]["location"]["lat"]
                runcitylng = runcity_geocode_result[0]["geometry"]["location"]["lng"]

                meetingpoint = request.form.get("location")+ ", " + request.form.get("city")        
                geocode_result = gmaps.geocode(meetingpoint)
                meetingpointlat = geocode_result[0]["geometry"]["location"]["lat"]
                meetingpointlng = geocode_result[0]["geometry"]["location"]["lng"]

                participant = mongo.db.users.find_one({"email": session['user']}, {"_id": 1, "firstname": 1, "lastname": 1, "initials": 1, "email": 1})
                creatorrunninglevel = mongo.db.users.find_one({"email": session['user']}).get('userlevel')
                
                distance = int(request.form.get("distance")[:2])

                editrun = {
                    "level": creatorrunninglevel,
                    "formrundate": formrundate,
                    "date": rundatestring,
                    "time": runtimestring,
                    "hour": request.form.get("hour"),
                    "minute": request.form.get("minute"),
                    "timestamp": runtimestamp,
                    "location": request.form.get("location"),
                    "city": request.form.get("city"),
                    "runcitylat": runcitylat,
                    "runcitylng": runcitylng,
                    "meetingpointlat": meetingpointlat,
                    "meetingpointlng": meetingpointlng,
                    "distance": request.form.get("distance"),
                    "intdistance": distance,
                    "levelrestriction": levelrestriction,
                    "createdby": session["user"],  
                    "createdon": createdon,
                    "participants": [participant]
                }
                if runtimestamp.date() < date.today():
                    flash("Please make sure your run is scheduled in the future", "mainwindowmessage")
                    return redirect(url_for("edit_run", run_id=run_id))

                mongo.db.runs.update({"_id": ObjectId(run_id)}, editrun)
                flash("Run was succesfully updated", "mainwindowmessage")
                return redirect(url_for("show_map"))

            user = mongo.db.users.find_one({"email": session['user']})
            run = mongo.db.runs.find_one({"_id": ObjectId(run_id)})
            runs = list(mongo.db.runs.find({
                                            "$and": [
                                                    {"city": user['location']},
                                                    {"timestamp": {"$gte": datetime.today()}}
                                                ]
                                            }).sort("timestamp", 1))
            return render_template("editrun.html", run=run, runs=runs, user=user)
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)


@app.route("/delete_run/<run_id>")
def delete_run(run_id):
    try:
        if session["user"]:
            run = mongo.db.runs.find_one({"_id": ObjectId(run_id)})
            runs = list(mongo.db.runs.find({"timestamp": {"$gte": datetime.today()}}).sort("timestamp", 1))
            user = mongo.db.users.find_one({"email": session['user']})
        return render_template("deleterun.html", run=run, runs=runs, user=user)
    except:
        return render_template("login.html", isLogin=True)
        
    return render_template("login.html", isLogin=True)


@app.route("/permanently_delete_run/<run_id>")
def permanently_delete_run(run_id):
    try:
        if session["user"]:
            mongo.db.runs.remove({"_id": ObjectId(run_id)})
            flash("Run was removed permanently", "mainwindowmessage")
        return redirect(url_for("show_map")) 
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)

@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    try:
        if session["user"] == user:
            genders = mongo.db.genders.find()    
            user = mongo.db.users.find_one({"email": user})
                    
            return render_template("profile.html", 
                                    user=user, genders=genders)
    except:
        return render_template("login.html", isLogin=True)
    
    return render_template("login.html", isLogin=True)


@app.route("/edit_profile/<user>", methods=["GET", "POST"])
def edit_profile(user):
    try:
        if session["user"] == user:
            if request.method == "POST":
                formdob = "{}-{}-{}".format(request.form.get("birthday"), request.form.get("birthmonth"), request.form.get("birthyear"))
                dob = datetime.strptime(formdob, "%d-%m-%Y")
                dobstring = dob.strftime("%d/%m/%Y")
                age = int((date.today() - dob.date()).days / days_in_year)
                        
                formbesttime = "{}:{}:{}".format(request.form.get("hours"), request.form.get("minutes"), request.form.get("seconds"))
                besttime = datetime.strptime(formbesttime, "%H:%M:%S")
                besttimestring = besttime.strftime("%H:%M:%S")
                userlevel = determine_user_level(age, besttime)

                initials = request.form.get("firstname")[0] + request.form.get("lastname")[0]

                userlocation = request.form.get("location")      
                geocode_result = gmaps.geocode(userlocation)
                userlocationlat = geocode_result[0]["geometry"]["location"]["lat"]
                userlocationlng = geocode_result[0]["geometry"]["location"]["lng"]

                completeprofile = {
                    "firstname": request.form.get("firstname"),
                    "lastname": request.form.get("lastname"),
                    "initials": initials,
                    "dateofbirth": dobstring,
                    "birthday": request.form.get("birthday"),
                    "birthmonth": request.form.get("birthmonth"),
                    "birthyear": request.form.get("birthyear"),
                    "gender": request.form.get("gender"),
                    "location": request.form.get("location"),
                    "userlocationlat": userlocationlat,
                    "userlocationlng": userlocationlng,
                    "besttime": besttimestring,
                    "hours" : request.form.get("hours"),
                    "minutes": request.form.get("minutes"),
                    "seconds": request.form.get("seconds"),
                    "userlevel": userlevel,
                }
                mongo.db.users.update_one({"email": user}, {"$set": completeprofile})
                flash("Your profile was successfully updated", "mainwindowmessage")
                return redirect(url_for("show_map", user=session["user"]))
                    
            genders = mongo.db.genders.find()    
            user = mongo.db.users.find_one({"email": user})
            return render_template("editprofile.html", 
                                        user=user, genders=genders)
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)


@app.route("/delete_profile/<user>")
def delete_profile(user):
    try:
        if session["user"] == user:
            user = mongo.db.users.find_one({"email": user})
            return render_template("deleteprofile.html", 
                                    user=user)
    except:
        return render_template("login.html", isLogin=True)
    
    return render_template("login.html", isLogin=True)


@app.route("/permanently_delete_profile/<user>")
def permanently_delete_profile(user):
    try:
        if session["user"] == user:
            mongo.db.users.remove({"email": user})
            return redirect(url_for("register"))
    except:
        return render_template("login.html", isLogin=True)

    return render_template("login.html", isLogin=True)


@app.route("/logout")
def logout():
    # remove user from session cookie
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
