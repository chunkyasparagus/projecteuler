"""https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.
"""
from typing import List
from math import gcd
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def sum_multiples(num: int, limit: int, include_limit: bool = False) -> int:
    """
    Returns the sum of all multiples of n for n < limit
    :param num: int whose multiples to sum
    :param limit: upper limit of summation, specify inclusiveness of limit with include_limit
    :param include_limit: bool True if the limit should be included in the summation if it is a multiple
    :return: int the sum of multiples of n until limit
    """
    if not include_limit:
        limit -= 1
    d, m = divmod(limit, num)
    return (limit - m + num) * d // 2


def sum_multiples_of_two_numbers(nums: List[int], limit: int, include_limit: bool = False) -> int:
    """
    Returns the sum of all multiples of integers in nums for each integer < or <= limit
    :param nums: list of ints whose multiples to sum
    :param limit: upper limit of summation, specify inclusiveness of limit with include_limit
    :param include_limit: bool True if the limit should be included in the summation if it is a multiple
    :return: int the sum of multiples of n until limit
    """
    return (
            sum_multiples(nums[0], limit, include_limit) +
            sum_multiples(nums[1], limit, include_limit) -
            sum_multiples(nums[0] * nums[1] // gcd(nums[0], nums[1]), limit, include_limit)  # remove duplicates
    )


if __name__ == '__main__':
    #  the following is provided by Hackerrank
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(sum_multiples_of_two_numbers([3, 5], n))
