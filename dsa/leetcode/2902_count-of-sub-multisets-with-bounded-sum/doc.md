# Count of Sub-Multisets With Bounded Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2902 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of non-negative integers and two bounds `l` and `r`. Count the sub-multisets of `nums` whose element sum lies in the inclusive interval $[l,r]$, and return the count modulo $10^9+7$.

For a value $x$ occurring `occ[x]` times in the input, a sub-multiset may contain $x$ exactly $0,1,\ldots,\texttt{occ[x]}` times. Order does not matter: two selections are the same when sorting them produces identical multisets. The empty multiset is allowed and has sum $0$.

### Function Contract

**Inputs**

- `nums`: A nonempty array of non-negative integers.
- `l`: The inclusive lower bound for an accepted sum.
- `r`: The inclusive upper bound for an accepted sum.

The shared bounds are $1\le n\le2\cdot10^4$, $0\le\texttt{nums[i]}\le2\cdot10^4$, and $0\le l\le r\le2\cdot10^4$. The sum of all elements in `nums` is at most $2\cdot10^4$. Let $D$ be the number of distinct positive values.

**Return value**

Return the number of distinct sub-multisets with sums in $[l,r]$, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 2, 3], l = 6, r = 6`
- **Output:** `1`
- **Explanation:** The only qualifying multiset is `{1, 2, 3}`.

#### Example 2

- **Input:** `nums = [2, 1, 4, 2, 7], l = 1, r = 5`
- **Output:** `7`
- **Explanation:** The qualifying multisets are `{1}`, `{2}`, `{4}`, `{2, 2}`, `{1, 2}`, `{1, 4}`, and `{1, 2, 2}`.

#### Example 3

- **Input:** `nums = [1, 2, 1, 3, 5, 2], l = 3, r = 5`
- **Output:** `9`
- **Explanation:** Nine distinct multiplicity selections have sums between $3$ and $5$ inclusive.
