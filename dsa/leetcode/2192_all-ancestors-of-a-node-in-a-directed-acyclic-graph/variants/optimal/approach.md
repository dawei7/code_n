## General

**Reverse the question for every possible ancestor**

Build the outgoing adjacency list. Instead of searching backward separately
from every destination, choose each node `ancestor` as a source and traverse
all nodes reachable from it. Every reached node must include that source in
its ancestor list.

A fresh `seen` array for each source prevents two different paths from
appending the same ancestor twice. The graph is acyclic, but convergence can
still create repeated reachability, so this deduplication remains necessary.

**Obtain sorted lists through processing order**

Process candidate ancestors from $0$ through $n-1$. Whenever traversal from
source $a$ first reaches node $v$, append $a$ to `ancestors[v]`. All earlier
entries were appended by smaller sources, so every list remains ascending
without a final sort.

For a fixed source, graph traversal reaches exactly its descendants: every
stack addition follows an edge from an already reachable node, and every
directed path is eventually explored. Thus the source is appended precisely
to nodes for which it is an ancestor. Repeating this for all sources records
all and only ancestor relationships, while `seen` ensures uniqueness.

## Complexity detail

Let $m=\lvert\texttt{edges}\rvert$. Each of the $n$ traversals initializes an
$n$-entry `seen` array and can inspect all $m$ edges, taking
$O(n^2+nm)$ time. The adjacency lists use $O(n+m)$ space, one traversal uses
$O(n)$ working space, and the returned ancestor lists can contain
$\Theta(n^2)$ values, for $O(n^2+m)$ total space including output.

## Alternatives and edge cases

- **Floyd-Warshall transitive closure:** Maintain reachability for every
  ordered node pair and try every intermediate node. It takes $O(n^3)$ time
  and $O(n^2)$ space.
- **Topological set propagation:** In topological order, merge each node and
  its ancestor set into every outgoing neighbor. It avoids repeated graph
  searches but set unions can still cost $O(nm)$.
- A one-node graph has one empty ancestor list.
- Nodes in disconnected components never become one another's ancestors.
- Multiple paths from one source to one destination contribute that ancestor
  only once.
- Direct predecessors and more distant reachable nodes are both ancestors.
- Input edge order does not determine output order.
