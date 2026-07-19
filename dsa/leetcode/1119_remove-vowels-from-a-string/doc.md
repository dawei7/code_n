# Remove Vowels from a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1119 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-vowels-from-a-string/) |

## Problem Description

### Goal

You are given a string `s` containing only lowercase English letters. Produce a new string after removing every occurrence of the lowercase vowels `a`, `e`, `i`, `o`, and `u`.

All consonants must remain in their original relative order. Removing a vowel closes the gap rather than replacing it with whitespace or another marker. If every character is a vowel, return the empty string; if there are no vowels, return `s` unchanged in value.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

- The subsequence of `s` formed by retaining exactly those characters not in `{a, e, i, o, u}`.

### Examples

**Example 1**

- Input: `s = "leetcodeisacommunityforcoders"`
- Output: `"ltcdscmmntyfrcdrs"`

**Example 2**

- Input: `s = "aeiou"`
- Output: `""`

**Example 3**

- Input: `s = "rhythm"`
- Output: `"rhythm"`
