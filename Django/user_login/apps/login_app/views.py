from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
import json

def index(request):
    return render(request, 'login_app/index.html')

def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')

def all_html(request):
    return render(request, 'login_app/all.html', {"users":User.objects.all()})

def find(request):
    return render(request, 'login_app/all.html', {"users":User.objects.filter(firstname__startswith=request.POST['firstname'])})

def create(request):
    User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'])
    return render(request, 'login_app/all.html', {"users":User.objects.order_by("-id")})
