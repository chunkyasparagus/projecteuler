"""https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, diagonal) in a
20x20 grid of integers?

Input consists of 20 lines of 20 integers i,  where 0 <= i <= 100

"""

from typing import List
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def greatest_product(in_grid: List[List[int]]) -> int:
    pass


if __name__ == '__main__':
    #  the below is provided by HackerRank
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)

    # the following is my own
    pass
