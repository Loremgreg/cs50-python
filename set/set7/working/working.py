import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # pattern = r"""
    # ^
    #     # ----- START TIME -----
    #     (\d{1,2})        # → heures à 1 ou 2 chiffres (9, 12, 05…)
    #     (?:
    #         :(\d{2})     # → minutes optionnelles: ": littéral"  "	
    #     )?               # 
    #     \s               # space before AM/PM
    #     (AM|PM)          # period

    #     \s+to\s+         # literal " to " with spaces allowed

    #     # ----- END TIME -----
    #     (\d{1,2})        # hours (1–2 digits)
    #     (?:
    #         :(\d{2})     # optional minutes (exactly 2 digits)
    #     )?
    #     \s               # space before AM/PM
    #     (AM|PM)
    #                     ## ce pattern capture 6 groupes 
    # $
    # """    

    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    hour1, min1, ap1, hour2, min2, ap2 = match.groups()
    hour1 = int(hour1)
    hour2 = int(hour2)
    min1 = int(min1) if min1 is not None else 0
    min2 = int(min2) if min2 is not None else 0


    if not 1 <= hour1 <= 12:
        raise ValueError
    if not 1 <= hour2 <= 12:
        raise ValueError
    if not 0 <= min1 <= 59:
        raise ValueError
    if not 0 <= min2 <= 59:
        raise ValueError

    def convert_to_24(hour, min, ap):
        if ap == "PM":
            if hour != 12:
                hour = hour + 12
        if ap == "AM":
            if hour == 12:
                hour = 0
        return f"{hour:02}:{min:02}"


    starting_hour = convert_to_24(hour1, min1, ap1)
    ending_hour = convert_to_24(hour2, min2, ap2)

    return f"{starting_hour} to {ending_hour}"




if __name__ == "__main__":
    main()


