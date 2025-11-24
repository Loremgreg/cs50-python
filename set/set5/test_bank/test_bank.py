from bank import value

def test_hello():
    assert value("hello") == 0

def test_first_letter():
    assert value("hi") == 20

def test_nohello_noh():
    assert value("salut") == 100

def test_case_insensitivity():
    assert value("Hello you") == 0
