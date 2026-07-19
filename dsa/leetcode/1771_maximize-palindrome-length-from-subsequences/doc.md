# Maximize Palindrome Length From Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1771 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) |

## Problem Description

### Goal

You are given strings `word1` and `word2`. Choose a nonempty subsequence from each word, then concatenate the subsequence from `word1` before the subsequence from `word2`.

The concatenated string must be a palindrome. Return the maximum possible length, or `0` when no such palindrome can use characters from both words.

A subsequence may delete any characters while preserving the relative order of those retained. A palindrome reads identically from left to right and right to left.

### Function Contract

**Inputs**

- `word1`: a lowercase English string with $1 \le A \le 1000$, where $A=\lvert\texttt{word1}\rvert$.
- `word2`: a lowercase English string with $1 \le B \le 1000$, where $B=\lvert\texttt{word2}\rvert$.

Let $L=A+B$.

**Return value**

- Return the greatest length of a palindrome expressible as a nonempty subsequence of `word1` followed by a nonempty subsequence of `word2`.
- Return `0` if no qualifying palindrome exists.

### Examples

**Example 1**

- Input: `word1 = "cacb", word2 = "cbba"`
- Output: `5`
- Explanation: Choose `"ab"` from `word1` and `"cba"` from `word2` to form `"abcba"`.

**Example 2**

- Input: `word1 = "ab", word2 = "ab"`
- Output: `3`
- Explanation: The subsequences `"ab"` and `"a"` concatenate to `"aba"`.

**Example 3**

- Input: `word1 = "aa", word2 = "bb"`
- Output: `0`
- Explanation: No character from one word can pair across the palindrome with a character from the other.
