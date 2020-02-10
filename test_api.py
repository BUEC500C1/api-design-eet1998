import pytest
from weather_api import api_call
from find_city import find_city

def test_good_1():
    assert find_city("Pickles Airport") == "Berryville"

if __name__ == "__main__":
    test_good_1()