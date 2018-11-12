from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": strftime("%b %d, %Y", gmtime())
    }
    return render(request, "time_display_app/index.html", context)