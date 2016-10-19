from django.db.models import Sum


# Bank transaction
from savings.date_utils import get_month_year


def get_bank_transaction_balance(owner):
    from savings.models import BankTransaction
    try:
        return BankTransaction.objects.filter(owner=owner).last().balance
    except:
        return 0


def get_expenses_in_cycle(owner, current_date, cycle):
    from savings.models import BankTransaction
    month, year = get_month_year(current_date, cycle)
    return BankTransaction.objects\
        .filter(owner=owner, amount__lt=0, date__month=month, date__year=year) \
        .exclude(category='Kimoni')\
        .aggregate(Sum('amount')).get('amount__sum')


def get_incomes_in_cycle(owner, current_date, cycle):
    from savings.models import BankTransaction
    month, year = get_month_year(current_date, cycle)
    return BankTransaction.objects\
        .filter(owner=owner, amount__gt=0, date__month=month, date__year=year)\
        .aggregate(Sum('amount')).get('amount__sum')


# Kimoni transaction
def get_kimoni_transaction_balance(owner):
    from savings.models import KimoniTransaction
    try:
        return KimoniTransaction.objects.filter(owner=owner).last().balance
    except:
        return 0


def get_savings_in_cycle(owner, current_date, cycle):
    from savings.models import KimoniTransaction
    month, year = get_month_year(current_date, cycle)
    return KimoniTransaction.objects\
        .filter(owner=owner, amount__gt=0, date__month=month, date__year=year)\
        .aggregate(Sum('amount')).get('amount__sum')

