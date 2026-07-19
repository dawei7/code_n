# Minimized Maximum of Products Distributed to Any Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2064 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) |

## Problem Description

### Goal

There are $n$ specialty stores and $m$ product types. The array `quantities` gives the available count of every type, and all products must be distributed. One product type may be split among several stores, but each store may receive products of at most one type. Stores are also allowed to receive nothing.

For a completed distribution, let $x$ be the largest number of products assigned to any one store. Return the smallest value of $x$ achievable while obeying the rules.

### Function Contract

**Inputs**

- `n`: the number of stores, where $1 \le n \le 10^5$.
- `quantities`: an array of $m$ positive product counts, where $1 \le m \le n$ and each count is at most $10^5$.

Let $Q=\max(\texttt{quantities})$.

**Return value**

- Return the minimum possible maximum number of products held by any store after distributing every product.

### Examples

**Example 1**

- Input: `n = 6, quantities = [11,6]`
- Output: `3`
- Explanation: Split the first type among four stores as `2,3,3,3` and the second among two stores as `3,3`.

**Example 2**

- Input: `n = 7, quantities = [15,10,10]`
- Output: `5`
- Explanation: The three types can use three, two, and two stores, each holding five products.

**Example 3**

- Input: `n = 1, quantities = [100000]`
- Output: `100000`
- Explanation: The only store must receive the complete quantity.
