"""https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes not greater than given N

The first line of input contains an integer T i.e. the numer of the test cases.
The next T lines will contain an integer N.

"""

from itertools import takewhile
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
def sum_of_primes(n_max: int, primes: List[int] = [2, 3]) -> int:
    """
    return the sum of all primes less than or equal to n
    """
    if n_max > primes[-1]:
        # extend the list of saved primes out to n
        primes.extend([num for num in range(primes[-1] + 2, n_max + 2, 2) if is_odd_prime(num, primes)])
    return sum(takewhile(lambda x: x <= n_max, primes))


if __name__ == '__main__':
    # the following is provided as part of the question:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # the following is my own
        print(sum_of_primes(n))
