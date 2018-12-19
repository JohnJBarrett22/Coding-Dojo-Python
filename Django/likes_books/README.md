# Likes/Books

Say that you wanted to create a website where users can upload their favorite books and other users on the website can indicate whether they 'like' the book.  For the database diagram, below is what you came up with.

Note that there are two distinct relationships between the users and the books table.  One is a one-to-many relationship where the field uploaded_by_id (in the books table) stores the id of the user who uploaded the book.  The second relationship is the many-to-many relationships where it contains information about who liked the particular book.

Now, if you were to have the shell execute: Book.objects.first.users, what would you expect it to return?  Would you expect Django to fetch all the users through the many-to-many relationship table (likes table) or would you expect Django to fetch who uploaded the book by looking up the uploaded_by_id field?

To avoid any confusion in situations like this, particularly where you have two tables with more than one relationships, you could create a diagram like below specifying the relationship.

### According to this:

* A record in the books table that is connected to the users record through uploaded_by_id will call its user: uploader (e.g. Book.objects.first().uploader)
* A record in the users table that is connected to the books table through uploaded_by_id will call its book: uploaded_books (e.g. User.objects.first().uploaded_books)
* A record in the books table that is connected to the users record through the many to many table (likes table) will call its users: liked_users (e.g. Book.objects.first().liked_users)
* A record in the users table that is connected to the books table through the many to many table (likes table) will call its books: liked_books (e.g. User.objects.first().liked_books)

### For your assignment:

* Create the appropriate models and the appropriate relationship.  Design your models so that the following command would be supported
* Book.objects.first().uploader - this should return the user who uploaded the book
* User.objects.first().uploaded_books - this should return all the books that are uploaded by the first user
* Book.objects.first().liked_users - this should return all the users who liked the first book
* User.objects.first().liked_books - this should return all the books that were liked by the first user
* Create 3 different user accounts
* Have the first user create/upload 2 books.
* Have the second user create/upload 2 other books.
* Have the third user create/upload 2 other books.
* Have the first user like the last book and the first book
* Have the second user like the first book and the third book
* Have the third user like all books
* Display all users who like the first book
* Display the user who uploaded the first book
* Display all users who like the second book
* Display the user who uploaded the second book
