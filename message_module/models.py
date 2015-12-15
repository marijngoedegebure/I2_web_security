from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField("text", max_length=200)
