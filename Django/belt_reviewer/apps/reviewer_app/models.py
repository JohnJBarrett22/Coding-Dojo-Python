from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=60)
    authored_by = models.ForeignKey(Author, related_name="authored_books", on_delete = models.CASCADE)
    uploader = models.ForeignKey(User, related_name="uploaded_books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name="written_reviews", on_delete = models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="reviews_of_book", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)