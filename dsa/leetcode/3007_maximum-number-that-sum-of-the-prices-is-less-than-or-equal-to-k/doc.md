# Maximum Number That Sum of the Prices Is Less Than or Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3007 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/) |

## Problem Description

### Goal

You are given positive integers `k` and `x`. Number binary positions starting
at 1 for the least significant bit. The price of a positive integer is the
number of its set bits whose positions are `x`, `2 * x`, `3 * x`, and so on.

The accumulated price through a number `num` is the sum of the individual
prices of every integer from 1 through `num`. A number is cheap when this sum
is at most `k`.

Return the greatest cheap number.

### Function Contract

**Inputs**

- `k`: the maximum permitted accumulated price
- `x`: the spacing between counted 1-indexed bit positions

The contract guarantees $1\le k\le10^{15}$ and $1\le x\le8$.

**Return value**

Return the greatest `num` whose accumulated selected-bit count does not exceed
`k`.

### Examples

#### Example 1

- **Input:** `k = 9, x = 1`
- **Output:** `6`

All set bits count when `x` is 1. The accumulated price through 6 is 9, while
including 7 raises it to 12.

#### Example 2

- **Input:** `k = 7, x = 2`
- **Output:** `9`

Only even-numbered binary positions count. The sum through 9 is 6, while the
sum through 10 is 8.
