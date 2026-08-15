import math


def p(n: int) -> int:
    """Find p(n), the number of strings of length n with distinct letters having exactly 1 position where character > prev_character."""
    # Combinatorial formula: C(26, n) * (2^n - n - 1)
    return math.comb(26, n) * (2**n - n - 1)


def solve() -> int:
    """Find the maximum value of p(n) for 1 <= n <= 26.

    Mathematical Principles Applied:
    1. Lexicographical Decrease / Single Increase Combinatorics:
       Choose n distinct letters out of 26 alphabet letters in C(26, n) ways.
       Sort the chosen n letters in strictly increasing order c_1 < c_2 < ... < c_n.
       A string of length n with a single lexicographical increase (c_i < c_{i+1}) corresponds to splitting
       the n letters into two non-empty decreasing sequences.

    2. Subset Partition Formula:
       The number of ways to partition n elements into two non-empty sets (left decreasing, right decreasing)
       such that exactly 1 increase occurs is:
       2^n - n - 1.
       Thus: p(n) = C(26, n) * (2^n - n - 1).

    3. Maximum Search over n = 1..26:
       Evaluate p(n) for n = 1 to 26 and find max_{1 <= n <= 26} p(n).

    Time Complexity: O(N) where N = 26 executing in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Return maximum value of p(n) for n in 1..26
    return max(p(n) for n in range(1, 27))


if __name__ == "__main__":
    print(solve())
