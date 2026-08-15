# Find Occurrences of an Element in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3159 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/) |

## Problem Description

### Goal

You are given an integer array `nums`, an integer array `queries`, and a target integer `x`. Each query is a positive occurrence number: for `queries[i] = k`, locate the index in `nums` where `x` appears for the $k$-th time while scanning from left to right. Indices in `nums` are zero-based, whereas the requested occurrence number is one-based.

Produce one answer for every query in its original order. If `nums` contains fewer than $k$ occurrences of `x`, the answer for that query is `-1`. Return the complete answer array.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^4$.
- `queries`: A list of $q$ positive integers, where $1 \le q \le 10^5$ and $1 \le \texttt{queries[i]} \le 10^5$.
- `x`: The target integer, with $1 \le x \le 10^4$.

**Return value**

Return a list of $q$ integers. Entry $i$ is the zero-based index of the `queries[i]`-th occurrence of `x` in `nums`, or `-1` when that occurrence does not exist.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 1, 7], queries = [1, 3, 2, 4], x = 1`
- **Output:** `[0, -1, 2, -1]`
- **Explanation:** The first and second occurrences of `1` are at indices `0` and `2`; no third or fourth occurrence exists.

#### Example 2

- **Input:** `nums = [1, 2, 3], queries = [10], x = 5`
- **Output:** `[-1]`
- **Explanation:** The target does not occur in `nums`.
