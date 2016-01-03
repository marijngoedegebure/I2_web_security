from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UnsafeUser(models.Model):
    username = models.CharField('username', max_length=100)
    password = models.CharField('password', max_length=100)
    is_admin = models.BooleanField('is admin', default=False)
