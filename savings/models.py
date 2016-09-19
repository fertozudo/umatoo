from __future__ import unicode_literals



from django.db import models

from django.contrib.auth.models import User


# USER INFORMATION
from core.admin import admin_site


class ProfileUser(models.Model):
    LEVELS = (
        (1, 'very low'),
        (2, 'low'),
        (3, 'medium'),
        (4, 'high'),
        (5, 'very high'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    notification_days_frequency = models.IntegerField(default=7)
    # Attributes
    risky = models.IntegerField(default=0, choices=LEVELS)
    steady = models.IntegerField(default=0, choices=LEVELS)
    purchasing_power = models.IntegerField(default=0, choices=LEVELS)



# BASE MODEL
class SavingsBaseModel(models.Model):
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# SAVINGS MODELS
class Target(SavingsBaseModel):
    name = models.CharField(max_length=100)
    target_amount = models.IntegerField(default=0)
    achieved_amount = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    achieved_date = models.DateField(null=True, blank=True)



class BankTransaction(SavingsBaseModel):
    CATEGORIES = (
        ('TV/Phone/Internet', 'TV/Phone/Internet'),
        ('Water/Gas/Electricity', 'Water/Gas/Electricity'),
        ('Restaurants', 'Restaurants'),
        ('Gym', 'Gym'),
        ('Other', 'Other')
    )
    date = models.DateField()
    category = models.CharField(max_length=30, choices=CATEGORIES)
    description = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    balance = models.IntegerField(default=0, editable=False)



class KimoniTransaction(SavingsBaseModel):
    CATEGORIES = (
        ('User request', 'User request'),
        ('Kimoni suggestion', 'Kimoni suggestion'),
        ('Kimoni algorithm', 'Kimoni algorithm'),
    )
    target = models.ForeignKey(Target, editable=False)
    date = models.DateField()
    category = models.CharField(max_length=30, choices=CATEGORIES)
    amount = models.IntegerField(default=0)
    balance = models.IntegerField(default=0, editable=False)









