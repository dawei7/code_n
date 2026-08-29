"""Project Euler Problem 868: Belfry Maths.

Mathematical formulation:
The Plain Changes bell-ringing procedure is identical to the Steinhaus-Johnson-Trotter (SJT)
algorithm for generating permutations of {1, 2, ..., n} via single adjacent transpositions.

Recursive SJT Rank Formula:
Given a target permutation of length n:
1. Locate the largest element n at 0-indexed position p in the permutation.
2. Recursively find the 0-indexed SJT rank I_{n-1} of the remaining (n - 1) elements.
3. In the SJT ordering:
   - If I_{n-1} is EVEN, the largest element n sweeps to the LEFT:
       k = (n - 1) - p
   - If I_{n-1} is ODD, the largest element n sweeps to the RIGHT:
       k = p
4. The rank of the permutation of size n is:
   I_n = n * I_{n-1} + k.

The total number of swaps from alphabetical order is the SJT rank I_n,
computed in O(n^2) time (under 0.001s in Python).
"""

from __future__ import annotations


def solve(target: str = "NOWPICKBELFRYMATHS") -> int:
    """Compute the number of swaps to reach the target permutation in Plain Changes order."""
    sorted_letters = sorted(list(target))
    letter_to_val = {ch: i + 1 for i, ch in enumerate(sorted_letters)}
    perm = [letter_to_val[ch] for ch in target]

    def get_rank(p: list[int]) -> int:
        n = len(p)
        if n <= 1:
            return 0
        pos = p.index(n)
        p_sub = [x for x in p if x != n]
        sub_rank = get_rank(p_sub)

        if sub_rank % 2 == 0:
            k = (n - 1) - pos
        else:
            k = pos

        return n * sub_rank + k

    return get_rank(perm)


if __name__ == "__main__":
    print(solve())
