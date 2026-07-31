## General

**Reverse edge deletion into edge addition.** At threshold $t$, precisely the edges with removal time greater than $t$ remain. Rather than deleting edges—which is difficult for union-find—start with no edges and add them from greatest removal time to smallest. A disjoint-set structure maintains the number of connected components as surviving edges are restored.

Before adding the edges whose time is $w$, the disjoint set contains exactly the edges with time greater than $w$. Its component count is therefore the count produced by threshold $t=w$. Initially this count is $n$, so every requested $k \le n$ is feasible at a sufficiently large threshold.

**Process equal times atomically.** Add every edge with time $w$ as one group. Each successful union decreases the component count by one. If the count becomes smaller than $k$ after the whole group is added, then thresholds below $w$ are infeasible because they retain the time-$w$ edges, while threshold $w$ itself was feasible immediately before the group. Thus $w$ is the minimum valid time.

If all edge groups can be added while at least $k$ components remain, the original graph already satisfies the requirement, so return `0`. This also covers `k = 1`, because every graph with at least one node has at least one component.

## Complexity detail

Let $m$ be the number of edges. Sorting takes $O(m\log m)$ time. Union-find initialization and all finds and unions take $O((n+m)\alpha(n))$ time, where $\alpha$ is the inverse Ackermann function. The sorted edge copy and disjoint-set arrays use $O(n+m)$ space.

## Alternatives and edge cases

- **Binary search plus connectivity checks:** Test a threshold by unioning only edges whose times exceed it. This is correct and uses $O((n+m)\log m\,\alpha(n))$ time after searching distinct times, but rebuilds connectivity repeatedly.
- **Forward edge deletion:** Ordinary union-find cannot split components, so processing removals chronologically needs a more complicated dynamic-connectivity structure.
- **Already enough components:** Return `0`; no edge needs to be removed.
- **Equal removal times:** Every edge in the group must be treated as removed simultaneously at that threshold.
- **Cycle edges:** Restoring an edge whose endpoints are already connected does not change the component count.
- **Maximum target `k = n`:** Every remaining edge prevents its endpoints from being separate, so the answer is the greatest removal time among edges when any exist.
- **No edges:** The graph starts with $n$ isolated components, and every valid `k` yields `0`.
