# Longest Subsequence With Limited Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2389 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) |

## Problem Description

### Goal

You are given a positive integer array `nums` and a list of positive query budgets. For each query, choose a subsequence of `nums` whose sum does not exceed that budget, and determine the greatest possible number of chosen elements.

Return one maximum length for every query in its original order. A subsequence retains the relative order of its selected elements, but because only its size and sum matter, any chosen set of indices can be represented in their original order. The empty subsequence is allowed when even the smallest value exceeds a query.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers.
- `queries`: A list of $m$ positive budget values.

Here $1 \le n,m \le 1000$, and every array or query value is at most $10^6$.

**Return value**

- Return a list of length $m$ where answer `i` is the maximum subsequence size with sum at most `queries[i]`.

**Selection semantics**

- Each query is independent and does not consume values from `nums`.
- The sum may equal the query budget.
- The empty subsequence has size zero.

### Examples

#### Example 1

- **Input:** `nums = [4,5,2,1], queries = [3,10,21]`
- **Output:** `[2,3,4]`

#### Example 2

- **Input:** `nums = [2,3,4,5], queries = [1]`
- **Output:** `[0]`
