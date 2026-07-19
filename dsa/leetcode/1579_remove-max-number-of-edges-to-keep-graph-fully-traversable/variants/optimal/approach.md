## General
**Use shared connectivity before private connectivity**

Maintain one disjoint-set union structure for Alice and another for Bob. Process every type-3 edge first. When such an edge joins two previously separate components, apply it to both structures and count it as one retained edge. If its endpoints are already connected, it is redundant and may be removed.

A useful shared edge performs connectivity work for both users at the cost of retaining one edge. Replacing it with private edges could require one type-1 and one type-2 edge, so consuming shared edges first can never reduce the number of removable edges.

**Complete each user's graph independently**

After all shared edges, process type 1 only in Alice's structure and type 2 only in Bob's. Retain an exclusive edge exactly when it merges two components; every edge whose endpoints are already connected is removable.

A successful union reduces one user's component count by one. Thus the retained edges form spanning forests throughout the algorithm and never include a cycle. Shared unions maximize the overlap between the two eventual spanning trees, while subsequent exclusive unions add only connections that the corresponding user still needs.

Finally, both component counts must equal one. If either is larger, no allowed edge subset can make that user's graph connected. Otherwise, subtract the number of successful unions from the total edge count to obtain the maximum removable count.

## Complexity detail
Each of the $E$ edges performs a constant number of disjoint-set operations. Path compression and union by rank give $O(E\alpha(N))$ total time.

The two parent arrays and two rank arrays store $O(N)$ values, so auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Minimum spanning tree framing:** assign shared edges priority and build two overlapping spanning trees. This is equivalent to the two-DSU greedy method without edge weights.
- **Process private edges first:** this can retain separate Alice and Bob edges before discovering that one shared edge could have served both, producing a non-maximum removal count.
- **Connectivity search after every deletion:** greedily trying removals with repeated BFS or DFS can require $O(E(N+E))$ time.
- **No redundant edges:** when exactly the required shared and private connections exist, the answer is zero.
- **Shared spanning tree:** if type-3 edges alone connect all nodes, every remaining edge is removable.
- **One user disconnected:** return `-1` even if the other user's graph is connected.
- **Cycles and parallel endpoint pairs of different types:** an edge is removable whenever it adds no connectivity to its permitted user or users.
- **Input order:** type-3 edges must be logically prioritized regardless of their positions in `edges`.
- **Minimum two-node graph:** one useful shared edge connects both users.
