# Number of Restricted Paths From First to Last Node

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) |
| Frontend ID | 1786 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An undirected, weighted, connected graph has `n` nodes labeled from `1` through `n`. Each entry `[u, v, weight]` in `edges` represents one positive-weight edge between `u` and `v`, and no node pair has more than one edge.

For any node `x`, define its distance to the last node as the minimum total edge weight of a path from `x` to node `n`. A path `[z_0, z_1, ..., z_k]` from node `1` to node `n` is restricted when this shortest-distance value strictly decreases at every step:

$$
\operatorname{dist}(z_i,n) > \operatorname{dist}(z_{i+1},n).
$$

Count all restricted paths from node `1` to node `n`, and return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: the number of nodes, where $1 \le n \le 2\cdot 10^4$.
- `edges`: between $n-1$ and $4\cdot 10^4$ entries `[u, v, weight]`, where endpoints are distinct labels from `1` through `n` and $1 \le \texttt{weight} \le 10^5$.
- The graph is connected, undirected, and simple.

Let $E=\lvert\texttt{edges}\rvert$.

**Return value**

- Return the number of paths from node `1` to node `n` whose distance-to-`n` values strictly decrease along every edge, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]`
- Output: `3`

The restricted paths are `1 → 2 → 5`, `1 → 2 → 3 → 5`, and `1 → 3 → 5`.

**Example 2**

- Input: `n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]`
- Output: `1`

Only `1 → 3 → 7` strictly descends the shortest-distance values.

**Example 3**

- Input: `n = 3, edges = [[1,2,5],[2,3,5],[1,3,20]]`
- Output: `2`

Both `1 → 2 → 3` and the heavier direct path `1 → 3` are restricted. A restricted path need not itself be a shortest path.

### Required Complexity

- **Time:** $O((n+E)\log n)$
- **Space:** $O(n+E)$

<details>
<summary>Approach</summary>

#### General

**Compute the ordering key from the destination**

The restriction compares every visited node's shortest distance to node `n`, so run Dijkstra's algorithm from `n`. Positive edge weights guarantee that the min-heap finalizes correct distances. Store the undirected graph as adjacency lists.

Running from the destination computes all required values in one shortest-path pass. Running separately from each node would repeat work and is unnecessary.

**Orient the graph by strictly decreasing distance**

Once distances are known, conceptually direct every edge from its larger-distance endpoint toward its smaller-distance endpoint. Ignore edges whose endpoint distances are equal. Along every directed edge the distance strictly decreases, so a directed cycle is impossible.

This turns the restricted-path relation into a directed acyclic graph, even though the original graph is undirected and may contain cycles.

**Count paths in distance order**

Set the number of ways at node `n` to one. Process nodes from smallest to largest distance. When processing `node`, its count already represents every restricted suffix from that node to `n`. For each neighbor with a larger distance, add `ways[node]` to that neighbor because taking the edge from the neighbor to `node` is a valid first descending step.

Apply the modulus after every addition. By increasing-distance order, all smaller-distance successors of a node have been completed before that node receives its final count.

Dijkstra supplies the exact values used by the definition. The orientation retains exactly those edge traversals that satisfy the strict inequality, and the dynamic program counts every directed path to `n` once by its first edge. Therefore `ways[1]` is precisely the number of restricted paths.

#### Complexity detail

Building adjacency lists takes $O(n+E)$ space and $O(E)$ time. Dijkstra with a binary heap takes $O((n+E)\log n)$ time. Sorting the nodes by distance costs $O(n\log n)$, and the dynamic program inspects both directions of every edge in $O(n+E)$ time. The total remains $O((n+E)\log n)$.

The graph, distance array, heap, ordering, and path counts use $O(n+E)$ space.

#### Alternatives and edge cases

- **Memoized depth-first search after Dijkstra:** Recursing only to smaller-distance neighbors computes the same DAG recurrence in $O(n+E)$ after distances are known, but a long restricted chain can exceed a language's recursion limit.
- **Integrate counting with Dijkstra finalization:** Counts can be propagated in finalized-distance order, but separating shortest paths from the DAG recurrence makes stale heap entries and equal-distance edges easier to handle correctly.
- **Bellman–Ford distances:** Positive weights do not require repeated relaxation; this increases shortest-path work to $O(nE)$.
- **Path enumeration:** Explicitly constructing every restricted path can be exponential even though the dynamic program has only one state per node.
- **Restricted is not shortest:** A traversed edge may be heavier than an alternative route; only the endpoint distance values must strictly decrease.
- **Equal distances:** An edge between equal-distance nodes cannot be used in either direction because the comparison is strict.
- **Single node:** When `n = 1`, the empty path from node `1` to itself contributes one.
- **Large path counts:** Reduce each accumulated count modulo $10^9+7$.

</details>
