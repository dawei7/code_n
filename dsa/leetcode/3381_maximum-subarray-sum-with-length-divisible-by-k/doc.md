# Maximum Subarray Sum With Length Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, consider every nonempty contiguous subarray whose length is divisible by `k`. Its elements may be positive, negative, or zero, so the best choice is not necessarily the longest eligible subarray or one beginning at index zero.

Return the maximum sum among all eligible subarrays. Because $k$ never exceeds the array length, at least one valid subarray always exists. The result may be negative when every eligible choice has a negative sum.

### Function Contract

**Inputs**

- `nums`: A nonempty list of integers.
- `k`: A positive divisor for the chosen subarray length.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1\leq k\leq n\leq 2\cdot10^5$ and $-10^9\leq\texttt{nums[i]}\leq10^9$.

**Return value**

- The maximum integer sum of a nonempty contiguous subarray whose length is a multiple of `k`.

### Examples

**Example 1**

- Input: `nums = [1,2], k = 1`
- Output: `3`
- Explanation: Every positive length is divisible by one, and the whole array has the greatest sum.

**Example 2**

- Input: `nums = [-1,-2,-3,-4,-5], k = 4`
- Output: `-10`
- Explanation: The only eligible length is four; the first four elements give the larger of the two possible sums.

**Example 3**

- Input: `nums = [-5,1,2,-3,4], k = 2`
- Output: `4`
- Explanation: The subarray `[1,2,-3,4]` has length four and sum four.
