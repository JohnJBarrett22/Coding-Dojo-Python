# Random Word Generator

## Objectives:
* Practice setting up a Django project
* Familiarity with passing data to a template
* Familiarity with using Django session

Create a new Django app called 'random_word'. Your template will show a random word with 14 characters in length.

The first time you use this app, it should say 'attempt #1'. Each time you generate a new random keyword, it should increment the attempt figure. The purpose of this assignment is to reinforce your use of session. Don't spend too much time on the random word generator, it's okay if your random word is not a real word.

Also when an http request is sent to, say, localhost:8000/random_word/reset, have it reset the counter for the attempt and redirect back to localhost:8000/random_word.

Hint for generating a random word: See https://stackoverflow.com/questions/25943850/django-package-to-generate-random-alphanumeric-string

There are many ways you could create a random string, but one way you could do this is by:
* importing get_random_string from django.utils.crypto (remember that you can import other libraries/modules in your views.py or any other python files)
* use get_random_string(length=14) to get a random string of length 14

As the goal of this assignment is to really help you get familiar with creating a new app, setting up routing, views, templates, etc, we've given you some hints. :)
