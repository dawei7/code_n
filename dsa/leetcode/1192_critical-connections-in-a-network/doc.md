# Critical Connections in a Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1192 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Graph Theory, Biconnected Component |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/critical-connections-in-a-network/) |

## Problem Description

### Goal

A network contains `n` servers numbered from `0` through `n - 1`. Each entry `connections[i] = [a_i,b_i]` represents an undirected server-to-server connection between its two endpoints. The network is initially connected, so every server can reach every other server through some direct or indirect route.

A critical connection is an edge whose removal makes at least one server unable to reach another server. Return every critical connection in any order. Either endpoint order is accepted for an edge because each connection is undirected.

### Function Contract

**Inputs**

- `n`: The number of servers, where $2\le n\le10^5$.
- `connections`: A list of $m$ distinct undirected edges, where $n-1\le m\le10^5$. Each edge has endpoints `a_i` and `b_i` satisfying $0\le a_i,b_i<n$ and $a_i\ne b_i$.

**Return value**

- All edges whose individual removal disconnects the network, in any list order and with either endpoint order.

### Examples

**Example 1**

- Input: `n = 4`, `connections = [[0,1],[1,2],[2,0],[1,3]]`
- Output: `[[1,3]]`

The first three servers lie on a cycle, while server `3` has no alternate route.

**Example 2**

- Input: `n = 2`, `connections = [[0,1]]`
- Output: `[[0,1]]`

The network's only edge is necessarily critical.

### Required Complexity

- **Time:** $O(n+m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Record discovery ancestry.** Build an adjacency list and run depth-first search from server `0`, which reaches the entire connected network. Assign `discovery[u]` when `u` is first visited. For each server, maintain `low[u]`, the smallest discovery time reachable from its DFS subtree by following tree edges and then at most one non-parent edge to an already discovered vertex.

**Propagate alternate routes upward.** After recursively exploring a previously unseen neighbor `v`, update `low[u] = min(low[u], low[v])`. An edge to an already discovered neighbor other than the DFS parent is a back edge, so update with that neighbor's discovery time instead. Ignoring only the parent edge prevents the immediate undirected return from being mistaken for an alternate route.

**Identify exactly the bridges.** For a DFS tree edge from `u` to `v`, the condition $\textit{low}[v]>\textit{discovery}[u]$ means no vertex in `v`'s subtree can reach `u` or an ancestor without that edge. Removing it therefore separates the subtree, so it is critical. If the inequality does not hold, a back edge supplies another route around the tree edge, and removing the edge cannot disconnect that subtree from the rest of the network.

#### Complexity detail

Let $m$ be the number of connections. Building the adjacency list takes $O(n+m)$ space and $O(m)$ time. DFS visits each server once and examines each undirected edge from both endpoints, for $O(n+m)$ total time. The adjacency list, discovery and low arrays, result, and recursion stack occupy $O(n+m)$ space.

#### Alternatives and edge cases

- **Remove every edge and retest connectivity:** A BFS or DFS after each removal is correct but costs $O(m(n+m))$ time.
- **Disjoint-set union per omitted edge:** Rebuilding connectivity for every candidate has the same prohibitive repeated-work pattern.
- **Single edge:** With two servers and one connection, that connection is a bridge.
- **Tree network:** Every edge is critical because a tree has no alternate route around any edge.
- **Cycle:** No edge on a cycle is critical; the remaining direction around the cycle preserves connectivity.
- **Cycle with a tail:** Cycle edges are protected by alternate routes, while every edge in the attached acyclic tail is critical.
- **Output order:** DFS discovery order need not match the input order, and either endpoint orientation represents the same undirected critical connection.
- **Recursion depth:** A chain may contain $10^5$ servers, so recursive implementations must provide enough call-stack capacity or use an explicit stack.

</details>
