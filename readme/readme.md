# Milestone Project 3: Impala

[View the live project here.](https://milestone-project-3-impala.herokuapp.com/)<br>


# UX

## Strategy

The purpose of Impala is bringing Runners together and easily keep track of who is running with who, when and where. The idea of this came from the fact that I am a pretty experienced runner myself and mostly when I ask others to join me, I get a negative answer because they say I run too fast. So what if there was an application that determines your user level and makes it easy to find other runners in a certain area? The idea of Impala was born.

### Site Goals

* Make it easy for runners to find other runners whether or not from the same level;
* Provide an overview of runs in a certain area;
* Provide an overview of participants for each run.

#### User stories: 
* First time Visitor Goals
    * As a first time visitor, I want to be able to register for Impala;
    * As a first time visitor, I want to be able to login to Impala;
    * As a first time visitor, I want to fill out my profile and have my level determined;
    * As a first time visitor, I want to get an overview of the scheduled runs in my area on a map on tablet and desktop, and a list overview on mobile;
    * As a first time visitor, I want to be able to set my attendance for a run;
    * As a first time visitor, I want to be able to schedule or create a run;
    * As a first time visitor, I want to be able to make changes or edit a run scheduled by me;
    * As a first time visitor, I want to be able to remove or delete a run scheduled by me.
    * As a first time visitor, I want to be able to search for runs in a certain area.
    * As a first time visitor, I want to be able to logout.
* Returning Visitor Goals
    * As a returning visitor, I obviously want the same application experience as a first time visitor;
    * As a returning visitor, I want to be able to edit or remove my profile;
* Frequent User Goals
    * As a frequent user of this application, I want to same user experience as a returning visitor.

## Scope 

Planned Features:<br>
* Responsive design;
* Navigation menu (Site Wide);
* MongoDB databases to store run and user/profile information;
* CRUD functionality;
* Registered user run creation and management.
* Map to provide an overview of the runs and searchable to all users;
* Profile page which can be editted; 
* Login functionality;
* Logout functionality;

## Structure

User Story:

> As a first time visitor, I want to be able to register for Impala.

Acceptance criteria:
* Landing page of Impala gives the possibility to register.

Implementation: 
* A registration form will be displayed on the registration page.

> As a first time visitor, I want to be able to login to Impala.

Acceptance criteria:
* Landing page or registration page of Impala displays the possibility to easily switch to login page.

Implementation:
* Login button will be displayed on the landing page in case a user has already registered. Once clicked the user is presented with a login form to entered his registered credentials.

> As a first time visitor, I want to fill out my profile and have my level determined.

Acceptance critera:
* After logging in the first time the user is being redirected to his an edit profile page he needs to fill out once for an optimal application experience.

Implementation:
* When the user has succesfully registered, he or she will be redirected directly to the edit profile page where he can fill out a form. Required info is the user's first name, last name, age (but this will be derived from his or her date of birth), gender, location he or she finds him/herself and finally his best time on 10 km. Based on his or hers age and best time on 10 km the user will be assigned a running level.

> As a first time visitor, I want to get an overview of the scheduled runs in my area on a map on tablet and desktop, and a list overview on mobile.

Acceptance critera:
* Once the required form is filled out, the user will be redirected to an overview of upcoming runs located in his or her area. On tablet and desktop the runs will be displayed on a map with a list overview in a pane populated with cards on the left side of the screen. The cards will display the date, time, level, planned distance and number of participants. On mobile the overview a list will be displayed with expandable cards to see the details of each run.

Implementation:
* [Leaflet](https://leafletjs.com/) will be used for implementation of the map. To suit the rest of the interface a [Mapbox](https://www.mapbox.com/) tilelayer theme was used called dark-v10. To render the runs on the map the coordinates of the meeting point adresses where necessary. Google maps module was imported into python to make use of its geocode functionality. The details of the runs will be displayed as a popup on the desktop and tablet version, on mobile the details will show by tapping on the card. 

> As a first time visitor, I want to be able to set my attendance for a run.

Acceptance critera:
* A user should be able to set his or hers attendance for a particular run when he has seen all the details.

Implementation:
* On tablet and desktop views, the popup will display a button where a user can set his or hers attendance to that particular run. The application will check whether the user is already participating or not and based on that outcome the button will display to join or to leave the run. Needless to say based on this action the user will be added or removed from the participantlist. 

> As a first time visitor, I want to be able to schedule or create a run.

Acceptance critera:
* As a registered user, it should be straight forward to add a run to the database.

Implementation:
* In the navigationbar a button will be displayed to add a run. Once clicked, a form will be displayed so the user can fill out the details of the run. Date, time, meetingpoint and planned distance can be written to the database by filling out this form. The application will automatically set the level of the run to the organisers run level. Additionally the user can restrict users with another running level to join the run.

> As a first time visitor, I want to be able to make changes or edit a run scheduled by me.

Acceptance critera:
* It should be straight forward to identify the runs created by the active user and make changes to the ones he or she has created.

Implementation:
* A font awesome icon will be displayed in the top right corner of each run card. That way it is fairly easy for users to spot which runs are theirs and once clicked they will be once again presented with a form to make changes for that particular run. The application fills in the details of each run automatically by reading the database. Changes can be made to this data and written to the database by clicking the save button 

> As a first time visitor, I want to be able to remove or delete a run scheduled by me.

Acceptance critera:
* It should be straight forward to delete runs created by the active user.

Implementation:
* Apart from making changes in the edit menu, the user is also able to remove the run by clicking the delete button which is also displayed in the bottom of the edit menu. Once clicked the user will have to confirm to delete the run permenantly. 

> As a first time visitor, I want to be able to search for runs in a certain area.

Acceptance critera:
* It should be fairly easy to search the database for runs in a particular region or city, in a certain time frame, and based on the planned distance.

Implementation:
* Next to the upcoming runs title a search button has been displayed, once clicked the application provides the user with a form to fill out his or hers search criteria, by clicking the search button in the bottom of this menu the application will launch a query based on the details that were entered in the form. The result of this query will be displayed in the pane on the left side of the screen and also the map will adjust to the location that was entered by the user.

> As a first time visitor, I want to be able to logout. 

Acceptance critera:
* It should be fairly easy for a user to log out.

Implementation:
* Apart from the add and upcoming runs button in the navigation, there is also a user section, where the user profile can be viewed, but it will also give the user the possibility to log out. 

## Skeleton

Below the wireframes:

* Desktop wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-3-Impala/blob/master/readme/images/impala-desktop-wireframes.png)
* Tablet wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-3-Impala/blob/master/readme/images/impala-tablet-wireframes.png)
* Mobile wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-3-Impala/blob/master/readme/images/impala-mobile-wireframes.png)

## Datebase Design

MongoDB Object format examples:

**Collection genders:**<br>
{<br>
_id: ObjectId("6097fa2bc2c2f86442acab77")<br>
gender: "M"<br>
}
<br><br>
**Collection levels:**<br>
{<br>
_id: ObjectId("60672683f9934b0f30267805")<br>
level: "Beginner"<br>
}
<br><br>
**Collection runs:**<br>
{<br>
_id: ObjectId("60b604946c1f8bdd033318a4")<br>
level: "Elite"<br>
formrundate: "2021-06-08"<br>
date: "08-06-2021"<br>
time: "09:00"<br>
hour: "09"<br>
minute: "00"<br>
timestamp: 2021-06-08T09:00:00.000+00:00<br>
location: "Korte Vanruusbroecstraat 6"<br>
city: "Antwerpen"<br>
runcitylat: 51.2194475<br>
runcitylng: 4.4024643<br>
meetingpointlat: 51.2087416<br>
meetingpointlng: 4.4251334<br>
distance: "10 km"<br>
intdistance: 10<br>
levelrestriction: "off"<br>
createdby: "nico_pauwels@hotmail.com"<br>
createdon: "31/05/2021, 12:37:38"<br>
participants: Array<br>
0: Object<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_id: ObjectId("60b5f9d66c1f8bdd0333189e")<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email: "nico_pauwels@hotmail.com"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firstname: "Nico"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initials: "NP"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lastname: "Pauwels"<br>
}
<br><br>
**Collection users:**<br>
{<br>
_id: ObejctId("60b5f9d66c1f8bdd0333189e")<br>
email: "nico_pauwels@hotmail.com"<br>
password: "pbkdf2:sha256:150000$NHbjcXlN$98b5651996d76f6306870057425a17689cf1722b..."<br>
membersince: "31/05/2021"<br>
besttime: "00:40:00"<br>
birthday: "31"<br>
birthmonth: "08"<br>
birthyear: "1987"<br>
dateofbirth: "31/08/1988"<br>
firstname: "Nico"<br>
gender: "M"<br>
hours: "00"<br>
initials: "NP"<br>
lastname: "Pauwels"<br>
location: "Antwerpen"<br>
minutes: "40"<br>
seconds: "00"<br>
userlevel: "Elite"<br>
userlocationlat: 50.8686544<br>
userlocationlng: 5.868221999999999<br>
}

## Security

Database connection details are set up in env.py for development, for security reasons this is not uploaded to GitHub so that database and connectiondetails are not visible to users. In production these are stored in Heroku.

## Surface

* Colour scheme
    * I chose to keep Impala quite dark with green accents; some colours used:
        * for backgrounds:
            * #12171E;
            * #293340;
            * #222730;
        * for text and elements that needed contrast:
            * #EAEDF0;
            * #4D5765;
    
* Typography
    * The main fonts used are Heebo and Hind Siliguri.

# Features

## Existing Features
* User registration
* User login
* Overview of runs (map on larger screens, list on mobile)
* Create a run (with or without levelrestriction)
* Edit a run
* Remove a run
* Participate in a run
* User profile page
* Edit profile page

## Features left to implement
I believe a lot is possible with this application. I have tried to set up Impala like this so that additional features can be build quite fluently upon this basis. <br><br>Some possibilities:
* Better level determination: For now manual user input is used to determine user levels, the application would definitely benefit from data input from applications that keep track of sporting efforts such as Strava;
* More restrictions: I have implemented a same user level restriction when a run event is being created but this feature easily can be translated to ie. same gender only restriction;
* Crew or private Runs: Creating user groups to organize crew runs, only members of the crew can view that particular run.
* Better view on participantslist: For now I have chosen to display the initials of users, but in a future versions profile pictures can be used and the lists become expandable so you can see the name of the users who registered to participate in that particular run.

# Technologies 

* [HTML5](https://en.wikipedia.org/wiki/HTML) 
    * This project uses HTML as the main language used to complete the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS)
    * This project uses custom written CSS to style the website.
* [Font Awesome](https://fontawesome.com/start) 
    * Font Awesome was used to import some icons.
* [Google Fonts](https://fonts.google.com/)
    * Google fonts was used to import some fonts.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    * A few lines of Javascript were used for the slider used in the forms.
* [Leaflet](https://leafletjs.com/)
    * Leaflet is the leading open-source JavaScript library for mobile-friendly interactive maps. Weighing just about 39 KB of JS, it has all the mapping features most developers ever need.
* [Mapbox](https://www.mapbox.com/)
    * Mapbox provides performant and customizable maps that suited the needs of this project.
* [Blender](https://www.blender.org/)
    * Blender was used to design the markers for the map.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * This projects core was created using Python, the back-end logic and the means to run/view the website.
    * Python modules used (these can be found in requirements.txt project file):
        * certifi==2020.12.5
        * chardet==4.0.0
        * click==7.1.2
        * dnspython==2.1.0
        * Flask==1.1.2
        * Flask-PyMongo==2.3.0
        * googlemaps==4.4.5
        * idna==2.10
        * itsdangerous==1.1.0
        * Jinja2==2.11.3
        * MarkupSafe==1.1.1
        * pymongo==3.11.3
        * requests==2.25.1
        * urllib3==1.26.4
        * Werkzeug==1.0.1
* [MongoDB](https://www.mongodb.com/)
    * MongoDB was used to create the document based databases (collections) used as data storage for this project.
* [Heroku](https://www.heroku.com/)
    * Heroku was used to deploy the live website.
* [Git](https://git-scm.com/) 
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to Github.
* [Github](https://github.com/) 
    * GitHub is used to store the projects code after being pushed from Git.
* [Balsamiq](https://balsamiq.com/) 
    * Balsamiq was used to create the wireframes during the design process.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    * Google chromes built in developer tools were constantly used throughout the development process to inspect page elements.
* [Visual Studio Code](https://code.visualstudio.com/)
    * All code was written in Visual Studio Code.

# Testing

* [W3C Markup Validator:](https://validator.w3.org/)<br><br>All html templates were manually entered in the HTML checker and inspected individually.<br>Some errors were caused by the Jinja syntax but besides that no errors or warnings were found.<br>


* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)<br><br>No errors were found in the CSS.
* [jshint.com](https://jshint.com/)<br><br>No errors were found in the script.js.
* [PEP8 Validator](http://pep8online.com/)<br><br>The check resulted in a a few errors.<br>All of them said "line too long", as some of them were a bit longer than 79 characters. 

## Testing user stories discussed earlier

* First time Visitor Goals
    * As a first time visitor, I want to be able to register for Impala;
    * As a first time visitor, I want to be able to login to Impala;
    * As a first time visitor, I want to fill out my profile and have my level determined;
    * As a first time visitor, I want to get an overview of the scheduled runs in my area on a map on tablet and desktop, and a list overview on mobile;
    * As a first time visitor, I want to be able to set my attendance for a run;
    * As a first time visitor, I want to be able to schedule or create a run;
    * As a first time visitor, I want to be able to make changes or edit a run scheduled by me;
    * As a first time visitor, I want to be able to remove or delete a run scheduled by me.
    * As a first time visitor, I want to be able to search for runs in a certain area.
    * As a first time visitor, I want to be able to logout.
* Returning Visitor Goals
    * As a returning visitor, I obviously want the same application experience as a first time visitor;
    * As a returning visitor, I want to be able to edit or remove my profile;

## Further Testing

* The website was tested on Google Chrome, Mozilla Firefox and Safari browsers.
* The website was viewed on a variety of devices such as desktops, laptops, iPhone 8 and some android devices.
* The website was viewed in google chrome dev tools to check overall responsiveness.
* Friends and family members were asked to review the game to point out any bugs and/or user experience issues.

## Known bugs

* On larger screens of desktops when the browser window is maximized, the ball not always bounces off the paddle but just flies through.
* When multiball has been active and sticky powerup is activated bugs might occur:
    * the balls don't serve correctly or dont serve at all when sticky powerup is active
    * the balls that went out of play suddenly appear back on the canvas

# Deployment

## Github pages

The project was deployed to GitHub Pages using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/NicoPauwels/Milestone-Project-2-Breakout).
2. At the top of the Repository, locate the "Settings" button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the new published site [link](https://nicopauwels.github.io/Milestone-Project-2-Breakout/) in the "Github Pages" section.

# Credits

## Code

### Tutorials
* [Tutorial 1](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript)
* [Tutorial 2](https://www.youtube.com/c/MtFordStudios/videos)
* Various ongoing problems were solved looking for solutions found on [Stackoverflow](https://www.stackoverflow.com) and [W3Schools](https://www.w3schools.com).

## Acknowledgments

* Antonio Rodriguez, my mentor for the continuous support and helpful feedback.
* John Traas, Code Institute alumni, for the continuous support and helpful feedback.