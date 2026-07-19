# Next Greater Element II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 503 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/next-greater-element-ii/) |

## Problem Description
### Goal
Given a nonempty circular integer array `nums`, treat the position after the final element as position zero. For each original index, scan forward in traversal order, wrapping through the beginning at most once, and seek the first later value that is strictly greater than the current value.

Return one answer per original position. Store that first greater value when it exists and `-1` otherwise. Equal values do not qualify, the search cannot use the starting occurrence as its own greater element, and a value found after wrapping is valid only when it is the earliest qualifying value along that circular traversal.

### Function Contract
**Inputs**

- `nums`: a nonempty integer array interpreted circularly

**Return value**

- One next-greater value per input position

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `[2, -1, 2]`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 3]`
- Output: `[2, 3, 4, -1, 4]`

**Example 3**

- Input: `nums = [5, 4, 3, 2, 1]`
- Output: `[-1, 5, 5, 5, 5]`
