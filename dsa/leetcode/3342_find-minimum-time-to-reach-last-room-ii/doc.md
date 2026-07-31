# Find Minimum Time to Reach Last Room II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3342 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) |

## Problem Description

### Goal

A dungeon contains $n \times m$ rooms arranged in a rectangular grid. For each room `(i, j)`, `moveTime[i][j]` is the earliest time when a move into that room may begin. You start in room `(0, 0)` at time `0`, so its own value does not delay the initial state.

You may move through a shared wall to the room immediately above, below, left, or right, waiting before a move whenever its destination is not yet available. Move durations alternate globally along the chosen route: the first move takes one second, the second takes two seconds, the third takes one second, and so on. Return the minimum time needed to reach `(n - 1, m - 1)`.

### Function Contract

**Inputs**

- `moveTime`: An $n \times m$ matrix, where $2 \le n,m \le 750$ and every entry is an integer from $0$ through $10^9$.

**Return value**

- The minimum integer time at which the bottom-right room can be reached.

### Examples

**Example 1**

- Input: `moveTime = [[0,4],[4,4]]`
- Output: `7`
- Explanation: Start the first move at time `4`, finish it at `5`, then take two seconds for the second move.

**Example 2**

- Input: `moveTime = [[0,0,0,0],[0,0,0,0]]`
- Output: `6`
- Explanation: A shortest route uses four moves whose durations are `1, 2, 1, 2`.

**Example 3**

- Input: `moveTime = [[0,1],[1,2]]`
- Output: `4`
