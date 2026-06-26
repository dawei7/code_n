# First Missing Positive

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_22` |
| Frontend ID | 41 |
| Difficulty | Hard |
| Topics | Array, Hash Table |
| Official Link | [first-missing-positive](https://leetcode.com/problems/first-missing-positive/) |

## Problem Description & Examples
### Goal
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

### Function Contract
**Inputs**

- `s`: str

**Return value**

bool - True if s is a palindrome (alphanumeric only, case-insensitive)

### Examples
**Example 1**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `True`

**Example 2**

- Input: `s = '4'`
- Output: `True`

**Example 3**

- Input: `s = 'j4'`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
