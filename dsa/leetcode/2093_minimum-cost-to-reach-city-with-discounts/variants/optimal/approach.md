## General
**Why the city alone is not a complete state**

Arriving at the same city with different numbers of discounts already used creates different future options. Represent a state as `(city, used)`, where `used` ranges from $0$ through $K$. A highway of toll $t$ creates a same-layer transition of cost $t$ and, when `used < K`, a transition to the next layer of cost $\lfloor t/2 \rfloor$.

**Running Dijkstra on the layered graph**

Build the undirected city adjacency list and maintain the best distance for every layered state. Start from `(0, 0)` with cost zero. For the cheapest queued state, relax both the full-price and optional discounted transitions for every adjacent highway. Ignore stale heap entries whose cost no longer equals the stored best distance.

**Why the first destination state is optimal**

Every transition cost is nonnegative, including zero tolls and discounted tolls. Dijkstra's extraction order therefore finalizes states in nondecreasing cost. The first extracted state whose city is `n - 1` is cheaper than every unprocessed state, regardless of how many discounts it used, so its cost is the global optimum.

If no destination layer is reached, no sequence of highway traversals connects the endpoints and the answer is `-1`. The construction also permits leaving discounts unused because every state always retains its full-price transitions.

## Complexity detail
There are $n(K+1)$ layered states and at most $O(E(K+1))$ directed relaxations up to a constant factor. Heap operations give $O(E(K+1)\log(n(K+1)))$ time. The graph, distance table, and heap occupy $O((n+E)(K+1))$ space.

## Alternatives and edge cases
- **Bellman-Ford on layered states:** Repeated relaxation handles nonnegative costs correctly but can require many full edge passes and is polynomially slower.
- **One shortest path followed by discount placement:** Discounts can change which route is optimal, so optimizing a fixed undiscounted route is not sufficient.
- **City-only Dijkstra:** Keeping only one distance per city discards whether future discounted transitions remain available.
- With zero discounts, the method reduces to ordinary Dijkstra.
- Integer division makes an odd toll $t$ cost $\lfloor t/2 \rfloor$ when discounted.
- Extra discounts need not be used and cannot be stacked on one highway traversal.
- Zero-toll highways remain valid nonnegative edges.
