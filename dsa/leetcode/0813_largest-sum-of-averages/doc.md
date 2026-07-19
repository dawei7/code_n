# Largest Sum of Averages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 813 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-sum-of-averages/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, partition the complete array into at most `k` nonempty adjacent subarrays. Every input element must belong to exactly one group, and the group order follows the array.

Define a partition's score as the sum of the arithmetic average of each group. Return the maximum score over all allowed partitions; the score need not be an integer, and using fewer than `k` groups is permitted. Answers within $10^{-6}$ of the exact value are accepted.

### Function Contract

**Inputs**

- `nums`: a nonempty list of positive integers.
- `k`: the maximum number of contiguous groups, with `1 <= k <= len(nums)`.

**Return value**

- The largest achievable sum of group averages.

### Examples

**Example 1**

- Input: `nums = [9,1,2,3,9], k = 3`
- Output: `20.0`
- Explanation: The partition `[9] | [1,2,3] | [9]` contributes $9 + 2 + 9$.

**Example 2**

- Input: `nums = [1,2,3,4,5,6,7], k = 4`
- Output: `20.5`
- Explanation: An optimal partition is `[1,2,3,4] | [5] | [6] | [7]`.

**Example 3**

- Input: `nums = [1,2,3], k = 1`
- Output: `2.0`
- Explanation: With one group, the result is the average of the entire array.
