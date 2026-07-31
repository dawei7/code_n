# Smallest Substring With Identical Characters I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3398 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-i/) |

## Problem Description

### Goal

You are given a binary string `s` of length $n$ and may change at most `numOps` of its characters. One operation chooses any index and flips that character from `0` to `1` or from `1` to `0`.

After the chosen flips, consider every contiguous substring whose characters are all identical. Minimize the length of the longest such substring, and return that minimum length. Operations are optional, so fewer than `numOps` flips may be used.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$, where $1\le n\le1000$.
- `numOps`: The maximum number of flips, where $0\le\texttt{numOps}\le n$.

Every character of `s` is either `0` or `1`.

**Return value**

- The minimum achievable length of the longest contiguous block of identical characters.

### Examples

**Example 1**

- Input: `s = "000001", numOps = 1`
- Output: `2`

Flipping `s[2]` produces `"001001"`, whose longest identical blocks have length two.

**Example 2**

- Input: `s = "0000", numOps = 2`
- Output: `1`

Flipping `s[0]` and `s[2]` produces the alternating string `"1010"`.

**Example 3**

- Input: `s = "0101", numOps = 0`
- Output: `1`

The input already alternates, so every identical block has length one.
