## General

**Reframe the objective as a weight threshold.** Suppose no retained edge may exceed a candidate value $W$. The best way to minimize the number of components under that restriction is to keep enough edges of weight at most $W$ to connect every pair they can connect. Thus $W$ is feasible exactly when the subgraph containing all edges of weight at most $W$ has at most `k` connected components. Feasibility is monotone as $W$ increases.

**Sweep thresholds with one Kruskal pass.** Sort edges by increasing weight and use union-find to add them in that order. Begin with `n` isolated components. Every successful union reduces the component count by one; cycle edges do not affect it. If `k == n`, retaining no edges already achieves cost zero. Otherwise, stop after the successful union that first reduces the count to exactly `k` and return that edge's weight.

At the returned weight $W$, the selected forest has `k` components and every selected edge weighs at most $W$, so cost $W$ is attainable. Immediately before processing weight $W$, more than `k` components remained even after using every lighter edge. No forest whose maximum edge is below $W$ can connect components that the complete lighter-edge subgraph cannot connect. Therefore every smaller cost is infeasible, proving the returned threshold is minimal. Keeping extra cycle edges is unnecessary because removing them never increases the component count.

## Complexity detail

Let $m$ be the number of edges. Sorting takes $O(m\log m)$ time. Union-find initialization and at most $m$ finds and unions take $O((n+m)\alpha(n))$ time with path compression and union by size, where $\alpha$ is the inverse Ackermann function. The sorted edge copy and union-find arrays use $O(n+m)$ space.

The benchmark defines $S=m$ on a chain with $n=m+1$ and `k = 1`. Distinct shuffled weights force the accepted solution to sort once and use every chain edge. A calibrated correct alternative tests thresholds from smallest to largest and rebuilds connectivity each time, adding an extra factor of $m$.

## Alternatives and edge cases

- **Binary search on the maximum weight:** Rebuild connectivity for each midpoint to obtain $O(m\log W)$ time after selecting a weight range. It is correct, but sorting and sweeping distinct weights once is direct and avoids repeated graph scans.
- **Test every distinct threshold independently:** This can take $O(m^2\alpha(n))$ time because union-find is rebuilt for every candidate.
- **Build a full minimum spanning tree:** Removing its `k - 1` largest edges yields the same bottleneck value, but Kruskal may stop as soon as `k` components remain.
- **`k == n`:** Remove all edges and return `0` because every isolated component has cost zero.
- **`k == 1`:** The selected forest must connect the whole graph; the answer is the bottleneck edge in a minimum spanning tree.
- **Equal weights:** Their internal processing order cannot change the returned value because every union in the group has the same threshold.
- **Cycle edges:** A high-weight cycle edge never needs to be retained and must not affect the component count or answer.
- **Single node:** With `n = k = 1`, no edges are needed and the answer is `0`.
