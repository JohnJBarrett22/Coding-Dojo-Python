# Survey Form
Build out the below wireframe in a new Django project with a new app called 'surveys'.

Start a new project from scratch this time. This will help you to:

* Reinforce the important concepts you want to master
* Get you to build things a lot faster as each iteration will help you optimize your workflow
* For any web app, it’s critical that you understand how a form can be submitted and how POST and session data work. As you build the app described below, make sure you feel very comfortable with how information can be relayed between a form in the html and the controller (found in views.py). From there, you must fully understand how session and POST data are handled.

## Good Practice
For this assignment:

* Do NOT have a single URL handle BOTH the POST submission as well as the rendering of the html. In other words, never render on a post.
* For example, the form that’s rendered from http://localhost should be submitted not to /result but to /process. The method that handles /process should do all the logic, process POST data, manipulate session data and redirect to another URL, say /result.
* The reason we have a method to handle processing input data and another method to render the html is because it makes reading your code much easier.
* Also, if the same URL handled both POST and the rendering of the html, when a user reloads that page, it would resubmit the form data. This is not good and is often a common mistake made by a rookie developer. 

## How to do this in Django?
In your controller/view file (named views.py), be sure to import redirect along with render.
