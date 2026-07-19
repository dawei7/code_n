# Split Array Largest Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 410 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/split-array-largest-sum/) |

## Problem Description
### Goal
Given a nonnegative integer array and a valid integer `m`, place $m - 1$ boundaries to divide the complete array into exactly `m` nonempty contiguous subarrays. Every input position must belong to one group and original order cannot change.

For each split, consider the largest sum among its groups. Return the minimum possible value of that largest sum over all valid boundary placements. The result balances groups rather than minimizing their total, which is fixed. A group may contain one element, and when $m = 1$ the answer is the whole-array sum.

### Function Contract
**Inputs**

- `nums`: the nonnegative integer array
- `m`: the exact number of contiguous groups

**Return value**

- Return the minimum achievable value of the largest group sum.

### Examples
**Example 1**

- Input: `nums = [7,2,5,10,8], m = 2`
- Output: `18`

**Example 2**

- Input: `nums = [1,2,3,4,5], m = 2`
- Output: `9`

**Example 3**

- Input: `nums = [1,4,4], m = 3`
- Output: `4`
