# Maximum Multiplication Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3290 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-multiplication-score/) |

## Problem Description

### Goal

You are given an integer array `a` containing exactly four values and another integer array `b` containing at least four values. Choose four indices $i_0 < i_1 < i_2 < i_3$ from `b`.

The selected indices produce the score `a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3]`. Return the maximum score obtainable while preserving this order. Values in either array may be negative, so the result is not necessarily positive.

### Function Contract

**Inputs**

- `a`: A list of exactly four integers used as ordered multipliers.
- `b`: A list of $n$ integers from which four ordered positions are selected.

The constraints guarantee $4 \le n \le 10^5$ and $-10^5 \le a[i], b[i] \le 10^5$.

**Return value**

- The maximum score over every increasing choice of four indices in `b`.

### Examples

#### Example 1

- **Input:** `a = [3,2,5,6]`, `b = [2,-6,4,-5,-3,2,-7]`
- **Output:** `26`
- **Explanation:** Choosing indices 0, 1, 2, and 5 gives `3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26`.

#### Example 2

- **Input:** `a = [-1,4,5,-2]`, `b = [-5,-1,-3,-2,-4]`
- **Output:** `-1`
- **Explanation:** Choosing indices 0, 1, 3, and 4 gives the maximum score, `-1`.
