# Search in Rotated Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_68` |
| Frontend ID | 33 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Problem Description & Examples
### Goal
Given a linked list (as array) and integer `n`, remove the `n`-th node from the end of the list and return the modified list.

### Function Contract
**Inputs**

- `head`: List[int]
- `n`: int - position from end (1-indexed)

**Return value**

List[int] - list with nth node removed

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], n = 2`
- Output: `[1, 2, 3, 5]`

**Example 2**

- Input: `head = [50, 98], n = 2`
- Output: `[98]`

**Example 3**

- Input: `head = [18, 73], n = 1`
- Output: `[18]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
