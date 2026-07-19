# Maximum Length of Subarray With Positive Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1567 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) |

## Problem Description
### Goal

Given an integer array `nums`, choose a contiguous, nonempty subarray whose element product is positive. The numerical product itself may be very large; only whether its sign is positive matters.

A zero makes the product zero and therefore cannot belong to a qualifying subarray. Negative values reverse the sign, so a zero-free subarray has a positive product exactly when it contains an even number of negative values. Return the greatest possible length of such a subarray, or `0` when none exists.

### Function Contract
**Inputs**

- `nums`: An integer array of length $N$, where $1 \le N \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the maximum length of a contiguous subarray whose product is strictly positive. Return `0` if every nonempty subarray has a zero or negative product.

### Examples
**Example 1**

- Input: `nums = [1,-2,-3,4]`
- Output: `4`

**Example 2**

- Input: `nums = [0,1,-2,-3,-4]`
- Output: `3`

**Example 3**

- Input: `nums = [-1,-2,-3,0,1]`
- Output: `2`
