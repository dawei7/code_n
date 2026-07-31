# Maximal Range That Each Element Is Maximum in It

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2832 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/) |

## Problem Description
### Goal

You are given a 0-indexed array `nums` whose integers are all distinct. Construct a 0-indexed array `ans` of the same length.

For every index `i`, `ans[i]` is the greatest possible length of a contiguous subarray `nums[l..r]` whose maximum element is `nums[i]`. Because every value is unique, such a subarray necessarily contains index `i`. The one-element range `nums[i..i]` is always valid.

Return `ans`.

### Function Contract
**Inputs**

- `nums`: A list of $n$ pairwise distinct integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

Return a list of length $n$ in which entry `i` is the maximum length of a contiguous subarray containing `nums[i]` and no value greater than `nums[i]`.

### Examples
**Example 1**

- Input: `nums = [1, 5, 4, 3, 6]`
- Output: `[1, 4, 2, 1, 5]`
- Explanation: The value `5` can be the maximum from indices `0` through `3`, while the final value `6` can be the maximum of the entire array.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `[1, 2, 3, 4, 5]`
- Explanation: For each `i`, the prefix `nums[0..i]` is the longest range whose maximum is `nums[i]`.
