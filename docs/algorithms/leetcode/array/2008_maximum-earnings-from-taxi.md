# Maximum Earnings From Taxi

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2008 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sorting |
| Official Link | [maximum-earnings-from-taxi](https://leetcode.com/problems/maximum-earnings-from-taxi/) |

## Problem Description & Examples
### Goal
Choose non-overlapping taxi rides along a one-dimensional route to maximize earnings. Each ride pays distance plus tip.

### Function Contract
**Inputs**

- `n`: final route point.
- `rides`: entries `[start, end, tip]`.

**Return value**

Return the maximum total earnings.

### Examples
**Example 1**

- Input: `n = 5, rides = [[2,5,4],[1,5,1]]`
- Output: `7`

**Example 2**

- Input: `n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]`
- Output: `20`

**Example 3**

- Input: `n = 6, rides = [[1,2,1],[2,4,2],[4,6,1]]`
- Output: `8`

---

## Underlying Base Algorithm(s)
Group rides by ending point. Let `dp[x]` be the best earnings by position `x`; carry forward `dp[x - 1]`, and for every ride ending at `x`, consider `dp[start] + end - start + tip`.

---

## Complexity Analysis
- **Time Complexity**: `O(n + r)`
- **Space Complexity**: `O(n + r)`
