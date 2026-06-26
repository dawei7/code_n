# Smallest String With Swaps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1202 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting |
| Official Link | [smallest-string-with-swaps](https://leetcode.com/problems/smallest-string-with-swaps/) |

## Problem Description & Examples
### Goal
Given index pairs that may be swapped any number of times, return the lexicographically smallest string reachable from `s`.

### Function Contract
**Inputs**

- `s`: original lowercase string.
- `pairs`: index pairs that allow swaps between connected positions.

**Return value**

The smallest string obtainable through any sequence of allowed swaps.

### Examples
**Example 1**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2]]`
- Output: `"bacd"`

**Example 2**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2],[0,2]]`
- Output: `"abcd"`

**Example 3**

- Input: `s = "cba"`, `pairs = [[0,1],[1,2]]`
- Output: `"abc"`

---

## Underlying Base Algorithm(s)
Union-Find connected components and sorting.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n + p alpha(n))`
- **Space Complexity**: `O(n)`
