# Maximum Candies Allocated to K Children

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2226 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) |

## Problem Description

### Goal

Each value in `candies` is the size of one pile. A pile may be divided into any number of smaller piles, but candies originating in different piles cannot be merged.

Allocate candies to exactly `k` children so every child receives the same number. Each child's allocation must come from one resulting subpile, and unused piles or remainders are allowed. Return the maximum equal amount per child. If the available piles cannot provide even one candy to every child, return zero.

### Function Contract

**Inputs**

- `candies`: A nonempty list of positive pile sizes.
- `k`: A positive integer giving the number of children.

Let $n=\lvert\texttt{candies}\rvert$ and let $V=\max(\texttt{candies})$.

**Return value**

Return the greatest integer portion size that can be produced at least `k` times without combining piles, or `0` when no positive size is feasible.

### Examples

#### Example 1

- **Input:** `candies = [5, 8, 6], k = 3`
- **Output:** `5`

#### Example 2

- **Input:** `candies = [2, 5], k = 11`
- **Output:** `0`

#### Example 3

- **Input:** `candies = [10], k = 3`
- **Output:** `3`
