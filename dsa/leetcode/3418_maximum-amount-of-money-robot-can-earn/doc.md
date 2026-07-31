# Maximum Amount of Money Robot Can Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3418 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/) |

## Problem Description

### Goal

A robot begins at the top-left cell of a rectangular grid and must reach the bottom-right cell by moving only right or down. Entering a cell with a nonnegative value earns that many coins. Entering a cell with a negative value encounters a robber and reduces the robot's total by the absolute value shown.

Along its chosen path, the robot may neutralize robbers in at most two cells. A neutralized negative cell contributes zero instead of reducing the total. Choose both the route and which robbers, if any, to neutralize so that the final profit is as large as possible. The maximum may still be negative.

### Function Contract

**Inputs**

- `coins`: A rectangular integer matrix describing gains and robber losses.

Let $m=\lvert\texttt{coins}\rvert$ and $n=\lvert\texttt{coins[0]}\rvert$. The constraints are $1\le m,n\le500$ and $-1000\le\texttt{coins[i][j]}\le1000$.

**Return value**

- The maximum profit obtainable on a top-left-to-bottom-right path after neutralizing at most two negative cells.

### Examples

**Example 1**

- Input: `coins = [[0, 1, -1], [1, -2, 3], [2, -3, 4]]`
- Output: `8`

One optimal route visits values `0, 1, -2, 3, 4` and neutralizes `-2`, producing $0+1+0+3+4=8$.

**Example 2**

- Input: `coins = [[10, 10, 10], [10, 10, 10]]`
- Output: `40`

No neutralization is needed on an all-positive route.

**Example 3**

- Input: `coins = [[-5, -10], [-20, -1]]`
- Output: `-1`

Every route contains three negative cells, so two can be neutralized and the least harmful remaining loss is `-1`.
