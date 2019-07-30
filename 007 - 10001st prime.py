"""https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

By listing the first six prime numbers, 2, 3, 4, 7, 11, 13 we can see that the 6th prime is 13.

What is the Nth prime number?

Constraints:  1 <= number of test cases T <= 1000, 1 <= N <= 10000
"""

import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def nth_prime(num: int) -> int:
    """
    return the nth prime number
    """
    pass


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # my own stuff below
        print(nth_prime(n))
