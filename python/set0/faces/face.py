def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text


def main():
    prompt = input("Hey ")
    print(convert(prompt))


main()

