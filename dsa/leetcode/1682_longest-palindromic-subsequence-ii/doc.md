# Longest Palindromic Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1682 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence-ii/) |

## Problem Description
### Goal

A subsequence of `s` is called good when it is a palindrome of even length and its neighboring characters are different everywhere except at its center. The two middle characters are therefore the only adjacent equal pair that the chosen sequence may contain. Characters that are not selected may occur anywhere between consecutive chosen positions in the original string.

For example, `"abba"` is good: it reads the same in both directions, has even length, and only its middle `"bb"` pair is equal. An odd palindrome such as `"bcb"` is not good, while `"bbbb"` is also invalid because it has equal neighbors outside the middle. Return the maximum possible length of a good palindromic subsequence of `s`; return zero when no equal pair can form its center.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters, with $n = \lvert s \rvert$

**Return value**

The length of the longest subsequence of `s` satisfying every good-palindrome rule.

### Examples
**Example 1**

- Input: `s = "bbabab"`
- Output: `4`

The subsequence `"baab"` is good.

**Example 2**

- Input: `s = "dcbccacdb"`
- Output: `4`

One longest choice is `"dccd"`.

**Example 3**

- Input: `s = "aaaa"`
- Output: `2`

Any equal pair is good, but all four characters would create equal neighbors outside the center.
