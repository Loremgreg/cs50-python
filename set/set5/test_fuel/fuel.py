def main():
    while True:
        try:
            fraction_input = input("Fraction: ")

            percentage = convert(fraction_input)
            print(gauge(percentage))
            break

        except ZeroDivisionError:
            print("You cannot divide by 0")
            continue

        except ValueError:
            print("Enter a valid fraction")
            continue


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    if x < 0 or y < 0:
        raise ValueError("Enter a valid fraction")
    if y == 0:
        raise ZeroDivisionError("You cannot divide by 0")
    if x > y:
        raise ValueError("Enter a valid fraction")
    return round((x / y) * 100)

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

