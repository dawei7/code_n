# Factor Combinations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/factor-combinations/) |

## Problem Description
### Goal
Given a positive integer `n`, find every way to express it as a product of at least two integer factors. Every factor must be greater than `1` and strictly smaller than `n`, so the trivial one-factor representation `[n]` is excluded.

Return each distinct factor combination once, writing factors within a combination in nondecreasing order so permutations do not create duplicates. The product of all entries must equal `n` exactly, and combinations may contain repeated factors when divisibility permits. Outer result order is unrestricted. Prime values and other inputs with no nontrivial factorization return an empty list.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

All unique nondecreasing factor combinations whose product is `n`.

### Examples
**Example 1**

- Input: `n = 12`
- Output: `[[2,6],[3,4],[2,2,3]]`

**Example 2**

- Input: `n = 37`
- Output: `[]`

**Example 3**

- Input: `n = 16`
- Output: `[[2,8],[4,4],[2,2,4],[2,2,2,2]]`
