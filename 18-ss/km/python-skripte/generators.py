#!/usr/bin/python3
# coding=utf-8

"""
Finds all generators for the cyclic group Z_n^* under multiplication modulo n.
"""

import argparse
from typing import List


def main() -> None:
    """
    Argument handling.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('modulus', type=int,
                        help='Modulus n of the cyclic group Z_n^*')
    args = parser.parse_args()

    generators = find_generators(args.modulus)
    print('Generators of Z_{}^*: {}'.format(args.modulus, generators))


def find_generators(modulus: int) -> List[int]:
    """
    Finds all generators for the cyclic group Z_n^* under multiplication modulo n.
    """
    generators = []
    for candidate in range(0, modulus):
        # Calculate the order of the candidate
        for exponent in range(1, modulus):
            if pow(candidate, exponent) % modulus == 1:
                # If this the *last* exponent for this candiate procuded the `1`
                # Then the cyclic group has the generator `candidate`
                if exponent == modulus - 1:
                    generators.append(candidate)

                # The exponentiation result `1` means a cycle within the group was completed.
                # Further exponentiations will only produce the same list of results again.
                break

    return generators


if __name__ == '__main__':
    main()
