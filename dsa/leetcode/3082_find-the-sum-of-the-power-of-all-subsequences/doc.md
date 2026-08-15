# Find the Sum of the Power of All Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3082 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-the-sum-of-the-power-of-all-subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$ and a positive integer `k`.

Define the **power** of an integer array as the number of its subsequences whose elements sum to exactly `k`. For every subsequence of `nums`, evaluate that subsequence as an array of its own and determine its power.

Return the sum of those powers over all subsequences of `nums`. Because this total can be large, return it modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 10^4$.
- `k`: The positive target sum, where $1 \le k \le 100$.

Elements are selected by index, so equal values at different positions form distinct subsequences.

**Return value**

- The sum of the powers of every subsequence of `nums`, modulo $10^9 + 7$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3], k = 3`
- **Output:** `6`
- **Explanation:** The full array has two target-sum subsequences, while four other outer subsequences each have one. Their powers sum to $2+1+1+1+1=6$.

#### Example 2

- **Input:** `nums = [2, 3, 3], k = 5`
- **Output:** `4`
- **Explanation:** Either occurrence of `3` can pair with `2`. Across all outer subsequences, those two indexed pairs contribute four times in total.

#### Example 3

- **Input:** `nums = [1, 2, 3], k = 7`
- **Output:** `0`
- **Explanation:** No subsequence sums to `7`, so every outer subsequence has power zero.
