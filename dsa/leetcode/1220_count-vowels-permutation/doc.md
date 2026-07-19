# Count Vowels Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1220 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-vowels-permutation/) |

## Problem Description

### Goal

Given an integer `n`, count the strings of length `n` that contain only the lowercase vowels `a`, `e`, `i`, `o`, and `u` and obey all of these adjacency rules:

- Each `a` may be followed only by `e`.
- Each `e` may be followed only by `a` or `i`.
- Each `i` may be followed by any vowel except `i`.
- Each `o` may be followed only by `i` or `u`.
- Each `u` may be followed only by `a`.

Return the number of valid strings modulo $M=10^9+7$.

### Function Contract

**Inputs**

- `n`: The required string length, where $1\le n\le2\cdot10^4$.

**Return value**

- The number of vowel strings of length `n` satisfying every transition rule, reduced modulo $M$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `5`

Each individual vowel is valid.

**Example 2**

- Input: `n = 2`
- Output: `10`

The valid strings are `ae`, `ea`, `ei`, `ia`, `ie`, `io`, `iu`, `oi`, `ou`, and `ua`.

**Example 3**

- Input: `n = 5`
- Output: `68`
