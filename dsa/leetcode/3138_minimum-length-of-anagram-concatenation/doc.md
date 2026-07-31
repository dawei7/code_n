# Minimum Length of Anagram Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3138 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-length-of-anagram-concatenation/) |

## Problem Description
### Goal
You are given a string `s` that can be divided into consecutive, equally sized pieces. There is some string `t` such that every piece is an anagram of `t`: each piece contains exactly the same letters with the same multiplicities, although their orders may differ.

An anagram rearranges a string's letters without adding or removing any occurrence. For instance, `"aab"`, `"aba"`, and `"baa"` are anagrams of one another.

More than one choice of `t` may explain the given string, including `t = s` itself. Return the minimum possible length of `t`.

### Function Contract
**Inputs**

- `s`: A nonempty string containing only lowercase English letters.

Let $n = \lvert\texttt{s}\rvert$, where $1 \le n \le 10^5$.

**Return value**

Return the minimum positive length of a string `t` whose anagrams can be concatenated, along the existing boundaries in `s`, to form all of `s`.

### Examples
**Example 1**

- Input: `s = "abba"`
- Output: `2`
- Explanation: The two pieces `"ab"` and `"ba"` are anagrams, so `t` may have length $2$.

**Example 2**

- Input: `s = "cdef"`
- Output: `4`
- Explanation: No shorter aligned partition works, while choosing `t = s` always does.

**Example 3**

- Input: `s = "abcbcacabbaccba"`
- Output: `3`
- Explanation: Splitting the string into five length-$3$ pieces gives `"abc"`, `"bca"`, `"cab"`, `"bac"`, and `"cba"`; all have the same character multiplicities.
