# Determine the Minimum Sum of a k-avoiding Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2829 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/) |

## Problem Description

### Goal

You are given positive integers `n` and `k`. An array is called k-avoiding when it contains `n` distinct positive integers and no two distinct elements in the array have a sum equal to `k`.

Choose any array that satisfies these conditions. The order of its elements is irrelevant to both the restriction and its total.

Return the smallest sum that any k-avoiding array of length `n` can have.

### Function Contract

**Inputs**

- `n`: The required number of distinct positive integers, where $1 \le n \le 50$.
- `k`: The forbidden sum, where $1 \le k \le 50$.

**Return value**

Return the minimum possible sum of `n` distinct positive integers such that no pair of distinct chosen elements sums to `k`.

### Examples

#### Example 1

- **Input:** `n = 5, k = 4`
- **Output:** `18`
- **Explanation:** `[1, 2, 4, 5, 6]` is k-avoiding and has sum `18`; no valid five-element array has a smaller sum.

#### Example 2

- **Input:** `n = 2, k = 6`
- **Output:** `3`
- **Explanation:** `[1, 2]` is valid and has the minimum possible sum `3`.
