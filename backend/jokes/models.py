from django.db import models

# Create your models here.



class Joke(models.Model):
    setup = models.CharField(max_length=10000)
    punchLine = models.CharField(max_length=10000)