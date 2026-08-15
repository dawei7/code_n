# Smallest Even Multiple

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2413 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-even-multiple/) |

## Problem Description

### Goal

Given a positive integer `n`, find the smallest positive integer divisible by both `n` and 2. In number-theoretic terms, the result is the least common multiple of `n` and 2, but only the parity of `n` is needed to determine it.

When `n` is already even, `n` itself satisfies both divisibility requirements and no smaller positive multiple of `n` exists. When `n` is odd, its first multiple is odd, while the next multiple, `2 * n`, is even and is therefore the first common multiple.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1 \le n \le 150$.

**Return value**

Return the smallest positive integer that is a multiple of both 2 and `n`.

### Examples

#### Example 1

- **Input:** `n = 5`
- **Output:** `10`

#### Example 2

- **Input:** `n = 6`
- **Output:** `6`

#### Example 3

- **Input:** `n = 1`
- **Output:** `2`
