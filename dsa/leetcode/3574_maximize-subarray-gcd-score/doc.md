# Maximize Subarray GCD Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3574 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-subarray-gcd-score/) |

## Problem Description

### Goal

An array `nums` contains positive integers. Before choosing a contiguous subarray, perform at most `k` operations on the array. One operation doubles one element, and no element may be doubled more than once.

The score of a selected subarray is its length multiplied by the greatest common divisor of all its elements after the chosen operations. Return the largest score achievable over every permitted set of doublings and every non-empty contiguous subarray.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1\le n\le1500$ and $1\le\texttt{nums[i]}\le10^9$.
- `k`: The maximum number of distinct elements that may be doubled, where $1\le k\le n$.

Let $M=\max(\texttt{nums})$.

**Return value**

Return the maximum possible product of a non-empty subarray's length and its GCD after at most `k` legal doubling operations.

### Examples

**Example 1**

- Input: `nums = [2,4], k = 1`
- Output: `8`
- Explanation: Double `2` to obtain `[4,4]`; the whole array has length `2` and GCD `4`.

**Example 2**

- Input: `nums = [3,5,7], k = 2`
- Output: `14`
- Explanation: Doubling `7` makes the singleton subarray `[14]` attain score `14`.

**Example 3**

- Input: `nums = [5,5,5], k = 1`
- Output: `15`
- Explanation: The whole array already scores `3 * 5`; doubling only one of its three elements cannot raise their common divisor.

---
