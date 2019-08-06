"""https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes not greater than given N

The first line of input contains an integer T i.e. the numer of the test cases.
The next T lines will contain an integer N.

"""
from typing import List
from math import sqrt
from typing import Iterator
from itertools import count, chain
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def primes() -> Iterator:
    """
    Generator function returning Iterator of all prime numbers

    (leaving this here for posterity)
    """
    prime_list = [2]
    yield 2
    for num in count(3, 2):
        if not any(num % fac == 0 for fac in chain(prime_list, range(prime_list[-1] + 2, num // 2 + 1, 2))):
            prime_list.append(num)
            yield num


def sieve_primes(n_max: int) -> List[int]:
    """
    Return a list primes <= n_max, implementing Sieve of Eratosthenes
    """
    all_nums = list(range(n_max + 1))
    all_nums[1] = 0  # remove 1 as it is not prime
    for test_prime in range(2, int(sqrt(n_max)) + 1):
        if all_nums[test_prime] > 0:  # this number is prime, remove all multiples, starting from test_prime ** 2
            for multiple in range(test_prime ** 2, n_max + 1, test_prime):
                all_nums[multiple] = 0
    return all_nums


# noinspection PyDefaultArgument
def sum_primes(n_max: int, sums=[0], all_primes=sieve_primes(1000000)) -> int:
    """
    Return the sum of all primes less than or equal to n_max, where n_max <= 1000000 (this may be increased by
    providing a larger list of prime numbers to all_primes)

    i-th element of sums list contains the sum of all primes less than or equal to i, saved to avoid re-calc'ing each
    time
    """

    # extend the sums list if it doesn't cover until our n_max
    for add_number in range(len(sums), n_max + 1):
        sums.append(sums[-1] + all_primes[add_number])
    return sums[n_max]


if __name__ == '__main__':
    # the following is provided as part of the question:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # the following is my own
        print(sum_primes(n))
