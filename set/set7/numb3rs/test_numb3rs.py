from numb3rs import validate

def test_first_group_in_range():
    assert validate("0.0.0.0") == True
    assert validate("256.256.256.256") == False


def test_five_byte():
    assert validate("0.0.0.0.0") == False

def test_range():
    assert validate("100.100.100.300") == False
