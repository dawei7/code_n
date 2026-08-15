# Smallest Value After Replacing With Sum of Prime Factors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2507 |
| Difficulty | Medium |
| Topics | Math, Simulation, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/) |

## Problem Description

### Goal

You are given a positive integer `n`. Repeatedly replace its current value with the sum of its prime factors. Prime factors are counted with multiplicity: if the same prime divides the value several times, that prime contributes once for every occurrence in the factorization.

Continue applying this replacement and return the smallest value that `n` takes on. Once a replacement produces the current value again, all later values are identical and no smaller value can appear.

### Function Contract

**Inputs**

- `n`: An integer whose prime factors are repeatedly summed.

The constraint is $2 \le n \le 10^5$.

**Return value**

An integer equal to the smallest value reached by the replacement process.

### Examples

#### Example 1

- **Input:** `n = 15`
- **Output:** `5`
- **Explanation:** The sequence is `15 -> 8 -> 6 -> 5`: the corresponding prime-factor sums are `3 + 5`, `2 + 2 + 2`, and `2 + 3`. The prime value `5` then maps to itself.

#### Example 2

- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** Because `3` is prime, its only prime factor is itself, so the first replacement leaves the value unchanged.
