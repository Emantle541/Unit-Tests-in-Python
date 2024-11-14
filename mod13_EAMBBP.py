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

class TestStockVisualizerInputs(unittest.TestCase):
    
    def test_symbol(self):
        valid_symbols = ["AAPL", "TSLA", "GOOG"]
        invalid_symbols = ["aapl", "APPL123", "TOOLONGSYMBOL"]
        for symbol in valid_symbols:
            self.assertTrue(validate_symbol(symbol), f"Failed on valid symbol: {symbol}")
        for symbol in invalid_symbols:
            self.assertFalse(validate_symbol(symbol), f"Failed on invalid symbol: {symbol}")

    def test_chart_type(self):
        self.assertTrue(validate_chart_type("line"))
        self.assertTrue(validate_chart_type("bar"))
        self.assertFalse(validate_chart_type("3")) 
        self.assertFalse(validate_chart_type(""))

    def test_time_series_choice(self):
        valid_choices = ["1", "2", "3", "4"]
        invalid_choices = ["0", "5", "a"]
        for choice in valid_choices:
            self.assertTrue(validate_time_series_choice(choice), f"Failed on valid time series choice: {choice}")
        for choice in invalid_choices:
            self.assertFalse(validate_time_series_choice(choice), f"Failed on invalid time series choice: {choice}")

    def test_dates_format(self):
        valid_dates = ["2023-01-01", "1990-12-31"]
        invalid_dates = ["2023-1-1", "01-01-2023", "2023-13-01", "abcd-ef-gh"]
        for date_str in valid_dates:
            self.assertTrue(validate_date_format(date_str), f"Failed on valid date: {date_str}")
        for date_str in invalid_dates:
            self.assertFalse(validate_date_format(date_str), f"Failed on invalid date: {date_str}")

    def test_date_range(self):
        self.assertTrue(validate_date_range("2023-01-01", "2023-12-31"))  # Valid range
        self.assertTrue(validate_date_range("2023-01-01", "2023-01-01"))  # Same start and end date
        self.assertFalse(validate_date_range("2023-12-31", "2023-01-01"))  # End date before start date
        self.assertFalse(validate_date_range("2023-01-01", "invalid-date"))  # Invalid end date format
        self.assertFalse(validate_date_range("invalid-date", "2023-01-01"))  # Invalid start date format

if __name__ == '__main__':
    unittest.main()