## General
**Reject an insufficient cable supply**

Any connected graph on `n` vertices needs at least $n-1$ edges. Moving a cable does not change the total, so when `len(connections) < n - 1`, connection is impossible and the answer is `-1`.

**Count components with disjoint sets**

Otherwise, initialize one disjoint-set component per computer. For every cable `[u, v]`, unite the components containing its endpoints. Union by size and path compression keep these operations nearly constant in amortized time. Each successful union reduces the component count by one; cables whose endpoints already share a root are redundant.

If $k$ components remain, at least $k-1$ moves are necessary because one new cable can merge at most two components. The initial edge-count check also guarantees enough redundant cables: a forest spanning the existing components uses $n-k$ cables, leaving at least $(n-1)-(n-k)=k-1$ cables available to relocate. Thus exactly $k-1$ operations are both necessary and achievable.

## Complexity detail
Initializing the disjoint-set arrays costs $O(n)$. Processing $m$ cables with union by size and path compression costs $O(m\alpha(n))$, for $O((n+m)\alpha(n))$ total time. The parent and size arrays use $O(n)$ space.

## Alternatives and edge cases
- **DFS or BFS:** Build an adjacency list and count connected components in $O(n+m)$ time and space; this is equally suitable but stores both directions of every cable.
- **Repeated reachability searches:** Recomputing a traversal from every computer can take $O(n(n+m))$ time and repeats the same component work.
- **Too few cables:** Return `-1` immediately even if most computers already belong to one large component.
- **Redundant cycles:** A cable on a cycle can be removed without disconnecting its current component and is available for relocation.
- **Already connected:** One remaining component requires 0 operations.
- **Isolated computers:** Each isolated vertex is its own component and must be joined once, provided enough redundant cables exist elsewhere.
