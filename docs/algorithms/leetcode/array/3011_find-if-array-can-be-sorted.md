# Find if Array Can Be Sorted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3011 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Sorting |
| Official Link | [find-if-array-can-be-sorted](https://leetcode.com/problems/find-if-array-can-be-sorted/) |

## Problem Description & Examples
### Goal
Determine whether a given array of integers can be transformed into a non-decreasing sorted sequence by repeatedly swapping adjacent elements that share the same number of set bits (binary 1s).

### Function Contract
**Inputs**

- `nums`: A list of positive integers.

**Return value**

- `bool`: Returns `True` if the array can be sorted under the given constraints, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [8, 4, 2, 30, 15]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `True`

**Example 3**

- Input: `nums = [3, 16, 8, 4, 2]`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem relies on the property that elements with the same number of set bits form "exchangeable groups." Within these groups, elements can be reordered arbitrarily. The array is sortable if and only if, when partitioning the array into contiguous segments of elements with the same bit count, the maximum value of a preceding segment is less than or equal to the minimum value of the succeeding segment.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once to identify segments and compare their bounds.
- **Space Complexity**: `O(1)`, as we only store a few variables to track the current segment's bounds and the previous segment's maximum.
