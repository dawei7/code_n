# Rotting Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 994 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/rotting-oranges/) |

## Problem Description

### Goal

You are given an $m\times n$ grid in which `0` represents an empty cell, `1` represents a fresh orange, and `2` represents a rotten orange. During each minute, every fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes required until no cell contains a fresh orange. If one or more fresh oranges can never be reached by this spreading process, return `-1`. When the grid initially has no fresh oranges, the required time is zero.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ matrix whose entries are `0`, `1`, or `2`, where $1\le m,n\le10$.

Define the grid area as $A=mn$.

**Return value**

- The minimum elapsed minutes needed to rot every fresh orange, or `-1` if that is impossible.

### Examples

**Example 1**

- Input: `grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]`
- Output: `4`

**Example 2**

- Input: `grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]`
- Output: `-1`
- Explanation: The fresh orange in the lower-left corner has no 4-directional path from a rotten orange.

**Example 3**

- Input: `grid = [[0, 2]]`
- Output: `0`
- Explanation: No fresh orange exists at minute zero.
