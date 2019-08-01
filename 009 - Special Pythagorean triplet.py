"""https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

A Pythagorean triplet is a set of three natural numbers, a < b < c for which a^2 + b^2 = c^2

Given N, check if there exists any Pythagorean triplet for which a + b + c = N

Find maximum possible value of abc among all of the possibilities.  If there is no such possibility, print -1
"""

from itertools import count, chain
from functools import reduce
from collections import OrderedDict
from operator import mul
from typing import Iterator, List
import sys
sys.stdin = open(__file__.replace('.py', ' - Inputs.txt'))  # Simulate inputs from stdin - remove this on Hackerrank


def euclids_pythagorean_triples() -> Iterator:
    """
    Generator iterating over all of Euclids Pythagorean Triples, given by
    a = m^2 - n^2, b = 2mn, c = m^2 - n^2 for m > n > 0, yielding all primative and some non-primative Pythagorean
    Triples
    :return: Iterator returning Tuple[Tuple[int, int, int], Tuple[int, int]] where 1st item is the PT, 2nd is (m, n)
    """
    for m in count(2):
        for n in range (1, m):
            a, b, c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
            yield ((a, b, c), (m, n))


# noinspection PyDefaultArgument
def pythagorean_triples_given_n(n: int, saved_triples=OrderedDict(), ept=euclids_pythagorean_triples()) -> List:
    """
    get a list of all Pythagorean Triples (a, b, c) such that a + b + c == n
    :param n:
    :param saved_triples: saved triples from euclids_pythagorean_triples to avoid cost of regenerating
    :param ept: Iterator here to avoid generating from start of set again
    :return: List of Tuple[int, Tuple[int, int, int]] where the first member is the product a * b * c,
    second item is the Pythagorean Triple
    """
    n_triples = set()

    for triple in chain(saved_triples, ept):
        saved_triples[triple] = None  # save this triple to avoid regeneration later

        if 2 * triple[1][0] ** 2 + 2 * triple[1][0] * triple[1][1] > n:
            break  # there can be no more triples where a + b + c == n

        total = sum(triple[0])
        factor, modulo = divmod(n, total)
        return_triple = tuple(sorted([item * factor for item in triple[0]]))
        product = reduce(mul, return_triple)
        if modulo == 0:  # this is a valid triple for a + b + c == n
            n_triples.add(
                (product, return_triple)
            )

    return sorted(n_triples, key=lambda item: -item[0])  # sorting to give highest product first


if __name__ == '__main__':
    #  Hackerrank provides the following for this code:
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        #  the following is my own
        triples = pythagorean_triples_given_n(n)
        if triples:
            print(triples[0][0])
        else:
            print(-1)
