"""https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

This problem is a programming version of Problem 4 from projecteuler.net

A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit
numbers is 101101 = 143 * 707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than N.

(101101 < N < 1000000)

"""
import sys
from typing import Optional

sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank

all_products = []
for x in range(100, 1000):
    for y in range(x, 1000):
        if x * y >= 100000:
            all_products.append(x * y)
all_products.sort(key=lambda product: -product)


def is_pallindrome_int(num: int) -> bool:
    return str(num) == str(num)[::-1]


def find_largest_pallindrome(limit: int) -> Optional[int]:
    try:
        return next(filter(lambda num: num < limit and is_pallindrome_int(num), all_products))
    except StopIteration:
        return None


if __name__ == '__main__':
    #  below from the HackerRank problem:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  below is my own.
        print(find_largest_pallindrome(n))
