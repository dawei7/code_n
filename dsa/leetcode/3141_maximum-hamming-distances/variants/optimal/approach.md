## General

Treat every $m$-bit value as a vertex of an $m$-dimensional hypercube. Two vertices share an edge exactly when one bit flip changes one into the other. Consequently, the shortest-path distance between two vertices is their Hamming distance.

**Turn a maximum into a minimum**

Let $\overline{x} = x \mathbin{\mathtt{xor}} (2^m-1)$ be the fixed-width complement of $x$. At every bit position, a value $y$ differs from $x$ precisely when it agrees with $\overline{x}$. Therefore

$$
\operatorname{ham}(x,y) = m - \operatorname{ham}(\overline{x},y).
$$

Maximizing the left side over all values in `nums` is thus the same as minimizing the distance from $\overline{x}$ to that set and subtracting the result from $m$.

**Find every nearest source at once**

Initialize a breadth-first search with every distinct value in `nums` at distance zero. When the BFS removes a vertex, flipping each of its $m$ bits enumerates all adjacent vertices. Multi-source BFS reaches every hypercube vertex by a shortest path to its nearest array value, because all edges have unit length and all sources enter the queue together.

After the traversal, `distance[z]` is exactly $\min_{y \in \texttt{nums}} \operatorname{ham}(z,y)$. For each original value $x$, return `m - distance[x ^ mask]`, where `mask = (1 << m) - 1`. The complement identity and the BFS distance guarantee that this is precisely the requested maximum. Iterating over the original array also preserves duplicates and output order.

## Complexity detail

The hypercube has $2^m$ vertices and $m2^{m-1}$ undirected edges. Each vertex is queued once and all $m$ one-bit neighbors are considered, taking $O(m \cdot 2^m)$ time. Seeding and answering the $n$ array entries adds $O(n)$ time, for $O(m \cdot 2^m + n)$ overall.

The distance array and queue each hold at most $2^m$ entries, giving $O(2^m)$ auxiliary space.

## Alternatives and edge cases

- **Compare every pair:** Computing each pair's XOR bit count directly is simple and correct, but costs $O(n^2)$ time and is the principal slower benchmark comparison.
- **Run one BFS per array value:** Searching separately from every complement repeats nearly the entire hypercube traversal and can cost $O(nm2^m)$.
- **Subset transforms:** Bitmask dynamic programming can propagate nearest-source information, but the hypercube BFS expresses the unit-bit metric directly with the same asymptotic state space.
- Leading zeroes are part of the $m$-bit representation; the mask limits complementation to exactly those $m$ positions.
- Duplicate values are inserted as a single BFS source but still produce separate answers in their original positions.
- If an exact complement occurs in `nums`, the nearest distance from the complement is zero and the answer is the full width $m$.
- If every array value is equal, each maximum distance is zero even though the BFS still covers the complete hypercube.
