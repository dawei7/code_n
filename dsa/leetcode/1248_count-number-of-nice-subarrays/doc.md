# Count Number of Nice Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1248 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-nice-subarrays/) |

## Problem Description

### Goal

You are given an integer array `nums` and a positive integer `k`. A contiguous subarray is called *nice* when it contains exactly `k` odd numbers.

Return the total number of nice subarrays of `nums`. A subarray must use consecutive array positions; elements cannot be skipped. Different start or end positions identify different subarrays, even when their values happen to be the same.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 50000$ and $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: the exact number of odd values required, with $1 \le k \le n$.

**Return value**

- Return the number of contiguous subarrays containing exactly `k` odd elements.

### Examples

**Example 1**

- Input: `nums = [1, 1, 2, 1, 1]`, `k = 3`
- Output: `2`
- Explanation: The two qualifying subarrays are `[1, 1, 2, 1]` and `[1, 2, 1, 1]`.

**Example 2**

- Input: `nums = [2, 4, 6]`, `k = 1`
- Output: `0`
- Explanation: No subarray can contain an odd value because the entire array is even.

**Example 3**

- Input: `nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]`, `k = 2`
- Output: `16`
