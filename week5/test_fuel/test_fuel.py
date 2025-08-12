from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("3/4") == 75
    assert convert("0/1") == 0

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("3/1")
    with pytest.raises(ValueError):
        convert("abc/xyz")  # Invalid input

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
