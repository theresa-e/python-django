from django.conf.urls import url
from . import views

# Must include links to the
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create_post$', views.create_post),
    url(r'^delete/(?P<id>\d+)$', views.delete_post),

]