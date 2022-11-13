"""
Week 3 Homework - Functions
"""
import typing


def filter_even(number_list: typing.List[int]) -> typing.List[int]:
    """
    Problem 1 - Filtering a list
    ---------
    Given an input list of integers, return a new list of only the even
    numbers in that list.

    e.g. filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    """
    raise NotImplementedError()


def reverse_string(input_string: str) -> str:
    """
    Problem 2 - Reversing a string
    ---------
    Given an input string, return the string in reverse. There are a
    number of ways to implement this!

    e.g. reverse_string("123abc") == "cba321"

    Hint:
      strings are "iterable", and can be thought of as lists of
      characters:  "abc" == ['a', 'b', 'c']
      help(slice)

    Hint:
      help(list.pop)
    """
    raise NotImplementedError()


class RomanNumeral():
    """
    Problem 3 - Finish implementing this class's functions.
    ---------
    Numbers in this system are represented by combinations of letters
    from the Latin alphabet. They can only represent positive integers
    for the purposes of this exercise.

    More details: https://en.wikipedia.org/wiki/Roman_numerals

    Symbol   I    V    X    L    C    D    M
    Value    1    5    10   50   100  500  1000

    e.g.
      III == 3
      IV == 4
      MMXXII == 2022
    """
    def __init__(self, *, numeral: str):
        """
        Create an object instance of this class.
        """
        if not RomanNumeral.is_valid(numeral):
            raise ValueError(f'[{self.numeral}] is not valid!')
        self.numeral = numeral.upper()

    @staticmethod
    def is_valid(numeral: str) -> bool:
        """
        Return True if and only if given value is a valid Roman Numeral.

        This is not trivial: https://projecteuler.net/about=roman_numerals

          Legal characters: ['IVXLCDM']
          (1) Numerals must be arranged in descending order of size.
          (2) M, C, and X cannot be equalled or exceeded by smaller
              denominations.
          (3) D, L, and V can each only appear once.

        A smaller number in front of a larger number means subtraction,
        all else means addition. For example, IV means 4, VI means 6.

        e.g.:
          RomanNumeral.is_valid('ABC')  # -> False - illegal chars
          RomanNumeral.is_valid('VM')   # -> False - violates rule 1
          RomanNumeral.is_valid('IXI')  # -> False - violates rule 2
          RomanNumeral.is_valid('DDX')  # -> False - violates rule 3
          RomanNumeral.is_valid('XIX')  # -> True - 19
          RomanNumeral.is_valid('MCMVII')  # -> True - 1907

        Note:
          This is a static method - it doesn't have access to {self},
          just {numeral}

        Args:
          numeral: the roman numeral as a string to test
        """
        raise NotImplementedError()

    def __int__(self) -> int:
        """
        Return the equivalent value in self.numeral as a number.
        """
        raise NotImplementedError()

    @classmethod
    def from_str(cls, numeral: str) -> 'RomanNumeral':
        """
        Create a RomanNumeral object from a string representation.
        """
        return cls(numeral=numeral)

    @classmethod
    def from_int(cls, number: int) -> 'RomanNumeral':
        """
        Create a RomanNumeral object from a given number.
        """
        # numeral = ... number ...
        # return cls(numeral=numeral)
        raise NotImplementedError()

    def __str__(self) -> str:
        """
        This is a special function that Python calls when you call
        str() on an object of this class.
        """
        return self.numeral

    def __bool__(self) -> bool:
        """
        If the numeral is an empty string, that makes it '0', and False-y.
        """
        return self.numeral == ''

    def __eq__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects for equality.

        e.g. (self == other)
        """
        return int(self) == int(other)

    def __ne__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects for non-equality.

        e.g. (self != other)
        """
        return int(self) != int(other)

    def __le__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects using less than or equal to.

        e.g. (self <= other)
        """
        raise NotImplementedError()

    def __lt__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects using less than.

        e.g. (self < other)
        """
        raise NotImplementedError()

    def __ge__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects using greather than or equal to.

        e.g. (self <= other)
        """
        raise NotImplementedError()

    def __gt__(self, other: 'RomanNumeral') -> bool:
        """
        Used to compare two objects using greater than.

        e.g. (self <= other)
        """
        raise NotImplementedError()

    def __add__(self, other: 'RomanNumeral') -> 'RomanNumeral':
        """
        Used to add two numerals together.
        """
        return RomanNumeral.from_int(int(self) + int(other))

    def __mul__(self, other: 'RomanNumeral') -> 'RomanNumeral':
        """
        Used to multiply two numerals together.
        """
        return RomanNumeral.from_int(int(self) * int(other))
