# HTML Table

##Objectives:
* Get comfortable passing information from the route to the template
* Get very comfortable iterating through a list of dictionaries to generate a html output.  This is very important for all web development as records returned from a database will almost always be in this format.

Create the following tuple of dictionaries and have it available for your route.  

users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
);

Pass users to your template and have your template output a beautiful HTML table like this:

First Name	Last Name	Full Name
Michael	Choi	Michael Choi
John	Supsupin	John Supsupin
Mark	Guillen	Mark Guillen

As you need to get into the habit of making your assignment look nice, we challenge you to use either Bootstrap or Foundation.  If you haven't dabbled with these frameworks, then just learn enough to do this assignment (creating a nice looking table) and ignore the rest.

### Extra Reminder
Please note that you can use a simple for loop to print the dictionary values in a list/tuple.  For example, consider:

student_info = (
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    );
    
To iterate this and print the student's name and age, you can do something like this in Jinja:
