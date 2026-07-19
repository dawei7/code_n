# Shortest Path to Get Food

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1730 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-to-get-food/) |

## Problem Description

### Goal

You are located at the unique `'*'` cell of an $m\times n$ character grid and want to reach food as quickly as possible. A `'#'` cell contains food, an `'O'` cell is open space, and an `'X'` cell is an obstacle. The grid may contain multiple food cells.

One step moves to an orthogonally adjacent cell—north, east, south, or west—provided that cell lies inside the grid and is not an obstacle. Return the minimum number of steps needed to reach any food cell. If no food is reachable, return `-1`.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ matrix whose entries are `'*'`, `'#'`, `'O'`, or `'X'`, where $1 \le m,n \le 200$ and exactly one `'*'` appears.

**Return value**

- Return the length of a shortest valid path from `'*'` to any `'#'`, or `-1` when no such path exists.

### Examples

**Example 1**

- Input: `grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]`
- Output: `3`
- Explanation: The nearest food can be reached in three orthogonal steps.

**Example 2**

- Input: `grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]`
- Output: `-1`
- Explanation: Obstacles separate the start from the food.

**Example 3**

- Input: `grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]`
- Output: `6`
- Explanation: Of the two food cells, the lower one is reachable in six steps.
