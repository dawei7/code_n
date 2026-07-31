# Subarray With Elements Greater Than Varying Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2334 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Union-Find, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `threshold`, choose a nonempty
contiguous subarray of length $k$. It is valid only when every element in that
subarray is strictly greater than $\texttt{threshold}/k$.

Return the length of any valid subarray. Different valid lengths may exist, and
any one of them is an acceptable answer. If no nonempty contiguous subarray
satisfies the strict inequality, return `-1`.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and every
  value lies in $[1,10^9]$.
- `threshold`: A positive integer no greater than $10^9$.

**Return value**

Any integer $k$ for which some length-$k$ subarray has every element greater
than $\texttt{threshold}/k$, or `-1` when no such length exists.

### Examples

**Example 1**

- Input: `nums = [1,3,4,3,1]`, `threshold = 6`
- Output: `3`
- Explanation: Every element of `[3,4,3]` exceeds $6/3=2$.

**Example 2**

- Input: `nums = [6,5,6,5,8]`, `threshold = 7`
- Output: `1`
- Explanation: The one-element subarray `[8]` satisfies $8>7$. Lengths 2
  through 5 are also valid, so any of them could be returned instead.

**Example 3**

- Input: `nums = [1,2,3]`, `threshold = 10`
- Output: `-1`
- Explanation: No subarray minimum multiplied by its length exceeds 10.
