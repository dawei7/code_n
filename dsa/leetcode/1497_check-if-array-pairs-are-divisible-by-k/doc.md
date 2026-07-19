# Check If Array Pairs Are Divisible by k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1497 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) |

## Problem Description
### Goal

You are given an integer array `arr` whose length $N$ is even, together with a positive integer `k`. Partition all array elements into exactly $N/2$ disjoint pairs, so every element belongs to one pair.

A pair is valid when the sum of its two values is divisible by `k`. Return `true` if at least one complete pairing makes every pair valid. Return `false` when no such partition exists; choosing only some compatible pairs is not sufficient.

### Function Contract
**Inputs**

Let $N$ be the length of `arr`, let $K$ be the value of `k`, and let $R$
be the number of distinct normalized remainders represented in `arr`.

- `arr`: an integer list with $1 \le N \le 10^5$ and even $N$.
- Every value satisfies $-10^9 \le \texttt{arr[i]} \le 10^9$.
- `k`: an integer with $1 \le K \le 10^5$.

**Return value**

Return `true` if the entire array can be divided into $N/2$ pairs whose sums are all divisible by $K$; otherwise, return `false`.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5,10,6,7,8,9], k = 5`
- Output: `true`
- Explanation: One valid partition uses the pairs $(1,9)$, $(2,8)$, $(3,7)$, $(4,6)$, and $(5,10)$.

**Example 2**

- Input: `arr = [1,2,3,4,5,6], k = 7`
- Output: `true`
- Explanation: The pairs $(1,6)$, $(2,5)$, and $(3,4)$ all sum to $7$.

**Example 3**

- Input: `arr = [1,2,3,4,5,6], k = 10`
- Output: `false`
- Explanation: No partition into three pairs makes every pair sum to a multiple of $10$.
