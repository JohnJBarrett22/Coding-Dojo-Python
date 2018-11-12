from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    print(request.session)
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    print(request.session['count'])
    context = {
        "random" : get_random_string(length=14),
        "count" : request.session['count']
    } 
    return render(request, "random_app/index.html", context)

def generate(request):
    return redirect ('/')

def reset(request):
    request.session.clear()
    return redirect ('/')


