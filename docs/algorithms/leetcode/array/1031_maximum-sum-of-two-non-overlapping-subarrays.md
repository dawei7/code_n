# Maximum Sum of Two Non-Overlapping Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1031 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [maximum-sum-of-two-non-overlapping-subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) |

## Problem Description & Examples
### Goal
Given an array and two subarray lengths, choose one subarray of each length with no overlap so their total sum is maximized.

### Function Contract
**Inputs**

- `nums`: List[int]
- `firstLen`: int
- `secondLen`: int

**Return value**

int - maximum combined sum

### Examples
**Example 1**

- Input: `nums = [0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen = 1, secondLen = 2`
- Output: `20`

**Example 2**

- Input: `nums = [3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen = 3, secondLen = 2`
- Output: `29`

**Example 3**

- Input: `nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen = 4, secondLen = 3`
- Output: `31`

---

## Underlying Base Algorithm(s)
Prefix sums plus one-pass best-left-window tracking.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for prefix sums
