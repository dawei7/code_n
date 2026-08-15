import math


def solve(n: int = 12) -> int:
    """Find the number of subset pairs that need to be tested for equality for n = 12 using Catalan combinatorics.

    Mathematical Principles Applied:
    1. Property 2 Dominance & Catalan Dyck Paths:
       For a sorted set A = (a_1 < a_2 < ... < a_n), we only need to test disjoint subset pairs (B, C) of equal size k (|B| = |C| = k >= 2).
       If B = (b_1 < b_2 < ... < b_k) and C = (c_1 < c_2 < ... < c_k) satisfy b_i < c_i for all i in 1..k,
       then sum(B) < sum(C) is automatically guaranteed by strict element-wise dominance, so NO equality test is needed!

    2. Counting Non-Dominant Subset Pairs via Catalan Numbers:
       For a chosen 2k elements from n:
       - Total equal-sized pairs: C(2k, k) / 2.
       - Dominant ordered pairs (Dyck paths): Catalan number C_k = C(2k, k) / (k + 1).
       - Non-dominant pairs needing testing: (C(2k, k) / 2) - C_k.

    3. Total Tests Formula:
       Sum over k = 2..floor(n/2):
       TotalTests = sum_{k=2}^{n/2} C(n, 2k) * [ (C(2k, k) / 2) - (C(2k, k) / (k + 1)) ].

    Time Complexity: O(n) constant time execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    total_testing_needed = 0

    # Loop subset size k from 2 up to n // 2
    for k in range(2, n // 2 + 1):
        # Number of ways to choose 2k elements out of n
        ways_to_choose_2k = math.comb(n, 2 * k)

        # Total pairs of subsets of size k from 2k elements
        total_pairs_2k = math.comb(2 * k, k) // 2

        # Catalan number C_k representing strictly dominant subset pairs
        catalan_k = math.comb(2 * k, k) // (k + 1)

        # Pairs requiring explicit equality testing
        pairs_needing_test = total_pairs_2k - catalan_k

        # Accumulate total test pairs
        total_testing_needed += ways_to_choose_2k * pairs_needing_test

    # Return total number of subset pairs needing equality testing for n = 12
    return total_testing_needed


if __name__ == "__main__":
    print(solve())
