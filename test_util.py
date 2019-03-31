# To run:
# python -m unittest test_util

import unittest
import util

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


if __name__ == '__main__':
    unittest.main()