# Distant Barcodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1054 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Official Link | [distant-barcodes](https://leetcode.com/problems/distant-barcodes/) |

## Problem Description & Examples
### Goal
Rearrange the barcodes so equal values are never adjacent. A valid arrangement is guaranteed to exist.

### Function Contract
**Inputs**

- `barcodes`: List[int]

**Return value**

List[int] - any arrangement with no equal adjacent values

### Examples
**Example 1**

- Input: `barcodes = [1, 1, 1, 2, 2, 3]`
- Output: `[1, 2, 1, 2, 1, 3]`

**Example 2**

- Input: `barcodes = [1, 1, 1, 1, 2, 2, 3, 3]`
- Output: `[1, 2, 1, 3, 1, 2, 1, 3]`

**Example 3**

- Input: `barcodes = [7, 7, 8, 8]`
- Output: `[7, 8, 7, 8]`

---

## Underlying Base Algorithm(s)
Greedy max-heap rearrangement.

---

## Complexity Analysis
- **Time Complexity**: `O(n log u)` where `u` is the number of distinct barcodes
- **Space Complexity**: `O(u)`
