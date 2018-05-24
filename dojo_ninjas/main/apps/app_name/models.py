from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    desc = models.CharField(max_length=255, default="Description")

class Ninja(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dojo = models.ForeignKey(Dojo, related_name="ninja")
