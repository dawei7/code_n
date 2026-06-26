# Minimum Operations to Make the Array K-Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2111 |
| Difficulty | Hard |
| Topics | Array, Binary Search |
| Official Link | [minimum-operations-to-make-the-array-k-increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/) |

## Problem Description & Examples
### Goal
Change as few values as possible so `arr[i] <= arr[i + k]` for every valid index.

### Function Contract
**Inputs**

- `arr`: a positive integer array.
- `k`: spacing between compared positions.

**Return value**

Return the minimum number of replacements needed.

### Examples
**Example 1**

- Input: `arr = [5,4,3,2,1], k = 1`
- Output: `4`

**Example 2**

- Input: `arr = [4,1,5,2,6,2], k = 2`
- Output: `0`

**Example 3**

- Input: `arr = [4,1,5,2,6,2], k = 3`
- Output: `2`

---

## Underlying Base Algorithm(s)
Split the array into `k` independent sequences by index modulo `k`. Each sequence must become non-decreasing. Keep its longest non-decreasing subsequence using `bisect_right`; every other element must be changed.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
