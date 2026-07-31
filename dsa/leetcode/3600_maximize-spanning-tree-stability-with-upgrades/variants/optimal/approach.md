## General
Process every mandatory edge first with a disjoint-set union structure. A failed union proves that the mandatory edges contain a cycle, which no spanning tree may contain. Successful unions contract the mandatory forest into components; the smallest mandatory strength is already an upper bound on the final stability because these edges cannot be upgraded.

Sort the optional edges by decreasing strength and apply Kruskal's rule to the contracted graph. Add an optional edge precisely when it joins two current components. If the selected edge count never reaches $n-1$, even all available edges cannot connect the graph while respecting the mandatory choices, so the answer is `-1`.

**Why maximum-spanning Kruskal is enough:** For every strength threshold, greedy Kruskal selects as many independent optional edges at or above that threshold as any completion can select. Consequently, after sorting the optional strengths chosen by any valid completion, the greedy completion's value at every rank is at least as large. This coordinate-wise dominance matters because upgrades only replace selected strengths by twice their original values: improving any original selected strength can never reduce the best achievable minimum.

For a fixed completion, upgrading a stronger edge while leaving a weaker selected optional edge unchanged cannot improve the minimum. Sort the selected optional strengths in ascending order and double the first `k` of them, or all of them when fewer than `k` were selected. The answer is the minimum of those adjusted strengths and the smallest mandatory strength. Thus the greedy completion dominates every other tree before upgrades and remains at least as good after placing upgrades optimally.

## Complexity detail
Let $m$ be the number of edges. Sorting the optional edges costs $O(m \log m)$ time. All disjoint-set operations together cost $O((n+m)\alpha(n))$, and sorting at most $n-1$ chosen optional strengths costs $O(n \log n)$; both are covered by $O(m \log m)$ for a connected candidate graph. The disjoint-set arrays, optional edge list, and chosen-strength list use $O(n+m)$ auxiliary space.

## Alternatives and edge cases
- **Binary search on stability:** A feasibility check can require every optional edge below half the candidate stability to be absent, count upgrades for edges in the intermediate range, and use DSU. This is correct but adds a logarithmic search over the strength range and is easier to implement incorrectly around mandatory edges.
- **Enumerate spanning trees:** Testing every subset exposes the definition directly but is exponential in the number of edges and is useful only as a tiny-instance oracle.
- **Selection-sort Kruskal:** Repeatedly extracting the strongest remaining optional edge preserves correctness but takes $O(m^2)$ time.
- **Mandatory cycle:** Any failed mandatory union makes a valid spanning tree impossible, regardless of optional edges or upgrades.
- **Disconnected completion:** Finishing with fewer than $n-1$ selected edges means that no allowed spanning tree exists.
- **Unused optional edges:** Only strengths belonging to the selected tree can be upgraded; cycle-forming optional edges are irrelevant.
- **More upgrades than selected optional edges:** Upgrade every selected optional edge, and leave the excess budget unused.
- **All edges mandatory:** No upgrade is possible, so the smallest mandatory strength is the stability if those edges form a tree.
- **Mandatory bottleneck:** Upgrades can improve optional edges but can never raise stability above the weakest mandatory edge.
