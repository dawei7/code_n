# Special Array With X Elements Greater Than or Equal X

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1608 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting |
| Official Link | [special-array-with-x-elements-greater-than-or-equal-x](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) |

## Problem Description & Examples
### Goal
Find a value `x` such that exactly `x` elements in the array are greater than or
equal to `x`.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The special value `x`, or `-1` if no such value exists.

### Examples
**Example 1**

- Input: `nums = [3, 5]`
- Output: `2`

**Example 2**

- Input: `nums = [0, 0]`
- Output: `-1`

**Example 3**

- Input: `nums = [0, 4, 3, 0, 4]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Since `x` must be between `0` and `n`, test each possible value and count how
many numbers are at least that value. Sorting or frequency counts make those
counts easy to compute.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` with sorting, or `O(n)` with frequency counts.
- **Space Complexity**: `O(1)` extra with sorting in place, or `O(n)` for counts.
