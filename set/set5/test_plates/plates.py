def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (starts_with_two_letters(s) and has_valid_length(s) and end_numbers(s) and is_alphanumeric(s))

def starts_with_two_letters(s):
    two_letters = s[0:2]
    if two_letters.isalpha():
        return True
    else:
        return False

def has_valid_length(s):
    length = len(s)
    if 2 <= length <= 6:
        return True
    else:
        return False

def end_numbers(s):
    for index, char in enumerate(s):
        if char.isdigit():
            end_plate = s[index:]
            if end_plate.isdigit() and end_plate[0] != "0":
                    return True
            else:
                return False
    return True

def is_alphanumeric(s):
    if s.isalnum():
        return True
    else:
        return False

if __name__ == "__main__":
    main()
