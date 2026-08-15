# Kth Smallest Amount With Single Denomination Combination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3116 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Bit Manipulation, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/) |

## Problem Description

### Goal

You are given distinct positive integers in `coins`, where each integer is a coin denomination. There is an unlimited supply of every denomination. An amount may be formed by using any positive number of coins, but all coins used for that amount must have the same denomination; coins of different denominations cannot be combined.

Consider every positive amount obtainable under this rule, remove duplicate amounts, and arrange the remaining values in increasing order. Return the $k$-th value in that infinite sequence. An amount belongs to the sequence exactly when it is a positive multiple of at least one denomination in `coins`.

### Function Contract

**Inputs**

- `coins`: A list of $n$ pairwise distinct coin denominations.
- `k`: The one-based rank of the desired obtainable amount.

The constraints are $1 \le n \le 15$, $1 \le \texttt{coins[i]} \le 25$, and $1 \le k \le 2 \cdot 10^9$.

**Return value**

Return the $k$-th smallest distinct positive amount obtainable using only one denomination per amount.

### Examples

#### Example 1

- **Input:** `coins = [3, 6, 9], k = 3`
- **Output:** `9`
- **Explanation:** The distinct obtainable amounts begin $3, 6, 9, 12, \ldots$, so the third is $9$.

#### Example 2

- **Input:** `coins = [5, 2], k = 7`
- **Output:** `12`
- **Explanation:** The increasing sequence begins $2, 4, 5, 6, 8, 10, 12, \ldots$. Although $10$ is a multiple of both denominations, it appears only once.
