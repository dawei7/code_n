# Largest Color Value in a Directed Graph

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/) |
| Frontend ID | 1857 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A directed graph has nodes numbered from 0 through $n-1$. The character `colors[i]` is the lowercase English letter assigned to node `i`, and each pair `[a, b]` in `edges` creates a directed edge from `a` to `b`.

A valid path follows directed edges and may contain one or more nodes. Its color value is the greatest frequency of any single color among the nodes on that path. Return the largest color value achieved by any valid path in the graph. If the graph contains any directed cycle, including one in a disconnected component, return `-1` instead.

### Function Contract

**Inputs**

- `colors`: a lowercase string of length $n$, one color per node.
- `edges`: a list of $m$ directed pairs `[source, target]`.
- $1\le n\le10^5$ and $0\le m\le10^5$.
- Every edge endpoint lies between 0 and $n-1$.

**Return value**

- For an acyclic graph, return the maximum number of occurrences of one color along any directed path.
- Return `-1` if any directed cycle exists.

### Examples

**Example 1**

- Input: `colors = "abaca"`, `edges = [[0, 1], [0, 2], [2, 3], [3, 4]]`
- Output: `3`

Path `0 -> 2 -> 3 -> 4` contains three nodes colored `a`.

**Example 2**

- Input: `colors = "a"`, `edges = [[0, 0]]`
- Output: `-1`

**Example 3**

- Input: `colors = "abc"`, `edges = []`
- Output: `1`

### Required Complexity

- **Time:** $O(26(n+m))$
- **Space:** $O(26n+m)$

<details>
<summary>Approach</summary>

#### General

Build an adjacency list and each node's indegree. Kahn's topological algorithm begins with every zero-indegree node and processes a node only after all its predecessors have been processed.

For each node, store 26 values. Entry `counts[node][c]` is the greatest number of color `c` nodes on any processed path ending just before counting this node. When the node leaves the queue, increment its own color entry exactly once. Then propagate the componentwise maximum of its vector into every outgoing neighbor.

Because a neighbor reaches indegree zero only after all incoming paths have propagated, its vector contains the best possible predecessor count for every color. Adding its own color therefore produces the best counts for all paths ending there. The maximum entry encountered across all processed nodes is the largest path color value.

Count how many nodes leave the queue. A directed acyclic graph admits a topological order containing all $n$ nodes. If fewer are processed, the remaining positive-indegree nodes belong to or depend on a cycle, so the contract requires `-1`.

#### Complexity detail

Building the graph takes $O(n+m)$ time and space. Every node and edge is processed once, and each edge propagation compares 26 color counts, giving $O(26(n+m))$ time. The adjacency lists use $O(m)$ space and the color-count table uses $O(26n)$.

#### Alternatives and edge cases

- **Depth-first search with memoization:** Can compute the same color vectors and detect recursion-stack cycles, but deep graphs risk recursion limits.
- **Restart DFS from every node:** Correct without memoization on a DAG but may revisit a long suffix $O(n^2)$ times.
- **Disconnected cycle:** Any cycle forces `-1`, even if another component has a valid high-value path.
- **Self-loop:** A one-node loop is a directed cycle.
- **Multiple predecessors:** Merge vectors componentwise; one predecessor may be best for one color and another for a different color.
- **Isolated nodes:** Each is a one-node path with color value 1.
- **Repeated colors:** Counts accumulate only along a single directed path, not across separate branches.
- **All nodes processed:** This condition is the cycle certificate for Kahn's algorithm.

</details>
