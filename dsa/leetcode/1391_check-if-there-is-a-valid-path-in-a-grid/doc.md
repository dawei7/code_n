# Check if There is a Valid Path in a Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1391 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) |

## Problem Description

### Goal

An $m \times n$ grid represents streets. Every cell contains one of six street types, and each type joins exactly two sides of its cell: type `1` joins left and right, type `2` joins up and down, type `3` joins left and down, type `4` joins right and down, type `5` joins left and up, and type `6` joins right and up.

A move between orthogonally adjacent cells is valid only when the current street opens toward the neighbor and the neighboring street opens back toward the current cell. Street pieces cannot be changed or rotated.

Determine whether the existing streets contain a valid path from the upper-left cell `(0, 0)` to the lower-right cell `(m - 1, n - 1)`.

### Function Contract

**Inputs**

- `grid`: a nonempty $m \times n$ matrix whose entries are street types from `1` through `6`, with $1 \le m,n \le 300$.

**Return value**

- `true` if compatible street connections join the upper-left and lower-right cells; otherwise `false`.

### Examples

**Example 1**

- Input: `grid = [[2,4,3],[6,5,2]]`
- Output: `true`

**Example 2**

- Input: `grid = [[1,2,1],[1,2,1]]`
- Output: `false`

**Example 3**

- Input: `grid = [[1,1,2]]`
- Output: `false`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Treat compatible borders as graph edges.** Associate each street type with its two opening directions. Begin a breadth-first search at `(0, 0)`. From a cell, inspect only the two neighbors indicated by its street piece.

An opening alone does not establish an edge. For a proposed direction `(dr, dc)`, first require the neighbor to lie inside the grid, then require its opening set to contain the reverse direction `(-dr, -dc)`. This reciprocal check precisely matches the rule that the two street pieces connect across their shared border.

Mark a cell when it enters the queue. Every enqueued cell is reachable by a sequence of compatible borders: this is true for the start, and the reciprocal check extends such a path by one valid move. Conversely, any valid path can be followed edge by edge by the search because each of its moves passes that same check. Thus reaching the lower-right cell is equivalent to the requested path existing. The visited set prevents cycles from causing repeated work.

#### Complexity detail

There are $mn$ cells. Each is enqueued at most once and exposes exactly two directions, so traversal time is $O(mn)$. The queue and visited state can each hold $O(mn)$ coordinates.

#### Alternatives and edge cases

- **Depth-first search:** A stack or recursion with the same reciprocal checks also runs in $O(mn)$; recursion can exceed the language call-stack limit on a long path.
- **Union-find:** Join every reciprocally compatible neighboring pair and compare the two endpoint roots. This also costs near-linear time but builds connectivity beyond what the single query needs.
- **One-sided opening:** A current tile pointing at a neighbor is insufficient when the neighbor does not point back.
- **Boundary-facing opening:** An opening that leaves the grid produces no move.
- **Cycles:** Visited state is necessary even though each tile has only two openings.
- **Single cell:** The start already equals the destination, so the answer is `true` regardless of its street type.
- **Destination orientation:** Reaching the destination is enough; its unused opening need not lead anywhere.

</details>
