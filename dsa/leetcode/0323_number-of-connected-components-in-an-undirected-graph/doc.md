# Number of Connected Components in an Undirected Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 323 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) |

## Problem Description
### Goal
Given `n` vertices labeled `0` through $n - 1$ and undirected edges between selected pairs, group vertices that can reach one another through any sequence of edges. Each maximal mutually reachable group is one connected component.

Return the total number of components. An isolated vertex with no incident edge forms a component by itself, while cycles and multiple routes within a group do not increase the count. Edges have no direction, and components may contain any number of vertices. When there are no edges, the answer is `n`; the task returns only the count, not the groups.

### Function Contract
**Inputs**

- `n`: the number of vertices
- `edges`: pairs `[u, v]` representing undirected edges

**Return value**

The number of maximal groups of vertices connected by paths.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1],[1,2],[3,4]]`
- Output: `2`

**Example 2**

- Input: `n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `1`

**Example 3**

- Input: `n = 4, edges = []`
- Output: `4`

### Required Complexity

- **Time:** $O(n + e \alpha(n))$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Begin with one component per vertex**

A disjoint-set union structure represents each current component by a root. Initially every vertex is its own parent, so the component count is `n`. For an edge `[u, v]`, find both roots. If they differ, the edge connects two previously separate components: link one root below the other and decrement the count. If the roots are equal, the edge lies inside an already connected component and changes nothing.

**Keep the representation shallow**

Union by size attaches the smaller tree below the larger tree. Path compression rewrites every parent followed during `find` to point nearer to the root. Together these rules make any sequence of operations nearly linear; no edge requires relabeling every vertex in a component.

For edges `[0,1]` and `[1,2]`, the first union reduces the count from five to four and the second from four to three. Edge `[3,4]` performs one more distinct union, leaving two components. A cycle-closing edge such as `[2,0]` finds the same root on both sides and correctly leaves the count unchanged.

**Successful unions correspond exactly to component merges**

At every point, two vertices have the same root exactly when processed edges connect them by a path. This is true initially because only zero-length self paths exist. An edge between different roots joins all paths in the two sets and the union mirrors that single component merge; an edge within one root adds no new connectivity between components.

Therefore every successful union reduces the true component count by one, and every unsuccessful union preserves it. Starting from `n` singleton components, the maintained count after all edges is exact, including vertices never mentioned by an edge.

#### Complexity detail

Creating the parent and size arrays costs $O(n)$. Across `e` edges, union-by-size with path compression gives $O(e \alpha(n))$ amortized work, where `alpha` is the inverse Ackermann function. Total time is $O(n + e \alpha(n))$, and the two arrays use $O(n)$ space.

#### Alternatives and edge cases

- **Build adjacency lists and run DFS or BFS:** is equally valid in $O(n + e)$ time and $O(n + e)$ space.
- **Relabel every vertex of one component after each edge:** is correct but can take $O(ne)$ time.
- **Subtract once for every edge:** fails on cycles because an edge inside an existing component does not merge components.
- With no edges, the answer is `n`. A single vertex is one component, and cycle-closing edges do not change the count.

</details>
