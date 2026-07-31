# Maximize Total Cost of Alternating Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3196 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/) |

## Problem Description
### Goal
You are given an integer array `nums` of length $n$. For any nonempty subarray
`nums[l..r]`, define its cost by alternating signs from its first element:

$$
\operatorname{cost}(l,r)
=\sum_{i=l}^{r}\texttt{nums[i]}(-1)^{i-l}.
$$

Split `nums` into contiguous, nonempty subarrays so that every element belongs
to exactly one part. Return the maximum possible sum of the parts' costs. You
may also leave the complete array as one subarray.

### Function Contract
**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$ and
  $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

The maximum total cost obtainable from a partition into contiguous subarrays.

### Examples
**Example 1**

- Input: `nums = [1, -2, 3, 4]`
- Output: `10`

Split the array into `[1, -2, 3]` and `[4]`. Their costs are
`1 - (-2) + 3 = 6` and `4`, totaling `10`.

**Example 2**

- Input: `nums = [1, -1, 1, -1]`
- Output: `4`

For example, `[1, -1]` and `[1, -1]` each cost `2`.

**Example 3**

- Input: `nums = [0]`
- Output: `0`

The one-element array cannot be split further.

**Example 4**

- Input: `nums = [1, -1]`
- Output: `2`

Keeping the whole array gives `1 - (-1) = 2`.
