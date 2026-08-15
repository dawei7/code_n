# K Items With the Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2600 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-items-with-the-maximum-sum/) |

## Problem Description

### Goal

A bag contains items labeled only `1`, `0`, or `-1`. You are given the number of items carrying each label as `numOnes`, `numZeros`, and `numNegOnes`.

Choose exactly `k` distinct available items from the bag. The score of a choice is the sum of their written values, so positive items help, zero items preserve the score, and negative items reduce it.

Return the maximum sum obtainable from exactly `k` selections.

### Function Contract

**Inputs**

- `numOnes`: The number of items labeled `1`.
- `numZeros`: The number of items labeled `0`.
- `numNegOnes`: The number of items labeled `-1`.
- `k`: The exact number of items to select.

All three counts are between $0$ and $50$, inclusive, and $0 \leq k \leq \texttt{numOnes} + \texttt{numZeros} + \texttt{numNegOnes}$.

**Return value**

- The greatest possible sum of the values on exactly `k` selected items.

### Examples

#### Example 1

- **Input:** `numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2`
- **Output:** `2`

Selecting two of the three positive items gives the maximum sum `2`.

#### Example 2

- **Input:** `numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4`
- **Output:** `3`

Take all three positive items and one zero-valued item, so the fourth selection does not reduce the sum.
