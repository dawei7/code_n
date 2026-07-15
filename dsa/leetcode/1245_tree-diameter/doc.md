# Tree Diameter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1245 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-diameter/) |

## Problem Description

### Goal

You are given `edges`, the undirected edges of a tree whose vertices are labeled with consecutive integers. A tree is connected and has no cycle, so exactly one simple path connects every pair of vertices.

Return the tree's diameter: the number of edges in its longest simple path. Either endpoint may appear anywhere in the input, and edge order has no significance. A tree consisting of one vertex has no edges and therefore has diameter zero.

### Function Contract

**Inputs**

- `edges`: A list of $n-1$ undirected pairs `[u, v]` forming one tree on $n$ vertices, with up to $10^4$ edges.

**Return value**

- The number of edges in the longest simple path between any two vertices.

### Examples

**Example 1**

- Input: `edges = [[0,1],[0,2]]`
- Output: `2`

The path from vertex `1` through `0` to `2` has two edges.

**Example 2**

- Input: `edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]`
- Output: `4`

One longest path runs from `3` through `2`, `1`, and `4` to `5`.

**Example 3**

- Input: `edges = []`
- Output: `0`

The single-vertex tree has no path edge.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Build undirected adjacency lists.** Add both directions for every edge so a breadth-first traversal can move through the tree. If `edges` is empty, return zero immediately.

**Find one diameter endpoint.** Run BFS from any vertex, such as `0`, and remember a farthest reached vertex `a`. In a tree, a vertex farthest from an arbitrary start is an endpoint of some diameter: if a longest path extended farther in the relevant direction, the unique paths would contradict `a`'s maximal distance.

**Measure from that endpoint.** Run BFS again from `a`. The greatest distance discovered is the distance to an opposite diameter endpoint and therefore equals the diameter. BFS distances count traversed edges, exactly matching the requested unit. Each traversal visits every vertex and edge once.

#### Complexity detail

Building adjacency lists takes $O(n)$ time and space because a tree has $n-1$ edges. Two BFS traversals each take $O(n)$ time and use an $O(n)$ distance array and queue, so the total bounds remain $O(n)$ time and $O(n)$ space.

#### Alternatives and edge cases

- **BFS from every vertex:** It finds every eccentricity and is correct, but takes $O(n^2)$ time on a tree.
- **One postorder depth-first search:** Combining the two greatest child depths at each vertex also runs in $O(n)$ time, but recursive implementations can exceed the call stack on a long path.
- **Repeated leaf removal:** Peeling layers locates the tree center, from which the diameter can be derived, though two traversals are more direct.
- **Single vertex:** With no edges, the diameter is `0`.
- **Path tree:** The two leaves are diameter endpoints and the result is $n-1$.
- **Star tree:** Any two leaves form a diameter of `2` when at least two leaves exist.
- **Input order:** Undirected adjacency makes edge orientation and ordering irrelevant.

</details>
