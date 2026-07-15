# Reachable Nodes In Subdivided Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 882 |
| Difficulty | Hard |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) |

## Problem Description
### Goal
An undirected original graph has `n` nodes labeled from `0` through `n - 1`. Each entry `[u, v, cnt]` replaces the original edge between `u` and `v` with a chain containing `cnt` new nodes and `cnt + 1` unit-length edges. When `cnt == 0`, the original endpoints remain directly adjacent.

In this subdivided graph, a node is reachable when its shortest distance from node `0` is at most `maxMoves`. Count all reachable original nodes and all reachable new subdivision nodes.

### Function Contract
**Inputs**

- `edges`: $m$ distinct undirected edges `[u, v, cnt]`, where $0 \leq m \leq \min(n(n-1)/2,10^4)$, $0 \leq u < v < n$, and $0 \leq \texttt{cnt} \leq 10^4$.
- `maxMoves`: the maximum allowed distance from node `0`, between $0$ and $10^9$.
- `n`: the number of original nodes, where $1 \leq n \leq 3000$.

**Return value**

Return the number of original and subdivided nodes whose shortest distance from node `0` is at most `maxMoves`.

### Examples
**Example 1**

- Input: `edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3`
- Output: `13`

**Example 2**

- Input: `edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4`
- Output: `23`

**Example 3**

- Input: `edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5`
- Output: `1`

Node `0` is disconnected, so only the starting node is reachable.

### Required Complexity
- **Time:** $O((n+m)\log n)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

**Compress each subdivided chain into one weighted edge**

Traveling from one original endpoint to the other crosses `cnt + 1` unit edges. Build an adjacency list on only the $n$ original nodes with that weight, then run Dijkstra's algorithm from node `0`. Every original node whose finalized distance is at most `maxMoves` contributes one to the answer.

**Count each chain from both reachable ends**

For an original node `u` at distance `dist[u]`, the remaining moves available to enter an incident chain are `max(0, maxMoves - dist[u])`. For edge `[u, v, cnt]`, approaches from its two ends can cover that many new nodes from each side. The number of distinct reachable subdivision nodes on the edge is therefore `min(cnt, from_u + from_v)`.

Dijkstra gives the true shortest distance to every original endpoint because all compressed weights are positive. Any path to a subdivision node must enter its chain through one endpoint, so the remaining-move counts describe exactly the reachable prefix from each side. Adding those prefixes and capping at `cnt` counts their union once even when they overlap.

#### Complexity detail

Building and scanning the adjacency list costs $O(n+m)$. Dijkstra performs $O(n+m)$ heap operations at $O(\log n)$ each, for $O((n+m)\log n)$ time. Distances, the heap, and adjacency entries use $O(n+m)$ space.

#### Alternatives and edge cases

- **Expand every subdivision node:** Ordinary BFS is correct on the expanded graph but can require time and space proportional to $\sum \texttt{cnt}$, which may be enormous.
- **Unweighted BFS on original nodes:** Original edges represent different chain lengths, so treating them equally gives incorrect distances.
- **Bellman-Ford:** It handles the positive weights but costs $O(nm)$ time.
- **Zero subdivisions:** The edge contributes no new nodes but still connects its endpoints with weight one.
- **Partial chain reach:** Reaching some new nodes does not imply reaching the opposite original endpoint.
- **Approach from both ends:** Cap their combined coverage at `cnt` to avoid double-counting overlap.
- **Disconnected node zero:** Node `0` itself is always reachable even when no edge is incident to it.

</details>
