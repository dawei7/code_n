# Find the K-Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2386 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-sum-of-an-array/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, consider every subsequence obtainable by deleting any set of elements without changing the order of those retained. Associate each subsequence with the sum of its elements; the empty subsequence is included and has sum zero.

Sort all $2^n$ subsequence sums in non-increasing order and retain duplicates produced by different choices of indices. Return the value at rank `k`. Thus the K-Sum is the $k$-th largest obtainable sum, not the $k$-th distinct sum.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.
- `k`: A rank satisfying $1 \le k \le \min(2000, 2^n)$.

**Return value**

- Return the $k$-th largest subsequence sum, counting equal sums at their full multiplicity.

**Ranking semantics**

- Choosing different index sets creates different subsequences even when their sums are equal.
- The empty subsequence contributes one sum of zero.
- The answer may require 64-bit signed integer range.

### Examples

**Example 1**

- Input: `nums = [2,4,-2], k = 5`
- Output: `2`
- Explanation: The descending sums are `6, 4, 4, 2, 2, 0, 0, -2`, so rank five is `2`.

**Example 2**

- Input: `nums = [1,-2,3,4,-10,12], k = 16`
- Output: `10`
