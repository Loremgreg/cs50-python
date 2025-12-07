from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(5)
    assert jar.capacity == 5

def test_init_ValueError():
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar(4)
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.withdraw(7)
        