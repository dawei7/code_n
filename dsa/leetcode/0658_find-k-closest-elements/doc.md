# Find K Closest Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 658 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/find-k-closest-elements/) |

## Problem Description
### Goal
Given an integer array `arr` sorted in ascending order and integers `k` and `x`, select the `k` integers in the array that are closest to `x`. Value `a` is closer than value `b` when $| a - x | < | b - x |$, or when the distances are equal and $a < b$.

Return the selected values sorted in ascending order. Duplicate array occurrences remain separate selectable elements, `x` does not need to appear in the array, and the smaller value wins every equal-distance tie before the final result is ordered.

### Function Contract
**Inputs**

- `arr`: a nonempty list of integers sorted in ascending order
- `k`: the positive number of elements to return, no greater than `len(arr)`
- `x`: the comparison value, which need not occur in the array

**Return value**

- The selected `k` closest values in increasing order

### Examples
**Example 1**

- Input: `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`
- Output: `[1, 2, 3, 4]`

**Example 2**

- Input: `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = -1`
- Output: `[1, 2, 3, 4]`

**Example 3**

- Input: `arr = [1, 2, 4, 5]`, `k = 2`, `x = 3`
- Output: `[2, 4]`
