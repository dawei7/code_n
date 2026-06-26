# Search in Rotated Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_69` |
| Frontend ID | 81 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [search-in-rotated-sorted-array-ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) |

## Problem Description & Examples
### Goal
Given a linked list (as array) `L: L0  L1  ...  Ln`, reorder it to `L0  Ln  L1  Ln-1  L2  Ln-2  ...` (in-place).

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

List[int] - reordered list

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4]`
- Output: `[1, 4, 2, 3]`

**Example 2**

- Input: `head = [50, 98]`
- Output: `[50, 98]`

**Example 3**

- Input: `head = [18, 73]`
- Output: `[18, 73]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
