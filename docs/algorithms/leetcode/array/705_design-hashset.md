# Design HashSet

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_9` |
| Frontend ID | 705 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Linked List, Design, Hash Function |
| Official Link | [design-hashset](https://leetcode.com/problems/design-hashset/) |

## Problem Description & Examples
### Goal
Design a HashSet without using any built-in hash table libraries.

Implement a `solve(operations)` function that processes a list of operations and returns the results. Each operation is `['add', key]`, `['remove', key]`, or `['contains', key]`. `contains` returns `True` or `False`.

### Function Contract
**Inputs**

- `operations`: List[List] - add/remove/contains operations

**Return value**

List[bool] - results of contains operations

### Examples
**Example 1**

- Input: `ops = [["add", 1], ["contains", 1], ["remove", 1], ["contains", 1]]`
- Output: `[True, False]`

**Example 2**

- Input: `operations = [['contains', 13], ['remove', 2], ['contains', 17], ['remove', 13]]`
- Output: `[False, False]`

**Example 3**

- Input: `operations = [['add', 5], ['add', 9], ['contains', 16], ['contains', 16]]`
- Output: `[False, False]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
