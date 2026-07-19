# Maximum Sum Circular Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 918 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Dynamic Programming, Queue, Monotonic Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/) |

## Problem Description
### Goal

Given a circular integer array `nums`, find the maximum possible sum of a non-empty subarray. Circular means the last position connects to the first: the next position after `nums[i]` is `nums[(i + 1) % n]`, and the previous position is `nums[(i - 1 + n) % n]`.

A chosen subarray must remain contiguous in that circular order and may include each position of the fixed array at most once. Return the greatest sum among all such non-empty subarrays.

### Function Contract
**Inputs**

- `nums`: an array of $n$ integers, where $1 \le n \le 3 \cdot 10^4$ and each value lies between $-3 \cdot 10^4$ and $3 \cdot 10^4$, inclusive.

**Return value**

The maximum sum of a non-empty subarray that may stay within the ordinary array bounds or wrap once from the end to the beginning.

### Examples
**Example 1**

- Input: `nums = [1,-2,3,-2]`
- Output: `3`
- Explanation: The single-element subarray `[3]` is optimal.

**Example 2**

- Input: `nums = [5,-3,5]`
- Output: `10`
- Explanation: The wrapping subarray joins the final and initial `5`.

**Example 3**

- Input: `nums = [-3,-2,-3]`
- Output: `-2`
- Explanation: A non-empty answer is required, so the largest single value is optimal.
