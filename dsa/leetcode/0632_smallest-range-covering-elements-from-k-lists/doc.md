# Smallest Range Covering Elements from K Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 632 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Greedy, Sliding Window, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) |

## Problem Description
### Goal
You are given `k` nonempty lists of integers, each sorted in non-decreasing order. Find an inclusive range `[a, b]` that contains at least one number from every one of the `k` lists.

Choose the smallest such range. Range `[a, b]` is smaller than `[c, d]` when $b - a < d - c$; if the widths are equal, it is smaller when $a < c$. Return the two endpoints of the selected range, including a zero-width range when one value occurs in every list.

### Function Contract
**Inputs**

- `nums`: `K` nonempty lists of integers, each sorted in nondecreasing order

**Return value**

- Two integers `[left, right]` describing the selected inclusive range
- The range must cover at least one element from every input list

### Examples
**Example 1**

- Input: `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`
- Output: `[20,24]`

**Example 2**

- Input: `nums = [[1,2,3],[1,2,3],[1,2,3]]`
- Output: `[1,1]`

**Example 3**

- Input: `nums = [[-2],[4],[10]]`
- Output: `[-2,10]`
