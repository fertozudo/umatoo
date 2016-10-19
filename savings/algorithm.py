from savings.services import get_expenses_in_cycle, get_incomes_in_cycle, get_savings_in_cycle, \
    get_bank_transaction_balance
from calendar import monthrange

FLOOR_BALANCE = 300
CYCLE = 1  # month
NUMBER_OF_CYCLES_TO_CALCULATE_AVERAGE = 3  # months


def execute_algorithm(owner, current_date):
    # 1. Max Saving calculation

    if get_bank_transaction_balance(owner)<FLOOR_BALANCE:
        return 0

    average_cycle_expenses = calculate_average_cycle_expenses(owner, current_date)
    average_cycle_incomes = calculate_average_cycle_incomes(owner, current_date)
    current_cycle_expenses = calculate_current_cycle_expenses (owner, current_date)
    current_cycle_incomes = calculate_current_cycle_incomes(owner, current_date)

    max_saving_by_cycle = average_cycle_incomes+average_cycle_expenses

    if current_cycle_expenses < average_cycle_expenses:
        max_saving_by_cycle = current_cycle_incomes+current_cycle_expenses

    if max_saving_by_cycle < 0:
        return 0

    savings_current_month = calculate_savings_current_month(owner, current_date)
    days_to_save_in_current_month = calculate_days_to_save_in_current_month(current_date)
    today_max_saving = (max_saving_by_cycle - savings_current_month) / days_to_save_in_current_month

    # 2. Adjustment by User profile Parameters
    today_saving = today_max_saving * 1

    return today_saving


def calculate_average_cycle_expenses(owner, current_date):
    total_expenses = 0
    for i in range(NUMBER_OF_CYCLES_TO_CALCULATE_AVERAGE):
        cycle = i + 1
        total_expenses = total_expenses + (get_expenses_in_cycle(owner, current_date, cycle) or 0)
    result = total_expenses/NUMBER_OF_CYCLES_TO_CALCULATE_AVERAGE
    return result


def calculate_average_cycle_incomes(owner, current_date):
    total_incomes = 0
    for i in range(NUMBER_OF_CYCLES_TO_CALCULATE_AVERAGE):
        cycle = i + 1
        total_incomes = total_incomes + (get_incomes_in_cycle(owner, current_date, cycle) or 0)
    result = total_incomes / NUMBER_OF_CYCLES_TO_CALCULATE_AVERAGE
    return result


def calculate_current_cycle_expenses (owner, current_date):
    cycle = 0
    result = (get_expenses_in_cycle(owner, current_date, cycle) or 0)
    return result


def calculate_current_cycle_incomes(owner, current_date):
    cycle = 0
    result = (get_incomes_in_cycle(owner, current_date, cycle) or 0)
    return result


def calculate_savings_current_month(owner, current_date):
    cycle = 0
    result = (get_savings_in_cycle(owner, current_date, cycle) or 0)
    return result


def calculate_days_to_save_in_current_month(current_date):
    return monthrange(current_date.year,current_date.month)[1]-(current_date.day-1)
