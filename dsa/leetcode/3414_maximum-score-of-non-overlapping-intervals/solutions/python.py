import bisect

def solve(intervals):
    n = len(intervals)
    # Store original indices to return them later
    indexed_intervals = []
    for i in range(n):
        indexed_intervals.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

    # Sort by end time
    indexed_intervals.sort(key=lambda x: x[1])

    # dp[k][i] = (max_weight, sorted_list_of_indices)
    # Using -1 as a sentinel for weight
    dp = [[(-1, []) for _ in range(n + 1)] for _ in range(5)]

    # Base case: 0 intervals have 0 weight
    for i in range(n + 1):
        dp[0][i] = (0, [])

    end_times = [x[1] for x in indexed_intervals]

    for k in range(1, 5):
        for i in range(1, n + 1):
            start, end, weight, original_idx = indexed_intervals[i-1]

            # Option 1: Don't include this interval
            res_weight, res_indices = dp[k][i-1]

            # Option 2: Include this interval
            # Find the rightmost interval that ends before current starts
            idx = bisect.bisect_left(end_times, start)
            prev_weight, prev_indices = dp[k-1][idx]

            if prev_weight != -1:
                current_total = prev_weight + weight
                current_indices = sorted(prev_indices + [original_idx])

                if current_total > res_weight:
                    res_weight, res_indices = current_total, current_indices
                elif current_total == res_weight:
                    if not res_indices or current_indices < res_indices:
                        res_indices = current_indices

            dp[k][i] = (res_weight, res_indices)

    best_weight, best_indices = dp[0][n]
    for k in range(1, 5):
        weight, indices = dp[k][n]
        if weight > best_weight or (weight == best_weight and indices < best_indices):
            best_weight, best_indices = weight, indices

    return best_indices
