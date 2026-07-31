## General

Each placement check depends only on the longest obstacle-free interval inside its prefix. Insertions split existing intervals, so the solution must support both ordered-neighbor searches and prefix maximum queries.

Treat coordinate `0` as a permanent left boundary and place a harmless sentinel at $C$, one position beyond every queried coordinate. A Fenwick tree stores `1` at every obstacle coordinate. Its prefix sums give an obstacle's rank, and binary lifting on those sums finds the obstacle with any requested rank. Thus, when inserting `x`, the predecessor and successor obstacles are both found in logarithmic time.

A segment tree stores a gap at its right obstacle: if consecutive obstacles are `left` and `right`, the leaf at `right` stores `right - left`. Inserting `x` between them creates the gap ending at `x` and shortens the gap ending at `right`; only those two leaves change.

For a check `[2, x, sz]`, a segment-tree maximum over coordinates through `x` covers every complete gap whose right obstacle lies inside the prefix. The prefix may end before the next obstacle, so separately compute `x - predecessor(x)` for its final truncated gap. The larger of these values is exactly the longest available interval in $[0,x]$. A block fits precisely when that length is at least `sz`; equality is allowed because touching an obstacle is permitted.

## Complexity detail

Let $q$ be the number of queries and $C$ be one more than the largest queried coordinate. Each Fenwick-tree search or update and each segment-tree query or update costs $O(\log C)$. Every input query performs only a constant number of them, so total time is $O(q \log C)$. The Fenwick tree, segment tree, and obstacle-presence array use $O(C)$ auxiliary space.

## Alternatives and edge cases

- **Ordered set plus a gap scan:** An ordered set can find insertion neighbors efficiently, but scanning all gaps for each type-2 query can require $O(q^2)$ total time.
- **Offline reverse processing:** Processing insertions as deletions in reverse can simplify some interval problems, but these prefix checks need answers at their exact historical state and require additional machinery to preserve the prefix maximum.
- **Endpoint touching:** A gap of length exactly `sz` is sufficient; obstacles prohibit intersection, not contact.
- **Prefix ending between obstacles:** The segment tree contains the full gap to the successor, so `x - predecessor(x)` must represent the truncated final interval instead.
- **Obstacle beyond `x`:** It must not reduce the answer for the current prefix.
- **Query independence:** A successful type-2 query never consumes space or changes any maintained state.
