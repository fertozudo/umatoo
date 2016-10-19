from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User



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
    control_mode = models.BooleanField(default=False)
    # Attributes
    risky = models.IntegerField(default=0, choices=LEVELS)
    steady = models.IntegerField(default=0, choices=LEVELS)
    income = models.IntegerField(default=0, choices=LEVELS)
    consumption = models.IntegerField(default=0, choices=LEVELS)
    saving_capacity = models.IntegerField(default=0, choices=LEVELS)


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


BANK_TRANSACTION_CATEGORIES = (
    ('Salary', 'Salary'),
    ('Kimoni', 'Kimoni'),
    ('TV/Phone/Internet', 'TV/Phone/Internet'),
    ('Water/Gas/Electricity', 'Water/Gas/Electricity'),
    ('Restaurants', 'Restaurants'),
    ('Gym', 'Gym'),
    ('Other', 'Other')
)


class BankTransaction(SavingsBaseModel):
    date = models.DateField()
    category = models.CharField(max_length=30, choices=BANK_TRANSACTION_CATEGORIES)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, editable=False)

    def save(self, *args, **kwargs):
        from savings.services import get_bank_transaction_balance
        self.balance = get_bank_transaction_balance(self.owner) + self.amount
        super(BankTransaction, self).save(*args, **kwargs)

KIMONI_TRANSACTION_CATEGORIES= (
    ('User request', 'User request'),
    ('Kimoni suggestion', 'Kimoni suggestion'),
    ('Kimoni algorithm', 'Kimoni algorithm'),
)


class KimoniTransaction(SavingsBaseModel):
    target = models.ForeignKey(Target, editable=False, null=True)
    date = models.DateField()
    category = models.CharField(max_length=30, choices=KIMONI_TRANSACTION_CATEGORIES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, editable=False)

    def save(self, *args, **kwargs):
        from savings.services import get_kimoni_transaction_balance
        self.balance = get_kimoni_transaction_balance(self.owner) + self.amount
        super(KimoniTransaction, self).save(*args, **kwargs)








