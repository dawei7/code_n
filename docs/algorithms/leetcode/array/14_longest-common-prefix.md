# Longest Common Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_5` |
| Frontend ID | 14 |
| Difficulty | Easy |
| Topics | Array, String, Trie |
| Official Link | [longest-common-prefix](https://leetcode.com/problems/longest-common-prefix/) |

## Problem Description & Examples
### Goal
Write a function to find the longest common prefix string among an array of strings. If there is no common prefix, return `""`.

### Function Contract
**Inputs**

- `strs`: List[str]

**Return value**

str - the longest common prefix

### Examples
**Example 1**

- Input: `strs = ["flower", "flow", "flight"]`
- Output: `"fl"`

**Example 2**

- Input: `strs = ['tkgkuhmpxnh']`
- Output: `'tkgkuhmpxnh'`

**Example 3**

- Input: `strs = ['ogm', 'omjfmxkpt']`
- Output: `'o'`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
