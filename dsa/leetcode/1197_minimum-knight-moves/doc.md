# Minimum Knight Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1197 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-knight-moves/) |

## Problem Description

### Goal

An infinite chessboard has integer coordinates extending without bound in every direction, and a knight begins at `[0,0]`. Each legal knight move travels two squares along one coordinate axis and one square along the other axis, giving eight possible signed displacements.

Given target coordinates `[x,y]`, return the minimum number of legal moves required to reach that square. A route is guaranteed to exist, including for targets with negative coordinates and for the starting square itself.

### Function Contract

**Inputs**

- `x`: The target horizontal coordinate, where $-300\le x\le300$.
- `y`: The target vertical coordinate, where $-300\le y\le300$.
- The target also satisfies $0\le\lvert x\rvert+\lvert y\rvert\le300$.

**Return value**

- The minimum number of knight moves from `[0,0]` to `[x,y]`.

### Examples

**Example 1**

- Input: `x = 2`, `y = 1`
- Output: `1`

One legal knight move reaches the target directly.

**Example 2**

- Input: `x = 5`, `y = 5`
- Output: `4`

One shortest route is `[0,0] -> [2,1] -> [4,2] -> [3,4] -> [5,5]`.

**Example 3**

- Input: `x = 0`, `y = 0`
- Output: `0`
