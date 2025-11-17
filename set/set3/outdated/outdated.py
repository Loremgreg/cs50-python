# USA: MM/DD/YYYY
# international: YYYY-MM-DD

# Ask user input month-day-year : formatted like 9/8/1636 or September 8, 1636
# if not valid input prompt again
# Output in YYYY-MM-DD format

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date_user_input = input("Date: ")
            year, month, day = parse_date(date_user_input)
            print(f"{year}-{month:02}-{day:02}")
            break
        except ValueError:
             pass

def parse_date(date_user_input):
        try:
            if "/" in date_user_input:
                month, day, year = date_user_input.split("/")
                # separe 4 5 1999

            elif "," in date_user_input:
                month_day, year = date_user_input.split(", ")
                 # Sépare "September" et  "8"
                month_name, day = month_day.split(" ")
                # month_list.index(month_name) trouve la position (qui commence à 0).
                # On ajoute 1 car les mois commencent pas a 0.
                month = month_list.index(month_name) + 1

            elif not ("," or "/") in date_user_input:
                 raise ValueError

            day, month, year = int(day), int(month), int(year)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                    raise ValueError
            return year, month, day

        except (KeyError, ValueError):
            raise ValueError("Invalid date")

main()

