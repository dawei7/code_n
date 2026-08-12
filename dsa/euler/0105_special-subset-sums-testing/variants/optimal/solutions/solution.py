import itertools
import urllib.request


def is_special_sum_set(a_raw: list[int]) -> bool:
    a = sorted(a_raw)
    n = len(a)

    # Property 2: sum of smallest (k+1) elements > sum of largest k elements
    for k in range(1, (n + 1) // 2):
        if sum(a[:k + 1]) <= sum(a[-k:]):
            return False

    # Property 1: no two disjoint subsets have equal sums
    subset_sums = set()
    for r in range(1, n + 1):
        for sub in itertools.combinations(a, r):
            s = sum(sub)
            if s in subset_sums:
                return False
            subset_sums.add(s)

    return True


def solve() -> int:
    """Identify all special sum sets in sets.txt and return the sum of S(A) for all valid sets.
    
    Time Complexity: O(100 * 2^N)
    Space Complexity: O(2^N)
    """
    url = "https://projecteuler.net/resources/documents/0105_sets.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    total_sum = 0
    for line in lines:
        s_set = [int(x) for x in line.split(",")]
        if is_special_sum_set(s_set):
            total_sum += sum(s_set)

    return total_sum
