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

* Desktop wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-3-Impala/blob/master/static/readme/impala-desktop-wireframes.png)
* Tablet wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-2-Breakout/blob/master/assets/images/readme/wireframe-tablet.png)
* Mobile wireframe - [View](https://github.com/NicoPauwels/Milestone-Project-2-Breakout/blob/master/assets/images/readme/wireframe-mobile.png)

## Surface

We want this version of Outbreak to have a more modern look than the original version.

* Colour scheme
    * The main colour is #0095DD.

* Typography
    * The main font for text paragraphs is Arial and this is the only font used throughout the project.

# Technologies Used

## Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML) 
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Libraries & Programs Used

* [Font Awesome](https://fontawesome.com/start) 
    * Font Awesome was used to import some icons.

* [Git](https://git-scm.com/) 
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to Github.

* [Github](https://github.com/) 
    * GitHub is used to store the projects code after being pushed from Git.

* [Balsamiq](https://balsamiq.com/) 
    * Balsamiq was used to create the wireframes during the design process.

# The realisation of this project

* [Tutorial 1:](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript)
    I started off the project based on this tutorial, when finalizing this tutorial I wanted to use the gained knowledge to add some powerups, I soon found myself down a rabbithole and I was losing way too much time trying to figure out how to add this powerup functionality to the game. I did manage to hide a few powerups underneath some bricks, and they do fall towards the bottom of the screen. I decided to browse the web to find another tutorial that contained these powerup functionality to see how it is done right and which logic was used.

* [Tutorial 2:](https://www.youtube.com/c/MtFordStudios/videos)
    As discussed in the previous bulletpoint, a second tutorial was used to gain more insight on how to properly implement powerups into the game. I quickly found myself facing another dilemma: trying to implement the poweruplogic from this tutorial in my already existing javascript code or starting from scratch. I decided to play it safe and start completely based on this tutorial.
    In the end I am sure this was the right thing to do because this tutorial was approaching some things in a complete different way and features that were being built at the end of the project were based on the solid foundation and logic layed out in the beginning.

* My very own feature:
     I just had to add a feature of my own to the project. I used to play this game at a very young age on my uncles 486. There was a powerup in the version I used to play that was not a part of this version yet: the multiball. I decided to give it a go and by reverse engineering what was going on in the existing code and some sleepless nights later I was able to implement the multiball feature. Although I have deactivated the spinBall() function to get it to work and some bugs might occur when combined with other powerups, I am happy with the outcome for now. It just comes down to fixing these bugs and refactoring the spinBall() function.

# Testing

The W3C Markup Validator, W3C CSS Validator and jshint.com services were used to validate every page of the project to ensure there were no syntax errors in the project.

* [W3C Markup Validator](https://validator.w3.org/) - [Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnicopauwels.github.io%2FMilestone-Project-2-Breakout%2F)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnicopauwels.github.io%2FMilestone-Project-2-Breakout%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 
* [jshint.com](https://jshint.com/) - There were some warnings but practically all of them were browser warnings.

## Testing user stories discussed earlier

* First time Visitor Goals
    * As a first time visitor, I want to be able to figure out what the game controls are;
        * The user is informed on the game controls on the landing page.
    * As a first time visitor, I want to be able to serve the ball;
        * When the spacebar is hit (desktop) or the screen is touched (mobile), the user serves the ball.
    * As a first time visitor, I want to be able to keep the ball inbound using the paddle;
        * The paddle can be moved to left and right with the corresponding arrow keys (desktop) or touching the left or right side of the screen (mobile) to catch the ball and bounce it back.
    * As a first time visitor, I want to see the powerups falling down to the bottom of the screen;
        * There's a 5 percent chance a destroyed brick has a powerup underneath, if this is the case the powerup will fall down towards the bottom of the screen.
    * As a first time visitor, I want to be able to catch the powerups and experience them in the gameplay;
        * When a powerup is caught by the paddle, it becomes active:
            * extra life
            * extended paddle
            * sticky paddle (paddle turns red)
            * superball (ball turns red)
            * multiball (two extra balls enter the game field)
    * As a first time visitor, I want to know which level I am playing, how many lives I've got left, my current score, my all time high score and whether the sound is on or off.
        * The level is being displayed and increases when all bricks have been destroyed, also a new level is being spawned.
        * The lives decrease when a ball is out of bounds, the game ends when all lives are lost and game over is being displayed.
        * The current score is being increased depending on the brick that was destroyed its rank.
        * The all time high score is kept track off by using window.localStorage and thus saves the high score across browser sessions.
        * Also whether the sound is on or off is being displayed.
* Returning Visitor Goals
    * As a returning visitor, I do not necessarily need to see the game controls;
        * The user has the option to check the "do not show this message again" checkbox in order to not see the game instructions again when the game is loaded next time.
    * As a returning visitor, I obviously want the same game experience as a first time visitor;
        * All of the functionality is in place as discussed above.
    * As a returning visitor, I want to see my all time high score.
        * The alltime high score is stored in localstorage and thus across browser sessions.
* Frequent User Goals
    * As a frequent user of this game, I want to same user experience as a returning visitor.

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