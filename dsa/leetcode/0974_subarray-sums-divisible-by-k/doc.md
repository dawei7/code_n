# Subarray Sums Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 974 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subarray-sums-divisible-by-k/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, count the non-empty subarrays whose sums are divisible by `k`.

A subarray is a contiguous part of the original array. Its elements must therefore occupy consecutive positions; choosing separated elements does not form a subarray.

For a range to qualify, its sum may be positive, negative, or zero, but it must equal an integer multiple of `k`. Count every distinct contiguous range that satisfies this condition, even when different ranges contain the same sequence of values or produce the same sum.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1 \le N \le 3\cdot10^4$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `k`: the positive divisor, where $2 \le K = \texttt{k} \le 10^4$.

Define the prefix sum through the first $i$ elements as

$$
P_i = \sum_{j=0}^{i-1}\texttt{nums[j]},
$$

with $P_0=0$.

**Return value**

- The number of non-empty contiguous subarrays whose element sum is divisible by $K$.

### Examples

**Example 1**

- Input: `nums = [4, 5, 0, -2, -3, 1], k = 5`
- Output: `7`
- Explanation: seven contiguous ranges have sums that are multiples of $5$, including the whole array, `[5]`, `[0]`, and `[-2, -3]`.

**Example 2**

- Input: `nums = [5], k = 9`
- Output: `0`
