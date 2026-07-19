# Find K-Length Substrings With No Repeated Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1100 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) |

## Problem Description

### Goal

Given a string `s` and an integer `k`, consider every substring of `s` whose length is exactly `k`. Count how many of those substrings contain no repeated characters.

Substrings are contiguous and are counted by their positions, so identical valid text at different starting indices contributes more than once. The value `k` may exceed the length of `s`; in that case no length-`k` substring exists.

### Function Contract

**Inputs**

- `s`: a string of $n$ lowercase English letters, where $1 \leq n \leq 10^4$.
- `k`: the required substring length, where $1 \leq k \leq 10^4$.

**Return value**

The number of start indices whose length-`k` substring has pairwise distinct characters.

### Examples

**Example 1**

- Input: `s = "havefunonleetcode", k = 5`
- Output: `6`

The valid windows are `"havef"`, `"avefu"`, `"vefun"`, `"efuno"`, `"etcod"`, and `"tcode"`.

**Example 2**

- Input: `s = "home", k = 5`
- Output: `0`
