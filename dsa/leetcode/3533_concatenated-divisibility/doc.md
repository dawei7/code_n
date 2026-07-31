# Concatenated Divisibility

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3533 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenated-divisibility/) |

## Problem Description

### Goal

You are given positive integers in `nums` and a positive divisor `k`. Arrange every element of `nums` exactly once. Reading the decimal representations in that order without separators forms one concatenated integer.

A permutation is valid when its concatenated integer is divisible by `k`. Among all valid permutations, return the lexicographically smallest list of integers. Lexicographic comparison applies to the list elements themselves, not to their concatenated string. If no full permutation is valid, return an empty list.

### Function Contract

**Inputs**

- `nums`: A list of positive integers, where $1 \le \lvert\texttt{nums}\rvert \le 13$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: The divisor, where $1 \le k \le 100$.

Repeated values are separate elements and must each appear in the returned permutation.

**Return value**

- The lexicographically smallest full permutation whose decimal concatenation is divisible by `k`, or `[]` when none exists.

### Examples

**Example 1**

- Input: `nums = [3,12,45], k = 5`
- Output: `[3,12,45]`
- Explanation: Both `[3,12,45]` and `[12,3,45]` produce a multiple of $5$; the first list is lexicographically smaller.

**Example 2**

- Input: `nums = [10,5], k = 10`
- Output: `[5,10]`
- Explanation: `510` is divisible by $10$, while `105` is not.

**Example 3**

- Input: `nums = [1,2,3], k = 5`
- Output: `[]`
- Explanation: Neither of the six full permutations produces a multiple of $5$.
