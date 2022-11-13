# ----------------------------------
# Tests
# ----------------------------------

import pytest

from homework.functions import (
    filter_even,
    reverse_string,
    RomanNumeral,
)


# --------------------------------------------------
def test_filter_even():
    assert filter_even([1, 2, 3, 5, 7, 8, 9]) == [2, 8]
    assert filter_even(list(range(10))) == [0, 2, 4, 6, 8]
    assert filter_even([]) == []


# --------------------------------------------------
def test_reverse_string():
    assert reverse_string('abcdef') == 'fedcba'
    assert reverse_string('spaces & things') == 'sgniht & secaps'

# --------------------------------------------------
@pytest.fixture
def roman_numeral_1901() -> RomanNumeral:
    return RomanNumeral.from_str('MCMI')

@pytest.fixture
def roman_numeral_2022() -> RomanNumeral:
    return RomanNumeral.from_str('MMXXII')

@pytest.fixture
def roman_numeral_2023() -> RomanNumeral:
    return RomanNumeral.from_str('MMXXIII')

@pytest.fixture
def roman_numeral_mixed_case() -> RomanNumeral:
    return RomanNumeral.from_str('clIX')

@pytest.fixture
def roman_numeral_19_str() -> RomanNumeral:
    return RomanNumeral.from_str('XiX')

@pytest.fixture
def roman_numeral_19_int() -> RomanNumeral:
    return RomanNumeral.from_int(19)

# --------------------------------------------------
def test_roman_numeral_1901(roman_numeral_1901):
    assert int(roman_numeral_1901) == 1901

def test_roman_numeral_2022(roman_numeral_2022):
    assert int(roman_numeral_2022) == 2022
    assert str(roman_numeral_2022) == 'MMXXII'

def test_roman_numeral_mixed_case(roman_numeral_mixed_case):
    assert str(roman_numeral_mixed_case) == 'CLIX'

def test_roman_numeral_19(roman_numeral_19_int, roman_numeral_19_str):
    assert str(roman_numeral_19_int) == 'XIX'
    assert roman_numeral_19_int == roman_numeral_19_str

def test_roman_numeral_comparison(roman_numeral_19_str, roman_numeral_2022):
    assert roman_numeral_2022 >= roman_numeral_19_str
    assert roman_numeral_2022 > roman_numeral_19_str
    assert roman_numeral_2022 != roman_numeral_19_str
    assert roman_numeral_19_str <= roman_numeral_2022
    assert roman_numeral_19_str < roman_numeral_2022

def test_roman_numeral_math(roman_numeral_19_str, roman_numeral_2022):
    assert int(roman_numeral_19_str + roman_numeral_2022) == 2041
    assert int(roman_numeral_19_str * roman_numeral_2022) == 38418
