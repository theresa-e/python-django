from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout$', views.checkout),
    url(r'^back$', views.go_back),
]  