"""https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

By listing the first six prime numbers, 2, 3, 4, 7, 11, 13 we can see that the 6th prime is 13.

What is the Nth prime number?

Constraints:  1 <= number of test cases T <= 1000, 1 <= N <= 10000
"""

from typing import List
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def is_odd_prime(num: int, primes: List[int]) -> bool:
    return (
            num > 2 and
            not any(num % fac == 0 for fac in primes) and
            not any(num % fac == 0 for fac in range(primes[-1] + 2, num // 2 + 1, 2))
    )


# noinspection PyDefaultArgument
def nth_prime(nth: int, primes: List[int] = [2, 3]) -> int:
    """
    return the nth prime number
    """
    #  extend the list if nec
    for _ in range(len(primes) - 1, nth):
        testnum = primes[-1] + 2
        while not is_odd_prime(testnum, primes):
            testnum += 2
        primes.append(testnum)
    return primes[nth - 1]


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # my own stuff below
        print(nth_prime(n))
