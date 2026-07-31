# Minimum Length of String After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3223 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-operations/) |

## Problem Description

### Goal

You are given a lowercase English string `s`. In one operation, choose an occurrence whose character also appears somewhere to its left and somewhere to its right. Delete the closest equal occurrence on each side, while keeping the chosen middle occurrence.

You may repeat this operation in any valid order. Return the smallest length that the string can have after all beneficial operations. Each operation deletes exactly two copies of one character; characters of other values remain in their relative order.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert\texttt{s}\rvert \leq 2\cdot10^5$.

**Return value**

Return the minimum achievable length after applying the operation any number of times.

### Examples

**Example 1**

- Input: `s = "abaacbcbb"`
- Output: `5`
- Explanation: The counts of `a`, `b`, and `c` reduce respectively to `1`, `2`, and `2`.

**Example 2**

- Input: `s = "aa"`
- Output: `2`
- Explanation: No occurrence has an equal character on both sides.

**Example 3**

- Input: `s = "aaaaa"`
- Output: `1`
- Explanation: Two operations remove four copies while preserving one middle copy.
