def solve(limit: int = 1000000) -> int:
    """Find smallest member of the longest amicable chain with no element exceeding limit.
    
    Time Complexity: O(limit * log limit)
    Space Complexity: O(limit)
    """
    # 1. Compute proper divisor sum array via Sieve of Eratosthenes
    sum_div = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            sum_div[j] += i

    # 2. Trace chains to find longest cycle
    visited = [False] * (limit + 1)
    max_len = 0
    best_min_elem = 0

    for i in range(1, limit + 1):
        if visited[i]:
            continue

        curr = i
        path = []
        path_set = set()

        while curr <= limit and curr > 0 and not visited[curr]:
            visited[curr] = True
            path.append(curr)
            path_set.add(curr)
            curr = sum_div[curr]

        if curr in path_set:
            idx = path.index(curr)
            cycle = path[idx:]
            cycle_len = len(cycle)
            if cycle_len > max_len:
                max_len = cycle_len
                best_min_elem = min(cycle)

    return best_min_elem
