from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, "reviewer_app/index.html")

def books(request):
    context = {
        'reviews' : Review.objects.all().order_by('-created_at')
    }
    return render(request, "reviewer_app/books.html", context)

def bookdetails(request, id):
    context = {
        'books' : Book.objects.get(id=id)
    }
    return render(request, "reviewer_app/bookdetails.html", context)

def userdetails(request, id):
    context = {
        'users' : User.objects.get(id=id)
    }
    return render(request, "reviewer_app/userdetails.html", context)

def add(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, "reviewer_app/add.html", context)

def addreview(request):
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], reviewer=User.objects.get(id=request.POST['reviewer']), book_reviewed=Book.objects.get(id=request.POST['book_reviewed']))
    return redirect('/books')

def addbook(request):
    if request.POST.get("preauthor") != "none":
        select_author = request.POST.get('preauthor')
    else:
        select_author = request.POST["author"]

    title = request.POST['title']
    author = select_author
    review = request.POST['review']
    rating = request.POST['rating']

    this_user = User.objects.get(id=request.session['u_id'])
    this_book = Book.objects.create(title=title, authored_by=author, uploader=this_user)

    Review.objects.create(review=review, rating=rating, reviewer=this_user, book=this_book)
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    error = False
    if len(request.POST['name']) < 2:
        error = True
        messages.error(request, "Name must be a minimum length of three characters!")

    if request.POST['name'].isalpha() == False:
        error = True
        messages.error(request, "Name cannot have a number in it or be blank!")

    if len(request.POST['alias']) < 2:
        error = True
        messages.error(request, "Alias must be a minimum length of three characters!")

    if request.POST['alias'].isalpha() == False:
        error = True
        messages.error(request, "Alias cannot have a number in it or be blank!")

    if len(request.POST['email']) < 7:
        error = True
        messages.error(request, "Email must be a minimum length of three characters!")
    
    if not EMAIL_REGEX.match(request.POST['email']):
        error = True
        messages.error(request, "Email must be a valid email address!")

    if len(request.POST['password']) < 8:
        error = True
        messages.error(request, "Password must be a minimum length of eight characters!")

    if request.POST['password'] != request.POST['confirm_password']:
        error = True
        messages.error(request, "Passwords must match!")

    if User.objects.filter(email=request.POST['email']):
        error = True
        messages.error(request, "User already exists!")

    if error:
        return redirect('/')

    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    decoded_hash = hashed.decode('utf-8')

    user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=decoded_hash)
    print(user)
    request.session['u_id'] = user.id
    return redirect("/books")

def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if not user_list:
        messages.error(request, "Invalid credentials!")
        return redirect('/')
   
    user = user_list[0]
   
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['u_id'] = user.id
        request.session['u_alias'] = user.alias
        return redirect("/books")
    else:
        messages.error(request, "Invalid credentials!")
        return redirect('/')