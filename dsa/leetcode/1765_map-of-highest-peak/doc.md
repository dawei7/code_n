# Map of Highest Peak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1765 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/map-of-highest-peak/) |

## Problem Description

### Goal

An $m \times n$ integer matrix `isWater` describes a map of land and water. A value of `1` marks water, while `0` marks land.

Assign a non-negative integer height to every cell. Every water cell must have height $0$, and the absolute height difference between any two cells sharing a side must be at most $1$. Diagonal cells are not adjacent.

Among all assignments satisfying these rules, maximize the greatest height appearing anywhere in the map. Return any height matrix that attains that maximum.

### Function Contract

**Inputs**

- `isWater`: an $R \times C$ binary matrix, with $1 \le R,C \le 10^3$.
- `isWater[r][c] = 1` denotes water and `isWater[r][c] = 0` denotes land.
- At least one cell is water.

**Return value**

- Return an $R \times C$ integer matrix whose water cells have height $0$, whose heights are non-negative, and whose side-adjacent cells differ by at most $1$.
- The maximum value in the returned matrix must be as large as any valid assignment permits.

### Examples

**Example 1**

- Input: `isWater = [[0,1],[0,0]]`
- Output: `[[1,0],[2,1]]`
- Explanation: The water cell is at height $0$; moving one step away raises the height by one.

**Example 2**

- Input: `isWater = [[0,0,1],[1,0,0],[0,0,0]]`
- Output: `[[1,1,0],[0,1,1],[1,2,2]]`
- Explanation: The greatest attainable height is $2$. Any valid assignment attaining that value is acceptable.

**Example 3**

- Input: `isWater = [[1]]`
- Output: `[[0]]`
- Explanation: The only cell is water, so its required height is $0$.
