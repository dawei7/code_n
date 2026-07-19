# Ugly Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 264 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Dynamic Programming, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number-ii/) |

## Problem Description
### Goal
Ugly numbers are positive integers whose prime factors are restricted to `2`, `3`, and `5`. The sequence is arranged in increasing order and begins with `1`, which is included despite having no prime factors.

Given a positive one-based index `n`, return the `n`th value in this sequence. Products may contain any repeated combination of the three allowed factors, but duplicate products such as those reachable in several ways occupy only one sequence position. The function returns the numeric value rather than the preceding sequence, and values containing any other prime factor must be excluded.

### Function Contract
**Inputs**

- `n`: a one-based position in the ugly-number sequence

**Return value**

The `n`th ugly number, with one as the first.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `12`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 15`
- Output: `24`
