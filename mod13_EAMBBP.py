import unittest
from datetime import datetime

# Validates the symbol
def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

# Validates the Chart Type as either line or bar
def validate_chart_type(chart_type):
    return chart_type in ['line', 'bar']

# Validates time series choice of 1,2,3 or 4
def validate_time_series_choice(time_series_choice):
    return time_series_choice in ['1', '2', '3', '4']

# Validates the date format
def validate_date_format(date_str):
    if len(date_str) != 10:  # Confirms date is a proper length
        return False
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Validates the date range are correct
def validate_date_range(start_date, end_date):
    if not (validate_date_format(start_date) and validate_date_format(end_date)):
        return False
    return datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime(end_date, '%Y-%m-%d')