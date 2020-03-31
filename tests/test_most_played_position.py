"""
test_most_played_position.py
Snehitha Mamidi
March 30, 2020
"""

import unittest
from problems.transformdata import TransformData

class TestNamesByPosition(unittest.TestCase):
    """
    Test for names_by_pos() method
    """
    def setUp(self):
        """
        Define attribute transform_data to hold object of type Problems
        """
        self.transform_data = TransformData()

    def test_most_played_position(self):
        """
        Test case
        """
        actual_result = self.transform_data.most_played_position()
        expected_result = {'PG': 13, 'PF': 12, 'SF': 9, 'SG': 9, 'C': 7}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
