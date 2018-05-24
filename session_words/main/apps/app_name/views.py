from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, strptime, localtime
from datetime import datetime

def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    return render(request, 'app_name/index.html')

def process(request):
    if 'word_size' in request.POST:
        checkbox_status = True
    else:
        checkbox_status = False
    temp_list = request.session['word_list']
    temp_list.append({
        "word": request.POST['user_word'],
        "color": request.POST['color'],
        "word_size": checkbox_status,
        "date": strftime("%B %d, %Y %H:%M %p", gmtime()),
    })
    request.session['word_list'] = temp_list
    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')