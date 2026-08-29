"""Project Euler Problem 719: Number Splitting.

Mathematical Formulation:
An S-number is an integer n^2 such that its decimal digits can be split into two or more
numbers that sum to n.
Find sum of all S-numbers <= 10^{12}.
"""

from __future__ import annotations

import math


def can_split(s: str, target: int) -> bool:
    """Check if string s can be split into parts summing to target."""
    n = len(s)
    if n == 0:
        return target == 0
    if target < 0:
        return False
        
    for i in range(1, n + 1):
        val = int(s[:i])
        if val > target:
            break
        if can_split(s[i:], target - val):
            return True
    return False


def solve(limit: int = 10**12) -> str:
    """Compute sum of all S-numbers <= limit."""
    max_n = math.isqrt(limit)
    total_sum = 0
    
    for n in range(4, max_n + 1):
        # Digital root invariant: n^2 = sum of parts == n (mod 9) => n == n^2 (mod 9) => n in {0, 1} (mod 9)
        rem = n % 9
        if rem != 0 and rem != 1:
            continue
            
        sq = n * n
        s_str = str(sq)
        # Must split into at least 2 parts
        for i in range(1, len(s_str)):
            val = int(s_str[:i])
            if val > n:
                break
            if can_split(s_str[i:], n - val):
                total_sum += sq
                break
                
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
