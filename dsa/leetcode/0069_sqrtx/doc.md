# Sqrt(x)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 69 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sqrtx/) |

## Problem Description
### Goal
Given a nonnegative 32-bit integer `x`, compute its integer square root. This is the greatest nonnegative integer `r` satisfying $r \cdot r \le x$; equivalently, it is the floor of the real square root.

Return `r` and discard any fractional portion, so the square root of `8` produces `2`. Do not use a built-in exponentiation operation to obtain the answer. Boundary values such as `0`, `1`, and large nonsquares must avoid overflow during comparisons.

### Function Contract
**Inputs**

- `x`: an integer in the 32-bit nonnegative range

**Return value**

$\lfloor \sqrt{x} \rfloor$ as an integer.

### Examples
**Example 1**

- Input: `x = 4`
- Output: `2`

**Example 2**

- Input: `x = 8`
- Output: `2`

**Example 3**

- Input: `x = 0`
- Output: `0`
