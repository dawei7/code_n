# Find Subarray With Bitwise OR Closest to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3171 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Choose a non-empty contiguous subarray `nums[l..r]`, compute the bitwise OR of all values from index `l` through index `r`, and compare that result with `k`.

Return the smallest possible absolute difference between `k` and the OR of a chosen subarray. If some subarray has bitwise OR exactly equal to `k`, the answer is `0`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: A positive target integer satisfying $1 \le k \le 10^9$.

Let $M = \max(\texttt{k}, \max(\texttt{nums}))$.

**Return value**

- The minimum value of $\lvert k - (\texttt{nums[l]} \mathbin{\mathrm{OR}} \cdots \mathbin{\mathrm{OR}} \texttt{nums[r]}) \rvert$ over all $0 \le l \le r < n$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 4, 5], k = 3`
- Output: `0`
- Explanation: The subarray `nums[0..1]` has OR value `3`, so its absolute difference from `k` is `0`.

**Example 2**

- Input: `nums = [1, 3, 1, 3], k = 2`
- Output: `1`
- Explanation: A one-element subarray containing `3` has difference `1`, and no subarray OR equals `2`.

**Example 3**

- Input: `nums = [1], k = 10`
- Output: `9`
- Explanation: The only non-empty subarray has OR value `1`.
