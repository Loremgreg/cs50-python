    import pytest
from fuel import convert, gauge

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("5/2")

def test_convert_zerro_error():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_negative_number():
    with pytest.raises(ValueError):
        convert("-2/-1")

def test_convert():
    assert convert("1/2") == 50

def test_gauge_e():
    assert gauge(1) == "E"

def test_gauge_f():
    assert gauge(99) == "F"

def test_gauge():
    assert gauge(50) == "50%"
