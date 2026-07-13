# Minimum Interval to Include Each Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1851 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-interval-to-include-each-query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-interval-to-include-each-query/).

### Goal
You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` describes the `i`-th interval. You are also given an integer array `queries`.

The size of an interval is defined as `right_i - left_i + 1`. We want to find the size of the smallest interval `i` such that the interval contains the query `j`.

Return an array containing the answer for each query. If no such interval exists, return `-1`.

### Function Contract
**Inputs**

- `intervals`: List[List[int]]
- `queries`: List[int]

**Return value**

List[int] - sizes of minimum intervals containing each query

### Examples
**Example 1**

- Input: `intervals = [[1, 4], [2, 4], [3, 6], [4, 4]], queries = [2, 3, 4, 5]`
- Output: `[3, 3, 1, 4]`

**Example 2**

- Input: `intervals = [[14, 14], [9, 17], [16, 22]], queries = [16, 12, 19]`
- Output: `[7, 9, 7]`

**Example 3**

- Input: `intervals = [[19, 20], [9, 10]], queries = [25, 15, 16]`
- Output: `[-1, -1, -1]`

---

## Solution
### Approach
- [Activity selection / interval choice](greedy_01_activity-selection.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
