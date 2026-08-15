def count_reversible_length(L: int) -> int:
    """Find the exact count of reversible numbers with digit length L.

    Mathematical Principles Applied:
    1. Reversible Definition:
       A positive integer n is reversible if n and its reverse rev(n) have no leading zeros,
       and every digit of n + rev(n) is odd.

    2. Combinatorial Classification Theorem by Digit Length L:
       - If L % 4 == 1: 0 reversible numbers exist (carry propagation creates an even digit).
       - If L is EVEN (L % 2 == 0):
         Outer pair (d_1, d_L) has 20 valid choices (d_1 + d_L is odd, no zero).
         Inner pairs (d_i, d_{L-i+1}) have 30 valid choices each.
         Count = 20 * (30 ^ (L // 2 - 1)).
       - If L % 4 == 3:
         Middle digit d_{(L+1)/2} requires carry from adjacent pair.
         Outer pair has 20 choices, inner pairs have 25 choices, middle digit has 5 choices.
         Count = 100 * (500 ^ ((L - 3) // 4)).
    """
    if L % 4 == 1:
        return 0
    elif L % 2 == 0:
        return 20 * (30 ** (L // 2 - 1))
    elif L % 4 == 3:
        k = (L - 3) // 4
        return 100 * (500**k)
    return 0


def solve(max_len: int = 9) -> int:
    """Find the total number of reversible numbers below 10^9 (1 billion).

    Time Complexity: O(max_len) linear execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Sum counts across all digit lengths L from 1 to 8 (below 10^9)
    return sum(count_reversible_length(L) for L in range(1, max_len))


if __name__ == "__main__":
    print(solve())
