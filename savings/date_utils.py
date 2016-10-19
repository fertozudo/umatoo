
def get_month_year(current_date, cycle):
    month, year = (current_date.month - cycle) % 12, current_date.year + (current_date.month - cycle - 1) // 12
    if not month:
        month = 12
    return month, year
