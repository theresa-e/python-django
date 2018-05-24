from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['first_name']) < 2:
            errors['first_name'] = "First name should be at least 5 characters long."
        if len(requestPOST['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 5 characters long."
        if len(requestPOST['email']) < 1:
            errors['email'] = "Please enter a valid email address."
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()