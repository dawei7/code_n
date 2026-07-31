# Maximum Product After K Increments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2233 |
| Difficulty | Medium |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-after-k-increments/) |

## Problem Description

### Goal

You are given an array `nums` of non-negative integers and an integer `k`. One operation chooses any array element and increases it by exactly one. Perform at most `k` such operations so that the product of all final array values is as large as possible.

The product must be maximized as an ordinary integer before modular reduction; the modulo operation must not influence how increments are assigned. Return that maximum product modulo $10^9+7$. Because increasing a non-negative factor cannot reduce the product, some optimal assignment always uses the complete operation budget.

### Function Contract

**Inputs**

- `nums`: A nonempty list of non-negative integers.
- `k`: A positive integer giving the maximum number of unit increments.

Let $n=\lvert\texttt{nums}\rvert$. Both $n$ and `k` are at most $10^5$, and every initial value is at most $10^6$.

**Return value**

Return the greatest product obtainable with at most `k` increments, reduced modulo $1{,}000{,}000{,}007$ only after the maximizing allocation is determined.

### Examples

**Example 1**

- Input: `nums = [0, 4], k = 5`
- Output: `20`

**Example 2**

- Input: `nums = [6, 3, 3, 2], k = 2`
- Output: `216`

**Example 3**

- Input: `nums = [1], k = 3`
- Output: `4`
