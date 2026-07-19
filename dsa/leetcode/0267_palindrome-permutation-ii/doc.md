# Palindrome Permutation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 267 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-permutation-ii/) |

## Problem Description
### Goal
Given a string `s`, rearrange all of its character occurrences to form palindromes. Every result must have the same length and exact character multiset as the input and must read identically from left to right and right to left.

Return every distinct palindromic permutation in any order. Repeated characters can cause many construction orders to produce the same final string, which must be listed only once. If the character frequencies cannot support a palindrome, return an empty list. For an odd-length input, exactly one odd-frequency character occupies the center of every valid result.

### Function Contract
**Inputs**

- `s`: the characters to permute

**Return value**

All distinct palindromic permutations in any order, or an empty list when none exists.

### Examples
**Example 1**

- Input: `s = "aabb"`
- Output: `["abba","baab"]`

**Example 2**

- Input: `s = "abc"`
- Output: `[]`

**Example 3**

- Input: `s = "aaa"`
- Output: `["aaa"]`
