# Minimum Cost to Split an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2547 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-cost-to-split-an-array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, split the entire array into one or more non-empty subarrays. Every part must be contiguous, and the parts must preserve the original order without omitting or reusing any element. The total cost is the sum of the importance values of the chosen parts.

To trim a subarray, remove every value that occurs exactly once within that subarray; all occurrences of every duplicated value remain. A subarray's importance is `k` plus the length of its trimmed form. Return the minimum total cost among all valid splits.

### Function Contract

**Inputs**

- `nums`: An integer array to partition into contiguous, non-empty pieces.
- `k`: The positive base cost paid once for every piece.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 1000$, $0 \le \texttt{nums[i]} < n$, and $1 \le k \le 10^9$.

**Return value**

Return the minimum possible sum of the parts' importance values.

### Examples

**Example 1**

- Input: `nums = [1,2,1,2,1,3,3], k = 2`
- Output: `8`
- Explanation: Splitting into `[1,2]` and `[1,2,1,3,3]` costs 2 and 6.

**Example 2**

- Input: `nums = [1,2,1,2,1], k = 2`
- Output: `6`
- Explanation: The split `[1,2]`, `[1,2,1]` has minimum total cost 6.

**Example 3**

- Input: `nums = [1,2,1,2,1], k = 5`
- Output: `10`
- Explanation: Keeping the whole array as one part costs $5 + 5 = 10$.
