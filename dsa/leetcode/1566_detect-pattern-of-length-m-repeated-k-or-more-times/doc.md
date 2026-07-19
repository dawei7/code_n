# Detect Pattern of Length M Repeated K or More Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1566 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/) |

## Problem Description
### Goal

Given an integer array `arr`, a pattern length `m`, and a repetition count `k`, determine whether some contiguous block of `m` values occurs at least `k` times consecutively in the array.

The repeated copies must be adjacent and identical element by element. The pattern may begin at any index, and values outside the repeated region do not matter. Return whether such a region exists.

### Function Contract
**Inputs**

- `arr`: An integer array of length $N$, where $2 \le N \le 100$ and $1 \le \texttt{arr[i]} \le 100$.
- `m`: The positive length of one pattern copy, where $1 \le m \le 100$.
- `k`: The number of consecutive copies required, where $2 \le k \le 100$.

**Return value**

Return `true` if there is an index at which the next $mk$ values consist of $k$ identical length-`m` blocks; otherwise return `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,4,4,4,4], m = 1, k = 3`
- Output: `true`

**Example 2**

- Input: `arr = [1,2,1,2,1,1,1,3], m = 2, k = 2`
- Output: `true`

**Example 3**

- Input: `arr = [1,2,1,2,1,3], m = 2, k = 3`
- Output: `false`
