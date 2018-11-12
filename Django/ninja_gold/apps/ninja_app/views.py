from django.shortcuts import render, redirect, HttpResponse
from time import strftime, localtime
import random, datetime


def index(request):
    if 'gold_total' in request.session:
        print('gold_total =', request.session['gold_total'])
        pass
    else:
        request.session['gold_total'] = 0
        request.session['message'] = []
        print('New Player!')
    return render(request, "ninja_app/index.html")


def process(request):
    timestamp = strftime('%#H:%M:%S%p, %B %#d, %Y', localtime())    
    if request.POST['building'] == 'farm':
        gold = random.randrange (10,21)
        print(gold)
        request.session['gold_total'] += gold
        data = {
            "ledger" : "Earned",
            "status" : "earned",
            'gold' : gold,
            'building' : request.POST['building'],
            'time' : timestamp
        }
        request.session['message'].append(data)
        request.session.modified = True
    if request.POST['building'] == 'cave':
        gold = random.randrange (5,11)
        print(gold)
        request.session['gold_total'] += gold
        data = {
            "ledger" : "Earned",
            "status" : "earned",
            'gold' : gold,
            'building' : request.POST['building'],
            'time' : timestamp
        }
        request.session['message'].append(data)
        request.session.modified = True
    if request.POST['building'] == 'house':
        gold = random.randrange (2,6)
        print(gold)
        request.session['gold_total'] += gold
        data = {
            "ledger" : "Earned",
            "status" : "earned",
            'gold' : gold,
            'building' : request.POST['building'],
            'time' : timestamp
        }
        request.session['message'].append(data)
        request.session.modified = True
    if request.POST['building'] == 'casino':
        gold = random.randrange (-50,51)
        print(gold)
        request.session['gold_total'] += gold
        if gold >= 0:
            data = {
                "ledger" : "Earned",
                "status" : "earned",
                'gold' : gold,
                'building' : request.POST['building'],
                'time' : timestamp
            }
            request.session['message'].append(data)
            request.session.modified = True
        else:
            data = {
                "ledger" : "Lost",
                "status" : "lost",
                'gold' : gold,
                'building' : request.POST['building'],
                'time' : timestamp
            }
            request.session['message'].append(data)
            request.session.modified = True
    return redirect ('/')

def reset(request):
    request.session.clear()
    return redirect ('/')