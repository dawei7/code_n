# Minimum Number of Days to Disconnect Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1568 |
| Difficulty | Hard |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) |

## Problem Description
### Goal

A binary grid represents land with `1` and water with `0`. Land cells belong to the same island when they are connected through shared horizontal or vertical sides. The grid is considered disconnected when it contains either no island or more than one island.

On each day, you may choose one land cell and change it to water. Return the minimum number of days required to make the grid disconnected. If it is already disconnected, return `0`; changing at most two cells is always sufficient.

### Function Contract
**Inputs**

- `grid`: An $R \times C$ binary matrix, where $1 \le R,C \le 30$. Each entry is `0` or `1`.

**Return value**

Return the minimum number of land cells that must be changed to water until the number of four-directionally connected islands is not exactly one. The answer is always `0`, `1`, or `2`.

### Examples
**Example 1**

- Input: `grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1,0,1,0]]`
- Output: `0`

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Interpret land as an undirected graph**

Make each land cell a vertex and connect horizontally or vertically adjacent land cells. A depth-first traversal from one land cell reports whether every land vertex is reachable. If no land exists or the traversal reaches fewer vertices than the total land count, the grid already has zero or multiple islands, so the answer is `0`.

A grid containing exactly one land cell needs one day: removing that cell leaves zero islands. For a larger connected island, one removal succeeds precisely when its graph contains an articulation vertex, a vertex whose deletion increases the number of connected components.

**Find articulation cells with discovery and low-link times**

During DFS, assign every cell a discovery time. Its low-link value is the earliest discovery time reachable from its DFS subtree using tree edges and at most one back edge. After visiting a child, propagate the child's low-link value upward.

A non-root cell is an articulation vertex when some child's low-link value is at least the cell's discovery time: that child subtree has no route to an ancestor that avoids the cell. The DFS root is an articulation vertex only when it has more than one DFS-tree child. If either condition occurs, one removal disconnects the island and the answer is `1`.

**Why the remaining answer is two**

If the connected island has at least two cells and no articulation vertex, no single removal works. Two removals are nevertheless sufficient. Consider a land cell on an extreme boundary of the island; it has at most two land neighbors in the four-directional grid. Removing those neighbors isolates that boundary cell, while the two-cell special case becomes empty after removing both cells. Therefore the remaining answer is `2`.

#### Complexity detail

Counting land and the DFS each inspect every cell and a constant number of grid edges, so the total time is $O(RC)$.

The discovery and low-link matrices, along with the DFS stack, can contain $O(RC)$ entries, giving $O(RC)$ auxiliary space.

#### Alternatives and edge cases

- **Try every single removal:** first count islands, then temporarily remove each land cell and recount. This is simpler and remains acceptable for small grids, but its worst-case time is $O((RC)^2)$.
- **Explicit adjacency graph:** map every land cell to an integer vertex and run standard articulation-point DFS. It has the same asymptotic bounds but stores edges that grid coordinates already provide implicitly.
- **No land:** zero islands already satisfies the disconnected definition, so the answer is `0`.
- **Multiple initial islands:** no removal is required, so the answer is `0`.
- **One land cell:** removing it creates zero islands in one day.
- **Two adjacent land cells:** removing either leaves one island, so both must be removed and the answer is `2`.
- **Bridge cell:** a narrow connector is an articulation vertex and yields answer `1`.
- **Dense rectangle or cycle:** these shapes have alternate paths around every single removed cell, so their answer is `2`.
- **Diagonal contact:** diagonal cells are not adjacent and therefore form separate islands unless a horizontal or vertical path joins them.

</details>
