# Max Consecutive Ones II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 487 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/max-consecutive-ones-ii/) |

## Problem Description
### Goal
Given a binary array, choose one contiguous subarray and optionally change at most one `0` within it to `1`. All other values remain unchanged, and the selected positions must be consecutive rather than joined across an unselected gap.

Return the maximum possible number of consecutive `1` values after that single permitted flip. A window containing no zero is valid without using the change, while a window with two zeroes cannot be made all ones. If the array contains only zeroes, one position can form a run of length one; the function returns only the best length.

### Function Contract
**Inputs**

- `nums`: a nonempty binary array

**Return value**

- The maximum possible consecutive-one length after at most one flip

### Examples
**Example 1**

- Input: `nums = [1, 0, 1, 1, 0]`
- Output: `4`

**Example 2**

- Input: `nums = [1, 0, 1, 1, 0, 1]`
- Output: `4`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`
