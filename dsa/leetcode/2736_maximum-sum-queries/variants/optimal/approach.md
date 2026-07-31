## General

Treat each aligned array index as a point $(a,b)$ weighted by $a+b$. A query asks for the greatest weight in the upper-right quadrant $a\ge x$ and $b\ge y$.

**Remove the first inequality offline.** Sort points by $a$ descending and queries by $x$ descending while retaining each query's original index. Before answering a query, insert every not-yet-used point with $a\ge x$. The active data structure then contains exactly the points satisfying the first threshold.

**Query the second inequality.** Coordinate-compress all point values of $b$. Reverse their compressed ranks so larger $b$ values receive smaller Fenwick indices. Updating a point stores its weight with a prefix-maximum Fenwick operation. The prefix ending at the reversed rank corresponding to `y` contains precisely active points with $b\ge y$, so its maximum is the query answer. An empty prefix returns `-1`.

Every point is inserted once, and processing queries in sorted order only grows the active set. Writing each result to its saved original index restores the required answer order.

## Complexity detail

Let $n$ be the number of points and $q$ the number of queries. Sorting points, queries, and compressed second coordinates takes $O(n\log n+q\log q)$. The $n$ Fenwick updates and $q$ prefix queries each take $O(\log n)$. A uniform bound for all terms is $O((n+q)\log(n+q))$. Sorted records, compressed coordinates, the Fenwick tree, and answers use $O(n+q)$ auxiliary space.

## Alternatives and edge cases

- **Scan every point per query:** Directly checking both thresholds is correct but takes $O(nq)$ time.
- **Segment tree:** A range-maximum segment tree over compressed second coordinates provides the same asymptotic complexity with a larger implementation.
- **Monotonic Pareto frontier:** Maintaining undominated `(b, a+b)` candidates and binary-searching it is also optimal but requires careful dominance updates.
- Equal first coordinates must all be inserted before answering a query at that threshold.
- Repeated second coordinates combine through maximum updates at the same compressed rank.
- A query threshold above every stored second coordinate produces an empty Fenwick prefix and answer `-1`.
- Query sorting must not change output order; retain and restore original indices.
- Coordinate sums may reach $2\cdot10^9$, requiring suitable integer width outside Python.
