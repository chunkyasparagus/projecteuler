"""https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from
1 to N?

Contraints:
1 <= N <= 40
"""

from functools import reduce
from operator import mul
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def remove_factor(num: int, factor: int) -> int:
    """
    return num divided by factor if this is possible with no remainder, if not possible return num
    """
    if num % factor == 0:
        return num // factor
    else:
        return num


def smallest_multiple(num: int) -> int:
    """
    calculate the smallest multiple of all numbers from 1 to num by creating a chain of each integer 1 <= i <= num
    with any existing factors in the chain removed from each i, and return the product of the chain
    """
    chain = []
    for i in range(1, num + 1):
        chain.append(reduce(remove_factor, chain, i))
    return reduce(mul, chain)


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(smallest_multiple(n))
