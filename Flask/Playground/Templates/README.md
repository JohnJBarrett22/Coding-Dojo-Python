# Playground

## Objectives:
* Get comfortable passing information from the route to the template
* Understand how to display information passed from the route in the template file
* Get comfortable with using for loops in the template file
* Get comfortable with using if statements in the template file

## Inline CSS
For this particular assignment, please don't worry about having to create an external css stylesheet, as we haven't taught you yet how to use/create static files.  Instead, please use internal css stylesheet approach like below 

## Level 1 Playground
When a user visits http://localhost:5000/play, have it render three beautiful looking blue boxes.  Please use a template to render this.

## Level 2 Playground
When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times.  For example, localhost:5000/play/7 should display these blue boxes 7 times.  Calling localhost:5000/play/35 would display these blue boxes 35 times.  Please remember that x originally is a string, and if you want to use it as an integer, you must first convert it to integer using int().  For example int("7") returns 7.

## Level 3 Playground
When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color).  For example, localhost:5000/play/5/green would display 5 beautiful green boxes.  Calling localhost:5000/play/35/red would display 35 beautiful red boxes.
