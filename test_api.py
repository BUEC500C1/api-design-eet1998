import pytest
from find_city import find_city

def test_good_1():
    assert find_city("Pickles Airport") == "Berryville"

def test_good_2():
    assert find_city("Lake Persimmon Airstrip") == "Lake Placid"

def test_good_3():
    assert find_city("Spotts Field") == "Nora Springs"

def test_bad():
    assert find_city("Hello World") == 0

if __name__ == "__main__":
    test_good_1()
    test_good_2()
    test_good_3()
    test_bad()