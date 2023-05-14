import pytest

def fizzbuzz(N):
    if N%2 == 0:
        return "fizz"
    else:
        return "buzz"

def test_fizzbuzz():
    assert fizzbuzz(2) == "fizz"

