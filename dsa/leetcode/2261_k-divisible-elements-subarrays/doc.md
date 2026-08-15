# K Divisible Elements Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2261 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Trie, Rolling Hash, Hash Function, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/k-divisible-elements-subarrays/) |

## Problem Description

### Goal

Given `nums`, consider every nonempty subarray: every contiguous sequence
formed by choosing a start and end index. A subarray is eligible when at most
`k` of its elements are divisible by `p`.

Count eligible subarrays by their value sequence rather than by where they
occur. Two sequences are distinct if their lengths differ or if some value at
the same relative position differs. Consequently, repeated occurrences of the
same sequence contribute only once, even when they come from different index
ranges. Return the number of distinct eligible sequences.

### Function Contract

**Inputs**

- `nums`: An array of $n$ integers, where $1\le n\le200$ and $1\le\texttt{nums[i]}\le200$.
- `k`: The maximum allowed number of divisible elements, with $1\le k\le n$.
- `p`: A divisor between $1$ and $200$.

**Return value**

Return the number of distinct nonempty contiguous value sequences containing
at most `k` elements `value` for which `value % p == 0`.

### Examples

#### Example 1

- **Input:** `nums = [2,3,3,2,2], k = 2, p = 2`
- **Output:** `11`

#### Example 2

- **Input:** `nums = [1,2,3,4], k = 4, p = 1`
- **Output:** `10`

#### Example 3

- **Input:** `nums = [1,1,1], k = 3, p = 2`
- **Output:** `3`
