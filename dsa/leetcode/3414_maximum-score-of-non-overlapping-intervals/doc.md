# Maximum Score of Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3414 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-score-of-non-overlapping-intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/).

### Goal
Given a collection of intervals, each defined by a start time, an end time, and a weight, select exactly four non-overlapping intervals to maximize the total sum of their weights. If multiple combinations yield the same maximum score, choose the one with the lexicographically smallest set of indices.

### Function Contract
**Inputs**

- `intervals`: A list of lists where each element is `[start, end, weight]`.

**Return value**

- A list of four integers representing the indices (0-indexed) of the selected intervals that produce the maximum total weight.

### Examples
**Example 1**

- Input: `intervals = [[1,3,2],[4,5,3],[7,9,4],[10,11,5]]`
- Output: `[0,1,2,3]`

**Example 2**

- Input: `intervals = [[5,8,2],[2,9,8],[3,7,1],[6,8,3]]`
- Output: `[0,1,2,3]` (Note: Indices are sorted by the problem requirement)

**Example 3**

- Input: `intervals = [[1,3,2],[1,3,2],[1,3,2],[1,3,2]]`
- Output: `[0,1,2,3]`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with Binary Search. We first sort the intervals by their end times. We define `dp[k][i]` as the maximum weight achievable using `k` non-overlapping intervals considering intervals up to index `i`. To optimize, we use binary search (`bisect_right`) to find the latest non-overlapping interval that ends before the current interval starts. To handle the lexicographical requirement, we store the indices alongside the weights in the DP table.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of intervals. Sorting takes `O(N log N)`, and the DP state transitions involve binary search, leading to `O(K * N log N)` where `K=4`.
- **Space Complexity**: `O(N * K)` to store the DP table and the associated indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
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
```
</details>
