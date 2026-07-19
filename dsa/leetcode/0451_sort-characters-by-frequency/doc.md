# Sort Characters By Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 451 |
| Difficulty | Medium |
| Topics | Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/) |

## Problem Description
### Goal
Given a string containing letters and digits, sort it in decreasing order based on the frequency of each case-sensitive character.

Return the sorted string, grouping each character's occurrences together according to decreasing frequency. When several characters have equal counts, return any valid group order. Preserve every occurrence exactly once and do not merge uppercase and lowercase forms. The task returns one valid reordered string rather than the frequency table.

### Function Contract
**Inputs**

- `s`: a string containing letters and digits

**Return value**

- A permutation of `s` ordered by nonincreasing character frequency. Characters with equal frequencies may appear in any relative order.

### Examples
**Example 1**

- Input: `s = "tree"`
- Output: `"eetr"`

**Example 2**

- Input: `s = "cccaaa"`
- Output: `"cccaaa"` (the tied groups may be reversed)

**Example 3**

- Input: `s = "Aabb"`
- Output: `"bbAa"`
