from django.conf.urls import url
from . import views

# Must include links to the
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^clear$', views.clear),
]