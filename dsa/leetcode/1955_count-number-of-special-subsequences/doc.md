# Count Number of Special Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1955 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-special-subsequences/) |

## Problem Description
### Goal
A sequence is special when it contains a positive number of `0` values,
followed by a positive number of `1` values, followed by a positive number of
`2` values. No other ordering or value is allowed within that sequence.

Given an array containing only `0`, `1`, and `2`, count its special
subsequences. A subsequence keeps the original relative order while possibly
discarding elements. Two subsequences count separately when they select
different sets of source indices, even if their resulting value sequences are
identical. Return the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le 10^5$ and every element is
  `0`, `1`, or `2`.

**Return value**

- The number of index-distinct special subsequences, reduced modulo
  $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 2]`
- Output: `3`

**Example 2**

- Input: `nums = [2, 2, 0, 0]`
- Output: `0`

**Example 3**

- Input: `nums = [0, 1, 2, 0, 1, 2]`
- Output: `7`
