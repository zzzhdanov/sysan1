import csv


def get_item(filename, string_number, column_number):

    if string_number < 0 or column_number < 0:
        raise ValueError("OUT OF RANGE")

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for index, row in enumerate(reader):
            if index == string_number:
                return row[column_number - 1]


print(get_item("test.csv", string_number=4, column_number=2))
