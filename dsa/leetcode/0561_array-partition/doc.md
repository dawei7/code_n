# Array Partition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 561 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/array-partition/) |

## Problem Description
### Goal
Given an integer array `nums` containing `2n` elements, divide all of its elements into exactly `n` pairs. Every element must belong to one pair, and the value contributed by a pair is the smaller of its two integers.

Return the maximized sum of these `n` minimum values. You may choose the pairs in any order, so the task is to arrange the elements so that pairing does not unnecessarily discard large values when each pair is reduced to its minimum.

### Function Contract
**Inputs**

- `nums`: a list containing `2n` integers

**Return value**

- The maximum possible sum of the minimum value from every pair

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [6, 2, 6, 5, 1, 2]`
- Output: `9`

**Example 3**

- Input: `nums = [-1, -2]`
- Output: `-2`
