# Maximum Product Difference Between Two Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1913 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [maximum-product-difference-between-two-pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) |

## Problem Description & Examples
### Goal
Choose four distinct elements `a`, `b`, `c`, and `d` to maximize `(a * b) - (c * d)`.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the maximum product difference.

### Examples
**Example 1**

- Input: `nums = [5,6,2,7,4]`
- Output: `34`

**Example 2**

- Input: `nums = [4,2,5,9,7,4,8]`
- Output: `64`

**Example 3**

- Input: `nums = [1,2,3,4]`
- Output: `10`

---

## Underlying Base Algorithm(s)
The best positive product uses the two largest numbers, and the smallest product to subtract uses the two smallest numbers. Track those four values directly or sort the array and use the ends.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` with direct tracking, or `O(n log n)` by sorting
- **Space Complexity**: `O(1)`
