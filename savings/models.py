from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField()
    gender = models.MultipleChoiceField(choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))


class SavingsBaseModel(models.Model):
    owner = models.ForeignKey(User, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Target(SavingsBaseModel):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    days = models.IntegerField(default=0)





