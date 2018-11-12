from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import *

def index(request):
    context = {
    'users' : User.objects.all()
    }
    return render(request, "restful_app/users.html", context)

def new(request):
    return render(request, "restful_app/new.html")

def edit(request, id):
    context = {
    'user' : User.objects.get(id=id)
    }
    return render(request, "restful_app/edit.html", context)

def show(request, id):
    context = {
        'user' : User.objects.get(id=id)
    }
    return render(request, "restful_app/show.html", context)

def create(request):
    User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'])
    return redirect("/users")

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect("/users")

def update(request):
    u = User.objects.get(id=request.POST['id'])
    u.firstname = request.POST['firstname']
    u.lastname = request.POST['lastname']
    u.email = request.POST['email']
    u.save()
    return redirect("/users/"+str(u.id))