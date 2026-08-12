import math


def solve(n: int = 12) -> int:
    """Find number of subset pairs that need to be tested for equality for n = 12 using Catalan combinatorics.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    total_testing_needed = 0

    for k in range(2, n // 2 + 1):
        ways_to_choose_2k = math.comb(n, 2 * k)
        total_pairs_2k = math.comb(2 * k, k) // 2
        catalan_k = math.comb(2 * k, k) // (k + 1)

        pairs_needing_test = total_pairs_2k - catalan_k
        total_testing_needed += ways_to_choose_2k * pairs_needing_test

    return total_testing_needed
