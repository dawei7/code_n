# Sort List

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `sort_04` |
| Frontend ID | 148 |
| Difficulty | Medium |
| Topics | Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort |
| Official Link | [sort-list](https://leetcode.com/problems/sort-list/) |

## Problem Description & Examples
### Goal
Sort the array in O(n log n) time using divide and conquer.
Split the array in half, sort each half, then merge.
Requirement: O(n log n) - quadratic solutions will FAIL!
Source: https://www.geeksforgeeks.org/merge-sort/

### Function Contract
**Inputs**

- `data`: list-like of n random integers. Mutate in place.
- `n`: length of data.

**Return value**

the same data object, sorted in place (in ascending order).

### Examples
**Example 1**

- Input: `data = [3, 1, 2], n = 3`
- Output: `[1, 2, 3]`

**Example 2**

- Input: `data = [5, 5, 2, 9], n = 4`
- Output: `[2, 5, 5, 9]`

**Example 3**

- Input: `data = [8, 4, 7, 1, 3], n = 5`
- Output: `[1, 3, 4, 7, 8]`

---

## Underlying Base Algorithm(s)
sorting

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `TODO`
