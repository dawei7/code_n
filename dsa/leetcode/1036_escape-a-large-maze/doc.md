# Escape a Large Maze

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1036 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/escape-a-large-maze/) |

## Problem Description

### Goal

A grid on the xy-plane contains one million rows and one million columns, with every coordinate component between $0$ and $999999$.

Start at `source = [sx, sy]` and try to reach `target = [tx, ty]`. Coordinates listed in `blocked` cannot be entered. Each move goes one square north, east, south, or west, must remain inside the grid, and must not land on a blocked square.

Return `true` if and only if some sequence of valid moves reaches `target` from `source`.

### Function Contract

**Inputs**

- `blocked`: $B$ distinct blocked coordinates, where $0 \le B \le 200$.
- `source` and `target`: different valid grid coordinates that are not blocked.
- Every coordinate component is in the interval $[0,10^6)$.

**Return value**

- Whether the target is reachable from the source by valid four-directional moves.

### Examples

**Example 1**

- Input: `blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]`
- Output: `false`
- Explanation: The grid boundary and the two blocked neighbors trap the source.

**Example 2**

- Input: `blocked = [], source = [0,0], target = [999999,999999]`
- Output: `true`
- Explanation: With no blocked cells, a path exists across the grid.
