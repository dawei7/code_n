# Kth Distinct String in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2053 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-distinct-string-in-an-array/) |

## Problem Description

### Goal

A string is *distinct* in `arr` only when it occurs exactly once in the complete array. Filter the array conceptually to those distinct strings while preserving their original relative order; repeated values contribute no entry at all, regardless of where their copies occur.

Given the one-based rank `k`, return the string occupying that position in the ordered distinct sequence. If the array contains fewer than `k` strings with total frequency one, return the empty string `""`.

### Function Contract

**Inputs**

- `arr`: an array of $n$ lowercase strings, where $1 \le n \le 1000$ and each string has length from $1$ through $5$.
- `k`: a one-based rank satisfying $1 \le k \le n$.

**Return value**

- Return the `k`th string, in original array order, whose total frequency is exactly one.
- Return `""` when fewer than `k` such strings exist.

### Examples

**Example 1**

- Input: `arr = ["d","b","c","b","c","a"], k = 2`
- Output: `"a"`
- Explanation: Only `"d"` and `"a"` occur once, in that order.

**Example 2**

- Input: `arr = ["aaa","aa","a"], k = 1`
- Output: `"aaa"`
- Explanation: Every value is distinct, so the first array element is also the first distinct string.

**Example 3**

- Input: `arr = ["a","b","a"], k = 3`
- Output: `""`
- Explanation: Only `"b"` is distinct, so a third distinct string does not exist.
