import csv
from external_sort import external_sort

def process_select(parsed):
    table = parsed['table']
    conditions = parsed['conditions']
    sorted_file = external_sort(table, conditions)

    with open(sorted_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if all(str(row[col]) == val for col, val in conditions):
                print(row)