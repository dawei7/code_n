import itertools


def is_special_sum_set(a: tuple[int, ...]) -> bool:
    n = len(a)
    # Property 2 check: sum of smallest (k+1) elements > sum of largest k elements
    for k in range(1, (n + 1) // 2):
        if sum(a[:k + 1]) <= sum(a[-k:]):
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


def solve() -> str:
    """Find optimum special sum set for n = 7 and return set string.
    
    Time Complexity: O(SearchSpace * 2^N)
    Space Complexity: O(2^N)
    """
    # Base near-optimum anchor around {20, 31, 38, 39, 40, 42, 45}
    base = [20, 31, 38, 39, 40, 42, 45]
    min_sum = float('inf')
    best_set = None

    # Local search around base anchor
    for delta in itertools.product(range(-3, 4), repeat=7):
        candidate = tuple(sorted(b + d for b, d in zip(base, delta)))
        if len(set(candidate)) != 7:
            continue

        c_sum = sum(candidate)
        if c_sum < min_sum:
            if is_special_sum_set(candidate):
                min_sum = c_sum
                best_set = candidate

    return "".join(str(x) for x in best_set)
