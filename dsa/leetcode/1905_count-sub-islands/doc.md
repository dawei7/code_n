# Count Sub Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1905 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) |

## Problem Description

### Goal

You receive two binary matrices `grid1` and `grid2` with identical dimensions. A value of `1` denotes land and `0` denotes water. Within either grid, an island is a maximal group of land cells connected through shared horizontal or vertical edges; diagonal contact does not connect cells.

An island from `grid2` is a sub-island only when every one of its land cells occupies a land position in `grid1`. Count how many complete `grid2` islands satisfy this containment condition. Cells beyond the matrix boundary are water.

### Function Contract

**Inputs**

- `grid1` and `grid2`: binary matrices with $m$ rows and $n$ columns.
- The dimensions satisfy $1 \le m,n \le 500$ and are equal for both grids.

**Return value**

Return the number of four-directionally connected islands in `grid2` whose every cell is also land in `grid1`.

### Examples

**Example 1**

- Input: `grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]`
- Output: `3`

**Example 2**

- Input: `grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]`
- Output: `2`

**Example 3**

- Input: `grid1 = [[1]], grid2 = [[1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Traverse each `grid2` component once.** Scan every cell. When an unvisited land cell is found, start an iterative depth-first search. Mark a cell visited as soon as it is placed on the stack, here by changing its `grid2` value to zero, so no land cell can enter two traversals.

**Accumulate containment without stopping early.** Begin the component with `contained = True`. For every popped cell, set this flag to false if the corresponding `grid1` position is water. Continue visiting the entire component even after a mismatch; otherwise its remaining cells could later be mistaken for separate islands. After the stack empties, add one to the answer only if the flag stayed true.

Every `grid2` island is discovered exactly once, and the flag is true exactly when all cells in that maximal component overlap land in `grid1`. Thus precisely the sub-islands are counted.

#### Complexity detail

Let $m$ and $n$ be the grid dimensions. The outer scan and all traversals together process each cell a constant number of times, for $O(mn)$ time. In the worst case the explicit DFS stack holds $O(mn)$ land cells, giving $O(mn)$ auxiliary space. Reusing `grid2` as the visited marker avoids a separate visited matrix.

#### Alternatives and edge cases

- **Recursive DFS:** It expresses the same logic but a large island can exceed the language's recursion limit.
- **Breadth-first search:** A queue gives the same $O(mn)$ bounds and containment test.
- **Union-find:** Components can be built with disjoint sets, but this requires additional structure without improving the asymptotic bound.
- **Stop on the first mismatch:** The answer flag may be settled, but the entire invalid component must still be consumed.
- **Diagonal land:** Diagonally touching cells belong to different islands.
- **All water:** With no `grid2` islands, return zero.
- **Extra `grid1` land:** Only cells used by a `grid2` island matter; surrounding or unrelated `grid1` land is irrelevant.

</details>
