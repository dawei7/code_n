# Smallest Range I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 908 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-range-i/) |

## Problem Description
### Goal
You are given an integer array `nums` and a nonnegative integer `k`. For each index `i`, you may perform at most one operation that replaces `nums[i]` with `nums[i] + x`, where `x` is an integer in the inclusive range $[-k,k]$. The choice of `x` may differ between indices.

The score of the resulting array is its maximum element minus its minimum element. Choose the allowed change for every index so that this score is as small as possible, and return that minimum score.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^4$ and $0 \leq \texttt{nums}[i] \leq 10^4$.
- `k`: an integer with $0 \leq \texttt{k} \leq 10^4$.

**Return value**

Return the minimum possible difference between the largest and smallest array values after applying the operation at most once per index.

### Examples
**Example 1**

- Input: `nums = [1], k = 0`
- Output: `0`

A one-element array has equal maximum and minimum values.

**Example 2**

- Input: `nums = [0,10], k = 2`
- Output: `6`

Changing the array to `[2,8]` reduces the score to $8-2=6$.

**Example 3**

- Input: `nums = [1,3,6], k = 3`
- Output: `0`

All three values can be changed to `4`.
