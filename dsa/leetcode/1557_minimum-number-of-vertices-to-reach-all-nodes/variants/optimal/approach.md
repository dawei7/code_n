## General

**Identify vertices that nothing else can enter**

A vertex with in-degree zero has no incoming directed edge. No path starting at a different vertex can reach it, because the final step of any such path would have to be an incoming edge.

Therefore every zero-in-degree vertex is mandatory in any starting set that reaches the whole graph. Omitting even one would leave that vertex unreachable.

The exact source counts which vertices appear as edge targets. `Counter(t for _, t in edges)` ignores each source endpoint and records one occurrence for every incoming edge at target `t`.

The actual numeric in-degree is more information than the final filter needs, but `Counter` provides it compactly.

**Use Counter's missing-key behavior**

For each vertex `i` from zero through `n-1`, the list comprehension checks `cnt[i] == 0`.

A `Counter` returns zero for a key that was never inserted. Thus a vertex that never occurs as a target is recognized without preinitializing all vertices in the counter.

Vertices with one or many incoming edges both fail the zero test and are excluded.

The returned order is increasing vertex number because `range(n)` is scanned in that order. The problem accepts any order, so this deterministic ordering is valid but not required.

**Why every selected vertex is necessary**

Take a returned vertex `v`. Its in-degree is zero.

If a path from another vertex reached `v`, that path would contain a last directed edge `u -> v`. Such an edge would give `v` positive in-degree, contradicting the selection rule.

The only way to make `v` reachable from the chosen set is therefore to choose `v` itself. Every valid solution must contain every returned vertex.

This proves a lower bound: no solution can use fewer starting vertices than the number of zero-in-degree vertices.

**Why zero-in-degree vertices reach everything in a DAG**

Necessity alone is not enough; the selected set must also cover every positive-in-degree vertex.

Take any vertex `x`. If its in-degree is zero, it is already selected. Otherwise, choose one predecessor that has an edge into `x`. If that predecessor has positive in-degree, choose one of its predecessors and continue moving backward.

The graph is finite and acyclic. The backward walk cannot continue forever and cannot revisit a vertex, because a revisit would create a directed cycle. It must eventually stop at a vertex with no predecessor, meaning in-degree zero.

Reversing this predecessor chain gives a directed path from that selected source to `x`. Hence every vertex is reachable from at least one returned vertex.

This is exactly where the directed-acyclic-graph guarantee matters. In a directed cycle, every vertex can have positive in-degree even though one starting vertex is still needed.

**Minimality and uniqueness**

The returned zero-in-degree vertices are sufficient by the backward-chain argument. They are all mandatory by the no-incoming-edge argument.

Therefore the set is minimum, and every minimum solution must contain exactly those vertices. This also explains the statement's unique-solution guarantee.

No graph traversal is needed because acyclicity lets local in-degree information characterize the global starting set completely.

**Tracing the first example**

Edges target vertices one, two, five, four, and two again. The counter has positive values for one, two, four, and five.

Vertices zero and three never occur as targets, so they have counter value zero and are returned.

From zero, directed paths reach one, two, and five. From three, paths reach four, then two and five. Together the selected sources cover all six vertices.

**Why sources of outgoing edges are not counted**

The question is not asking which vertices can reach another vertex directly. It asks which vertices cannot themselves be reached from elsewhere.

Only target appearances determine incoming degree. A vertex may have many outgoing edges and still be mandatory if it has no incoming edge. Conversely, a sink with no outgoing edges is not necessarily a starting vertex if an incoming path reaches it.

**No need for exact indegree magnitudes**

The filter distinguishes zero from positive. A Boolean array marking target appearances would produce the same result and can have more predictable storage.

The source's `Counter` still runs in linear expected time and makes the meaning close to the graph term “in-degree.”

## Complexity detail

Let $N$ be vertex count and $M$ be edge count. Building the counter examines each edge once, costing expected $O(M)$ time. Scanning all vertices costs $O(N)$. Total time is $O(N+M)$, matching the manifest.

The counter contains at most $N$ target keys, so auxiliary space is $O(N)$. The returned list may also contain up to $N$ vertices, but output space is normally excluded from the auxiliary bound.

Hash-counter access is expected $O(1)$ under ordinary Python dictionary behavior.

## Alternatives and edge cases

- **Boolean target array:** Mark every destination true and return false entries. It uses $O(N)$ space and avoids storing exact counts.
- **Full DFS from candidate sources:** It repeats reachability work that the DAG in-degree proof makes unnecessary.
- **Topological sorting:** Its initial queue contains the same zero-in-degree vertices, but producing the complete ordering is extra work.
- **Vertex with several incoming edges:** It is excluded just like a vertex with one incoming edge.
- **Vertex with no outgoing edges:** It may still be reachable and does not belong in the answer unless its in-degree is also zero.
- **Disconnected underlying graph:** Each DAG component has at least one zero-in-degree source, and the method selects sources from every component.
- **No incoming target occurrence:** `Counter` returns zero for the missing key.
- **Multiple source vertices:** Every one is mandatory even when their reachable regions overlap.
- **Any output order:** Increasing numeric order from the comprehension is acceptable.
- **Cycle outside the contract:** A cyclic source component could have no zero-in-degree vertex, so the proof would fail.
- **Duplicate edges:** The contract excludes duplicate pairs, but duplicates would only increase a positive count and would not change the zero/nonzero classification.
- **Self-loop:** It is incompatible with a DAG and would also invalidate the reachability argument.
- **Unique solution:** It follows from every zero-in-degree vertex being mandatory and the entire set being sufficient.
