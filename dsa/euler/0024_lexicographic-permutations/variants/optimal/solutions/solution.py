"""Project Euler Problem 24: Lexicographic Permutations.

Mathematical Formulation:
Millionth lexicographic permutation of digits 0..9 evaluated via factoradic sequence.
"""

from __future__ import annotations


def solve(target_index: int = 1000000) -> str:
    """Compute the 1,000,000th permutation in pure Python."""
    digits = list(range(10))
    idx = target_index - 1
    result = []
    
    for n in range(9, -1, -1):
        fact = 1
        for f in range(1, n + 1):
            fact *= f
        d_idx = idx // fact
        idx %= fact
        result.append(digits.pop(d_idx))
        
    return "".join(str(d) for d in result)


if __name__ == "__main__":
    print(solve())
