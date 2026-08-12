import math


def is_pentagonal(p: int) -> bool:
    """Check if p is a pentagonal number P_n = n(3n-1)/2."""
    val = 1 + 24 * p
    root = math.isqrt(val)
    return root * root == val and root % 6 == 5


def solve() -> int:
    """Find pentagonal pair P_j, P_k whose sum and difference are pentagonal, minimizing D = |P_k - P_j|.
    
    Time Complexity: O(K^2)
    Space Complexity: O(K)
    """
    pents = []
    i = 1
    while True:
        pi = i * (3 * i - 1) // 2
        for pj in reversed(pents):
            diff = pi - pj
            if is_pentagonal(diff) and is_pentagonal(pi + pj):
                return diff
        pents.append(pi)
        i += 1
