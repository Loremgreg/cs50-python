vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def main():
    tweet = input("Input: ")
    print(shorten(tweet))


def shorten(tweet):
    vowels_in_tweet = []
    consonne_in_tweet = []
    for letter in tweet:
        if letter in vowels:
            vowels_in_tweet.append(letter)
        else:
            consonne_in_tweet.append(letter)

    final_tweet = "".join(consonne_in_tweet)

    return final_tweet

if __name__ == "__main__":
    main()
