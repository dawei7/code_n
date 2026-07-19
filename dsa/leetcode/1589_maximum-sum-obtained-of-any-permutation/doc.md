# Maximum Sum Obtained of Any Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1589 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) |

## Problem Description
### Goal

You are given an integer array `nums` and several requests. Each request `[start, end]` asks for the sum of the values at every index from `start` through `end`, including both endpoints. All indices are zero-based.

Before evaluating the requests, you may permute the values of `nums` in any way. The same chosen permutation is then used for every request. Find the largest possible total after adding all requested range sums together.

Return that maximum modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: An array of $N$ integers, where $1 \le N \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.
- `requests`: An array of $R$ inclusive ranges `[start, end]`, where $1 \le R \le 10^5$ and $0 \le \texttt{start} \le \texttt{end} < N$.

**Return value**

Return the maximum total of all request sums over every permutation of `nums`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5], requests = [[1,3],[0,1]]`
- Output: `19`

**Example 2**

- Input: `nums = [1,2,3,4,5,6], requests = [[0,1]]`
- Output: `11`

**Example 3**

- Input: `nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]`
- Output: `47`
