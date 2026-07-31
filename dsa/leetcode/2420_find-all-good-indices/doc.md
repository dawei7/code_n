# Find All Good Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2420 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-good-indices/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` and a positive integer `k`, consider indices $i$ satisfying $k \le i < n-k$. Such an index has exactly `k` available elements immediately before it and `k` available elements immediately after it; the value at index $i$ itself belongs to neither checked block.

Call $i$ good when the preceding block is in non-increasing order and the following block is in non-decreasing order. Equality is permitted in both directions. Return every good index in increasing order.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: The required length of both neighboring ordered blocks.

The contract guarantees $3 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le 10^6$, and $1 \le k \le \lfloor n/2\rfloor$.

**Return value**

Return all indices $i$ with $k \le i < n-k$ whose `k` preceding values are non-increasing and whose `k` following values are non-decreasing.

### Examples

**Example 1**

- Input: `nums = [2,1,1,1,3,4,1]`, `k = 2`
- Output: `[2,3]`

**Example 2**

- Input: `nums = [2,1,1,2]`, `k = 2`
- Output: `[]`

**Example 3**

- Input: `nums = [1,2,3,4,5]`, `k = 1`
- Output: `[1,2,3]`
