# Number of Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 200 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-islands/) |

## Problem Description
### Goal
Given a nonempty rectangular grid whose cells are `"1"` for land and `"0"` for water, group land cells that can reach one another through a sequence of horizontal or vertical land neighbors. Each maximal connected group represents one island surrounded by water or the grid boundary.

Return the number of distinct islands. Diagonal contact alone does not connect land, separate components must be counted independently even when close together, and every land cell belongs to exactly one component. An all-water grid returns `0`, while any connected shape of land—regardless of holes or irregular boundaries—contributes one island.

### Function Contract
**Inputs**

- `grid`: a nonempty matrix whose cells are `"1"` for land or `"0"` for water

**Return value**

The number of distinct land components connected horizontally or vertically.

### Examples
**Example 1**

- Input: `[["1","1","0"],["1","0","0"],["0","0","1"]]`
- Output: `2`

**Example 2**

- Input: all water
- Output: `0`

**Example 3**

- Diagonal land cells only
- Output: one island per land cell

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

An island is a connected component in a graph whose vertices are land cells and whose edges connect horizontal or vertical neighbors. The task is therefore to count connected components without building an explicit graph.

Scan the grid in row-major order. When a land cell has not been visited, it is the first encountered representative of a new island: increment the count and traverse from that seed. An explicit stack avoids recursion-depth limits. Mark the seed visited before pushing or immediately when discovered, then repeatedly inspect its four neighboring coordinates and add each in-bounds, unvisited land neighbor.

Marking at discovery time matters. If marking were delayed until a cell is popped, two adjacent cells could both enqueue the same neighbor, increasing work and stack size. The visited set separates discovery state from grid contents and preserves the input.

For

```text
1 1 0
1 0 0
0 0 1
```

the first `1` seeds a traversal that reaches the other two cells in the upper-left component. Those cells are then skipped by the outer scan. The bottom-right `1` remains unvisited, seeds a second traversal, and gives a total of two.

Diagonal cells are never considered neighbors. Two `1`s touching only at a corner therefore seed separate traversals and count as separate islands.

Starting from an unvisited land seed, the traversal follows every allowed four-direction land edge. It therefore visits every cell reachable from the seed and cannot visit a cell outside that connected component. When the traversal finishes, that entire island is marked. No marked cell can seed another count, while every island has a first cell encountered by the complete grid scan and therefore seeds exactly one traversal. Consequently the counter equals the number of islands.

#### Complexity detail

The outer scan examines `mn` cells. Each land cell is marked once, pushed and popped at most once, and checks four neighbors, so total time is $O(mn)$. The visited set and explicit stack can each hold $O(mn)$ coordinates in the worst case, matching the required $O(mn)$ auxiliary-space bound.

#### Alternatives and edge cases

- Mutating visited land from `"1"` to `"0"` removes the separate visited set and can reduce auxiliary storage, but changes the caller's grid.
- Recursive DFS is concise but can overflow the call stack on a large or snake-shaped island.
- Breadth-first search with a queue has the same asymptotic bounds and correctness.
- Union-find is valuable when connectivity changes dynamically, but adds parent/rank machinery for this static scan.
- All water returns zero; all connected land returns one. One-row and one-column grids use the same logic.

</details>
