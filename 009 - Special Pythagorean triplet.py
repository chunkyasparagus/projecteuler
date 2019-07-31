"""https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

A Pythagorean triplet is a set of three natural numbers, a < b < c for which a^2 + b^2 = c^2

Given N, check if there exists any Pythagorean triplet for which a + b + c = N

Find maximum possible value of abc among all of the possibilities.  If there is no such possibility, print -1
"""

import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def pythagorean_triplets(total: int):
    pass


if __name__ == '__main__':
    #  Hackerrank provides the following for this code:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        print(pythagorean_triplets(n))
