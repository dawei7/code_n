# Minimum Value to Get Positive Step by Step Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1413 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [minimum-value-to-get-positive-step-by-step-sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/) |

## Problem Description & Examples
### Goal
Choose the smallest positive starting value so that when the numbers are added from left to right, every running total stays at least `1`.

### Function Contract
**Inputs**

- `nums`: a list of integers applied one by one to the running total.

**Return value**

The minimum positive integer start value that keeps every intermediate sum positive.

### Examples
**Example 1**

- Input: `nums = [-3,2,-3,4,2]`
- Output: `5`

**Example 2**

- Input: `nums = [1,2]`
- Output: `1`

**Example 3**

- Input: `nums = [1,-2,-3]`
- Output: `5`

---

## Underlying Base Algorithm(s)
Prefix sum tracking. The chosen start value only needs to offset the lowest prefix sum; if the minimum prefix is `m`, the answer is `max(1, 1 - m)`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
