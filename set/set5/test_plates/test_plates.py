from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("34rtty67"[0:2]) == False

def test_has_valid_length():
    assert is_valid("q") == False
    assert is_valid("we34rtyu") == False

def test_end_numbers():
    assert is_valid("C5Y0") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50A") == False


def test_is_alphanumeric():
    assert is_valid("CS!50") == False
