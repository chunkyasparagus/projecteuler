"""https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, diagonal) in a
20x20 grid of integers?

Input consists of 20 lines of 20 integers i, separated by a space each,  where 0 <= i <= 100

"""

from typing import List
from functools import reduce
from operator import mul
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def greatest_product(fullgrid: List[List[int]], conseq_len=4) -> int:
    """
    get the greatest product of n consecutively appearing numbers (horizontally, vertically, or diagonally)
    appearing in a two-dimensional matrix (list of lists) fullgrid.  the grid can be any size.
    """
    def not_in_right_gutter(test_i):
        return 0 <= test_i % grd_wdth <= grd_wdth - conseq_len  # index is at least conseq_len from rhs of grid

    def not_in_left_gutter(test_i):
        return conseq_len <= test_i % grd_wdth <= grd_wdth - 1  # index is at least conseq_len from lhs of grid

    def not_in_bottom_gutter(test_i):
        return test_i < grd_hght * grd_wdth - grd_wdth * conseq_len  # index is at least conseq_len from bottom

    grd_hght, grd_wdth = len(fullgrid), len(fullgrid[0])
    flat_grid = [item for row in fullgrid for item in row]  # create single flat list for slicing

    all_sets = []
    for i in range(len(flat_grid)):
        if not_in_right_gutter(i):
            # append horizontal line starting from this position
            all_sets.append(flat_grid[i: i + conseq_len])
        if not_in_bottom_gutter(i):
            # append vertical line starting from this position
            all_sets.append(flat_grid[i: i + grd_wdth * conseq_len: grd_wdth])
            if not_in_right_gutter(i):
                # append diagonal-right line starting from this position
                all_sets.append(flat_grid[i: i + grd_wdth * conseq_len: grd_wdth + 1])
            if not_in_left_gutter(i):
                # append diagonal-left line starting from this position
                all_sets.append(flat_grid[i: i + (grd_wdth - 1) * conseq_len: grd_wdth - 1])

    # return maximum product of all of these sets
    return max([reduce(mul, one_set) for one_set in all_sets])


if __name__ == '__main__':
    #  the below is provided by HackerRank
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)

    # the following is my own
    print(greatest_product(grid))
