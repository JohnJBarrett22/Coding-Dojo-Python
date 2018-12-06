# Blogs

## Objectives
* Familiarity with setting up a new Django project
* Familiarity with setting up a new Django app
* 8Familiarity with routing
* Familiarity with views and how to render a simple Http Response
* Using what you've learned, please do the following:

## Create a new project 

Have the following URL either display a simple HttpResponse or redirect to a different URL for the following apps:
* / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
* /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
* /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
* /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
* /{{number}}/edit - display 'placeholder to edit blog {{number}}'.  Have this be handled by a method named 'edit'.
* /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /. 
