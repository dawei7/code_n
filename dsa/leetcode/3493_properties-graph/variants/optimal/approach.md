## General

The property universe contains only values from $1$ through $100$. Encode the distinct values of each row in one integer bit mask: set bit $v$ whenever value $v$ appears. Repeated values set an already-set bit and therefore disappear automatically, matching the definition of a distinct intersection.

For every unordered pair of rows $i<j$, compute `masks[i] & masks[j]`. Its set-bit count is exactly the number of distinct values common to the two rows. When that count reaches `k`, the corresponding graph edge exists.

There is no need to store the dense graph explicitly. Maintain a disjoint-set union structure while testing pairs. A qualifying pair unites its two components; path compression and union by size keep these operations nearly constant. Start with $n$ components and decrement the count only when a union merges two different roots.

Every possible edge is tested once, and DSU maintains precisely the transitive closure of the qualifying edges processed so far. Therefore, after the last pair, two row indices have the same root exactly when they are connected in the defined graph, and the maintained count is the required number of connected components.

## Complexity detail

Let $n$ be the number of rows and $m$ their common length. Building the masks takes $O(nm)$ time. There are $\binom n2=O(n^2)$ pairs; each intersection and bit count operates on the fixed 101-bit universe, and a qualifying pair performs amortized $O(\alpha(n))$ DSU work. Total time is $O(nm+n^2\alpha(n))$.

The row masks, parent array, and size array each contain $O(n)$ entries, so auxiliary space is $O(n)$. The algorithm does not materialize the $O(n^2)$ edge set.

The benchmark size is $m$ while $n=100$ is fixed. Identical rows force every pair to compute the full qualifying intersection. The optimal bit-mask representation keeps pair tests word-bounded, whereas the calibrated slower implementation explicitly scans one row's distinct values against the other row for every pair and scales as $O(n^2m)$.

## Alternatives and edge cases

- **Set intersection for every pair:** Direct and correct, but it allocates or scans up to $O(m)$ values for each of $O(n^2)$ pairs.
- **Explicit adjacency list plus DFS/BFS:** Connectivity traversal is valid, but storing all qualifying edges can require $O(n^2)$ additional space; DSU consumes each edge immediately.
- **Count raw matching positions:** This is incorrect because the intersection concerns distinct values and is independent of positions or multiplicity.
- **Duplicate values within a row:** Bit insertion is idempotent, so duplicates never inflate an intersection.
- **Transitive connectivity:** Rows can share a component through intermediate nodes even when their own intersection is below `k`; DSU preserves those paths.
- **Single row:** With no pairs to test, the initial component count of one is returned.
- **No qualifying pairs:** No unions occur, so all $n$ nodes remain separate components.
- **Threshold greater than a row's distinct count:** That row cannot form an edge, even though `k` is at most the row length including duplicates.
