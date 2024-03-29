from functools import lru_cache
from itertools import chain
from typing import List
from math import sqrt
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


@lru_cache(maxsize=None)
def is_prime(num: int) -> bool:
    """
    Check if a number is prime
    :param num: int of number to check
    :return: True if num is prime, False otherwise
    """
    return num > 1 and not any(num % x == 0 for x in range(2, num))


@lru_cache(maxsize=None)
def prime_factors(num: int) -> List[int]:
    """
    Get a list of prime factors of num
    :param num: int to factorize
    :return: List of ints which are prime factors of num
    """
    factors = []
    for factor in chain([2], range(3, int(sqrt(num)) + 1, 2)):
        while num % factor == 0:
            num //= factor
            if is_prime(factor):
                factors.append(factor)
            else:
                factors.extend(prime_factors(factor))
        if num == 1:
            return factors
    factors.append(num)
    return factors


if __name__ == '__main__':
    #  the following is provided by HackerRank
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # the below is my own
        print(max(prime_factors(n)))
