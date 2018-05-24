from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random$', views.random),
    url(r'^random/reset$', views.reset),
]