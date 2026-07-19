# Vowels of All Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2063 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/vowels-of-all-substrings/) |

## Problem Description

### Goal

For every nonempty contiguous substring of a lowercase English string `word`, count how many of its characters are vowels: `a`, `e`, `i`, `o`, or `u`. Return the sum of those counts over all substrings. If one vowel occurrence belongs to several index ranges, include it once for each such substring.

The result can exceed the range of a signed 32-bit integer, so calculations must preserve the full integer value.

### Function Contract

**Inputs**

- `word`: a lowercase English string of length $n$, where $1 \le n \le 10^5$.

**Return value**

- Return the total number of vowel occurrences counted across every nonempty substring of `word`.

### Examples

**Example 1**

- Input: `word = "aba"`
- Output: `6`
- Explanation: Across `"a"`, `"ab"`, `"aba"`, `"b"`, `"ba"`, and `"a"`, the vowel counts sum to $6$.

**Example 2**

- Input: `word = "abc"`
- Output: `3`
- Explanation: The first `a` occurs in `"a"`, `"ab"`, and `"abc"`.

**Example 3**

- Input: `word = "ltcd"`
- Output: `0`
- Explanation: No substring contains a vowel because the string has none.
