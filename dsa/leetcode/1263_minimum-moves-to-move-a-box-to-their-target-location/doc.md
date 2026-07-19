# Minimum Moves to Move a Box to Their Target Location

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1263 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) |

## Problem Description

### Goal

A grid contains walls `"#"`, open cells `"."`, one player `"S"`, one movable box `"B"`, and one target `"T"`. The player may walk one cell horizontally or vertically through open cells, but cannot walk through walls or through the box.

When the player stands next to the box, the player may push it into the adjacent cell on the opposite side if that destination is open. The player cannot pull the box. Only pushes count as moves; ordinary player steps have zero cost. Return the minimum pushes needed to place the box on the target, or `-1` when this is impossible.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ character matrix, where $6 \le m,n \le 20$, with exactly one `"S"`, `"B"`, and `"T"`.
- Let $V=mn$ be the total number of grid cells.

**Return value**

- Return the minimum number of box pushes required to reach `"T"`, or `-1` if no valid sequence exists.

### Examples

**Example 1**

- Input: `grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `3`

**Example 2**

- Input: the same layout with row three replaced by all walls except its final open corridor cell.
- Output: `-1`

**Example 3**

- Input: `grid = [["#","#","#","#","#","#"],["#","T",".",".","#","#"],["#",".","#","B",".","#"],["#",".",".",".",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]`
- Output: `5`
