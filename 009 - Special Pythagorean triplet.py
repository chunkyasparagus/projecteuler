"""https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

A Pythagorean triplet is a set of three natural numbers, a < b < c for which a^2 + b^2 = c^2

Given N, check if there exists any Pythagorean triplet for which a + b + c = N

Find maximum possible value of abc among all of the possibilities.  If there is no such possibility, print -1
"""

from functools import reduce
from operator import mul
from typing import List, Tuple
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def pythagorean_triplets(perimeter: int) -> List[Tuple[int, int, int]]:
    """
    gets a list of Pythagorean Triplets for a given perimeter
    :param perimeter: sum of the sides of a triangle whose sides are the Pythagorean Triplet
    :return: list of possible Pythagorean Triplets, or an empty list
    """
    triplets = []
    for side1 in range(1, perimeter // 2):
        for side2 in range(side1, perimeter - side1):
            side3 = perimeter - side1 - side2
            if side1 ** 2 + side2 ** 2 == side3 ** 2:
                triplets.append((side1, side2, side3))
    return triplets


def get_maximum_abc(triplets: List[Tuple[int, int, int]]) -> int:
    """
    out of a list of Pythagorean Triplets (PT), get the maximum a * b * c, where a, b, c are members of a PT
    """
    if triplets:
        return max(reduce(mul, triplet) for triplet in triplets)
    else:
        return -1


if __name__ == '__main__':
    #  Hackerrank provides the following for this code:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(get_maximum_abc(pythagorean_triplets(n)))
