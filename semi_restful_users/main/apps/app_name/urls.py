from django.conf.urls import url
from . import views

# Must include links to the
urlpatterns = [
    url(r'^users$', views.index),  #  main page
    url(r'^users/new', views.new),  #  new user page
    url(r'^users/(?P<id>\d+)/edit', views.edit),  #  users edit info page
    url(r'^users/(?P<id>\d+)/show', views.show),  #  user info based on ID
    url(r'^users/(?P<id>\d+)/delete$', views.delete),  #  delete user record
    url(r'^create$', views.create),  #  create new user form
    url(r'^update$', views.update),  #  update user info

]