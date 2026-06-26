# Check if Array Is Sorted and Rotated

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1752 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [check-if-array-is-sorted-and-rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |

## Problem Description & Examples
### Goal
Determine whether an array could be produced by taking a nondecreasing sorted array and rotating it some number of positions.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return `True` if `nums` is sorted and rotated, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [3,4,5,1,2]`
- Output: `True`

**Example 2**

- Input: `nums = [2,1,3,4]`
- Output: `False`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `True`

---

## Underlying Base Algorithm(s)
In a sorted-and-rotated nondecreasing array, there can be at most one place where `nums[i] > nums[(i + 1) % n]`. Count those drops around the circular boundary and accept only when the count is at most one.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
