from twttr import shorten
# import twttr.py from set2 

def test_consonne_lower():
    assert shorten("twitter") == "twttr"

def test_consonne_upper():
    assert shorten("Twitter") == "Twttr"

def test_capitalized_vowels():
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("Hello, you!") == ("Hll, y!")


