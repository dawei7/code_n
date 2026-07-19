# Concatenation of Consecutive Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1680 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) |

## Problem Description
### Goal

For every integer from $1$ through `n`, write its ordinary binary representation without leading zeroes. Concatenate those representations in increasing numeric order, so the bits for $1$ come first, followed by the bits for $2$, and continuing through the bits for `n`.

Treat the resulting bit string as one binary integer and return its decimal value modulo $10^9 + 7$. The conceptual concatenation may contain far more bits than a machine integer can hold, so the required result must be computed without relying on the full unreduced value fitting in a fixed-width type.

### Function Contract
**Inputs**

- `n`: a positive integer marking the inclusive end of the consecutive sequence

Let $M = 10^9 + 7$.

**Return value**

The base-10 value of `binary(1) + binary(2) + ... + binary(n)`, reduced modulo $M$.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `1`

**Example 2**

- Input: `n = 3`
- Output: `27`

**Example 3**

- Input: `n = 12`
- Output: `505379714`
