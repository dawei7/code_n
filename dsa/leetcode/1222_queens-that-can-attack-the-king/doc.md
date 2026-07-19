# Queens That Can Attack the King

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1222 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/queens-that-can-attack-the-king/) |

## Problem Description

### Goal

On an $8\times8$ chessboard, each coordinate is written as `[row, column]`, with both components between `0` and `7`. You are given the distinct coordinates in `queens` occupied by black queens and the coordinate `king` occupied by the white king. No queen shares the king's square.

A queen can attack along its row, column, or either diagonal. However, another queen between it and the king blocks that line of attack.

Return the coordinates of every queen that can directly attack the king. The coordinates may be returned in any order.

### Function Contract

**Inputs**

- `queens`: A list of $q$ distinct queen coordinates, where $1\le q\le63$ and each row and column lies from `0` through `7`.
- `king`: The king's coordinate on an unoccupied square of the same board.

**Return value**

- The coordinates of all queens with an unobstructed row, column, or diagonal attack on the king, in any order.

### Examples

**Example 1**

- Input: `queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]`, `king = [0,0]`
- Output: `[[0,1],[1,0],[3,3]]`

The queens at `[4,0]` and `[0,4]` are blocked by nearer queens on their respective rays.

**Example 2**

- Input: `queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]`, `king = [3,3]`
- Output: `[[2,2],[3,4],[4,4]]`

**Example 3**

- Input: `queens = [[5,6],[7,7],[2,1]]`, `king = [4,5]`
- Output: `[[5,6]]`
