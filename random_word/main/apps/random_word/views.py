from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    context = {
        'random_word' : get_random_string(length=14),
         'count' : request.session['count'],
    }
    print('*'*10, )
    return render(request, 'random_word/index.html', context)

def random(request):
    print(request.session['count'])
    return redirect ('/')

def reset(request):
    request.session.flush()
    return redirect ('/')