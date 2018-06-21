from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    print('home')
    return render(request, 'post/index.html', { 'posts': Post.objects.all()})

def create_post(request):
    context = {
    'new_post': Post.objects.create(post_content=request.POST['post_content'])
        }
    print('new post:', context)
    return render(request, 'post/post.html', context)

def delete_post(request, id):
    context = {
        'deleted_post' : Post.objects.filter(id=id).first().delete()
    }
    print('deleted a post')
    return redirect('/')