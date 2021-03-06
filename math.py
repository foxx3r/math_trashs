import unittest
from functools import *


def head(x):
    if len(x) == 0:
        return []
    return x[0]


def tail(xs):
    if len(xs) < 1:
        return []
    return xs[1:]


def fact(n, accumulator=1):
    """
    TAIL RECURSION
    n - object to be factored
    accumulator - the accumulator of the previous state
    """
    if n == 0:
        return accumulator
    else:
        return fact(n - 1, accumulator * n)


def permutate(p, n):
    """
    p - object to be permutated
    n - the length of fields (by elimination)
    """
    return int(fact(p) / fact(p - n))


def combinate(l, p):
    """
    l - length of object
    p - number of possibilities
    """
    return p ** l


def combinate_multiples(l, p):
    """
    l - length of object
    p - list of possibilities for each field

    WARNING
    It's very important that you do not put 0 in the list p
    """
    if l != len(p):
        raise "1st argument must be equal to the length of the 2nd argument"
    return reduce(lambda x, y: x * y, p, 1)


class SuitCase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(fact(5), 5 * 4 * 3 * 2 * 1)

    def test_permutate(self):
        """
        Imagine a scenario where I am gonna choose the five best
        workers of the month, how can I calculate how much combinations
        can it derive from?
        """
        self.assertEqual(permutate(30, 5), 30 * 29 * 28 * 27 * 26)

    def test_combination(self):
        """
        Imagine a scenario where I am gonna calculate how many numbers I can
        writen on a paper that requires three numbers
        """
        self.assertEqual(combinate(3, 10), 10 * 10 * 10)

    def test_combinate_multiples(self):
        self.assertEqual(combinate_multiples(5, [9, 12, 8, 7, 3]), 9 * 12 * 8 * 7 * 3)


if __name__ == '__main__':
    unittest.main()
