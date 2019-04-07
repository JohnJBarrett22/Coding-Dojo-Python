from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers

def index(request):
    return render(request, "demo_app/index.html")

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize("json", users)
    print (users_json)
    return HttpResponse(users_json, content_type='application/json')

def all_html(request):
    users = User.objects.all()
    return render(request, "demo_app/all.html", {"users": users})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])
    print(users)
    return render(request, "demo_app/all.html", {"users": users})

