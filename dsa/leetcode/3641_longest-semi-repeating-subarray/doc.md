# Longest Semi-Repeating Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3641 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-semi-repeating-subarray/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, call a contiguous subarray semi-repeating when at most `k` distinct element values appear more than once inside that subarray.

A value with frequency two, three, or more counts as one repeating element value, not as several repetitions. Values occurring exactly once do not count toward the limit.

Return the maximum length of any semi-repeating subarray.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: The maximum number of distinct repeating values, where $0 \le k \le n$.

**Return value**

Return the length of the longest contiguous subarray containing at most `k` distinct values whose frequencies exceed one.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 1, 2, 3, 4], k = 2`
- **Output:** `6`
- **Explanation:** `[2, 3, 1, 2, 3, 4]` repeats only values 2 and 3.

#### Example 2

- **Input:** `nums = [1, 1, 1, 1, 1], k = 4`
- **Output:** `5`
- **Explanation:** Despite five occurrences, only the value 1 is a repeating value.

#### Example 3

- **Input:** `nums = [1, 1, 1, 1, 1], k = 0`
- **Output:** `1`
- **Explanation:** Any longer range repeats the value 1.
