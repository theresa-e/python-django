from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Blog object: first_name:{}, last_name:{}, email:{}>".format(self.first_name, self.last_name, self.email)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name="liked_books")
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    def __repr__(self):
        return "<Blog object: Title: {}, Description: {}>".format(self.name, self.desc, self.liked_by, self.uploader)