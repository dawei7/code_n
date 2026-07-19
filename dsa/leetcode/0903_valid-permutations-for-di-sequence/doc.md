# Valid Permutations for DI Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 903 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-permutations-for-di-sequence/) |

## Problem Description
### Goal
You are given a string `s` of length `n` whose characters are `"D"` for decreasing or `"I"` for increasing.

Consider every permutation `perm` of all $n+1$ integers in the range $[0,n]$. It is valid when each character describes the corresponding adjacent pair: `"D"` requires `perm[i] > perm[i + 1]`, while `"I"` requires `perm[i] < perm[i + 1]`. All comparisons are strict because the permutation contains distinct values.

Return the number of valid permutations modulo $10^9+7$.

### Function Contract
Let $n=\lvert\texttt{s}\rvert$ and $P=10^9+7$.

**Inputs**

- `s`: a string with $1 \leq n \leq 200$ consisting only of `"D"` and `"I"`.

**Return value**

Return the number of permutations of $[0,n]$ satisfying every encoded adjacent relation, reduced modulo $P$.

### Examples
**Example 1**

- Input: `s = "DID"`
- Output: `5`

**Example 2**

- Input: `s = "D"`
- Output: `1`

**Example 3**

- Input: `s = "I"`
- Output: `1`
