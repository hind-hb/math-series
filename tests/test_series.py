from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import other_values
from math_series.series import sum_series



def test_fibonacciest_one():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacciNigative():
    actual = fibonacci(-5)
    expected = 'Pleas Enter a positive Number'
    assert actual == expected

    
def test_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected




def test_lucasNigative():
    actual = lucas(-5)
    expected = 'Pleas Enter a positive Number'
    assert actual == expected

    

def test_other_values():
    actual = other_values(5,5,3)
    expected = 30
    assert actual == expected


def test_other_valuesNigative():
    actual = other_values(-5,5,3)
    expected = 'Plz Enter a positive Number'
    assert actual == expected

def test_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected