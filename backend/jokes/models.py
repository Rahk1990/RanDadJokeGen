from django.db import models

# Create your models here.



class Joke(models.Model):
    setup = models.TextField()
    punchLine = models.TextField()