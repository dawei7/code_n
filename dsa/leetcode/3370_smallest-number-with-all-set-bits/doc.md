# Smallest Number With All Set Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3370 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-number-with-all-set-bits/) |

## Problem Description

### Goal

Given a positive integer `n`, find the smallest integer $x$ such that $x\geq n$ and every digit in the binary representation of $x$ is a set bit. In other words, the representation must consist entirely of ones and may not contain any zero.

The eligible values therefore have the form $1$, $3$, $7$, $15$, and so on. If `n` already has this form, return `n` itself; otherwise advance to the first such value above it. The answer must be determined for the complete legal range from $1$ through $1000$.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1\leq n\leq1000$.

**Return value**

- The smallest integer at least `n` whose binary representation contains only set bits.

### Examples

**Example 1**

- Input: `n = 5`
- Output: `7`
- Explanation: `7` is `111` in binary.

**Example 2**

- Input: `n = 10`
- Output: `15`
- Explanation: `15` is `1111` in binary.

**Example 3**

- Input: `n = 3`
- Output: `3`
- Explanation: `3` already has binary representation `11`.
