# Email Validation with DB
## Objectives:
* Practice fetching data from a database connected to a Flask application
* Validate user input before adding it to the database
* Practice using flash messages
* Practice redirecting after going to a POST route

Create an application that asks a user to enter an email address and validates whether that email is valid and whether it exists in the database.

### index.html
A simple form for the user to submit an email.

### Error
If the email address is not valid, have a notification "Email is not valid!" to display on the homepage.

### success.html
Once a valid email address is entered, save to the database the email address the user entered. On the success page, display all the email addresses entered along with the date and the time (e.g. June 24th, 2013, 6:00 PM) when the email addresses were entered 

### Bonus
Add a delete button onto your success page that allows the user to delete entries from the database from the success page. With the bonus feature added, your app should look a little different than above!
