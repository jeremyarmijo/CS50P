from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("10/3")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("50-40")
    with pytest.raises(ZeroDivisionError):
        convert("11/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(40) == "40%"
    assert gauge(98) == "98%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(2) == "2%"