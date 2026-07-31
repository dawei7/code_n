# Count Equal and Divisible Pairs in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2176 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` and a positive integer `k`, count index
pairs $(i,j)$ satisfying all three conditions:

$$
0 \le i < j < n,\qquad \texttt{nums[i]}=\texttt{nums[j]},\qquad
k \mid ij.
$$

The divisibility condition applies to the product of the indices, not the
array values. Equal values alone are insufficient when the index product is
not a multiple of `k`. Each qualifying pair is counted once.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1\le n\le100$ and
  $1\le\texttt{nums[i]}\le100$.
- `k`: an integer with $1\le k\le100$.

**Return value**

Return the number of pairs $(i,j)$ with $i<j$, equal stored values, and an
index product divisible by `k`.

### Examples

**Example 1**

- Input: `nums = [3,1,2,2,2,1,3]`, `k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1,2,3,4]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [5,5,5]`, `k = 3`
- Output: `2`, because index `0` forms a qualifying pair with every later
  equal value while `(1,2)` does not.
