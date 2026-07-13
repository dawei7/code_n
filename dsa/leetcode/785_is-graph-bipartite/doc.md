# Is Graph Bipartite?

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 785 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/is-graph-bipartite/) |

## Problem Description

### Goal

Given an undirected graph as an adjacency list, determine whether it is bipartite. A bipartite graph's vertices can be divided into two disjoint groups so that every edge connects a vertex in one group to a vertex in the other.

Return `True` if such a division exists and `False` otherwise. Every vertex must belong to one group, disconnected components may choose their group orientations independently, and no edge may have both endpoints in the same group.

### Function Contract

**Inputs**

- `graph`: an adjacency list where `graph[node]` contains every vertex joined to `node`; vertices are numbered from `0` through `len(graph) - 1`.

**Return value**

- `True` if the graph is bipartite; otherwise `False`.

### Examples

**Example 1**

- Input: `graph = [[1,2,3],[0,2],[0,1,3],[0,2]]`
- Output: `False`
- Explanation: Vertices `0`, `1`, and `2` form an odd cycle.

**Example 2**

- Input: `graph = [[1,3],[0,2],[1,3],[0,2]]`
- Output: `True`
- Explanation: The four-cycle can be split into groups `{0,2}` and `{1,3}`.

**Example 3**

- Input: `graph = [[],[]]`
- Output: `True`
- Explanation: Isolated vertices impose no cross-group conflicts.

### Required Complexity

- **Time:** $O(V + E)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Propagate opposite colors**

Store `0` for an uncolored vertex and `1` or `-1` for the two groups. Choose an uncolored start vertex, assign one color, and breadth-first search its component. Every uncolored neighbor receives the opposite color of the current vertex.

**Detect an impossible constraint**

If an edge reaches a neighbor that already has the current vertex's color, the two-group requirement is contradictory, so return false. Otherwise every processed edge has opposite-colored endpoints.

**Cover disconnected components**

One search may not visit the whole graph. Start another search from each still-uncolored vertex; an isolated vertex simply forms a valid one-vertex component. If all components finish without conflict, the recorded colors themselves provide a valid bipartition. Conversely, a same-color edge arises only after the path constraints force both endpoints into one group, which makes any bipartition impossible.

#### Complexity detail

Each of the `V` vertices enters the queue at most once, and each undirected edge is inspected from both endpoints, for $O(V + E)$ time. The color array and queue use $O(V)$ auxiliary space.

#### Alternatives and edge cases

- **Depth-first coloring:** An iterative or recursive DFS applies the same opposite-color rule with $O(V + E)$ time.
- **Union-find neighbors:** Union all neighbors of a vertex into the opposite set while checking that the vertex is not connected to them; this is less direct but valid.
- **Adjacency-matrix scan:** Testing every possible neighbor for every visited vertex takes $O(V^2)$ time on sparse graphs.
- **Try every partition:** Enumerating all two-group assignments takes exponential time.
- **Disconnected graph:** Every component needs its own initial color.
- **Isolated vertices:** They can belong to either group and never cause a conflict.
- **Odd cycle:** Its alternating constraints return to the start with the wrong color, so the graph is not bipartite.
- **Even cycle or tree:** Alternating colors remain consistent throughout the component.

</details>
