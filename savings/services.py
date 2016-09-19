def get_bank_transaction_balance(owner):
    from savings.models import BankTransaction
    try:
        return BankTransaction.objects.filter(owner=owner).last().balance
    except:
        return 0

    
def get_kimoni_transaction_balance(owner):
    from savings.models import KimoniTransaction
    try:
        return KimoniTransaction.objects.filter(owner=owner).last().balance
    except:
        return 0
