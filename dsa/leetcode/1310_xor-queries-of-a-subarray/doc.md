# XOR Queries of a Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1310 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/) |

## Problem Description
### Goal
A positive-integer array `arr` is accompanied by a list of inclusive index ranges. For each query `[left, right]`, compute the bitwise XOR of every array element in the subarray from `arr[left]` through `arr[right]`.

Return one value per query in the same order as the queries were given. Queries may overlap, repeat, cover one element, or span the entire array; each answer is based on the unchanged original array.

### Function Contract
**Inputs**

- `arr`: an array of $n$ positive integers, where $1\le n\le3\cdot10^4$ and $1\le\texttt{arr[i]}\le10^9$.
- `queries`: an array of $q$ pairs, where $1\le q\le3\cdot10^4$.
- Every query satisfies $0\le\texttt{left}\le\texttt{right}<n$.

**Return value**

An array `answer` of length $q$ such that

$$
\texttt{answer[i]}
=
\texttt{arr[left]}\mathbin{\mathtt{XOR}}\cdots\mathbin{\mathtt{XOR}}\texttt{arr[right]}
$$

for the inclusive range in `queries[i]`.

### Examples
**Example 1**

- Input: `arr = [1,3,4,8]`, `queries = [[0,1],[1,2],[0,3],[3,3]]`
- Output: `[2,7,14,8]`

**Example 2**

- Input: `arr = [4,8,2,10]`, `queries = [[2,3],[1,3],[0,0],[0,3]]`
- Output: `[8,0,4,4]`

**Example 3**

- Input: `arr = [5]`, `queries = [[0,0],[0,0]]`
- Output: `[5,5]`
