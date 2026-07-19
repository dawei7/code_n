# Increasing Decreasing String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1370 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/increasing-decreasing-string/) |

## Problem Description

### Goal

Rearrange a string of lowercase English letters through repeated increasing and decreasing selections. First choose the smallest remaining character and then repeatedly choose the smallest remaining character strictly greater than the one just appended. When no greater character remains, choose the largest remaining character and repeatedly choose the largest remaining character strictly smaller than the last appended character.

Remove each chosen occurrence from the remaining multiset. Alternate these increasing and decreasing phases until every original occurrence has been appended, then return the resulting string.

### Function Contract

**Inputs**

- `s`: a string of length $n$ containing lowercase English letters.
- Let $A=26$ be the alphabet size and $F$ the maximum frequency of any character.

**Return value**

- The permutation of `s` produced by the prescribed alternating increasing and decreasing selection process.

### Examples

**Example 1**

- Input: `s = "aaaabbbbcccc"`
- Output: `"abccbaabccba"`

**Example 2**

- Input: `s = "rat"`
- Output: `"art"`

**Example 3**

- Input: `s = "leetcode"`
- Output: `"cdelotee"`
