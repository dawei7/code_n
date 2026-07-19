# Divide Array Into Increasing Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1121 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/divide-array-into-increasing-sequences/) |

## Problem Description

### Goal

You are given an integer array `nums` sorted in non-decreasing order and a positive integer `k`. Divide all array elements into one or more disjoint subsequences. Every element must belong to exactly one subsequence, while its relative order from `nums` is preserved.

Each resulting subsequence must be strictly increasing and must contain at least `k` elements. Return `true` when such a division exists and `false` otherwise. The subsequences need not use contiguous positions, and their lengths may exceed `k`.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, sorted in non-decreasing order.
- `k`: the minimum permitted length of every resulting subsequence.

**Return value**

- `true` exactly when all elements can be partitioned into disjoint strictly increasing subsequences, each of length at least `k`.

### Examples

**Example 1**

- Input: `nums = [1,2,2,3,3,4,4]`, `k = 3`
- Output: `true`

One division is `[1,2,3,4]` and `[2,3,4]`.

**Example 2**

- Input: `nums = [5,6,6,7,8]`, `k = 3`
- Output: `false`

The duplicate `6` requires at least two strictly increasing subsequences, but five elements cannot give both a length of at least three.
