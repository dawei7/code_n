# Maximum Score of a Good Subarray

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) |
| Frontend ID | 1793 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a 0-indexed positive integer array `nums` and an index `k`. For endpoints $i$ and $j$ with $i \le j$, the score of the contiguous subarray from $i$ through $j$ is

$$
\min_{i \le q \le j}\texttt{nums[q]}\,(j-i+1).
$$

A subarray is good exactly when it contains the required index, so its endpoints must satisfy $i \le k \le j$. Return the largest score among all good subarrays.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 2\cdot 10^4$.
- `k`: a valid required index satisfying $0 \le k < n$.

**Return value**

- Return the maximum integer score of any contiguous subarray that contains index `k`.

### Examples

**Example 1**

- Input: `nums = [1, 4, 3, 7, 4, 5], k = 3`
- Output: `15`

The interval from index `1` through `5` has minimum `3`, length `5`, and score `15`.

**Example 2**

- Input: `nums = [5, 5, 4, 5, 4, 1, 1, 1], k = 0`
- Output: `20`

The prefix ending at index `4` has minimum `4` and length `5`.

**Example 3**

- Input: `nums = [2, 3, 3, 1], k = 1`
- Output: `6`

Either the first three values or the two adjacent `3` values attain score `6`.
