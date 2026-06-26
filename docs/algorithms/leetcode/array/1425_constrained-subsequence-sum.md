# Constrained Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1425 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Official Link | [constrained-subsequence-sum](https://leetcode.com/problems/constrained-subsequence-sum/) |

## Problem Description & Examples
### Goal
Choose a non-empty subsequence whose adjacent chosen indices differ by at most `k`, and maximize the sum of chosen values.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `k`: the maximum allowed gap between consecutive chosen indices.

**Return value**

The maximum constrained subsequence sum.

### Examples
**Example 1**

- Input: `nums = [10,2,-10,5,20], k = 2`
- Output: `37`

**Example 2**

- Input: `nums = [-1,-2,-3], k = 1`
- Output: `-1`

**Example 3**

- Input: `nums = [10,-2,-10,-5,20], k = 2`
- Output: `23`

---

## Underlying Base Algorithm(s)
Dynamic programming with a monotonic deque. Let `dp[i]` be the best valid subsequence ending at `i`; it uses the maximum positive `dp` from the previous `k` positions.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(k)` for the deque, or `O(n)` if all DP values are stored.
