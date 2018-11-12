from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    return render(request, 'logreg_app/index.html')

def register(request):
    # print(request.POST)
    error = False
    if len(request.POST['first_name']) < 2:
        error = True
        messages.error(request, "First name must be a minimum length of three characters!")

    if request.POST['first_name'].isalpha() == False:
        error = True
        messages.error(request, "First name cannot have a number in it or be blank!")

    if len(request.POST['last_name']) < 2:
        error = True
        messages.error(request, "Last name must be a minimum length of three characters!")

    if request.POST['last_name'].isalpha() == False:
        error = True
        messages.error(request, "Last name cannot have a number in it or be blank!")

    if len(request.POST['email']) < 7:
        error = True
        messages.error(request, "Last name must be a minimum length of three characters!")
    
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

    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=decoded_hash)
    print(user)
    request.session['u_id'] = user.id
    return redirect('/success')

def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if not user_list:
        messages.error(request, "Invalid credentials!")
        return redirect('/')
   
    user = user_list[0]
   
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['u_id'] = user.id
        request.session['u_fname'] = user.first_name
        return redirect('/success')
    else:
        messages.error(request, "Invalid credentials!")
        return redirect('/')

def success(request):
    return render(request, 'logreg_app/success.html')
