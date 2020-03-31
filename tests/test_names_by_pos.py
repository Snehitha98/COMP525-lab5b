"""
test_names_by_pos.py
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
        Define attribute p to hold object of type Problems
        """
        self.transform_data = TransformData()

    def test_names_by_pos(self):
        """
        Test case
        """
        actual_result = self.transform_data.names_by_pos()
        expected_result = {
            'PG': ['Stephen Curry', 'Russell Westbrook', 'Chris Paul',
                   'James Harden', 'Kyle Lowry', 'Mike Conley', 'Damian Lillard',
                   'Jrue Holiday', 'Kyrie Irving', 'Zach LaVine', 'John Wall',
                   'Jeff Teague', 'George Hill'],
            'PF': ['Blake Griffin', 'Paul Millsap', 'Al Horford', 'Joel Embiid',
                   'Anthony Davis', 'Giannis Antetokounmpo', 'Kevin Love',
                   'LaMarcus Aldridge', 'Serge Ibaka', 'Aaron Gordon', 'Ryan Anderson',
                   'Jabari Parker'],
            'SF': ['Gordon Hayward', 'Paul George', 'Kevin Durant',
                   'Otto Porter Jr.', 'Andrew Wiggins', 'Chandler Parsons',
                   'Harrison Barnes', 'Kawhi Leonard', 'Danilo Gallinari'],
            'SG': ['DeMar DeRozan', 'CJ McCollum', 'Bradley Beal', 'Nicolas Batum',
                   'Victor Oladipo', 'Jimmy Butler', 'Tyler Johnson', 'Klay Thompson',
                   'Wesley Matthews'],
            'C': ['Hassan Whiteside', 'Nikola Jokic', 'Steven Adams',
                  'Marc Gasol', 'Rudy Gobert', 'DeAndre Jordan', 'Enes Kanter']
        }
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
