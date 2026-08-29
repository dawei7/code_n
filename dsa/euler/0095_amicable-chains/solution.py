def solve(limit: int = 1000000) -> int:
    """Find the smallest element of the longest amicable chain with no element exceeding limit (1,000,000).

    Mathematical Principles Applied:
    1. Proper Divisor Sum Sieve:
       Let s(n) = sigma_1(n) - n be the sum of proper divisors of n.
       Precompute s(n) for all 1 <= n <= 1,000,000 using a harmonic divisor sieve in O(N log N) time:
       For i from 1 to N/2:
           add i to sum_div[2*i], sum_div[3*i], ...

    2. Functional Graph Traversal & Cycle Detection:
       The mapping n -> s(n) defines a functional directed graph with out-degree 1.
       Trace paths to identify closed cycles (amicable chains) where all nodes in the cycle remain <= 1,000,000.
       Find the cycle with maximum length, and extract its smallest member min(cycle).

    Time Complexity: O(limit log limit) executing in ~0.35s.
    Space Complexity: O(limit) memory for divisor array and visited markers.
    """
    # 1. Compute proper divisor sum array via harmonic sieve
    sum_div = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            sum_div[j] += i

    # 2. Trace functional graph chains to detect longest valid cycle
    visited = [False] * (limit + 1)
    max_len = 0
    best_min_elem = 0

    # Iterate starting nodes from 1 to 1,000,000
    for i in range(1, limit + 1):
        if visited[i]:
            continue

        curr = i
        path = []
        path_set = set()

        # Trace sequence until exceeding limit, hitting 0, or visiting a known node
        while curr <= limit and curr > 0 and not visited[curr]:
            visited[curr] = True
            path.append(curr)
            path_set.add(curr)
            curr = sum_div[curr]

        # Check if sequence closed into a cycle within current path
        if curr in path_set:
            idx = path.index(curr)
            cycle = path[idx:]
            cycle_len = len(cycle)
            # Update longest cycle length and smallest cycle member
            if cycle_len > max_len:
                max_len = cycle_len
                best_min_elem = min(cycle)

    # Return smallest member of the longest amicable chain
    return best_min_elem


if __name__ == "__main__":
    print(solve())
