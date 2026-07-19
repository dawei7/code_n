# Find Subsequence of Length K With the Largest Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2099 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Select exactly `k` elements whose sum is as large as possible, and return them as a subsequence of the original array.

A subsequence may omit any elements, but it must preserve the relative order of every selected position. If several size-$k$ subsequences attain the same largest sum, any one of them is acceptable.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: a list of $n$ integers, where $1 \le n \le 1000$ and $-10^5 \le \texttt{nums[i]} \le 10^5$.
- `k`: the required subsequence length, where $1 \le k \le n$.

**Return value**

Return any length-$k$ subsequence whose element sum is maximum.

### Examples

**Example 1**

- Input: `nums = [2,1,3,3]`, `k = 2`
- Output: `[3,3]`
- Explanation: The maximum sum is $6$.

**Example 2**

- Input: `nums = [-1,-2,3,4]`, `k = 3`
- Output: `[-1,3,4]`
- Explanation: These values retain their original order and sum to $6$.

**Example 3**

- Input: `nums = [3,4,3,3]`, `k = 2`
- Output: `[3,4]`
- Explanation: `[4,3]` is another valid subsequence with the same maximum sum $7$.
