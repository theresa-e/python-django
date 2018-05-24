from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print ('*'*10, 'Main URL was visited, user was redirected to /store.', '*'*10)
    return redirect('/store')