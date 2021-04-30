@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    # get the session user by registered email address
    email = mongo.db.users.find_one(
        {"email": session["user"]})["email"]

    firstname = mongo.db.users.find_one(
        {"email": session["user"]},
        {"firstname": 1}
    )["firstname"]

    lastname = mongo.db.users.find_one(
        {"email": session["user"]},
        {"lastname": 1}
    )["lastname"]

    dateofbirth = mongo.db.users.find_one(
        {"email": session["user"]},
        {"dateofbirth": 1}
    )["dateofbirth"]

    gender = mongo.db.users.find_one(
        {"email": session["user"]},
        {"gender": 1}
    )["gender"]

    location = mongo.db.users.find_one(
        {"email": session["user"]},
        {"location": 1}
    )["location"]

    weight = mongo.db.users.find_one(
        {"email": session["user"]},
        {"weight": 1}
    )["weight"]

    biography = mongo.db.users.find_one(
        {"email": session["user"]},
        {"biography": 1}
    )["biography"]

    membersince = mongo.db.users.find_one(
        {"email": session["user"]},
        {"membersince": 1}
    )["membersince"]

    bestavgpace = mongo.db.users.find_one(
        {"email": session["user"]},
        {"bestavgpace": 1}
    )["bestavgpace"]

    user = mongo.db.users.find_one(
        {"email": session["user"]},
        {"firstname": 1},
        {"lastname": 1} 
    )["user"]

    return render_template("profile.html", 
                            email=email, 
                            firstname=firstname, 
                            lastname=lastname, 
                            dateofbirth=dateofbirth, 
                            gender=gender, 
                            location=location, 
                            weight=weight, 
                            biography=biography, 
                            membersince=membersince, 
                            bestavgpace=bestavgpace, 
                            isProfile=True)