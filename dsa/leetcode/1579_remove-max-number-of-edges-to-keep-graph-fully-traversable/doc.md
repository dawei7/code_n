# Remove Max Number of Edges to Keep Graph Fully Traversable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1579 |
| Difficulty | Hard |
| Topics | Union-Find, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) |

## Problem Description
### Goal

An undirected graph has $N$ nodes numbered from $1$ through $N$. Each edge is represented as `[type, u, v]` and can be used by Alice, Bob, or both: type 1 is Alice-only, type 2 is Bob-only, and type 3 is shared by both users.

Alice and Bob traverse the same node set but may use only the edge types available to them. The graph is fully traversable for a user when that user can travel between every pair of nodes using allowed retained edges.

Remove as many edges as possible while leaving the graph fully traversable for both Alice and Bob. Return that maximum removable count, or `-1` if no retained subset can connect the graph for both users.

### Function Contract
**Inputs**

- `n`: The number of nodes, with nodes labeled $1$ through $N$.
- `edges`: A list of distinct undirected edges `[type, u, v]`, where `type` is $1$, $2$, or $3$ and $1 \le u < v \le N$.
- $1 \le N \le 10^5$, and the edge count is at most $10^5$.

**Return value**

Return the maximum number of removable edges that preserves full traversal for both users, or `-1` when this is impossible.

### Examples
**Example 1**

- Input: `n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]`
- Output: `2`

**Example 2**

- Input: `n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]`
- Output: `0`

**Example 3**

- Input: `n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]`
- Output: `-1`

### Required Complexity

- **Time:** $O(E\alpha(N))$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Use shared connectivity before private connectivity**

Maintain one disjoint-set union structure for Alice and another for Bob. Process every type-3 edge first. When such an edge joins two previously separate components, apply it to both structures and count it as one retained edge. If its endpoints are already connected, it is redundant and may be removed.

A useful shared edge performs connectivity work for both users at the cost of retaining one edge. Replacing it with private edges could require one type-1 and one type-2 edge, so consuming shared edges first can never reduce the number of removable edges.

**Complete each user's graph independently**

After all shared edges, process type 1 only in Alice's structure and type 2 only in Bob's. Retain an exclusive edge exactly when it merges two components; every edge whose endpoints are already connected is removable.

A successful union reduces one user's component count by one. Thus the retained edges form spanning forests throughout the algorithm and never include a cycle. Shared unions maximize the overlap between the two eventual spanning trees, while subsequent exclusive unions add only connections that the corresponding user still needs.

Finally, both component counts must equal one. If either is larger, no allowed edge subset can make that user's graph connected. Otherwise, subtract the number of successful unions from the total edge count to obtain the maximum removable count.

#### Complexity detail

Each of the $E$ edges performs a constant number of disjoint-set operations. Path compression and union by rank give $O(E\alpha(N))$ total time.

The two parent arrays and two rank arrays store $O(N)$ values, so auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Minimum spanning tree framing:** assign shared edges priority and build two overlapping spanning trees. This is equivalent to the two-DSU greedy method without edge weights.
- **Process private edges first:** this can retain separate Alice and Bob edges before discovering that one shared edge could have served both, producing a non-maximum removal count.
- **Connectivity search after every deletion:** greedily trying removals with repeated BFS or DFS can require $O(E(N+E))$ time.
- **No redundant edges:** when exactly the required shared and private connections exist, the answer is zero.
- **Shared spanning tree:** if type-3 edges alone connect all nodes, every remaining edge is removable.
- **One user disconnected:** return `-1` even if the other user's graph is connected.
- **Cycles and parallel endpoint pairs of different types:** an edge is removable whenever it adds no connectivity to its permitted user or users.
- **Input order:** type-3 edges must be logically prioritized regardless of their positions in `edges`.
- **Minimum two-node graph:** one useful shared edge connects both users.

</details>
