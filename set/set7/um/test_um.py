from um import count

def test_maj():
    assert count("Um") == True

def test_in_words():
    assert count("pneumonoultramicroscopicsilicovolcanoconiosis") == False

