def count_reversible_length(L: int) -> int:
    """Find number of reversible numbers of exact digit length L."""
    if L % 4 == 1:
        return 0
    elif L % 2 == 0:
        return 20 * (30 ** (L // 2 - 1))
    elif L % 4 == 3:
        # 5 * 20^((L+1)/2 - 1) * 25^((L-3)/4)
        k = (L - 3) // 4
        return 100 * (500 ** k)
    return 0


def solve(max_len: int = 9) -> int:
    """Find total number of reversible numbers below 10^max_len using combinatorial digit analysis.
    
    Time Complexity: O(max_len)
    Space Complexity: O(1)
    """
    return sum(count_reversible_length(L) for L in range(1, max_len))
