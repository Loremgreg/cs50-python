import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    match = re.findall(pattern, s, re.IGNORECASE)

    um_count = 0
    for um in match:
        um_count += 1

    return um_count

if __name__ == "__main__":
    main()
