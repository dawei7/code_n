# Maximum Frequency of an Element After Performing Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3346 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/) |

## Problem Description

### Goal

You are given an integer array `nums`, a non-negative adjustment limit `k`, and an operation count `numOperations`. Perform exactly `numOperations` operations. In each operation, choose an index that has not been chosen before and add one integer from the inclusive range `[-k, k]` to that element.

The added integer may be zero, so an operation is allowed to leave its selected element unchanged. After all operations, determine the largest possible frequency of any single integer in `nums`. Each array position can participate in at most one operation, and different selected positions may receive different adjustments.

### Function Contract

**Inputs**

- `nums`: A non-empty list of integers with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: The maximum absolute adjustment in one operation, with $0 \le k \le 10^5$.
- `numOperations`: The exact number of distinct indices to select, with $0 \le \texttt{numOperations} \le \lvert\texttt{nums}\rvert$.

An operation on index `i` replaces `nums[i]` by `nums[i] + delta`, where `-k <= delta <= k` and that index has not been selected earlier.

**Return value**

Return the maximum frequency attainable by any integer after performing all operations.

### Examples

**Example 1**

- Input: `nums = [1, 4, 5], k = 1, numOperations = 2`
- Output: `2`
- Explanation: Select `4` and add zero, then select `5` and add `-1`; the value `4` appears twice.

**Example 2**

- Input: `nums = [5, 11, 20, 20], k = 5, numOperations = 1`
- Output: `2`
- Explanation: The two existing copies of `20` already give frequency two. Selecting `11` and adding zero fulfills the operation without changing that frequency.

**Example 3**

- Input: `nums = [1, 5], k = 2, numOperations = 2`
- Output: `2`
- Explanation: Neither endpoint is initially `3`, but adding `2` to `1` and `-2` to `5` makes both elements equal to `3`.
