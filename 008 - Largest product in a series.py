"""https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem

Find the greatest product of K consecutive digits in the N digit number.

Example, for 10-digit number 3675356291, and selecting K=5 digits, we have 36753, 67535, 75356, 53562, 35629, and 56291.

In this case, 6 * 7 * 5 * 3 * 5 gives  maximum product of 3150  (answer: 3150)
"""

from operator import mul
from functools import reduce
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def largest_product_of_digits(stringnum: str, k_digits: int) -> int:
    return max(
        reduce(mul, (int(digit) for digit in stringnum[start_digit:start_digit + k_digits]))
        for start_digit in range(len(stringnum) - k_digits)
    )


if __name__ == '__main__':
    #  the following provided by HackerRank - leaving as is
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        num = input().strip()
        # my code
        print(largest_product_of_digits(num, k))
