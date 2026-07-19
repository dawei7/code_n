# Monotonic Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 896 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/monotonic-array/) |

## Problem Description
### Goal
An array is monotonic when it is either monotone increasing or monotone decreasing.

The integer array `nums` is monotone increasing if every pair of indices $i \leq j$ satisfies $\texttt{nums}[i] \leq \texttt{nums}[j]$. It is monotone decreasing if every such pair satisfies $\texttt{nums}[i] \geq \texttt{nums}[j]$. Equal neighboring values are therefore allowed in either direction.

Given `nums`, determine whether at least one of these two definitions holds.

### Function Contract
Let $n$ be the length of `nums`.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^5$ and $-10^5 \leq \texttt{nums}[i] \leq 10^5$.

**Return value**

Return `True` if `nums` is monotone increasing or monotone decreasing; otherwise return `False`.

### Examples
**Example 1**

- Input: `nums = [1,2,2,3]`
- Output: `true`

**Example 2**

- Input: `nums = [6,5,4,4]`
- Output: `true`

**Example 3**

- Input: `nums = [1,3,2]`
- Output: `false`
