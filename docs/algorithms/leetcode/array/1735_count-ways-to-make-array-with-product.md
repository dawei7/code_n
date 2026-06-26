# Count Ways to Make Array With Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1735 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Number Theory |
| Official Link | [count-ways-to-make-array-with-product](https://leetcode.com/problems/count-ways-to-make-array-with-product/) |

## Problem Description & Examples
### Goal
For each query `[n, k]`, count arrays of length `n` made of positive integers whose product is exactly `k`. Return each count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `queries`: a list of `[n, k]` pairs.

**Return value**

Return the count for every query in order.

### Examples
**Example 1**

- Input: `queries = [[2,6],[5,1],[73,660]]`
- Output: `[4,1,50734910]`

**Example 2**

- Input: `queries = [[1,1],[2,2],[3,4]]`
- Output: `[1,2,6]`

**Example 3**

- Input: `queries = [[4,8],[3,12],[2,36]]`
- Output: `[20,18,9]`

---

## Underlying Base Algorithm(s)
Prime-factorize `k`. For each prime exponent `e`, distribute `e` identical factors among `n` positions, which has `C(n + e - 1, e)` possibilities by stars and bars. Multiply these values over all prime factors. Precompute factorials and inverse factorials up to the maximum needed exponent plus `n`.

---

## Complexity Analysis
- **Time Complexity**: `O(q * sqrt(k) + M)` for factorization plus combinatorics precomputation
- **Space Complexity**: `O(M)`
