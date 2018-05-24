from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'users' : User.objects.all()
    }
    print(context)
    return render(request, 'app_name/index.html', context)

def new(request):
    return render(request, 'app_name/usernew.html')

def edit(request, id):
    user = User.objects.get(id=id)
    context = {
        'user' : user
    }
    return render(request, 'app_name/edituser.html', context)

def show(request, id):
    context ={
        'user' : User.objects.get(id=id)
    }
    return render(request, 'app_name/userinfo.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        return redirect ('/users/new')
    if request.method == 'POST':
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        print('this is the user id :', user.id)
    return redirect('/users')

def update(request):
    user = User.objects.get(id=request.POST['userid'])
    id = request.POST['userid']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        return redirect (edit, id)
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')

def delete(request, id):
    delete_user = User.objects.get(id=id)
    delete_user.delete()
    return redirect('/users')