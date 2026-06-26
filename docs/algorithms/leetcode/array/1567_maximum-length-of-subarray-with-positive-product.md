# Maximum Length of Subarray With Positive Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1567 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [maximum-length-of-subarray-with-positive-product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) |

## Problem Description & Examples
### Goal
Find the longest contiguous subarray whose product is positive.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The maximum length of a subarray with positive product.

### Examples
**Example 1**

- Input: `nums = [1, -2, -3, 4]`
- Output: `4`

**Example 2**

- Input: `nums = [0, 1, -2, -3, -4]`
- Output: `3`

**Example 3**

- Input: `nums = [-1, -2, -3, 0, 1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Track two lengths while scanning: the longest subarray ending here with positive
product and the longest ending here with negative product. A positive number
extends both lengths, a negative number swaps the roles, and zero resets both.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
