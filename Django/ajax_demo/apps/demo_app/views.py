from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from models import *

def index(request):
    return render(request, "demo_app/index.html")