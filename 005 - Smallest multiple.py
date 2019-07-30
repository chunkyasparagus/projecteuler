"""https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from
1 to N?

Contraints:
1 <= N <= 40
"""

import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def smallest_multiple(num: int) -> int:
    pass


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(smallest_multiple(n))
