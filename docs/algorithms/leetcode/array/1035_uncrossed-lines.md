# Uncrossed Lines

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1035 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [uncrossed-lines](https://leetcode.com/problems/uncrossed-lines/) |

## Problem Description & Examples
### Goal
Given two integer arrays, draw as many noncrossing equal-value connections as possible between the arrays. Return the maximum number of connections.

### Function Contract
**Inputs**

- `nums1`: List[int]
- `nums2`: List[int]

**Return value**

int - maximum number of noncrossing matching pairs

### Examples
**Example 1**

- Input: `nums1 = [1, 4, 2], nums2 = [1, 2, 4]`
- Output: `2`

**Example 2**

- Input: `nums1 = [2, 5, 1, 2, 5], nums2 = [10, 5, 2, 1, 5, 2]`
- Output: `3`

**Example 3**

- Input: `nums1 = [1, 3, 7, 1, 7, 5], nums2 = [1, 9, 2, 5, 1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Longest common subsequence dynamic programming.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
- **Space Complexity**: `O(n)`
