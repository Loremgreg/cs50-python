from validator_collection import checkers

def main():

    user_email = input("Email: ")

    if checkers.is_email(user_email):
        print("Valid")
    else:
        print("Invalid")

main()
