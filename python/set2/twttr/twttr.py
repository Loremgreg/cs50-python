vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

tweet = input("Input: ")
vowels_in_tweet = []
consonne_in_tweet = []


for letter in tweet:
    if letter in vowels:
        vowels_in_tweet.append(letter)
    else:
        consonne_in_tweet.append(letter)

final_tweet = "".join(consonne_in_tweet)

print(final_tweet, end="")

