## General
**View each limit as a connectivity snapshot**

For a fixed limit, discard every edge whose distance is not strictly smaller. The query is then an ordinary connectivity question in the remaining undirected graph. As the limit increases, edges are only added; connected components merge and never split. This monotonicity allows all queries to share one incremental graph sweep.

Sort the edges by distance. Attach each query's original index and sort queries by limit. Maintain a disjoint-set union structure initially containing $n$ singleton components and an edge pointer. Before answering a query with limit `limit`, union every still-unprocessed edge satisfying `distance < limit`. Do not union an equal-distance edge yet.

At that moment, the disjoint-set components are exactly the connected components of the graph containing all and only edges below the current limit. The query is true precisely when `find(p) == find(q)`. Store that boolean at the query's original index so sorting does not reorder the returned answers.

**Keep component operations nearly constant**

Path compression shortens parent chains during `find`, and union by component size attaches the smaller tree beneath the larger. These rules give amortized $O(\alpha(n))$ time per operation. Each edge is unioned at most once across the entire sweep rather than reconsidered for each query.

The component invariant follows initially from the empty eligible graph. Adding the next eligible edge merges exactly the two components that this edge connects, preserving the invariant. Therefore every saved answer matches the strict-threshold graph for its query.

## Complexity detail
Sorting the $E$ edges and $Q$ indexed queries takes $O(E\log E+Q\log Q)$ time. At most $E$ unions and $2Q$ query finds add $O((E+Q)\alpha(n))$, which is within $O((E+Q)\log(E+Q))$. Parents and sizes use $O(n)$ space, while sorted edge and indexed-query lists plus answers use $O(E+Q)$.

## Alternatives and edge cases
- **Graph search per query:** filtering edges and running BFS or DFS independently is straightforward but can take $O(Q(n+E))$ time.
- **Minimum spanning forest:** the maximum edge on a minimax path can answer queries after additional tree preprocessing, but the offline threshold sweep is simpler for a static query batch.
- **Union equal-weight edges too early:** this changes the strict `< limit` rule into `<= limit` and produces incorrect boundary answers.
- **Parallel edges:** each edge is processed independently; a lighter parallel edge may connect endpoints under a limit that excludes the heavier one.
- **Disconnected graph:** vertices in distinct final components remain false for every limit.
- **Query order:** sorting is internal only; answers must be written back by original index.
- **Repeated limits:** all queries at one limit observe the same component snapshot, and no equal-weight edge is eligible for any of them.
