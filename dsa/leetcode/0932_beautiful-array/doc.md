# Beautiful Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 932 |
| Difficulty | Medium |
| Topics | Array, Math, Divide and Conquer |
| Official Link | [LeetCode](https://leetcode.com/problems/beautiful-array/) |

## Problem Description

### Goal

An array of length $n$ is called beautiful when it is a permutation of the integers from $1$ through $n$ and it contains no three positions that form an arithmetic progression in value while preserving their index order. More precisely, for every pair of indices $0 \le i < j < n$, there must be no index $k$ with $i < k < j$ such that $2a_k = a_i + a_j$, where $a_t$ denotes the value at position $t$.

Given the integer `n`, construct and return any beautiful array of length $n$. Different valid permutations are accepted, and at least one valid answer is guaranteed for every allowed value of `n`.

### Function Contract

**Inputs**

- `n`: the permutation length, where $1 \le n \le 1000$.

**Return value**

Return a permutation $(a_0,a_1,\ldots,a_{n-1})$ of the integers from $1$ through $n$ such that $2a_k \ne a_i + a_j$ for every $0 \le i < k < j < n$.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `[2,1,4,3]`

**Example 2**

- Input: `n = 5`
- Output: `[3,1,2,5,4]`

Other permutations satisfying the same conditions are also valid.
