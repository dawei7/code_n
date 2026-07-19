# Binary Search

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 704 |
| Difficulty | Easy |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search/) |

## Problem Description
### Goal
Given an integer array `nums` sorted in ascending order and an integer `target`, search for `target` in the array.

If the value exists, return its zero-based index; otherwise return `-1`. The required algorithm must run in $O(\log n)$ time, so it should use the sorted ordering to discard part of the remaining search interval after each comparison rather than scanning every element.

### Function Contract
**Inputs**

- `nums`: a nonempty strictly increasing integer array
- `target`: the value to locate

**Return value**

- The zero-based index of `target`, or `-1` when it is absent

### Examples
**Example 1**

- Input: `nums = [-1,0,3,5,9,12], target = 9`
- Output: `4`

**Example 2**

- Input: `nums = [-1,0,3,5,9,12], target = 2`
- Output: `-1`

**Example 3**

- Input: `nums = [5], target = 5`
- Output: `0`
