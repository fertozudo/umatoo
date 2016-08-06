from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class Target(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    created_by = models.ForeignKey(User)




