## General

Treat array indices as graph vertices. A reversal is an edge from the current position to the position where that reversal places the `1`, and breadth-first search therefore supplies minimum operation counts.

If the `1` is currently at index $x$ and a length-`k` reversal begins at $s$, its new index is

$$
y = 2s + k - 1 - x.
$$

The valid starts form the integer interval

$$
\max(0, x-k+1) \leq s \leq \min(x, n-k).
$$

Consequently, all destinations from $x$ form an inclusive interval with step two: they share one parity, and their smallest and largest values come from the two endpoint starts. The challenge is to enumerate only destinations that are neither banned nor already visited without rescanning that interval for every BFS vertex.

Maintain separate successor disjoint sets for even and odd indices. Within one parity, compress actual index $i$ to $\lfloor i/2 \rfloor$. A representative answers: "what is the first still-available compressed index at or after this one?" Removing a banned or visited index links it to its successor. For a BFS interval, find the first available representative, visit it, remove it, and ask again until the representative lies beyond the interval.

Every legal unvisited destination in the step-two interval is returned, so BFS explores exactly the same edges needed to discover new vertices. Removing a vertex at discovery time prevents duplicate queue entries. Standard BFS layering gives the shortest operation count, while banned vertices were removed before the search and can never be discovered.

## Complexity detail

There are $n$ parity-compressed positions. Each position is removed at most once, and successor queries use path-compressed disjoint-set operations with amortized $O(\alpha(n))$ cost. The total time is $O(n\alpha(n))$, where $\alpha$ is the inverse Ackermann function. The parity arrays, parents, answer, and BFS queue use $O(n)$ space.

## Alternatives and edge cases

- **Ordered sets by parity:** A balanced search tree can find and erase every destination in $O(n\log n)$ total time and is conceptually close to the successor structure.
- **Enumerate every reversal start:** Straightforward BFS is correct, but a vertex can have $\Theta(k)$ candidate starts, leading to $O(nk)$ time.
- **Length one:** Reversals do not move the `1`; only `p` is reachable.
- **Whole-array reversal:** Each position has at most one possible destination, its mirror index.
- **Parity behavior:** Odd `k` preserves index parity, while even `k` switches parity after every move.
- **Banned semantics:** A reversal may span banned indices; it is illegal only when the `1` would finish on one of them.
- **Initial position:** `p` is guaranteed not to be banned and always has distance zero.
