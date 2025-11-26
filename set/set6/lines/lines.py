import sys


def main():
    count = counting_lines()
    print(count)

def counting_lines():
    number_of_lines = []
    comment_lines = []
    blank_lines = []

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]

    if not file_name.endswith('.py'):
        sys.exit("Not a Python file")

    elif len(sys.argv) == 2:
        try:
            with open(file_name, "r") as file:
            # readlines() give back the lines as items in a list
                lines = file.readlines()
        except FileNotFoundError:
                sys.exit("File does not exist")


        for line in lines:
            # lstrip() supprime tous les espaces avant de tester (#)
            if line.lstrip().startswith("#"):
                comment_lines.append(line)
            elif line.lstrip() == "":
                blank_lines.append(line)
            else:
                number_of_lines.append(line)
        # print(len(number_of_lines))
        # print(len(comment_lines))
        # print(len(blank_lines))
        return len(number_of_lines)

main()


