def valid_L(L: int) -> int:
    """Find the number of valid hexadecimal numbers of exact digit length L containing at least one '0', '1', and 'A'."""
    # Inclusion-Exclusion Principle formula:
    # 15*16^(L-1) - 43*15^(L-1) + 41*14^(L-1) - 13*13^(L-1)
    return 15 * 16 ** (L - 1) - 43 * 15 ** (L - 1) + 41 * 14 ** (L - 1) - 13 * 13 ** (L - 1)


def solve(max_len: int = 16) -> str:
    """Find the total count of hexadecimal numbers up to 16 digits containing at least one '0', '1', and 'A',
    formatted as an uppercase hexadecimal string.

    Mathematical Principles Applied:
    1. Inclusion-Exclusion Principle by Digit Length L:
       Let total hex numbers of length L (no leading zero) be N = 15 * 16^(L-1).
       Let S_0, S_1, S_A be sets of numbers missing '0', '1', 'A' respectively:
       - Missing '0': 15 * 15^(L-1).
       - Missing '1': 14 * 15^(L-1).
       - Missing 'A': 14 * 15^(L-1).
       Sum missing 1 digit: 43 * 15^(L-1).
       - Missing ('0', '1'): 14 * 14^(L-1).
       - Missing ('0', 'A'): 14 * 14^(L-1).
       - Missing ('1', 'A'): 13 * 14^(L-1).
       Sum missing 2 digits: 41 * 14^(L-1).
       - Missing ('0', '1', 'A'): 13 * 13^(L-1).
       Combining via Inclusion-Exclusion:
       valid(L) = 15*16^(L-1) - 43*15^(L-1) + 41*14^(L-1) - 13*13^(L-1).

    2. Total Summation across L = 3..16:
       Sum valid(L) for L from 3 to 16, and format total in uppercase hexadecimal string.

    Time Complexity: O(max_len) executing in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total = sum(valid_L(L) for L in range(3, max_len + 1))

    # Return uppercase hexadecimal string representation
    return hex(total)[2:].upper()


if __name__ == "__main__":
    print(solve())
