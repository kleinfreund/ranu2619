#!/usr/bin/python3
# coding=utf-8

"""
Finds the modular multiplicative inverse of a number with respect to modulus n.
"""

import argparse
from math import gcd


def main() -> None:
    """
    Argument handling.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int,
                        help='Some number')
    parser.add_argument('modulus', type=int,
                        help='Modulus n of the cyclic group Z_n^*')
    args = parser.parse_args()

    inverse = multiplicative_inverse(args.number, args.modulus)
    print('{}*{} ≡ 1 (mod {})'.format(args.number, inverse, args.modulus))
    print('Multiplicative inverse: {}'.format(inverse))


def multiplicative_inverse(number: int, modulus: int) -> int:
    """
    Finds the modular multiplicative inverse `x` of an integer `a` such that
    `ax` is congruent 1 with respect to modulus `n`: ax ≡ 1 (mod n)
    """
    if gcd(number, modulus) == 1:
        for candidate in range(0, modulus):
            if (candidate * number) % modulus == 1:
                return candidate

    return None


if __name__ == '__main__':
    main()
