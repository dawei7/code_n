"""Project Euler 277: A Modified Collatz sequence

Find the smallest a_1 > 10^15 that begins with the sequence 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'.
"""

from __future__ import annotations


def solve(
    seq: str = "UDDDUdddDDUDDddDdDddDDUDDdUUDd",
    min_val: int = 10**15,
) -> str:
    """Calculates the smallest integer a_1 > min_val whose modified Collatz trajectory begins with

    the given prefix using 3-adic Hensel modular lifting.
    """
    transitions = {
        "D": lambda a: a // 3,
        "U": lambda a: (4 * a + 2) // 3,
        "d": lambda a: (2 * a - 1) // 3,
    }
    char_map = {0: "D", 1: "U", 2: "d"}

    # Iterative Hensel lifting mod 3^L
    r = 0
    mod = 1

    for i, target_char in enumerate(seq):
        for m in (0, 1, 2):
            cand = r + m * mod
            val = cand
            for k in range(i):
                val = transitions[seq[k]](val)
            if char_map[val % 3] == target_char:
                r = cand
                mod *= 3
                break

    # Determine smallest a_1 > min_val of the form r + k * mod
    k = (min_val - r) // mod
    while r + k * mod <= min_val:
        k += 1

    ans = r + k * mod
    return str(ans)


if __name__ == "__main__":
    print(solve())
