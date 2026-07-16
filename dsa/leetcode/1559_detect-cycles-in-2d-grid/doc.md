# Detect Cycles in 2D Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1559 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/) |

## Problem Description
### Goal

You are given an $R \times C$ grid of lowercase English letters. Two cells are adjacent when they share a horizontal or vertical side. A valid cycle is a path of at least four cells whose cells all contain the same letter, whose first and last cells are adjacent, and which does not reuse any cell except for closing the path at its start.

Determine whether at least one such cycle exists anywhere in the grid. The cycle may belong to any same-letter connected component and does not need to touch the grid boundary.

### Function Contract
**Inputs**

- `grid`: A rectangular matrix with $2 \le R,C \le 500$.
- Every `grid[r][c]` is a lowercase English letter. Movement is allowed only up, down, left, or right.

**Return value**

Return `true` if the grid contains a valid same-letter cycle of length at least four; otherwise return `false`.

### Examples
**Example 1**

- Input: `grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]`
- Output: `true`

**Example 2**

- Input: `grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]`
- Output: `true`

**Example 3**

- Input: `grid = [["a","b","b"],["b","z","b"],["b","b","a"]]`
- Output: `false`

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Treat each letter component as an undirected graph**

Each cell is a vertex, and an edge connects orthogonally adjacent cells with the same letter. Traverse every not-yet-seen component with an explicit DFS stack. Along with each cell, store the parent cell from which it was first discovered.

When examining a same-letter neighbor, three cases exist. An unseen neighbor is marked immediately and pushed with the current cell as its parent. The parent itself is ignored because an undirected edge naturally appears in both directions and walking straight back does not form a cycle. Any other already-seen neighbor proves that two distinct traversal paths have reached the same vertex, so the component contains a cycle.

**Why the detected cycle meets the length rule**

Grid adjacency forms a bipartite graph: color cells by the parity of `row + column`, and every move switches parity. Therefore an undirected grid graph has no odd cycle, and parallel edges do not exist. Once the parent edge is excluded, any detected cycle must contain at least four distinct cells, exactly matching the contract's minimum length.

Marking a cell when it is pushed, rather than when it is later popped, prevents two frontier cells from scheduling it independently and keeps the parent relation unambiguous. If every component finishes without a non-parent visited edge, each component is a tree and no cycle exists.

#### Complexity detail

Every one of the $RC$ cells is marked once, and each cell examines at most four neighbors. The total time is $O(RC)$.

The visited matrix and explicit stack can each hold $O(RC)$ entries. Thus auxiliary space is $O(RC)$, while the iterative traversal also avoids recursion-depth failure on a component containing hundreds of thousands of cells.

#### Alternatives and edge cases

- **Recursive DFS:** the same parent-aware logic is concise, but a large legal component can exceed Python's recursion limit.
- **Breadth-first search:** a queue with parent coordinates provides the same $O(RC)$ guarantees and cycle test.
- **Union-find:** process right and down same-letter edges; an edge whose endpoints are already connected closes a cycle. This is effective but uses a less direct disjoint-set representation.
- **Path-local backtracking:** searching separately from every cell can detect cycles but repeats entire components and becomes superlinear.
- **Smallest cycle:** a same-letter $2 \times 2$ block is a valid four-cell cycle.
- **Two-cell backtracking:** moving to a neighbor and immediately returning is only the parent edge and must not be reported.
- **Diagonal matches:** equal diagonal cells are not adjacent and contribute no edge.
- **Disconnected components:** traversal must restart from every unseen cell because a cycle may occur outside the first component.
- **Early discovery:** returning as soon as one cycle is found is safe because the requested result is Boolean.

</details>
