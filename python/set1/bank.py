def greetings():
    hello = input("Hey! ").strip().lower()

    if "hello" in hello:
        print("$0")
    elif hello.startswith("h"):
        print("$20")
    else:
        print("$100")

greetings()
