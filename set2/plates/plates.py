def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if first_letter(s) and check_length(s) and end_numbers(s) and alnum(s) == True:
        return True
    else:
        return False

def first_letter(s):
    two_letters = s[0:2]
    if two_letters.isalpha():
        return True
    else:
        return False

def check_length(s):
    lenght = len(s)
    if 2 <= lenght <= 6:
        return True
    else:
        return False

def end_numbers(s):
    for i in s:
        if i.isdigit():
            end_plate = s[i:]
    if end_plate.isdigit() and end_plate[0] != "0":
        return True
    else:
        return False

def alnum(s):
    is_alnum = s.isalnum()
    if is_alnum:
        return True
    else:
        return False

main()
