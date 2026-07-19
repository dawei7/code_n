# Valid Palindrome II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 680 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-palindrome-ii/) |

## Problem Description
### Goal
Given a string `s`, determine whether it can be a palindrome after deleting at most one character. A palindrome reads the same from left to right and from right to left.

Return `True` if the original string is already palindromic or if removing one character from any position makes it palindromic; otherwise return `False`. Deletion closes the gap while preserving the order of every remaining character, and you may not replace, reorder, or delete two characters.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string

**Return value**

- `true` if deleting zero or one character can produce a palindrome; otherwise `false`

### Examples
**Example 1**

- Input: `s = "aba"`
- Output: `true`

**Example 2**

- Input: `s = "abca"`
- Output: `true`

**Example 3**

- Input: `s = "abc"`
- Output: `false`
