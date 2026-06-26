# Find the Smallest Divisor Given a Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1283 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [find-the-smallest-divisor-given-a-threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/) |

## Problem Description & Examples
### Goal
Find the smallest positive divisor such that the sum of each number divided by the divisor and rounded up is at most `threshold`.

### Function Contract
**Inputs**

- `nums`: positive integer array.
- `threshold`: maximum allowed rounded-up division sum.

**Return value**

The smallest divisor satisfying the threshold.

### Examples
**Example 1**

- Input: `nums = [1,2,5,9]`, `threshold = 6`
- Output: `5`

**Example 2**

- Input: `nums = [44,22,33,11,1]`, `threshold = 5`
- Output: `44`

**Example 3**

- Input: `nums = [2,3,5,7,11]`, `threshold = 11`
- Output: `3`

---

## Underlying Base Algorithm(s)
Binary search on the answer.

---

## Complexity Analysis
- **Time Complexity**: `O(n log max(nums))`
- **Space Complexity**: `O(1)`
