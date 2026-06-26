# GCD Sort of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1998 |
| Difficulty | Hard |
| Topics | Array, Math, Union-Find, Sorting, Number Theory |
| Official Link | [gcd-sort-of-an-array](https://leetcode.com/problems/gcd-sort-of-an-array/) |

## Problem Description & Examples
### Goal
You may swap two numbers whenever their greatest common divisor is greater than `1`. Decide whether the array can be sorted in non-decreasing order.

### Function Contract
**Inputs**

- `nums`: an array of positive integers.

**Return value**

Return `True` if the array can be sorted using allowed swaps, otherwise `False`.

### Examples
**Example 1**

- Input: `nums = [7,21,3]`
- Output: `True`

**Example 2**

- Input: `nums = [5,2,6,2]`
- Output: `False`

**Example 3**

- Input: `nums = [10,5,9,3,15]`
- Output: `True`

---

## Underlying Base Algorithm(s)
Numbers connected through shared prime factors can be freely rearranged within their component. Factor each number, union it with its prime factors, then compare each original value with the value at the same position in the sorted array; mismatched values must belong to the same component.

---

## Complexity Analysis
- **Time Complexity**: `O(n sqrt M + n log n)` with trial division factorization.
- **Space Complexity**: `O(n + M)` depending on union-find indexing.
