## General
**Maintain the components formed by earlier edges**

Create one disjoint-set component per node. For each input edge `[u, v]`, find the representative of each endpoint. If they differ, union the components because this edge safely connects two previously separate trees.

**The first failed union closes the unique cycle**

If both endpoints already have the same representative, earlier edges already contain a path between them. Adding `[u, v]` closes a cycle, so this edge can be removed without disconnecting the graph. Return it instead of performing a union.

**Why this edge satisfies the last-occurrence rule**

The original graph has exactly one extra edge and therefore exactly one cycle. Before the scan reaches the last input edge belonging to that cycle, the cycle edges seen so far form only a path and every union succeeds. When the final cycle edge arrives, its endpoints are already connected and the union fails. That edge is precisely the latest cycle edge in input order, which is the required choice among all removable cycle edges.

**Keep representative operations shallow**

Path compression rewrites find paths toward their roots, and union by size attaches the smaller tree below the larger. These rules preserve component membership while making a sequence of operations nearly linear.

## Complexity detail
There are `N` edges and at most `N` labels. With path compression and union by size, each disjoint-set operation costs amortized $O(\alpha(N))$, giving $O(N \alpha(N))$ time. Parent and size arrays use $O(N)$ space.

## Alternatives and edge cases
- **DFS before each insertion:** search the current adjacency graph to see whether the endpoints are already connected; it is correct but can take $O(N^2)$ total time.
- **Remove each candidate and test tree properties:** follows the output definition, but repeatedly rebuilding and traversing the graph is quadratic or worse.
- **One DFS with parent tracking:** can identify the cycle in $O(N)$ time, then select its last input edge; it needs extra bookkeeping to recover edge order.
- The returned endpoints preserve their order from the input edge.
- An edge between distant nodes can be redundant even when neither endpoint has appeared recently.
- Labels are 1-based, so disjoint-set arrays need an unused index zero or explicit offset conversion.
