# Dojo Survey

## Objectives:
* Practice creating a server with Flask from scratch
* Practice adding routes to a Flask app
* Practice having the client send data to the server with a form
* Practice having the server render a template using data provided by the client
* Practice how to redirect a http request to another url

Build a flask application that accepts a form submission and presents the submitted data on a results page.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.

When you build this, please make sure that your program meets the following criteria:

* http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
* http://localhost:5000/result - have this display a html with the information that was submitted by POST
* http://localhost:5000/danger - have this redirect back to "/".  Before redirecting back print in the terminal/console a message: "a user tried to visit /danger.  we have redirected the user to /".

## Reminders
Please remember that anything you want to submit by a form needs to have a name and value (even <select> and <textarea>.  For example, the following html form would not submit any information by post!

The reason above would not submit any information via POST is because select, textarea and input are all missing names and values.  

It's always a good idea to print request.form to see if the form is delivering all the information you need in your routing method.
