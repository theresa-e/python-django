from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "My first request! :)"
    return HttpResponse(response)