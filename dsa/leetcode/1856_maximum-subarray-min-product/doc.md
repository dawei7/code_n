# Maximum Subarray Min-Product

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-subarray-min-product/) |
| Frontend ID | 1856 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For any non-empty contiguous subarray of the positive integer array `nums`, define its min-product as the smallest value in that subarray multiplied by the sum of all its values. Different subarrays may share the same minimum while having different sums and products.

Find the greatest min-product over every possible non-empty subarray. The unreduced maximum is guaranteed to fit in a signed 64-bit integer. Only after choosing that true maximum, return it modulo $10^9+7$; applying the modulus to candidates before comparing them would change their ordering.

### Function Contract

**Inputs**

- `nums`: a list of $n$ positive integers.
- $1\le n\le10^5$.
- Every element satisfies $1\le\texttt{nums[i]}\le10^7$.

**Return value**

- For every non-empty subarray, multiply its sum by its minimum value.
- Return the maximum such product modulo $1\,000\,000\,007$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 2]`
- Output: `14`

The subarray `[2, 3, 2]` has minimum 2, sum 7, and min-product 14.

**Example 2**

- Input: `nums = [2, 3, 3, 1, 2]`
- Output: `18`

**Example 3**

- Input: `nums = [3, 1, 5, 6, 4, 2]`
- Output: `60`

The subarray `[5, 6, 4]` contributes $4(5+6+4)=60$.
