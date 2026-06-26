# Koko Eating Bananas

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_65` |
| Frontend ID | 875 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [koko-eating-bananas](https://leetcode.com/problems/koko-eating-bananas/) |

## Problem Description & Examples
### Goal
Given a linked list (as a list) and integers `left` and `right` (1-indexed), reverse the nodes from position `left` to `right`. Return the modified list.

### Function Contract
**Inputs**

- `head`: List[int]
- `left`: int - start position (1-indexed)
- `right`: int - end position

**Return value**

List[int] - list with sublist reversed

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], left = 2, right = 4`
- Output: `[1, 4, 3, 2, 5]`

**Example 2**

- Input: `head = [50, 98], left = 2, right = 2`
- Output: `[50, 98]`

**Example 3**

- Input: `head = [18, 73], left = 1, right = 2`
- Output: `[73, 18]`

---

## Underlying Base Algorithm(s)
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
