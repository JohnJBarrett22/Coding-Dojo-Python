# Ninja Gold

## Objectives:
* Practice using session
* Practice having the server use data sent by the client in a form
* Practice using hidden inputs

Create a simple game to test your understanding of flask, and implement the functionality below.

For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

## Guidelines
Refer to the wireframe below.

Have the four forms appear when the user goes to http://localhost:5000.

For the farm, your form would look something like

In other words, you want to include a hidden value in the form and have each form submit the form information to /process_money.

Have /process_money determine how much gold the user should have.

You should only have 2 routes -- '/' and '/process_money' (reset can be another route if you implement this feature).

Please make sure that...

when you visit, "localhost:5000/" you are seeing the page we described above (in other words, we don't want to have to go to "/gold/index" or other URL to see this app).
the forms are sent to "/process_money" and not any other URL.
the activities are stored in the session. No need to store anything in the database.
