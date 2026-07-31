# Furthest Point From Origin

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2833 |
| Difficulty | Easy |
| Topics | String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/furthest-point-from-origin/) |

## Problem Description
### Goal

A string `moves` of length $n$ describes movement on a number line beginning at coordinate $0$. Each `L` forces a one-unit move left, each `R` forces a one-unit move right, and every `_` may independently be chosen as either a left or right move.

Choose the direction of every `_` to make the final point as far from the origin as possible. Return that greatest possible distance after all $n$ moves. The distance is the absolute value of the final coordinate; an intermediate point reached before the last move does not determine the answer.

### Function Contract
**Inputs**

- `moves`: A nonempty string of length $n$, where $1 \le n \le 50$, containing only `L`, `R`, and `_`.

**Return value**

Return the maximum possible absolute final coordinate after resolving every `_` as one unit left or one unit right.

### Examples
**Example 1**

- Input: `moves = "L_RL__R"`
- Output: `3`
- Explanation: Resolving the flexible moves to obtain `"LLRLLLR"` finishes at coordinate $-3$.

**Example 2**

- Input: `moves = "_R__LL_"`
- Output: `5`
- Explanation: One optimal resolution is `"LRLLLLL"`, which finishes at coordinate $-5$.

**Example 3**

- Input: `moves = "_______"`
- Output: `7`
- Explanation: Directing every move right reaches coordinate $7$.
