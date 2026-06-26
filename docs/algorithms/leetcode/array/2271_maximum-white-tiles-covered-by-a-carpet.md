# Maximum White Tiles Covered by a Carpet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2271 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum |
| Official Link | [maximum-white-tiles-covered-by-a-carpet](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/) |

## Problem Description & Examples
### Goal
Place one carpet of fixed integer length over nonoverlapping intervals of white floor tiles. Maximize the number of white tile positions covered, including carpet endpoints.

### Function Contract
**Inputs**

- `tiles`: disjoint inclusive intervals `[start, end]`.
- `carpetLen`: the number of consecutive positions covered by the carpet.

**Return value**

The maximum number of white tiles the carpet can cover.

### Examples
**Example 1**

- Input: `tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]`, `carpetLen = 10`
- Output: `9`

**Example 2**

- Input: `tiles = [[10, 11], [1, 1]]`, `carpetLen = 2`
- Output: `2`

**Example 3**

- Input: `tiles = [[1, 3]]`, `carpetLen = 2`
- Output: `2`

---

## Underlying Base Algorithm(s)
Sort intervals and use a sliding window whose carpet begins at the current interval's start. Advance the right pointer across intervals fully covered by the carpet while maintaining their total lengths, then add any partial coverage of the next interval. Remove the left interval as the start advances and maximize the total.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` including sorting; the window scan is `O(n)`
- **Space Complexity**: `O(1)` auxiliary space when sorting in place
