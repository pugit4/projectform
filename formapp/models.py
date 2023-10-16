from django.db import models

# Create your models here.
class application(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    about = models.TextField()