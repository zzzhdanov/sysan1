import csv


def get_item(filename, string_number, column_number):
    num = 0
    
    if string_number < 0 or column_number < 0:
        raise ValueError("OUT OF RANGE")

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            num += 1
            if num == string_number + 1:
                return row[column_number - 1]


print(get_item("test.csv", string_number=4, column_number=2))
