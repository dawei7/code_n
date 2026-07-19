# Find if Path Exists in Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1971 |
| Difficulty | Easy |
| Topics | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/find-if-path-exists-in-graph/) |

## Problem Description
### Goal
An undirected graph has `n` vertices labeled from `0` through `n - 1`.
Each pair in `edges` connects its two endpoint vertices in both directions.
No edge connects a vertex to itself, and no unordered vertex pair appears more
than once.

Given vertices `source` and `destination`, determine whether some valid path
connects them. A path may contain any number of edges, including zero edges
when the two designated vertices are the same.

### Function Contract
**Inputs**

- `n`: the number of vertices $V$, where $1 \le V \le 2\cdot10^5$.
- `edges`: a list of $E$ unique undirected edges, where
  $0 \le E \le 2\cdot10^5$ and every endpoint is a valid vertex label.
- `source`: the starting vertex.
- `destination`: the target vertex.

**Return value**

- `true` if `destination` is reachable from `source`; otherwise `false`.

### Examples
**Example 1**

- Input: `n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2`
- Output: `true`

**Example 2**

- Input: `n = 6, edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, destination = 5`
- Output: `false`

**Example 3**

- Input: `n = 1, edges = [], source = 0, destination = 0`
- Output: `true`

### Required Complexity
- **Time:** $O(V+E)$
- **Space:** $O(V+E)$

<details>
<summary>Approach</summary>

#### General

**Represent both directions explicitly**

Build an adjacency list with one entry from `u` to `v` and another from `v`
to `u` for every edge `[u, v]`. Begin breadth-first search at `source`, marking
it visited before placing it in the queue.

Repeatedly remove one queued vertex and inspect its neighbors. Enqueue only
neighbors that have not been visited before. Return `true` as soon as
`destination` is removed from the queue. If the queue empties first, return
`false`.

**Why the search answers reachability exactly**

Every vertex placed in the queue is connected to `source`: the source itself
has a zero-edge path, and each later vertex extends the established path to
its predecessor by one real graph edge. Thus reaching `destination` proves a
valid path.

Conversely, consider any path from `source`. Once the search visits one vertex
of that path, it examines the edge to the next vertex and visits that vertex
unless it was already discovered. Repeating this argument along the path
eventually discovers `destination`. Queue exhaustion therefore proves that no
such path exists.

#### Complexity detail

The graph has $V$ vertices and $E$ edges. Building the adjacency lists stores
two entries per edge. Breadth-first search visits each reachable vertex once
and examines each incident adjacency entry once, for $O(V+E)$ time. The
adjacency lists, visited array, and queue use $O(V+E)$ space.

#### Alternatives and edge cases

- **Depth-first search:** An iterative stack gives the same $O(V+E)$ bounds.
  Recursive DFS risks exceeding the language call-stack limit on a long path.
- **Union-find:** Union every edge and compare the final representatives of
  `source` and `destination`. This is effective when many connectivity queries
  share one graph, but a single BFS can stop after exploring only the source
  component.
- **Repeated edge scanning:** Expanding the reachable set by rescanning every
  edge can take $O(VE)$ time on an adversarially ordered chain.
- If `source == destination`, the zero-edge path is valid even when that vertex
  is isolated.
- An empty edge list connects no distinct pair of vertices.
- Because edges are undirected, either endpoint may lead to the other; storing
  only the input orientation would change the graph's semantics.

</details>
