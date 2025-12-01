from seasons import parse_date, calc_minutes, minutes_to_words
from datetime import date
import pytest

def test_parse_date_valid():
    assert parse_date("2000-10-25") == date(2000, 10, 25)

def test_parse_date_invalid():
    with pytest.raises(SystemExit):
        parse_date("25-10-2000")

def test_minutes_to_words():
    assert minutes_to_words("20566080") == "Twenty million, five hundred sixty-six thousand eighty"
