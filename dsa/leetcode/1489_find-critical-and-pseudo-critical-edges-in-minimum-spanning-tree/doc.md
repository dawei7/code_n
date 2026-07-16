# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1489 |
| Difficulty | Hard |
| Topics | Union-Find, Graph Theory, Sorting, Minimum Spanning Tree, Strongly Connected Component |
| Official Link | [LeetCode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) |

## Problem Description
### Goal

A connected, weighted, undirected graph has `n` vertices numbered from `0` through `n - 1`. Each `edges[i] = [a, b, weight]` describes one bidirectional edge, and index `i` is that edge's identity in the requested output. A minimum spanning tree (MST) connects every vertex without a cycle and has the minimum possible total weight.

Classify the original edge indices. An edge is **critical** when removing it makes the best possible spanning-tree weight larger, so it belongs to every MST. An edge is **pseudo-critical** when it can belong to at least one MST but does not belong to all MSTs. Return `[critical, pseudo_critical]`; indices within either list may be in any order.

### Function Contract
**Inputs**

Let $V=n$ and let $E$ be the number of edges.

- `n`: the vertex count, with $2 \le V \le 100$.
- `edges`: an array with
  $1 \le E \le \min\left(200, V(V-1)/2\right)$.
- Every edge is `[a, b, weight]` with
  $0 \le a < b < V$ and $1 \le \texttt{weight} \le 1000$.
- Every unordered endpoint pair is distinct.
- The graph is connected.

**Return value**

Return two lists:

1. indices of edges that occur in every MST;
2. indices of edges that occur in at least one, but not every, MST.

An edge that occurs in no MST belongs to neither list. Index order inside each category is unrestricted, but the two category positions are fixed.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]`
- Output: `[[0,1],[2,3,4,5]]`
- Explanation: Edges zero and one are forced in every optimum. Each of edges two through five can be selected in some optimum, while the heavier final edge cannot.

**Example 2**

- Input: `n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]`
- Output: `[[],[0,1,2,3]]`
- Explanation: Removing any one edge from the equal-weight cycle gives an MST, so every edge is optional but eligible.

### Required Complexity
- **Time:** $O(E \log E)$
- **Space:** $O(V + E)$

<details>
<summary>Approach</summary>

#### General

**Preserving original edge identity while sorting**

Attach each edge's input index, then sort all augmented edges by weight. Kruskal's algorithm decides among edges of the same weight only after all strictly lighter connections are fixed, so classification must process equal-weight edges as one batch rather than unioning them one by one.

Maintain a disjoint-set union structure representing connectivity through weights strictly below the current batch.

**Contracting components formed by cheaper edges**

For a current edge `(u, v)`, find its lower-weight components `ru` and `rv`. If `ru == rv`, a strictly cheaper path already connects its endpoints. Adding this edge would create a cycle containing a heavier edge, so it cannot occur in any MST and belongs to neither output category.

Otherwise, add an edge between `ru` and `rv` in a temporary undirected multigraph. Keep its original input index as the temporary edge identifier. Different original endpoint pairs can become parallel edges after their cheaper components are contracted.

**Finding bridges within one weight batch**

Run Tarjan's bridge algorithm on every connected part of the temporary multigraph. Store a discovery time and low-link value for each contracted vertex. A DFS tree edge to child `v` is a bridge exactly when

$$
\texttt{low[v]} > \texttt{discovery[parent]}.
$$

Skip only the exact parent edge identifier, not every edge leading to the parent vertex. That distinction is essential for parallel edges: the second parallel edge is a back edge, lowers the low-link value, and proves that neither parallel edge is forced.

**Why temporary bridges are critical**

Before the current weight, each contracted vertex is already internally connected as cheaply as possible. If a temporary edge is a bridge, removing it separates the temporary component into two parts with no other current-weight connection. Any spanning tree must then reconnect those parts using a heavier edge, increasing the optimum weight. The original edge is therefore present in every MST and is critical.

**Why non-bridge candidates are pseudo-critical**

A candidate that is not a bridge lies on a cycle of current-weight edges in the contracted multigraph. A spanning forest for that multigraph can include the candidate and omit another edge on the cycle without changing total weight. It can also omit the candidate in a different forest. Extending either choice with Kruskal's later weight groups yields an MST, so the edge occurs in some but not all MSTs and is pseudo-critical.

**Advancing the global Kruskal state**

Only after every edge in the weight group has been classified, union all of the group's endpoints in the global DSU. This records connectivity available to heavier groups without letting arbitrary order inside the current group distort its bridge structure.

Finally, sort the two index lists for deterministic app output. The semantic validator keeps the critical and pseudo-critical categories in place while accepting any index order within each.

**Why every edge is classified exactly once**

An edge whose endpoints were already joined by cheaper weights is in no MST. Every remaining edge appears once in exactly one temporary graph. Tarjan marks it either as a bridge or non-bridge, which correspond respectively to critical and pseudo-critical status. These cases are disjoint and exhaust all original edges.

#### Complexity detail

Sorting costs $O(E \log E)$. Across all weight groups, each edge appears in at most one temporary multigraph, each temporary vertex-edge incidence is traversed a constant number of times, and DSU operations take near-constant amortized time. The total is $O(E \log E)$ time. The DSU, grouped edges, temporary adjacency lists, DFS state, and output require $O(V + E)$ space.

#### Alternatives and edge cases

- **Exclude and force every edge with Kruskal:** Compute the baseline MST, rerun Kruskal without each edge to test criticality, and force each remaining edge to test eligibility. It is straightforward and correct but takes $O(E^2 \alpha(V))$ time after sorting.
- **Enumerate spanning trees:** Comparing all spanning trees gives the definitions directly but is exponential and infeasible.
- **One arbitrary MST:** Membership in one MST cannot distinguish forced edges from alternatives or identify eligible edges omitted from that particular tree.
- **Unique MST:** Every edge in that MST is critical, and no edge is pseudo-critical.
- **Equal-weight cycle:** Its edges are pseudo-critical because any one can be omitted.
- **Temporary bridge:** It is critical even when other equal-weight cycles exist elsewhere in the graph.
- **Cheaper internal path:** An edge whose contracted endpoints coincide cannot occur in an MST.
- **Parallel contracted edges:** Neither is a bridge merely because they share endpoints; edge identifiers must distinguish them during DFS.
- **Heavy unused edge:** It belongs to neither list when lighter edges already connect its endpoints.
- **Original indices:** Sorting for Kruskal must never replace the identities requested in the output.
- **Category order:** The first result list is critical and the second is pseudo-critical; only order within a list is arbitrary.
- **Connected input:** A spanning tree is guaranteed to exist, so no disconnected-graph fallback is required.

</details>
