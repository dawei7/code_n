# Number of Self-Divisible Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2992 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Bit Manipulation, Backtracking, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-self-divisible-permutations/) |

## Problem Description

### Goal

Given `n`, consider every permutation of the 1-indexed array
`[1, 2, ..., n]`. A permutation is **self-divisible** when the value placed at
every 1-indexed position $i$ is coprime with $i$; equivalently,
$\gcd(a_i,i)=1$ for all $1\le i\le n$.

Return the number of permutations satisfying this condition. Each value from
`1` through `n` must appear exactly once.

### Function Contract

**Inputs**

- `n`: the length and largest value of the permutation

The contract guarantees $1\le n\le12$.

**Return value**

Return the number of self-divisible permutations of `[1, 2, ..., n]`.

### Examples

#### Example 1

- **Input:** `n = 1`
- **Output:** `1`

#### Example 2

- **Input:** `n = 2`
- **Output:** `1`
- **Explanation:** Only `[2,1]` places a value coprime with each position.

#### Example 3

- **Input:** `n = 3`
- **Output:** `3`
