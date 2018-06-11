#!/usr/bin/python3
# coding=utf-8

"""
Calculates the average order of g^{ab} for all possible values a, b in {1, …, p-1}.
"""

import argparse
from math import gcd
from itertools import product
from order import order


def main() -> None:
    """
    Argument handling
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('generator', type=int,
                        help='Generator g in the cyclic group Z_n^*')
    parser.add_argument('modulus', type=int,
                        help='Modulus n of the cyclic group Z_n^*')
    args = parser.parse_args()

    print('Average order: {0}'.format(
        average_order(args.generator, args.modulus)))


def average_order(generator: int, modulus: int) -> float:
    """
    Calculates the average order of g^{ab} for all possible values a, b in {1, …, p-1}.
    """
    generator_order = order(generator, modulus)
    accumulate_order = 0

    for a_value, b_value in product(range(1, modulus), repeat=2):
        accumulate_order += 1/gcd(generator_order, a_value*b_value)

    return generator_order * accumulate_order/((modulus - 1)*(modulus - 1))


if __name__ == '__main__':
    main()
