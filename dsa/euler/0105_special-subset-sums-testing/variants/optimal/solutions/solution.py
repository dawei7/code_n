import itertools
import os


def is_special_sum_set(a_raw: list[int]) -> bool:
    """Check if input integer array a_raw satisfies Special Subset Sum Properties 1 & 2.

    Mathematical Principles Applied:
    1. Property 2 (Cardinality Sum Inequality):
       If |B| > |C|, then sum(B) > sum(C).
       For a sorted set A = (a1, a2, ..., an), it suffices to check:
       sum(a[:k+1]) > sum(a[-k:]) for all 1 <= k <= (n // 2).

    2. Property 1 (Disjoint Subset Sum Uniqueness):
       For any two non-empty disjoint subsets B and C of set A, sum(B) != sum(C).
       If all 2^n - 1 subset sums are distinct, then no two disjoint subsets can share equal sums.
    """
    a = sorted(a_raw)
    n = len(a)

    # Property 2 check: sum of smallest (k+1) elements > sum of largest k elements
    for k in range(1, (n + 1) // 2):
        if sum(a[: k + 1]) <= sum(a[-k:]):
            return False

    # Property 1 check: no two disjoint subsets have equal sums
    subset_sums = set()
    for r in range(1, n + 1):
        for sub in itertools.combinations(a, r):
            s = sum(sub)
            if s in subset_sums:
                return False
            subset_sums.add(s)

    return True


def solve(filepath: str = "") -> int:
    """Identify all special sum sets in sets.txt and return the sum of S(A) for all valid sets.

    Time Complexity: O(100 * 2^N) where N <= 12 elements (executes in ~0.05s).
    Space Complexity: O(2^N) memory for subset sum tracking.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0105_special-subset-sums-testing/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "sets.txt")

    # Read sets text file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    total_sum = 0
    # Process each set line in sets.txt
    for line in lines:
        s_set = [int(x) for x in line.split(",")]
        # Test if candidate set satisfies special sum set properties
        if is_special_sum_set(s_set):
            total_sum += sum(s_set)

    # Return sum of S(A) for all valid special sum sets
    return total_sum


if __name__ == "__main__":
    print(solve())
