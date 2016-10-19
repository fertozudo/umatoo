
from random import randint
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def simulation(owner, salary=1000):
    from savings.models import KimoniTransaction
    from savings.models import KIMONI_TRANSACTION_CATEGORIES
    from savings.algorithm import execute_algorithm
    from savings.models import BankTransaction

    # borrado
    KimoniTransaction.objects.filter(owner=owner).delete()
    BankTransaction.objects.filter(owner=owner).delete()

    end_date = date.today()
    start_date = end_date - timedelta(days=290)

    for current_date in daterange(start_date, end_date):
        # execute algorithm
        today_saving = execute_algorithm(owner, current_date)
        if today_saving > 0:
            kimoni_transaction = KimoniTransaction(owner=owner,
                                                   date=current_date,
                                                   category=KIMONI_TRANSACTION_CATEGORIES[2][0],
                                                   amount=today_saving)
            kimoni_transaction.save()
            from savings.models import BANK_TRANSACTION_CATEGORIES
            transaction = BankTransaction(owner=owner,
                                          date=current_date,
                                          category=BANK_TRANSACTION_CATEGORIES[1][0],
                                          amount=-today_saving)
            transaction.save()
        # write bank movement
        create_bank_transaction_random(owner, current_date, salary)


def create_bank_transaction_random(owner, date, salary):
    from savings.models import BankTransaction
    from savings.models import BANK_TRANSACTION_CATEGORIES
    try:
        if date.day == 1:
            transaction = BankTransaction(owner=owner,
                                          date=date,
                                          category=BANK_TRANSACTION_CATEGORIES[0][0],
                                          amount=salary)
            transaction.save()
        if date.day == 3:
            transaction = BankTransaction(owner=owner,
                                          date=date,
                                          category=BANK_TRANSACTION_CATEGORIES[2][0],
                                          amount=-salary/4)
            transaction.save()

        if randint(0,3) == 0:
            transaction = BankTransaction(owner=owner,
                                          date=date,
                                          category=BANK_TRANSACTION_CATEGORIES[randint(3, 6)][0],
                                          amount=-randint(500, 8000)/100)
            transaction.save()

    except Exception as e:
        print e
        return 0
