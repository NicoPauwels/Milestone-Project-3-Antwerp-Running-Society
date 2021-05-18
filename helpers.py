import datetime

def determine_user_level(age, besttime):
    if age < 30:
        if besttime > datetime.datetime.strptime("01:05:39", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:05:39", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:54:42", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:54:42", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:47:01", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:47:01", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:41:20", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    elif age > 30 & age < 35:
        if besttime > datetime.datetime.strptime("01:06:15", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:06:15", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:55:13", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:55:13", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:47:27", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:47:27", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:41:42", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    elif age > 35 & age < 40:
        if besttime > datetime.datetime.strptime("01:08:08", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:08:08", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:56:46", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:56:46", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:48:48", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:48:48", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:42:53", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    else:
        if besttime > datetime.datetime.strptime("01:10:53", "%H:%M:%S"):
            userlevel = "Beginner"
        elif besttime < datetime.datetime.strptime("01:10:53", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:59:04", "%H:%M:%S"):
            userlevel = "Novice"
        elif besttime < datetime.datetime.strptime("00:59:04", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:50:46", "%H:%M:%S"):
            userlevel = "Intermediate"
        elif besttime < datetime.datetime.strptime("00:50:46", "%H:%M:%S") and besttime > datetime.datetime.strptime("00:44:37", "%H:%M:%S"):
            userlevel = "Advanced"
        else:
            userlevel = "Elite"
    return userlevel