from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strptime, localtime
from datetime import datetime

def index(request):
    context = {
        "date": strftime("%B %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)