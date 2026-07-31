# Minimum Absolute Difference Between Elements With Constraint

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2817 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a non-negative integer `x`. Select two indices whose distance is at least `x`, then measure the absolute difference between their values.

Among every pair $i, j$ satisfying $\lvert i-j\rvert \geq x$, return the minimum possible value of $\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert$. When `x = 0`, the same index may be chosen for both positions, so the answer is necessarily zero.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `x`: The minimum allowed distance between the selected indices.

The constraints are $1 \leq n \leq 10^5$, $1 \leq \texttt{nums[i]} \leq 10^9$, and $0 \leq x < n$.

**Return value**

Return the smallest absolute value difference among two array elements whose indices are at least `x` apart.

### Examples

**Example 1**

- Input: `nums = [4,3,2,4], x = 2`
- Output: `0`
- Explanation: Indices `0` and `3` are at least two positions apart and contain equal values.

**Example 2**

- Input: `nums = [5,3,2,10,15], x = 1`
- Output: `1`
- Explanation: The values `3` and `2` occur at neighboring indices and have the smallest possible difference.

**Example 3**

- Input: `nums = [1,2,3,4], x = 3`
- Output: `3`
- Explanation: Only indices `0` and `3` satisfy the required distance, giving `|1 - 4| = 3`.
