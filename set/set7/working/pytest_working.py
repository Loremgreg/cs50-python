import pytest
from working import convert

def test_hours_off_by_one():
    assert convert("11 AM to 9 PM") == "11:00 to 21:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_min_off_by_five():
    assert convert("9:05 AM to 5:45 PM") == "09:05 to 17:45"


def test_forget_to():
    with pytest.raises(ValueError):
     convert("09 AM 6 PM")

def test_out_of_range():
   with pytest.raises(ValueError):
     convert("13 AM to 6 PM")
   with pytest.raises(ValueError):
     convert("12 AM to 15 PM")

