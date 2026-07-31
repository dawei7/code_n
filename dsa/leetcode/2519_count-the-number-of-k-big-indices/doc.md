# Count the Number of K-Big Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2519 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-k-big-indices/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `k`.

An index `i` is `k`-big when both sides of it contain enough smaller values. Specifically, at least `k` different indices before `i` must hold values strictly smaller than `nums[i]`, and at least `k` different indices after `i` must also hold values strictly smaller than `nums[i]`.

Return the number of indices that satisfy both conditions. Equal values do not count as smaller.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le n$.
- `k`: The minimum number of strictly smaller values required on each side, where $1 \le k \le n$.

**Return value**

Return the number of indices `i` having at least `k` earlier indices `j` with $\texttt{nums[j]} < \texttt{nums[i]}$ and at least `k` later indices `j` satisfying the same strict inequality.

### Examples

**Example 1**

- Input: `nums = [2, 3, 6, 5, 2, 3], k = 2`
- Output: `2`
- Explanation: Indices `2` and `3` each have at least two strictly smaller values on both their left and right sides.

**Example 2**

- Input: `nums = [1, 1, 1], k = 3`
- Output: `0`
- Explanation: No value has three earlier and three later indices, and equal values would not satisfy the strict comparison anyway.
