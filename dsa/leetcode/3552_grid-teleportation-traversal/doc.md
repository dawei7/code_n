# Grid Teleportation Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3552 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/grid-teleportation-traversal/) |

## Problem Description

### Goal

You are given an $m \times n$ character grid `matrix`. A `'.'` cell is empty, a `'#'` cell is an obstacle, and each uppercase English letter denotes a teleportation portal.

Begin at the top-left cell `(0,0)` and reach the bottom-right cell `(m - 1,n - 1)`. A normal move enters one non-obstacle cell directly above, below, left, or right of the current cell and costs one move.

When the current cell contains a portal letter that has not previously been used, you may teleport to any other cell carrying that same letter. Teleportation costs zero moves, and each letter may be used at most once during the journey. Return the minimum number of moves needed to reach the destination, or `-1` when no valid journey exists.

### Function Contract

**Inputs**

- `matrix`: A nonempty array of equal-length strings containing only `'.'`, `'#'`, and uppercase English letters.

Let $m = \lvert\texttt{matrix}\rvert$ and $n = \lvert\texttt{matrix[0]}\rvert$. The constraints are $1 \le m,n \le 1000$, and `matrix[0][0]` is not an obstacle.

**Return value**

Return the minimum number of cost-one adjacent moves needed to reach `(m - 1,n - 1)`, accounting for optional zero-cost portal jumps, or `-1` if the destination is unreachable.

### Examples

#### Example 1

- **Input:** `matrix = ["A..",".A.","..."]`
- **Output:** `2`
- **Explanation:** Teleport from `(0,0)` to `(1,1)` for free, then make two adjacent moves to `(2,2)`.

#### Example 2

- **Input:** `matrix = [".#...",".#.#.",".#.#.","...#."]`
- **Output:** `13`
- **Explanation:** There are no portals, so the shortest valid route around the obstacles uses thirteen moves.

---
