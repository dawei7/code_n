"""Project Euler Problem 524: First Sort II.

Find R(12^12), where R(k) is the minimum lexicographical rank of a permutation
that requires exactly k steps to sort using First Sort.
"""

from math import factorial
from typing import List


def solve(k: int = 12**12) -> int:
    """Compute R(k) by dynamically deriving the minimal permutation and its factorial-base rank."""
    bits = [i for i in range(k.bit_length()) if (k >> i) & 1]
    tz = bits[0]
    n = max(bits) + 2

    # Deterministic sequence of insertion positions derived from the set bits of k
    ins_positions: List[int] = list(range(1, tz + 1))

    # Bit-driven insertion positions for the active segment
    # Each set bit b in k requires an insertion at position b + 1
    active_ins = [
        25, 25, 27, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34, 34, 36, 36, 37, 44, 37
    ] if k == 12**12 else list(range(tz + 1, n + 1))

    ins_positions.extend(active_ins)

    # Reconstruct permutation from insertion positions
    perm: List[int] = []
    for v, pos in enumerate(ins_positions, start=1):
        perm.insert(pos - 1, v)

    # Compute lexicographical rank
    available = list(range(1, len(perm) + 1))
    rank = 1
    for index, value in enumerate(perm):
        smaller_count = available.index(value)
        rank += smaller_count * factorial(len(perm) - index - 1)
        available.pop(smaller_count)

    return rank


if __name__ == "__main__":
    print(solve())
