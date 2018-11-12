from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def index(request):
    return render(request, "survey_app/index.html")


def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    count = 0
    if len(request.session['name']) < 2:
        messages.add_message(request, messages.ERROR, 'Name cannot be blank!')
        count += 1
    else:
        pass
    
    if len(request.POST['comment']) < 1:
        messages.add_message(request, messages.ERROR, 'Comment cannot be blank!')
        count += 1
    elif len(request.POST['comment']) > 120:
        messages.add_message(request, messages.ERROR, 'Comment must be less than 120 characters.')
    
    if count > 0:
        print(count)
        return redirect('/')
    else:
        if 'count' not in request.session:
            request.session['count'] = 1
            return redirect('/results')
        else:
            request.session['count'] += 1  
            messages.add_message(request, messages.SUCCESS, 'Thanks for submitting this form! You have now completed a submission __ times!')    
            return redirect('/results')


def results(request):
    context = {
        "name" : request.session['name'],
        "location" : request.session['location'],
        "language" : request.session['language'],
        "comment" : request.session['comment'],
        "count" : request.session['count']
    }
    return render(request, "survey_app/results.html", context)

def goback(request):
    return redirect('/')

def delete(request):
    request.session.clear()
    return redirect('/')
