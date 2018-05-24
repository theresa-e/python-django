from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^store$', views.index),
    url(r'^buy$', views.buy),
]  