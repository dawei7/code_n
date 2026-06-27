# Closest Equal Element Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3488 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search |
| Official Link | [closest-equal-element-queries](https://leetcode.com/problems/closest-equal-element-queries/) |

## Problem Description & Examples
### Goal
Given an array of integers, process a series of queries. Each query provides an index `i` and an integer `k`. You must find the index `j` such that `nums[j] == nums[i]` and the absolute distance `|i - j|` is minimized, subject to the constraint that `|i - j| <= k`. If multiple such indices exist, return the one with the smallest index; if none exist, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `queries`: A list of lists, where each inner list contains two integers `[i, k]`.

**Return value**

- A list of integers representing the result for each query.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1, 1, 2], queries = [[0, 2], [5, 1]]`
- Output: `[3, -1]`

**Example 2**

- Input: `nums = [1, 1, 1], queries = [[1, 1]]`
- Output: `[0]`

**Example 3**

- Input: `nums = [1, 2, 3], queries = [[0, 1]]`
- Output: `[-1]`

---

## Underlying Base Algorithm(s)
The problem is solved by pre-processing the array to map each unique value to a sorted list of its indices. For each query `(i, k)`, we use binary search (`bisect_left` and `bisect_right`) on the index list corresponding to `nums[i]` to find candidates within the range `[i-k, i+k]`. We then evaluate the distance to `i` for the neighbors of `i` in the sorted list to identify the closest valid index.

---

## Complexity Analysis
- **Time Complexity**: `O(N + Q log N)`, where `N` is the length of `nums` and `Q` is the number of queries. Pre-processing takes `O(N)`, and each query takes `O(log N)` due to binary search.
- **Space Complexity**: `O(N)` to store the hash map of indices.
