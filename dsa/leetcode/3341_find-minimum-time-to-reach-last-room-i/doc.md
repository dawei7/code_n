# Find Minimum Time to Reach Last Room I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3341 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/) |

## Problem Description

### Goal

A dungeon contains $n \times m$ rooms arranged as a rectangular grid. For every position `(i, j)`, `moveTime[i][j]` is the earliest time at which that room is open for entry. You begin in `(0, 0)` at time `0`; the opening value of the starting room therefore does not delay the initial state.

From a room, you may move through a shared wall to the room immediately above, below, left, or right. You may wait as long as necessary before a move, and traversing one such edge takes exactly one second. Find the minimum time at which you can reach `(n - 1, m - 1)`.

### Function Contract

**Inputs**

- `moveTime`: An $n \times m$ matrix of room-opening times, where $2 \le n,m \le 50$ and every entry is between $0$ and $10^9$, inclusive.

**Return value**

- The minimum integer time at which the bottom-right room can be reached.

### Examples

#### Example 1

- **Input:** `moveTime = [[0,4],[4,4]]`
- **Output:** `6`
- **Explanation:** Wait until time `4`, finish the first move at time `5`, and finish the second at time `6`.

#### Example 2

- **Input:** `moveTime = [[0,0,0],[0,0,0]]`
- **Output:** `3`
- **Explanation:** No waiting is required, so any three-move shortest grid path arrives at time `3`.

#### Example 3

- **Input:** `moveTime = [[0,1],[1,2]]`
- **Output:** `3`
