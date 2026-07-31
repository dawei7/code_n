## General

**Turn partitions into a choice of start indices.** Once the $k-1$ starts after index $0$ are chosen in increasing order, the contiguous subarrays are determined. The objective is therefore to choose their values, while the distance rule depends only on the first and last chosen indices.

**Fix the last start.** Suppose the last subarray begins at index `right`. The first chosen start after zero must be at least `right - dist`. The remaining $k-2$ starts may be any distinct indices in

$$
[\max(1,\texttt{right}-\texttt{dist}),\ \texttt{right}-1].
$$

For this fixed `right`, the best choice is exactly the $k-2$ smallest values in that interval. Adding `nums[right]` gives the best cost whose last start is `right`. Taking the minimum over every possible `right` covers every legal partition.

**Maintain the moving order statistics.** Coordinate-compress `nums[1:]` and maintain two Fenwick trees over the compressed ranks: one stores value counts and the other stores value sums. When `right` advances, insert the newly included index `right - 1` and remove `right - dist - 1` once it leaves the interval.

To sum the smallest $t=k-2$ values, binary-lift over the count tree to find the rank containing the $t$th value. The sum tree provides the total of all smaller ranks, and the remaining copies at the boundary rank complete the answer. Counts make duplicate values behave as separate eligible indices.

Every legal partition appears when its final start is processed. For that same final start, replacing any selected interior value by a smaller unselected value cannot violate the index span and cannot increase the cost. Thus the Fenwick query gives the minimum for each final start, and the minimum of those candidates is the global optimum.

## Complexity detail

Let $N$ be the length of `nums`. Coordinate compression costs $O(N\log N)$. Each index is inserted and removed at most once, and each Fenwick update or smallest-sum query costs $O(\log N)$. The total time is $O(N\log N)$ and the compressed values plus both trees use $O(N)$ space.

## Alternatives and edge cases

- **Two balanced multisets:** Keep the selected $k-2$ smallest values and the remaining window values in separate ordered multisets, together with the selected sum. This also achieves $O(N\log N)$ time but needs careful duplicate-aware rebalancing.
- **Two heaps with lazy deletion:** A maximum heap for selected values and a minimum heap for the rest can match the target bound, but expiring arbitrary window elements makes bookkeeping more intricate.
- **Sort every interval:** Rebuilding and sorting the eligible interval for every final start is correct, but costs as much as $O(ND\log D)$ for window width $D=\texttt{dist}$.
- **Tight distance:** When `dist = k - 2`, every fixed final start has exactly enough preceding positions, so all of them must be chosen.
- **Duplicate costs:** Equal values remain separate choices; the count Fenwick tree preserves their multiplicity.
- **Large values:** Costs can exceed 32-bit integer range, so implementations should accumulate sums in a sufficiently wide integer type.

