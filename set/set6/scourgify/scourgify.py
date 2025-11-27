import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

if len(sys.argv) == 3:
    try:
        with open(file_to_read, newline='') as csvrfile:
            reader = csv.DictReader(csvrfile)

            with open(file_to_write, 'w', newline='') as csvwfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvwfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    name = row['name']
                    house = row['house']
                    last, first = row["name"].split(",")
                    last, first  = last.strip(), first.strip()
                    writer.writerow({"first": first, "last": last, "house": house})


    except FileNotFoundError:
        sys.exit(f"Could not read {file_to_read}")



