# Minimum Number of Operations to Make X and Y Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2998 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Breadth-First Search, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/) |

## Problem Description

### Goal

You are given two positive integers `x` and `y`. An operation changes `x` in
exactly one of four ways: increment it by one, decrement it by one, divide it
by 5 when it is divisible by 5, or divide it by 11 when it is divisible by 11.

Return the minimum number of operations needed to make the changing value of
`x` equal `y`. Division is unavailable unless the current value is an exact
multiple of the chosen divisor.

### Function Contract

**Inputs**

- `x`: the positive integer that may be changed
- `y`: the positive target integer

The contract guarantees $1 \le x,y \le 10^4$. Let $X=\max(x,y)$.

**Return value**

Return the fewest permitted operations needed to transform `x` into `y`.

### Examples

#### Example 1

- **Input:** `x = 26, y = 1`
- **Output:** `3`

Decrementing to 25 and then dividing by 5 twice reaches 1.

#### Example 2

- **Input:** `x = 54, y = 2`
- **Output:** `4`

Incrementing to 55 enables division by 11 and then by 5; one final increment
reaches 2.

#### Example 3

- **Input:** `x = 25, y = 30`
- **Output:** `5`

Five increments are optimal because division only moves the value farther
below the larger target.
