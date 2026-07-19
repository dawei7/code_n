# Minimum Non-Zero Product of the Array Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1969 |
| Difficulty | Medium |
| Topics | Math, Greedy, Recursion |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/) |

## Problem Description
### Goal
For a positive integer `p`, form a 1-indexed array containing every integer in
the inclusive range from $1$ through $2^p-1$, represented with `p` binary
positions. An operation chooses two array elements and one bit position, then
swaps the bits occupying that same position in the two chosen elements.

Perform any number of these operations to minimize the product of all array
elements, subject to the product remaining nonzero. The minimum is determined
before applying a modulus; return that minimum modulo $10^9+7$.

### Function Contract
**Inputs**

- `p`: the binary width, where $1 \le p \le 60$.
- Let

  $$
  Q=2^p-1
  $$

  denote both the largest initial element and the `p`-bit all-ones value.

**Return value**

- The minimum positive product reachable through corresponding-bit swaps,
  reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `p = 1`
- Output: `1`

**Example 2**

- Input: `p = 2`
- Output: `6`

**Example 3**

- Input: `p = 3`
- Output: `1512`
