from django.contrib.auth.models import User
from django.db import models


class UnsafeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plaintext_password = models.CharField(max_length=100)
