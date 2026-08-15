# Alternating Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2544 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [alternating-digit-sum](https://leetcode.com/problems/alternating-digit-sum/) |

## Problem Description

### Goal

A positive integer `n` is read from its most significant digit to its least significant digit. Give the first digit a positive sign, then alternate signs so that every following digit has the opposite sign from the digit immediately before it.

Return the sum of all decimal digits after applying those signs. Zero digits still occupy positions in the alternation even though their numerical contribution is zero.

### Function Contract

**Inputs**

- `n`: The positive integer whose decimal digits receive alternating signs.

The public constraint is $1 \leq n \leq 10^9$.

**Return value**

Return the signed digit sum that begins positively at the most significant digit.

### Examples

#### Example 1

- **Input:** `n = 521`
- **Output:** `4`
- **Explanation:** $5-2+1=4$.

#### Example 2

- **Input:** `n = 111`
- **Output:** `1`
- **Explanation:** $1-1+1=1$.

#### Example 3

- **Input:** `n = 886996`
- **Output:** `0`
- **Explanation:** $8-8+6-9+9-6=0$.
