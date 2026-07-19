## General
**Interpret swaps as connectivity.** Create an undirected graph whose vertices are string indices and whose edges are the allowed pairs. Along any path, successive edge swaps can move a character between the path's endpoints. Consequently, every permutation of characters within one connected component is reachable, while no character can cross between components.

**Build components with disjoint sets.** Initialize each index as its own parent and union the endpoints of every pair. Path compression and union by size keep the amortized cost of each operation at $O(\alpha(n))$. After all unions, indices with the same representative are exactly the positions whose characters may be permuted together.

**Make each component lexicographically minimal.** Gather the characters belonging to every representative and sort each group in descending order. Traverse output indices from left to right and pop the smallest remaining character from that index's component. Assigning the smallest available character to the earliest available position is lexicographically optimal; any alternative placing a larger character there would produce a larger string at the first differing index.

## Complexity detail
The $p$ unions and $n$ representative lookups take $O((n+p)\alpha(n))$ time. Across all components, sorting character groups costs at most $O(n\log n)$, and reconstruction is $O(n\alpha(n))$. Total time is $O((n+p)\alpha(n)+n\log n)$. Parent, size, group, and output storage use $O(n)$ space.

## Alternatives and edge cases
- **Graph traversal:** DFS or BFS can identify each component in $O(n+p)$ time and then apply the same per-component sorting.
- **Repeated label propagation:** Scanning all pairs until component labels stop changing is correct but can take $O(np)$ time on a long adversarial chain.
- **Enumerate swap sequences:** Searching reachable strings grows factorially with component size and is infeasible.
- **No pairs:** Every index is isolated, so the original string is already the only reachable result.
- **One connected component:** All characters may be globally sorted.
- **Repeated characters:** Equal characters are interchangeable but every occurrence must still be assigned.
- **Duplicate or self pairs:** Union operations are idempotent and do not change the component partition.
- **Disconnected components:** Lexicographic choices in one component cannot consume characters belonging to another.
