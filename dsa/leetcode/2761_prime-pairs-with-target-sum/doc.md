# Prime Pairs With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2761 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Enumeration, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Prime Pairs With Target Sum](https://leetcode.com/problems/prime-pairs-with-target-sum/) |

## Problem Description

### Goal

Given an integer `n`, find every pair of prime numbers `[x, y]` satisfying $1 \leq x \leq y \leq n$ and $x + y = n$.

Return the pairs as a two-dimensional list ordered by increasing `x`. If no qualifying prime pair exists, return an empty list. A prime is an integer greater than $1$ whose only positive divisors are $1$ and itself.

### Function Contract

**Inputs**

- `n`: An integer with $1 \leq n \leq 10^6$.

**Return value**

Return all pairs `[x, y]` for which both entries are prime, $x \leq y$, and $x + y = n$. Order the result by increasing `x`.

### Examples

#### Example 1

- **Input:** `n = 10`
- **Output:** `[[3,7],[5,5]]`
- **Explanation:** Both pairs sum to $10$, and their entries are prime. The pair beginning with $3$ comes first.

#### Example 2

- **Input:** `n = 2`
- **Output:** `[]`
- **Explanation:** No two primes satisfying $x \leq y$ sum to $2$.

#### Example 3

- **Input:** `n = 5`
- **Output:** `[[2,3]]`
- **Explanation:** The only representation of $5$ as the sum of two primes is $2 + 3$.
