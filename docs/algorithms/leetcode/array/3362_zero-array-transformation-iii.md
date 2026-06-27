# Zero Array Transformation III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3362 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Official Link | [zero-array-transformation-iii](https://leetcode.com/problems/zero-array-transformation-iii/) |

## Problem Description & Examples
### Goal
Given an array `nums` and a collection of `queries` where each query `[l, r]` allows you to decrement all elements in the range `[l, r]` by 1, determine the minimum number of queries required to make every element in `nums` equal to 0. If it is impossible to reduce all elements to 0, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the target values to be reduced to zero.
- `queries`: A list of lists, where each inner list `[l, r]` represents an interval that can be decremented.

**Return value**

- An integer representing the minimum number of queries needed, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `nums = [2, 0, 2]`, `queries = [[0, 2], [0, 2], [1, 1]]`
- Output: `2`

**Example 2**

- Input: `nums = [4, 3, 2, 1]`, `queries = [[1, 3], [0, 2], [0, 0], [0, 3]]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 1, 1]`, `queries = [[0, 1], [1, 2]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with a Max-Heap**. We iterate through the array indices, maintaining a set of "active" queries that cover the current index. We use a difference array (or a sweep-line technique) to track the current reduction applied to each index. If the current value is still greater than zero, we greedily pick the available queries that extend the furthest to the right to satisfy the requirement, as these are most likely to help with future indices.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + Q log Q)`, where `N` is the length of `nums` and `Q` is the number of queries. This accounts for sorting the queries and heap operations.
- **Space Complexity**: `O(N + Q)` to store the difference array and the query structures.
