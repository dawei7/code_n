# Smallest Substring With Identical Characters II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3399 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/) |

## Problem Description

### Goal

You are given a binary string `s` of length $n$ and may perform at most `numOps` operations. Each operation selects one position and flips its character: `0` becomes `1`, while `1` becomes `0`.

After all chosen operations, inspect every contiguous substring made entirely of one repeated character. Choose the flips so that the longest such substring is as short as possible, then return its length. The operation budget is an upper bound; an optimal transformation may use fewer flips.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$, where $1\le n\le10^5$.
- `numOps`: The maximum number of character flips, where $0\le\texttt{numOps}\le n$.

Every character of `s` is either `0` or `1`.

**Return value**

- The minimum possible length of the longest contiguous block of identical characters.

### Examples

**Example 1**

- Input: `s = "000001", numOps = 1`
- Output: `2`

Flipping `s[2]` gives `"001001"`, where the longest equal-character blocks have length two.

**Example 2**

- Input: `s = "0000", numOps = 2`
- Output: `1`

Flipping `s[0]` and `s[2]` yields the alternating string `"1010"`.

**Example 3**

- Input: `s = "0101", numOps = 0`
- Output: `1`

No operation is needed because the input already alternates.
