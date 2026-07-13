# Graph Valid Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 261 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/graph-valid-tree/) |

## Problem Description
### Goal
Given `n` labeled nodes from `0` through $n - 1$ and a collection of undirected edges, determine whether the resulting graph is one valid tree. A tree connects every node while containing no cycle or redundant route between two nodes.

Return `True` only when all `n` nodes belong to a single connected component and the edges are acyclic. A disconnected forest is not a tree even if each component is acyclic, and a connected graph with an extra edge is not a tree because it contains a cycle. Isolated nodes count, so the graph with one node and no edges is valid.

### Function Contract
**Inputs**

- `n`: the number of nodes
- `edges`: undirected endpoint pairs

**Return value**

`True` exactly when the graph is connected and contains no cycle.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]`
- Output: `true`

**Example 2**

- Input: `n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`
- Output: `false`

**Example 3**

- Input: `n = 1, edges = []`
- Output: `true`

### Required Complexity

- **Time:** $O(n + e)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The edge count reduces the remaining question to cycles**

An undirected tree on `n` nodes must have exactly $n - 1$ edges. Reject any other count, then use disjoint sets to ensure those edges do not create a cycle.

Each disjoint-set root represents one connected component of all edges processed so far. Unioning different roots merges components; encountering equal roots means the new edge closes a cycle.

**Successful unions prove both acyclicity and connectivity**

An edge whose endpoints already share a root closes a path into a cycle, so rejecting it is necessary. If all $n - 1$ edges instead join different components, each union reduces the component count by one: starting from `n`, exactly $n - 1$ successful unions leave one component. The graph is therefore connected and acyclic, which is precisely a tree.

#### Complexity detail

Union by size with path compression takes $O((n + e) \alpha(n))$, conventionally written $O(n + e)$. Parent and size arrays use $O(n)$ space.

#### Alternatives and edge cases

- **DFS/BFS:** also achieves $O(n + e)$ by checking connectivity while ignoring each node's parent edge.
- **Search for a path before every insertion:** can take $O(ne)$.
- One isolated node is a tree; zero nodes are outside the native constraints.

</details>
