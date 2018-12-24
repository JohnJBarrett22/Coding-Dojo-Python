# Checkerboard

## Objectives:
* Continue to learn how to pass information from the url to the route
* Get comfortable passing information from the route to the template
* Understand how to use for loop properly in the template
* Recognize the value of creating a html/css first and then adding logic/code

Write a program that generates an HTML page that looks like a checkerboard.  For this assignment, you're allowed to use <table> if you want.  You could use <div> if desired.  (Note: During Web Fundamentals, we discouraged you from using <table> as we didn't want you to use <table> to position different contents of your website on different parts of the table.  For this assignment however, you are allowed to use <table>.)

Your program should have the following output

http://localhost:5000 - should display 8 by 8 checkerboard
http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)
