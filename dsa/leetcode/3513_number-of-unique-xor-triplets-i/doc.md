# Number of Unique XOR Triplets I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3513 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-i/) |

## Problem Description

### Goal

You are given an integer array `nums` of length $n$. The array is guaranteed to be a permutation of every integer from $1$ through $n$, so each value in that range appears exactly once.

Choose indices satisfying $0 \le i \le j \le k<n$. Their XOR triplet value is `nums[i] XOR nums[j] XOR nums[k]`. Equal indices are allowed, and different index triplets may produce the same value.

Consider every valid choice of `(i, j, k)` and return the number of distinct XOR triplet values it can produce.

### Function Contract

**Inputs**

- `nums`: A permutation of the integers from $1$ through $n$, where $1 \le n \le 10^5$.

**Return value**

Return the number of unique integers among all values `nums[i] XOR nums[j] XOR nums[k]` with $i \le j \le k$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2]`
- **Output:** `2`
- **Explanation:** Every valid triplet produces either `1` or `2`.

#### Example 2

- **Input:** `nums = [3, 1, 2]`
- **Output:** `4`
- **Explanation:** The attainable distinct values are `0`, `1`, `2`, and `3`.
