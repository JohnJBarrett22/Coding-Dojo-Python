# Time Display

## Objectives:
* Practice setting up a Django project
* Familiarity with passing data to a template

Create a Django app called time_display according to the below wireframe.

In the controller of your app called time_display - the file ...apps/time_display/views.py) - create a method named index.

When you go to the URL localhost:8000 or localhost:8000/time_display/ this should run the index() method in your controller file, (views.py). Have that method render a template that displays the current date and time.

The keys of your context dictionary are available to be accessed on your page.html.

The above line will print out “somevalue” on your HTML!

There are many ways to get the current time in Python. For example, you could have views.py import gmtime, strftime from 'time' and pass the appropriate string to the render method. For example, your views.py could look like:

Recognize that working with time - especially timezones - is among the more frustrating parts of computer programming. Do not spend more than 15 minutes exploring timezones. We will have numerous opportunities to discuss the challenges of timezones. Essentially, we want to store any timestamps in our database in UTC, and eventually use JavaScript to get the time from the user's browser to customize how times are displayed. For now, the easy fix is to set your Django settings to the timezone that works for you and move on. You have more important things to cover at this part of your career as a developer than timezones.
