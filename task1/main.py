import csv
from typing import Optional


def get_item(filename: str, string_number: int, column_number: int) -> Optional[str]:
    """
        Returns an element from a csv table

    :param filename: file path
    :param string_number: number of string
    :param column_number: number of column

    :return: str
    """

    if string_number <= 0 or column_number <= 0:
        raise ValueError("Incorrect string number or column number")

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for index, row in enumerate(reader):
            if column_number > len(row):
                return None
            if index == string_number:
                return row[column_number - 1]


assert get_item("test.csv", string_number=1, column_number=1) == "sw1"
assert get_item("test.csv", string_number=1, column_number=4) == "London"
assert get_item("test.csv", string_number=1, column_number=15) is None
