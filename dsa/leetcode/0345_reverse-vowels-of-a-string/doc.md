# Reverse Vowels of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 345 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/) |

## Problem Description
### Goal
Given a string `s`, identify occurrences of the English vowels `a`, `e`, `i`, `o`, and `u` in either uppercase or lowercase form. Reverse the sequence of those vowel characters across their existing positions.

Return a new string in which the first vowel position receives the last original vowel, the second receives the second-to-last, and so on. Preserve each vowel's original case as part of the moved character. Every consonant, digit, space, and symbol must remain at its original index. Strings with fewer than two vowels are returned unchanged.

### Function Contract
**Inputs**

- `s`: the source string

**Return value**

- A string with the sequence of vowels reversed and all non-vowel positions unchanged.

### Examples
**Example 1**

- Input: `s = "IceCreAm"`
- Output: `"AceCreIm"`

**Example 2**

- Input: `s = "leetcode"`
- Output: `"leotcede"`

**Example 3**

- Input: `s = "rhythm"`
- Output: `"rhythm"`
