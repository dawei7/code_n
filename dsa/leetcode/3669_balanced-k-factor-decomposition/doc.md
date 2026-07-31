# Balanced K-Factor Decomposition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3669 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/balanced-k-factor-decomposition/) |

## Problem Description
### Goal

Given positive integers `n` and `k`, decompose `n` into exactly `k` positive integer factors. Multiplying all returned factors must reproduce `n`.

For a decomposition, compare its largest and smallest factors. Its imbalance is their difference, $max-min$. Among every valid $k$-factor decomposition, choose one whose imbalance is as small as possible.

Return any optimal decomposition. The factors may appear in any order, and distinct optimal outputs are equally valid.

### Function Contract

**Inputs**

- `n`: an integer satisfying $4\le n\le10^5$.
- `k`: an integer satisfying $2\le k\le5$.

The value `k` is strictly smaller than the number of positive divisors of `n`, ensuring a nontrivial legal search domain.

**Return value**

Return exactly `k` positive integers whose product is `n` and whose maximum-minus-minimum difference is minimum among all such decompositions.

### Examples

**Example 1**

- Input: `n = 100`, `k = 2`
- Output: `[10, 10]`
- The product is `100` and the spread is zero.

**Example 2**

- Input: `n = 44`, `k = 3`
- Output: `[2, 2, 11]`
- Its spread `9` is smaller than those of `[1, 1, 44]`, `[1, 2, 22]`, and `[1, 4, 11]`.

**Example 3**

- Input: `n = 36`, `k = 4`
- Output: `[2, 2, 3, 3]`
- The factors differ by at most one.
