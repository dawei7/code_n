# Longest Increasing Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2407 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Dynamic Programming, Binary Indexed Tree, Segment Tree, Queue, Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence-ii/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, choose a subsequence by
deleting any number of elements without changing the order of those retained.
The chosen values must be strictly increasing.

In addition, the difference between every two adjacent chosen values must be
at most `k`. Return the greatest possible subsequence length. A value jump
larger than `k` is forbidden even when the resulting sequence would otherwise
be increasing.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, with $1 \le n \le 10^5$.
- `k`: The maximum allowed increase between adjacent subsequence elements.

Every value and `k` is between 1 and $10^5$. Let
$M=\max(\texttt{nums})$.

**Return value**

Return the maximum length of an index-ordered subsequence
$a_1,a_2,\ldots,a_t$ satisfying
$1\le a_{j+1}-a_j\le k$ for every adjacent pair.

### Examples

#### Example 1

- **Input:** `nums = [4,2,1,4,3,4,5,8,15]`, `k = 3`
- **Output:** `5`
- **Explanation:** `[1,3,4,5,8]` is valid, while appending 15 would make a jump
  of 7.

#### Example 2

- **Input:** `nums = [7,4,5,1,8,12,4,7]`, `k = 5`
- **Output:** `4`
- **Explanation:** One longest valid subsequence is `[4,5,8,12]`.

#### Example 3

- **Input:** `nums = [1,5]`, `k = 1`
- **Output:** `1`
- **Explanation:** The increase from 1 to 5 exceeds `k`.
