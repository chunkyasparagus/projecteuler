"""https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

Find the largest prime factor of a given number

Sample Inputs
2
10
17

(two test cases, first 10, second 17)

Sample Outputs
5
17

(the greatest prime factors of 10 and 17 respectively)
"""

import sys
from functools import lru_cache, reduce
from typing import Iterator, List, Optional
from operator import mul, floordiv

sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


@lru_cache(maxsize=None)
def is_prime(num: int) -> bool:
    return num > 1 and not any(num % x == 0 for x in range(2, num // 2 + 1))


def primes() -> Iterator:
    """
    returns an Iterator of all prime numbers
    :return: Iterator
    """
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


def prime_factors(num: int, factor_list: List[int] = None) -> Optional[List[int]]:
    """
    return a list of prime factors for a given num
    :param num:
    :param factor_list:
    :return:
    """
    if factor_list is None:
        try_factor_list = []
    else:
        try_factor_list = factor_list.copy()
    for prime in primes():
        if reduce(floordiv, try_factor_list, num) % prime == 0:
            try_factor_list.append(prime)
            print(try_factor_list)
            product = reduce(mul, try_factor_list)
            if product == num:
                return try_factor_list
            elif product < num:
                new_factor_list = prime_factors(num, try_factor_list)
                if new_factor_list is None:
                    try_factor_list.pop()
                else:
                    return new_factor_list
    return None


if __name__ == '__main__':
    #  the following is provided by HackerRank
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(max(prime_factors(n)))
