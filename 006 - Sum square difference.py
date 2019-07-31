"""https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

The sum of squares of the first ten natural numers is 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
The square of the sum of the sfirst ten natural numbers is (1 + 2 + 3 + ... + 10) ^ 2 = 3025

Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the
sum is 3025 - 385 = 2640

Find the absolute difference between the sum of the squares of the first N natural numbers and the sq of the sum
"""

from typing import List
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


# noinspection PyDefaultArgument
def sum_square_diff(num: int, sums: List[int] = [0], sum_of_squares: List[int] = [0]) -> int:
    """
    return the absolute difference between:
     i) the sum of squares of numbers 1 <= i <= num, and
    ii) the square of sum of numbers 1 <= i <= num

    This version saves the sum of numbers until num and sum of squares until num to avoid repeating the loop when
    called several times
    """
    # extend nums and sums if nec
    for i in range(len(sums), num + 1):
        sums.append(sums[-1] + i)
        sum_of_squares.append(sum_of_squares[-1] + i ** 2)

    return abs(sums[num] ** 2 - sum_of_squares[num])


if __name__ == '__main__':
    # the following is provided as part of the problem - leaving untouched
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        # my own stuff below
        print(sum_square_diff(n))
