# Largest Subarray Length K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1708 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-subarray-length-k/) |

## Problem Description
### Goal

You are given an integer array `nums` whose values are all distinct and a positive integer `k`. Consider every contiguous subarray containing exactly `k` elements. Compare two such arrays lexicographically: at the first position where their values differ, the one with the greater value is larger.

Return the lexicographically largest length-`k` subarray. The result must preserve the original contiguous order; elements cannot be rearranged or selected with gaps. Since all input values are distinct, the best subarray is unique.

### Function Contract
**Inputs**

- `nums`: a list of $n$ distinct integers
- `k`: the required subarray length, with $1 \le k \le n$
- $1 \le n \le 10^5$, and every value in `nums` lies between $1$ and $10^9$

**Return value**

A new list containing the lexicographically largest contiguous subarray of `nums` with exactly `k` elements.

### Examples
**Example 1**

- Input: `nums = [1, 4, 5, 2, 3], k = 3`
- Output: `[5, 2, 3]`

The eligible starting values are `1`, `4`, and `5`. The window beginning with `5` is lexicographically largest.

**Example 2**

- Input: `nums = [1, 4, 5, 2, 3], k = 4`
- Output: `[4, 5, 2, 3]`

Only indices `0` and `1` can start a four-element window, and `4` is the larger of those first values.

**Example 3**

- Input: `nums = [1, 4, 5, 2, 3], k = 1`
- Output: `[5]`

For one-element subarrays, lexicographic order is simply the order of their only values.
