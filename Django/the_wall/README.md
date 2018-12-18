# The Wall

## Objectives:
* Practice connecting a Django application to a MySQL database
* Include login and registration
* Include one-to-many relationships
* Practice validating user input and using flash messages

Create a wall/forum page where users will be able to post a message and see the message displayed by other users. Store the messages in a table called 'messages' and retrieve the messages from the database. Follow the below wireframe.

1. Create a login and registration page that is displayed when a user navigates to 'localhost:8000/'

2. Once the user has logged in successfully redirect them to 'localhost:8000/wall' that will show the wall.

Once you get the messages to show up, allow users to post comments for any message. Store the replies/comments to the message in a separate table called 'comments'.

### Helpful Tip
In Jinja, say that you made available a variable called 'messages' where 'messages' contained all the messages in the Wall.  For some reason, the following code would not work:

This however does work.

### Extra Credit I (optional but highly recommended) 
Allow the user to delete his/her own messages.

### Extra Credit II (optional but highly recommended)
Allow the user to delete his/her own message but only if the message was made in the last 30 minutes.
