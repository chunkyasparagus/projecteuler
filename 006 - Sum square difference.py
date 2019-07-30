"""https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

The sum of squares of the first ten natural numers is 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
The square of the sum of the sfirst ten natural numbers is (1 + 2 + 3 + ... + 10) ^ 2 = 3025

Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the
sum is 3025 - 385 = 2640

Find the absolute difference between the sum of the squares of the first N natural numbers and the sq of the sum
"""

from operator import add
from functools import reduce
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def sum_square_diff(num: int) -> int:
    """
    return the absolute difference between:
     i) the sum of squares of numbers 1 <= i <= num, and
    ii) the square of sum of numbers 1 <= i <= num
    """
    rng = range(1, num + 1)
    return abs(reduce(add, [i ** 2 for i in rng]) - reduce(add, rng) ** 2)


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # my own stuff below
        print(sum_square_diff(n))
