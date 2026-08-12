def valid_L(L: int) -> int:
    """Find number of valid hexadecimal numbers of length L containing digits 0, 1, A."""
    return 15 * 16**(L - 1) - 43 * 15**(L - 1) + 41 * 14**(L - 1) - 13 * 13**(L - 1)


def solve(max_len: int = 16) -> str:
    """Find total count of hexadecimal numbers <= max_len digits containing 0, 1, A, formatted as hex string.
    
    Time Complexity: O(max_len)
    Space Complexity: O(1)
    """
    total = sum(valid_L(L) for L in range(3, max_len + 1))
    return hex(total)[2:].upper()
