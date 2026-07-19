# Minimum Number of Operations to Reinitialize a Permutation

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/) |
| Frontend ID | 1806 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For an even integer `n`, begin with the identity permutation `perm`, where `perm[i] = i`. One operation constructs a new array `arr`: at every even index $i$, set `arr[i] = perm[i / 2]`; at every odd index, set `arr[i] = perm[n / 2 + (i - 1) / 2]`. Replace `perm` with `arr`.

Repeat this fixed transformation until the permutation first becomes the identity again. Return the minimum positive number of operations required.

### Function Contract

**Inputs**

- `n`: an even integer satisfying $2 \le n \le 1000$.
- Let $k$ denote the minimum positive number of transformations that restore the identity.

**Return value**

- Return $k$.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `1`

The only transformation already preserves `[0,1]`.

**Example 2**

- Input: `n = 4`
- Output: `2`

The first transformation changes the permutation and the second restores it.

**Example 3**

- Input: `n = 6`
- Output: `4`

Four repeated applications are required for the identity to return.
