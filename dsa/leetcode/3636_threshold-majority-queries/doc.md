# Threshold Majority Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3636 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Divide and Conquer, Counting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/threshold-majority-queries/) |

## Problem Description

### Goal

You are given an integer array `nums` and queries of the form `[l, r, threshold]`. Each query examines the inclusive subarray from index `l` through index `r`.

Within that range, find the element with the highest frequency. If several elements share that frequency, choose the smallest value. Return the chosen value only when its frequency is at least `threshold`; otherwise return `-1`.

Produce one answer for every query in the original query order.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^4$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `queries`: A list of $q$ triples `[l, r, threshold]`, where $1 \le q \le 5\times10^4$, $0 \le l \le r < n$, and $1 \le \texttt{threshold} \le r-l+1$.

**Return value**

Return a list in which each entry is the maximum-frequency value for that query, using the smallest value to break a frequency tie, or `-1` when the maximum frequency is below the threshold.

### Examples

#### Example 1

- **Input:** `nums = [1, 1, 2, 2, 1, 1], queries = [[0, 5, 4], [0, 3, 3], [2, 3, 2]]`
- **Output:** `[1, -1, 2]`
- **Explanation:** The full range contains four ones; the first four values have no frequency reaching three; the final queried pair contains two twos.

#### Example 2

- **Input:** `nums = [3, 2, 3, 2, 3, 2, 3], queries = [[0, 6, 4], [1, 5, 2], [2, 4, 1], [3, 3, 1]]`
- **Output:** `[3, 2, 3, 2]`
- **Explanation:** Each answer is the range mode when that mode reaches the requested threshold.
