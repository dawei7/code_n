# Maximum Manhattan Distance After K Changes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3443 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/) |

## Problem Description

### Goal

Starting at $(0,0)$ on an infinite grid, follow a string of moves in order. `N` and `S` change the vertical coordinate by one, while `E` and `W` change the horizontal coordinate by one.

Before following the path, you may replace at most `k` characters with any of the four directions. Determine the greatest Manhattan distance from the origin that can be reached after any prefix of the resulting path. For a position $(x,y)$, this distance is $\lvert x\rvert+\lvert y\rvert$.

### Function Contract

**Inputs**

- `s`: A movement string of length $n$, where $1\le n\le10^5$, containing only `N`, `S`, `E`, and `W`.
- `k`: The maximum number of directions that may be changed, where $0\le k\le n$.

**Return value**

Return the maximum achievable Manhattan distance from the origin at any time while executing the moves in order.

### Examples

#### Example 1

- **Input:** `s = "NWSE", k = 1`
- **Output:** `3`

Changing `S` to `N` produces `"NWNE"`, whose third move reaches distance $3$.

#### Example 2

- **Input:** `s = "NSWWEW", k = 3`
- **Output:** `6`

The path can be changed to `"NNWWWW"`, ending at Manhattan distance $6$.
