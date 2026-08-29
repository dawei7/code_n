"""Project Euler Problem 571: Super Pandigital Numbers.

Find the sum of the 10 smallest 12-super-pandigital numbers, which are positive
integers simultaneously pandigital in all bases from 2 to 12.
"""

import itertools
from typing import List


def _is_pandigital(number: int, base: int, all_bits: int) -> bool:
    used = 0
    while number:
        used |= 1 << (number % base)
        if used == all_bits:
            return True
        number //= base
    return used == all_bits


def solve(base: int = 12, num_results: int = 10) -> int:
    """Find the sum of the first `num_results` super-pandigital numbers in base `base`."""
    digits = tuple(range(base))
    check_bases = list(range(base - 1, 1, -1))
    if 8 in check_bases:
        check_bases.remove(8)
        check_bases.insert(0, 8)

    all_bits = [(1 << b) - 1 for b in range(base + 1)]

    num_found = 0
    total = 0

    for first_digit in range(1, base):
        remaining = digits[:first_digit] + digits[first_digit + 1 :]
        for tail in itertools.permutations(remaining):
            current = first_digit
            for digit in tail:
                current = current * base + digit

            is_good = True
            for b in check_bases:
                if b == 8:
                    # Fast bitwise check for base 8
                    tmp = current
                    used = 0
                    while tmp:
                        used |= 1 << (tmp & 7)
                        if used == 0xFF:
                            break
                        tmp >>= 3
                    if used != 0xFF:
                        is_good = False
                        break
                elif not _is_pandigital(current, b, all_bits[b]):
                    is_good = False
                    break

            if is_good:
                total += current
                num_found += 1
                if num_found == num_results:
                    return total

    return total


if __name__ == "__main__":
    print(solve())
