from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later display all the list of blogs.")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/')

def show(request, num):
    print(num)
    return HttpResponse("Placeholder to edit blog " + num + ".")

def edit(request, num):
    print(num)
    return HttpResponse("Placeholder to edit blog " + num + ".")

def destroy(request, num):
    print(num)
    return redirect('/')