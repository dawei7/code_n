## General

**A component has one minimum mask.** Bitwise AND can only clear bits as more edge weights are included. For a connected component $C$, define

$$
A_C=\mathop{\mathbin{\&}}_{e\in E(C)} w_e,
$$

the bitwise AND of every edge weight in that component. Any walk inside $C$ uses only component edges, so its cost cannot clear a bit that survives in every edge. Consequently, no walk can have cost smaller than $A_C$.

**The all-edge mask is attainable.** Because the component is connected and a walk may repeat vertices and edges, start at the query's source, detour until every component edge has been traversed at least once, and then continue to the target. Repeated weights do not change a bitwise AND. This walk has cost exactly $A_C$, proving that every pair of distinct vertices in the same component has the same minimum cost. Vertices in different components have no walk between them.

**Build connectivity before aggregating weights.** First union the endpoints of every edge with disjoint-set union, using union by size and path compression. After all unions are complete, every edge can be assigned to its final representative. Initialize each component mask to $-1$, whose binary representation acts as all one-bits, and AND in every edge weight. For a query, compare the two representatives: return $-1$ if they differ and the stored component mask otherwise.

The separate aggregation pass is important. If masks were attached to temporary roots while unions were still changing representatives, every merge would also need to transfer both partial masks correctly. Resolving final roots first keeps connectivity and mask accumulation independent.

## Complexity detail

Let $m$ and $q$ be the edge and query counts defined in the function contract. Union by size with path compression gives amortized $O(\alpha(n))$ time per disjoint-set operation, where $\alpha$ is the inverse Ackermann function. The union pass, mask pass, and query pass therefore take $O((n+m+q)\alpha(n))$ time in total. The parent, size, and component-mask arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Depth-first component labeling:** Traverse each component once, assign a component identifier, and accumulate its edge-weight AND. This also takes $O(n+m+q)$ time and $O(n+m)$ space with an adjacency list, but DSU avoids storing a second graph representation.
- **Search separately for every query:** A BFS or DFS can determine connectivity, but even a direct path is not enough because the cheapest walk may detour through unrelated component edges. Exploring the whole component per query can cost $O(q(n+m))$ time.
- **Shortest-path algorithms:** Dijkstra's algorithm assumes an additive path objective and does not model a repeatable bitwise-AND walk. The answer depends on the entire connected component, not a shortest simple path.
- **Parallel edges:** Every parallel edge belongs to the component mask, even if another edge already connects the same endpoints.
- **Zero-weight edge:** If any component edge has weight zero, the minimum cost between every queried pair in that component is zero.
- **Disconnected or isolated vertices:** Distinct vertices with different representatives have no valid walk and return $-1$. Query endpoints are guaranteed to be distinct, so an empty walk needs no special definition.
