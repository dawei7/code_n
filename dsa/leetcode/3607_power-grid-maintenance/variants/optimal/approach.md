## General

**Separate permanent connectivity from changing availability.** Taking a station offline does not delete it from the graph. Consequently, every station's power-grid component is fixed for the entire query sequence. Union all cable endpoints once with a disjoint-set structure, then record the representative of every station.

**Keep the smallest possible responder at each heap root.** Group station identifiers by component while visiting identifiers in increasing order. Each resulting list is already a valid min-heap. Maintain a Boolean online flag for every station. An outage only clears that flag; removing its identifier from the middle of a heap is unnecessary.

For a maintenance query, an online target must answer for itself even if a smaller station exists in its component. If the target is offline, inspect its component heap. Repeatedly pop the heap root while that station is offline. The remaining root is the smallest online station because every smaller identifier has just been proved offline and removed; an empty heap means no responder exists.

This lazy deletion is safe because stations never return online. Each stale identifier is removed at most once over the entire execution. Union-find gives every query the correct permanent component, and the heap invariant gives exactly the smallest online member when substitution is required.

## Complexity detail

Let $m$ be the number of connections and $q$ the number of queries. Union-find preprocessing takes $O((c+m)\alpha(c))$ time, where $\alpha$ is the inverse Ackermann function. Query iteration costs $O(q)$ apart from heap removals. Across all queries, at most $c$ stations are popped, costing $O(c\log c)$ in total. Overall time is $O((c+m)\alpha(c)+q+c\log c)$. The component, disjoint-set, online-state, heap, and output storage use $O(c+q)$ space.

## Alternatives and edge cases

- **DFS or BFS component labels:** Building an adjacency list and traversing each component is equally valid, with $O(c+m)$ preprocessing, but union-find avoids storing adjacency solely for labeling.
- **Ordered set per component:** Eager deletion and minimum lookup give $O(\log c)$ per update or query, but Python has no built-in balanced ordered set.
- **Scan the component on every offline check:** This is correct but may revisit $\Theta(c)$ stations for each query and degrade to quadratic time.
- **Target still online:** Return the target itself, not the globally smallest station in its component.
- **Offline bridge station:** Connectivity is unchanged, so its former neighbors remain in one grid and may answer for it.
- **Repeated outages:** Taking an already offline station offline again has no additional effect.
- **Exhausted component:** After every member is offline, any maintenance check for that component returns `-1`.
