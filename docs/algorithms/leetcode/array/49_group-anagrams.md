# Group Anagrams

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_6` |
| Frontend ID | 49 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [group-anagrams](https://leetcode.com/problems/group-anagrams/) |

## Problem Description & Examples
### Goal
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Function Contract
**Inputs**

- `strs`: List[str]

**Return value**

List[List[str]] - groups of anagrams

### Examples
**Example 1**

- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

**Example 2**

- Input: `strs = ['gdce']`
- Output: `[['gdce']]`

**Example 3**

- Input: `strs = ['eg', 'ge']`
- Output: `[['eg', 'ge']]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
