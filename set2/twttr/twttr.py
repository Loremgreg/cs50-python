vowels = ["a", "e", "i", "o", "u"]

tweet = input("Input: ").lower()
new_tweet = []
final_tweet = "".join(new_tweet)

for letter in tweet:
    if letter in vowels:
        tweet.replace(letter, "")
    else:
        new_tweet.append(letter)

print(f"Output: {new_tweet}")

