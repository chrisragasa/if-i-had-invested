import unittest
import json
import sys
sys.path.append("..")
import util

# Get test data
with open('testdata_daily.json') as json_file:  
    testdata_daily = json.load(json_file)

with open('testdata_monthly.json') as json_file:  
    testdata_monthly = json.load(json_file)

with open('testdata_error.json') as json_file:  
    testdata_error = json.load(json_file)

class TestUtil(unittest.TestCase):

    def test_dollars_to_shares(self):
        # Testing for Invalid Inputs
        self.assertEqual(util.dollars_to_shares(0, 0), -1)
        self.assertEqual(util.dollars_to_shares(1, 0), -1)
        self.assertEqual(util.dollars_to_shares(-1, 0), -1)
        self.assertEqual(util.dollars_to_shares(0, -1), -1)
        self.assertEqual(util.dollars_to_shares(-1, -1), -1)
        self.assertEqual(util.dollars_to_shares('NaN', 1), -1)
        self.assertEqual(util.dollars_to_shares(1, 'NaN'), -1)
        # Testing for Valid Inputs
        self.assertEqual(util.dollars_to_shares(1, 1), 1)
        self.assertEqual(util.dollars_to_shares(0, 1), 0)
        self.assertEqual(util.dollars_to_shares(10, 5), 2)
        self.assertEqual(util.dollars_to_shares(10, 4), 2)
        self.assertEqual(util.dollars_to_shares(5, 2.5), 2)
        self.assertEqual(util.dollars_to_shares(2.5, 0.5), 5)
    
    def test_shares_to_dollars(self):
        # Testing for Invalid Inputs
        self.assertEqual(util.shares_to_dollars(-1, 0), -1)
        self.assertEqual(util.shares_to_dollars(0, -1), -1)
        self.assertEqual(util.shares_to_dollars(-1, -1), -1)
        self.assertEqual(util.shares_to_dollars(-1, -1), -1)
        self.assertEqual(util.shares_to_dollars('NaN', 1), -1)
        self.assertEqual(util.shares_to_dollars(1, 'NaN'), -1)
        # Testing for Valid Inputs
        self.assertEqual(util.shares_to_dollars(1, 1), 1)
        self.assertEqual(util.shares_to_dollars(0, 1), 0)
        self.assertEqual(util.shares_to_dollars(10, 5), 50)
        self.assertEqual(util.shares_to_dollars(10, 4), 40)
        self.assertEqual(util.shares_to_dollars(5, 2), 10)
        self.assertEqual(util.shares_to_dollars(2.5, 2), 5)

    def test_is_valid_data(self):
        # Testing for invalid data / error message from API call
        self.assertEqual(util._is_valid_data(testdata_error), False)
        # Testing for valid data / stock data from API call
        self.assertEqual(util._is_valid_data(testdata_daily), True)
        self.assertEqual(util._is_valid_data(testdata_monthly), True)
    
    def test_get_prev_price(self):
        # Test for a valid date
        price = testdata_monthly.get("Monthly Time Series").get("2019-03-29").get("4. close")
        self.assertEqual(util.get_prev_price(testdata_monthly, "2019-03"), price)
        # Test for an invalid date
        self.assertEqual(util.get_prev_price(testdata_monthly, "1998-01"), -1)
        # Test for invalid object content
        self.assertEqual(util.get_prev_price(testdata_error, "2019-03"), -1)
        self.assertEqual(util.get_prev_price(testdata_error, "1998-01"), -1)

    def test_get_current_price(self):
        # Test for valid date
        self.assertEqual(float(util.get_current_price(testdata_daily)), 118.0700)
        # Test for invalid object content
        self.assertEqual(util.get_current_price(testdata_error), -1)
        self.assertEqual(util.get_current_price(testdata_error), -1)


if __name__ == '__main__':
    unittest.main()