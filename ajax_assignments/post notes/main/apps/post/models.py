from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)