# Strange Printer II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1591 |
| Difficulty | Hard |
| Topics | Array, Graph Theory, Topological Sort, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/strange-printer-ii/) |

## Problem Description
### Goal

A printer starts with a blank grid. On each turn, it chooses one color and fills every cell of one solid axis-aligned rectangle with that color. New printing overwrites anything previously present in the chosen rectangle.

Each color may be used in at most one turn, so all final cells of one color must originate from a single rectangle even if later colors cover parts of it. Given the desired color matrix, decide whether some ordering of one rectangle per used color can produce it exactly.

### Function Contract
**Inputs**

- `targetGrid`: An $M$-by-$N$ matrix, where $1 \le M,N \le 60$ and every cell color is between $1$ and $60$.

Let $C$ be the number of distinct colors in the grid.

**Return value**

Return `true` if the grid can be formed while using every color at most once; otherwise, return `false`.

### Examples
**Example 1**

- Input: `targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]`
- Output: `true`

**Example 2**

- Input: `targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]`
- Output: `true`

**Example 3**

- Input: `targetGrid = [[1,2,1],[2,1,2],[1,2,1]]`
- Output: `false`
