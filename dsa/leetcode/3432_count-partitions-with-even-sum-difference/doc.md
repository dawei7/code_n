# Count Partitions with Even Sum Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3432 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-partitions-with-even-sum-difference/) |

## Problem Description

### Goal

Given an integer array `nums` of length $n$, choose an index $i$ with $0\le i<n-1$. That index partitions the array into the non-empty prefix covering indices $0$ through $i$ and the non-empty suffix covering indices $i+1$ through $n-1$.

For each possible partition, subtract the suffix sum from the prefix sum. Count how many of the resulting differences are even and return that count. Each boundary between adjacent elements represents one distinct partition.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2\le n\le100$ and $1\le\texttt{nums[i]}\le100$.

**Return value**

Return the number of partitions whose left-sum minus right-sum difference is even.

### Examples

#### Example 1

- **Input:** `nums = [10,10,3,7,6]`
- **Output:** `4`

#### Example 2

- **Input:** `nums = [1,2,2]`
- **Output:** `0`

#### Example 3

- **Input:** `nums = [2,4,6,8]`
- **Output:** `3`
