from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "amadon_app/index.html", context)

def buy(request):
    request.session['quantity'] = request.POST['quantity']
    request.session['id'] = request.POST['id']
    return redirect("/amadon/checkout")

def checkout(request):
    Item.objects.get(id=request.session['id'])

    return render(request, "amadon_app/checkout.html")