# Find the N-th Value After K Seconds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3179 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation, Combinatorics, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/) |

## Problem Description
### Goal
Start with an array `a` containing $n$ elements, all equal to $1$. At the end of each second, every element is replaced simultaneously: the new value at index $i$ is the sum of the old values from index $0$ through index $i$, inclusive. Thus `a[0]` stays unchanged, while each later position receives the prefix sum ending at that position.

Apply this update for exactly $k$ seconds. Return the resulting value of `a[n - 1]`. Because that value can grow very large, return it modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: The length of the array initialized entirely with ones.
- `k`: The positive number of simultaneous prefix-sum updates to perform.

The constraints are $1 \le n \le 1000$ and $1 \le k \le 1000$. Let $M=10^9+7$ denote the required modulus.

**Return value**

Return the last array value after $k$ seconds, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 4, k = 5`
- Output: `56`

The successive states are `[1, 1, 1, 1]`, `[1, 2, 3, 4]`, `[1, 3, 6, 10]`, `[1, 4, 10, 20]`, `[1, 5, 15, 35]`, and `[1, 6, 21, 56]`. The last entry after five updates is therefore $56$.

**Example 2**

- Input: `n = 5, k = 3`
- Output: `35`

The array evolves from `[1, 1, 1, 1, 1]` to `[1, 2, 3, 4, 5]`, then `[1, 3, 6, 10, 15]`, and finally `[1, 4, 10, 20, 35]`.
