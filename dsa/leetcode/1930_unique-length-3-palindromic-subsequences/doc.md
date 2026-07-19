# Unique Length-3 Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1930 |
| Difficulty | Medium |
| Topics | Hash Table, String, Bit Manipulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/) |

## Problem Description
### Goal
Given a lowercase English string `s`, count the distinct palindromes of length
three that can be formed as subsequences of `s`. A subsequence retains the
relative order of its selected characters but may delete any number of the
other characters. A palindrome reads identically from left to right and from
right to left.

Different choices of source indices can produce the same three-character
string. Such a palindrome contributes only once to the answer, regardless of
how many index triples realize it. Return the number of unique strings that
satisfy both the subsequence and palindrome requirements.

### Function Contract
**Inputs**

- `s`: a string of $N$ lowercase English letters, where
  $3 \le N \le 10^5$.

**Return value**

- The number of distinct length-three palindromes that occur as subsequences
  of `s`.

### Examples
**Example 1**

- Input: `s = "aabca"`
- Output: `3`

The distinct palindromes are `"aaa"`, `"aba"`, and `"aca"`.

**Example 2**

- Input: `s = "adc"`
- Output: `0`

**Example 3**

- Input: `s = "bbcbaba"`
- Output: `4`

The distinct palindromes are `"aba"`, `"bab"`, `"bbb"`, and `"bcb"`.
