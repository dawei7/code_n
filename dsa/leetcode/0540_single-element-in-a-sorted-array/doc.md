# Single Element in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 540 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` sorted in ascending order, exactly one value appears once and every other value appears exactly twice. Equal pairs are adjacent because of the sorted order.

Return the single value that lacks a matching occurrence. Do not return its index, and do not treat one member of a normal pair as the answer. Meet the required $O(\log n)$ time and $O(1)$ extra space by exploiting how pair alignment changes around the singleton rather than scanning or copying the complete array.

### Function Contract
**Inputs**

- `nums`: a nonempty sorted integer array of odd length with one singleton and adjacent duplicate pairs

**Return value**

- The unique value that occurs once

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]`
- Output: `2`

**Example 2**

- Input: `nums = [3, 3, 7, 7, 10, 11, 11]`
- Output: `10`

**Example 3**

- Input: `nums = [1]`
- Output: `1`
