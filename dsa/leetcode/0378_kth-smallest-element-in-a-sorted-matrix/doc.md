# Kth Smallest Element in a Sorted Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 378 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |

## Problem Description
### Goal
Given an $n \times n$ integer matrix whose rows and columns are each sorted in ascending order, consider the multiset of all $n^{2}$ cell values arranged from smallest to largest. Duplicate values at different cells occupy separate positions, so the task asks for the `k`th smallest element in sorted order, not the `k`th distinct element.

Return the value at the valid one-based rank `k`, rather than its coordinates or a sorted matrix. Use the two-dimensional ordering and meet the memory constraint instead of flattening and fully sorting every cell. For $k = 1$ return a minimum; for $k = n^{2}$ return a maximum.

### Function Contract
**Inputs**

- `matrix`: an $n \times n$ integer matrix sorted nondecreasing across every row and column
- `k`: a one-based rank between `1` and $n^{2}$

**Return value**

- The value at rank `k` in the multiset of all matrix entries.

### Examples
**Example 1**

- Input: `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`
- Output: `13`

**Example 2**

- Input: `matrix = [[-5]], k = 1`
- Output: `-5`

**Example 3**

- Input: `matrix = [[1,2],[1,3]], k = 2`
- Output: `1`
