# Maximum Subarray Sum with One Deletion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1186 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-subarray-sum-with-one-deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) |

## Problem Description & Examples
### Goal
Find the maximum sum of a non-empty contiguous subarray after deleting at most one element from that subarray.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The largest possible subarray sum with zero or one deletion.

### Examples
**Example 1**

- Input: `arr = [1,-2,0,3]`
- Output: `4`

**Example 2**

- Input: `arr = [1,-2,-2,3]`
- Output: `3`

**Example 3**

- Input: `arr = [-1,-1,-1,-1]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Kadane-style dynamic programming with two states.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
