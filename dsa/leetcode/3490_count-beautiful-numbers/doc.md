# Count Beautiful Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3490 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-beautiful-numbers/) |

## Problem Description

### Goal

For a positive integer, multiply all of its decimal digits and separately add all of its decimal digits. The integer is **beautiful** when the digit product is divisible by the digit sum. A zero digit makes the product zero, which is divisible by every positive digit sum.

Given the inclusive interval from `l` through `r`, count how many integers in that interval are beautiful. Both endpoints are positive, and the upper endpoint is strictly less than $10^9$.

### Function Contract

**Inputs**

- `l`: The positive inclusive lower endpoint.
- `r`: The positive inclusive upper endpoint.

The endpoints satisfy $1 \le l \le r < 10^9$.

**Return value**

Return the number of beautiful integers in the inclusive interval $[l,r]$.

### Examples

#### Example 1

- **Input:** `l = 10, r = 20`
- **Output:** `2`
- **Explanation:** `10` and `20` have digit product zero, so both are beautiful; no other number in the interval qualifies.

#### Example 2

- **Input:** `l = 1, r = 15`
- **Output:** `10`
- **Explanation:** Every one-digit number from `1` through `9` qualifies because its product equals its sum, and `10` also qualifies because its product is zero.
