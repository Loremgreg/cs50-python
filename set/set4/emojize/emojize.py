import emoji
# pip install emoji


def main():
    user_input = input()

    output = emojized(user_input)
    print(output)

def emojized(user_input):
    emo = emoji.emojize(user_input, language='alias')
    return emo

main()
