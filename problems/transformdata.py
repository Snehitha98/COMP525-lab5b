"""
dataset.py
Mihaela
March 11, 2020
"""


class TransformData():
    """
    Data processing functionality
    """

    def __init__(self):
        """
        Creates and initializes the class attributes.
        Attributes: three parallel lists
            names: list of strings
            salaries: list of integers
            positions: list of 2-character strings
        """
        self.names = [
            'Stephen Curry', 'Russell Westbrook', 'Chris Paul', 'James Harden',
            'Blake Griffin', 'Gordon Hayward', 'Kyle Lowry', 'Paul George',
            'Mike Conley', 'Kevin Durant', 'Paul Millsap', 'Al Horford',
            'Damian Lillard', 'DeMar DeRozan', 'Otto Porter Jr.',
            'Jrue Holiday', 'CJ McCollum', 'Joel Embiid', 'Andrew Wiggins',
            'Bradley Beal', 'Anthony Davis', 'Hassan Whiteside',
            'Nikola Jokic', 'Steven Adams', 'Giannis Antetokounmpo',
            'Marc Gasol', 'Kevin Love', 'Chandler Parsons', 'Harrison Barnes',
            'Nicolas Batum', 'Rudy Gobert', 'Kawhi Leonard', 'DeAndre Jordan',
            'LaMarcus Aldridge', 'Serge Ibaka', 'Aaron Gordon',
            'Danilo Gallinari', 'Victor Oladipo', 'Jimmy Butler',
            'Ryan Anderson', 'Kyrie Irving', 'Jabari Parker', 'Zach LaVine',
            'Tyler Johnson', 'John Wall', 'Jeff Teague', 'George Hill',
            'Klay Thompson', 'Enes Kanter', 'Wesley Matthews'
        ]
        self.salaries = [
            37457154, 35654150, 35654150, 35650150, 32088932, 31214295,
            31200000, 30560700, 30521115, 30000000, 29230769, 28928709,
            27977689, 27739975, 26011913, 25976111, 25759766, 25467250,
            25467250, 25434263, 25434263, 25434262, 24605181, 24157303,
            24157303, 24119025, 24119025, 24107258, 24107258, 24000000,
            23241573, 23114067, 22897200, 22347015, 21666667, 21590909,
            21587579, 21000000, 20445779, 20421546, 20099189, 20000000,
            19500000, 19245370, 19169800, 19000000, 19000000, 18988725,
            18622514, 18622514
        ]
        self.positions = [
            'PG', 'PG', 'PG', 'PG', 'PF', 'SF', 'PG', 'SF', 'PG', 'SF', 'PF',
            'PF', 'PG', 'SG', 'SF', 'PG', 'SG', 'PF', 'SF', 'SG', 'PF', 'C',
            'C', 'C', 'PF', 'C', 'PF', 'SF', 'SF', 'SG', 'C', 'SF', 'C', 'PF',
            'PF', 'PF', 'SF', 'SG', 'SG', 'PF', 'PG', 'PF', 'PG', 'SG', 'PG',
            'PG', 'PG', 'SG', 'C', 'SG'
        ]


    def record_per_row(self):
        """
        Writes a CSV file with as many records as the size of any of the lists
        A record is a row in the file, with three columns, corresonding to
        a name, salary, and position.
        """
        with open('nba.txt', 'w') as nba_file:
            for name, salary, position in zip(
                    self.names, self.salaries, self.positions
            ):
                nsp_row = name + ',' + str(salary) + ',' + position + '\n'
                nba_file.write(nsp_row)


    @classmethod
    def names_by_pos(cls):
        """
        Create a dictionary keyed by positions and values are lists
        of the names corresponding to each position.
        Returns : dictionary
           keys are positions
           values are list of names that correspond to that position
        """
        file_ref = open("nba.txt", "r")
        names_by_pos = {}
        for line in file_ref.readlines():
            lst = line.split(",")
            a_name = lst[0]
            a_position = lst[2]
            a_position = a_position.replace("\n", "")
            if a_position in names_by_pos:
                names_by_pos[a_position] += [a_name]
            else:
                names_by_pos[a_position] = [a_name]
        file_ref.close()
        return names_by_pos


    @classmethod
    def most_played_position(cls):
        """
        call names_by_pos(self), use the dictionary to create a new dictionary
        whose keys are the positions and the values are the lengths of the
        lists of players for each position.
        input : dictionary
           keys are positions
           values are list of names that correspond to that position
        Returns : dictionary
           keys are positions
           values are lengths of the lists of players for each position
        """
        names_by_pos = TransformData().names_by_pos()
        most_played_position = {}
        for key in names_by_pos:
            len_of_list = len(names_by_pos[key])
            most_played_position[key] = len_of_list
        return most_played_position


def main():
    """
    main function to execute function calls
    """
    TransformData().record_per_row()
    result = TransformData().names_by_pos()
    print(f'names_by_pos returns {result}')
    result = TransformData().most_played_position()
    print(f'most_played_position returns {result}')


if __name__ == '__main__':
    main()
