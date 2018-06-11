#!/usr/bin/python3
# coding=utf-8

"""
Calculates the order of a generator in the cyclic group Z_n^*.
"""

import argparse


def main() -> None:
    """
    Argument handling.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('generator', type=int,
                        help='Generator g in the cyclic group Z_n^*')
    parser.add_argument('modulus', type=int,
                        help='Modulus n of the cyclic group Z_n^*')
    args = parser.parse_args()

    generator_order = order(args.generator, args.modulus)
    print('ord(g) = {} with g = {} in Z_{}^*'.format(generator_order,
                                                     args.generator, args.modulus))


def order(generator: int, modulus: int) -> int:
    """
    Calculates the order of a generator in the cyclic group Z_n^*.
    """
    for exponent in range(1, modulus):
        if pow(generator, exponent) % modulus == 1:
            return exponent

    return -1


if __name__ == '__main__':
    main()
