## General

**Separate the already energized region.** Build the directed graph and start a traversal from every point in `crystals`. Any point reached by this multi-source traversal already receives magic without a new rune. An existing edge cannot lead from this region to an unmarked point, because following that edge would have marked its destination as well.

**Treat cycles as indivisible units.** Within a strongly connected component (SCC), reaching any one point energizes every point in the component. Use two iterative Kosaraju passes—finishing order in the original graph, then component assignment in the reversed graph—to contract all cycles without risking recursion depth at the maximum input size.

The SCC condensation is a directed acyclic graph. Ignore components already reached from crystals and mark which remaining components have an incoming edge from another remaining component. Every unmarked source component needs a newly added incoming rune: no existing path from another unreachable component can enter it, and no existing edge can enter it from the energized region.

Conversely, one new rune from any energized point into each such source component is sufficient. From every source, existing condensation edges spread magic through all downstream components, and every component in a finite DAG is reachable from at least one source. Therefore the number of unreachable source SCCs is both a lower bound and an achievable answer.

## Complexity detail

Let $m$ be the number of existing runes. Building both adjacency lists, marking crystal reachability, performing the two SCC passes, and scanning cross-component edges each take $O(n+m)$ time. The graphs, traversal arrays, stacks, and component metadata use $O(n+m)$ space.

The benchmark defines `size` as $n$ and uses $m=n/2$ disjoint directed pairs. The reference visits every vertex and edge a constant number of times. A correct slower baseline computes the same SCCs but rescans all $m$ edges separately for every component to discover incoming edges, taking $O(nm)$ time, which is quadratic on these tiers.

## Alternatives and edge cases

- **Count zero-indegree vertices:** A vertex inside an unreachable cycle has positive indegree but the cycle still needs one connection from an energized point.
- **Connect every unreachable vertex:** This always works but wastes runes because one connection can energize an entire SCC and all of its descendants.
- **Greedy DFS from arbitrary unreachable vertices:** Without condensation indegrees, traversal order can choose downstream components first and overcount additions.
- **Recursive SCC traversal:** It has the same asymptotic complexity but can exceed the language recursion limit on a chain of $10^5$ points.
- **Multiple crystals in one component:** The component is simply marked reachable once and does not affect the count.
- **All points already reachable:** There are no unreachable source components, so the answer is zero.
- **Isolated noncrystal points:** Each is a singleton source SCC and requires its own new rune.
- **Several unreachable cycles feeding one tail:** Each source cycle needs a connection, while their shared downstream components require none.
