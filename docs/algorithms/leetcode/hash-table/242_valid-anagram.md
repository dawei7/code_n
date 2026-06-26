# Valid Anagram

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_3` |
| Frontend ID | 242 |
| Difficulty | Easy |
| Topics | Hash Table, String, Sorting |
| Official Link | [valid-anagram](https://leetcode.com/problems/valid-anagram/) |

## Problem Description & Examples
### Goal
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once.

### Function Contract
**Inputs**

- `s`: str
- `t`: str

**Return value**

bool - True if t is an anagram of s

### Examples
**Example 1**

- Input: `s = "anagram", t = "nagaram"`
- Output: `True`

**Example 2**

- Input: `s = 'c', t = 'b'`
- Output: `False`

**Example 3**

- Input: `s = 'ac', t = 'ab'`
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
