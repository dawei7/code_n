# Largest Values From Labels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1090 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Official Link | [largest-values-from-labels](https://leetcode.com/problems/largest-values-from-labels/) |

## Problem Description & Examples
### Goal
Pick at most `numWanted` items to maximize the total value, while using no more than `useLimit` items with the same label.

### Function Contract
**Inputs**

- `values`: item values.
- `labels`: label for each item at the same index.
- `numWanted`: maximum number of chosen items.
- `useLimit`: maximum chosen items allowed for any single label.

**Return value**

The largest possible sum of selected values.

### Examples
**Example 1**

- Input: `values = [5,4,3,2,1]`, `labels = [1,1,2,2,3]`, `numWanted = 3`, `useLimit = 1`
- Output: `9`

**Example 2**

- Input: `values = [5,4,3,2,1]`, `labels = [1,3,3,3,2]`, `numWanted = 3`, `useLimit = 2`
- Output: `12`

**Example 3**

- Input: `values = [9,8,8,7,6]`, `labels = [0,0,0,1,1]`, `numWanted = 4`, `useLimit = 2`
- Output: `30`

---

## Underlying Base Algorithm(s)
Greedy sorting with per-label counting.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for sorting and label counts.
