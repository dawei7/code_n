# Maximum Score of Non-overlapping Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3414 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Official Link | [maximum-score-of-non-overlapping-intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming combined with Binary Search. We first sort the intervals by their end times. We define `dp[k][i]` as the maximum weight achievable using `k` non-overlapping intervals considering intervals up to index `i`. To optimize, we use binary search (`bisect_right`) to find the latest non-overlapping interval that ends before the current interval starts. To handle the lexicographical requirement, we store the indices alongside the weights in the DP table.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of intervals. Sorting takes `O(N log N)`, and the DP state transitions involve binary search, leading to `O(K * N log N)` where `K=4`.
- **Space Complexity**: `O(N * K)` to store the DP table and the associated indices.
