import sys
from tabulate import tabulate
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_name = sys.argv[1]

if not file_name.endswith('.csv'):
        sys.exit("Not a CSV file")

elif len(sys.argv) == 2:
    try:
        with open(file_name, newline='') as csvfile:
            table = csv.reader(csvfile)
            print(tabulate(table, headers="firstrow"))
    except FileNotFoundError:
            sys.exit("File does not exist")

