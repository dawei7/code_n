# Find Minimum in Rotated Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 154 |
| Difficulty | Hard |
| Topics | Array, Binary Search |
| Official Link | [find-minimum-in-rotated-sorted-array-ii](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) |

## Problem Description & Examples
### Goal
Find the minimum value in a nondecreasing array that was rotated an unknown
number of times and may contain duplicates.

### Function Contract
**Inputs**

- `nums`: the rotated sorted array.

**Return value**

The smallest value in `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 3, 5]`
- Output: `1`

**Example 2**

- Input: `nums = [2, 2, 2, 0, 1]`
- Output: `0`

**Example 3**

- Input: `nums = [10, 1, 10, 10, 10]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Use binary search against the right boundary. If `nums[mid] > nums[right]`, the
minimum is to the right of `mid`; if `nums[mid] < nums[right]`, it is at `mid` or
to the left. When equal, decrement `right` because duplicates hide the pivot but
dropping one equal endpoint keeps a minimum in range.

---

## Complexity Analysis
- **Time Complexity**: `O(log n)` on typical inputs, `O(n)` in the duplicate-heavy worst case.
- **Space Complexity**: `O(1)`.
