# Strings Differ by One Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1554 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Rolling Hash, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strings-differ-by-one-character/) |

## Problem Description
### Goal
You are given a dictionary of distinct lowercase strings, all having the same length. Determine whether the dictionary contains two different strings whose characters differ at exactly one index.

The two strings must match at every other position. A pair that differs in two or more positions is invalid, and equal strings would differ at zero positions rather than one. Return whether at least one qualifying pair exists.

### Function Contract
**Inputs**

- `dict`: $q$ distinct lowercase strings, all of width $ell$, with $1 \le q \le 10^5$, $1 \le \ell \le 20$, and at most $10^5$ characters in total.

**Return value**

`true` if some two dictionary strings have Hamming distance exactly one; otherwise `false`.

### Examples
**Example 1**

- Input: `dict = ["abcd", "acbd", "aacd"]`
- Output: `true`
- Explanation: `"abcd"` and `"aacd"` differ only at their second character.

**Example 2**

- Input: `dict = ["ab", "cd", "yz"]`
- Output: `false`
- Explanation: Every pair differs in both positions.

**Example 3**

- Input: `dict = ["abcd", "cccc", "abyd", "abab"]`
- Output: `true`
- Explanation: `"abcd"` and `"abyd"` differ only at index two.
