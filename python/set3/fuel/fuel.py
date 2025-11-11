def main():
    while True:
        try:
            fraction_input = input("Fraction: ")
            x, y = fraction_input.split("/")
            x, y = int(x), int(y)
            percentage = convert_to_percentage(x, y)
            print(format_percentage(percentage))
            break

        except (ZeroDivisionError, ValueError):
            continue


def convert_to_percentage(x, y):

    if x < 0 or y < 0:
        raise ValueError("Enter a valid fraction")
    if y == 0:
        raise ZeroDivisionError("You cannot divide by 0")
    if x > y:
        raise ValueError("Enter a valid fraction")
    return round((x / y) * 100)

def format_percentage(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


main()

