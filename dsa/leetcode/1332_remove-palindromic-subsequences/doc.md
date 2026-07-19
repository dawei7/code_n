# Remove Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1332 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-palindromic-subsequences/) |

## Problem Description
### Goal
Given a non-empty string `s` containing only the letters `a` and `b`, repeatedly remove a palindromic subsequence until the string is empty. A subsequence keeps the relative order of its chosen characters but does not have to occupy consecutive positions. A palindrome reads identically from left to right and from right to left.

Return the minimum number of removal steps. Each step may choose any non-empty palindromic subsequence of the current string.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1\le n\le1000$ and every character is either `a` or `b`.

**Return value**

The minimum number of palindromic subsequences that must be removed to empty `s`.

### Examples
**Example 1**

- Input: `s = "ababa"`
- Output: `1`
- Explanation: The complete string is a palindrome and can be removed at once.

**Example 2**

- Input: `s = "abb"`
- Output: `2`
- Explanation: Remove `"a"`, then remove `"bb"`.

**Example 3**

- Input: `s = "baabb"`
- Output: `2`
- Explanation: For example, remove `"baab"` and then the remaining `"b"`.
