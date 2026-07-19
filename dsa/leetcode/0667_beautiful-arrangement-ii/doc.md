# Beautiful Arrangement II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 667 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-arrangement-ii/) |

## Problem Description
### Goal
Given integers `n` and `k`, construct an array `answer` containing `n` different positive integers ranging from `1` through `n`. For every adjacent pair, form the absolute difference `abs(answer[i] - answer[i + 1])`.

The collection of those adjacent differences must contain exactly `k` distinct integers. Return any array satisfying both the permutation and difference requirements. Each value from `1` through `n` must appear exactly once; the goal concerns the number of distinct differences, not the sum or maximum of the differences.

### Function Contract
**Inputs**

- `n`: the permutation length
- `k`: the required number of distinct adjacent absolute differences, with $1 \le k < n$

**Return value**

- Any permutation of `1..n` satisfying the difference requirement

### Examples
**Example 1**

- Input: `n = 3`, `k = 1`
- Output: `[1, 2, 3]`

**Example 2**

- Input: `n = 3`, `k = 2`
- Output: `[1, 3, 2]`

**Example 3**

- Input: `n = 4`, `k = 3`
- Output: `[1, 4, 2, 3]`
