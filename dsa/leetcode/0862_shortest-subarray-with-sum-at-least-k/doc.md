# Shortest Subarray with Sum at Least K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 862 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) |

## Problem Description
### Goal
Given an integer array `nums` and a positive integer `k`, find the length of the shortest non-empty subarray whose elements sum to at least `k`. A subarray is a contiguous portion of the original array, so selected elements must occupy consecutive indices without gaps.

The entries of `nums` may be negative, zero, or positive. Negative values mean that extending a subarray can decrease its sum, so the usual sliding-window rule for positive arrays does not apply. Return `-1` when no non-empty contiguous subarray reaches the required sum.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \leq n \leq 10^5$ and $-10^5 \leq \texttt{nums[i]} \leq 10^5$.
- `k`: the required sum threshold, where $1 \leq k \leq 10^9$.

Define prefix sums by $P[0]=0$ and

$$
P[i]=\sum_{t=0}^{i-1}\texttt{nums[t]}
\quad\text{for }1\leq i\leq n.
$$

Then the sum of the subarray from index `i` through `j - 1` is $P[j]-P[i]$.

**Return value**

Return the minimum positive length of a subarray with sum at least `k`, or `-1` if none exists.

### Examples
**Example 1**

- Input: `nums = [1], k = 1`
- Output: `1`

**Example 2**

- Input: `nums = [1,2], k = 4`
- Output: `-1`

**Example 3**

- Input: `nums = [2,-1,2], k = 3`
- Output: `3`

Only the full array reaches the threshold.
