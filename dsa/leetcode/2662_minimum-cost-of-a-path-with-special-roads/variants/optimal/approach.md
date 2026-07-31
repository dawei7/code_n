## General

Ordinary movement makes every coordinate reachable, but an optimal route only needs to pause at `start` and at destinations of special roads. Between such a position and a road entrance, the best unrestricted movement is exactly their Manhattan distance. After taking that road, its destination becomes the next relevant state. The target needs no stored state because its best cost can be evaluated directly from every settled position.

First cap each special-road cost by the Manhattan distance between its endpoints. A more expensive road is interchangeable with ordinary travel and can never deserve its excess cost. Then run Dijkstra's algorithm from `start`. When state `(x, y)` is removed from the heap with cost `d`, update the answer with `d` plus the Manhattan distance from `(x, y)` to `target`. For every special road, also consider moving normally from `(x, y)` to its entrance and then paying the road's capped cost; relax the distance to that road's destination.

Every constructed transition is a legal sequence of ordinary movement followed by one directed road, so any distance produced by the algorithm represents a valid route. Conversely, take any optimal route and divide it immediately after each special-road use. Each intervening ordinary segment can be replaced by a direct Manhattan trip without increasing its cost. The route therefore corresponds to transitions considered by the algorithm, followed by direct travel to the target. Dijkstra settles all these nonnegative transitions in increasing cost order, so the minimum recorded candidate is the true optimum.

## Complexity detail

Let $r$ be the number of special roads. At most $r+1$ distinct states—the start and road destinations—need to be settled. Each settled state scans all $r$ roads, producing $O(r^2)$ relaxations and heap operations, so the time bound is $O(r^2 \log r)$. The road list and distance map use $O(r)$ space. Without a decrease-key operation, one destination may have several stale heap entries, so the heap can contain $O(r^2)$ entries and the total auxiliary-space bound is $O(r^2)$.

The benchmark uses `size` as $r$. Every road has a distinct destination that Dijkstra reaches and processes, forcing the reference to scan all roads from every state. A correct all-pairs shortest-path alternative completes the legal tiers but performs $O(r^3)$ work.

## Alternatives and edge cases

- **Explicit complete graph:** Build edges among `start`, every road endpoint, and `target`, then run Dijkstra. This is correct but stores $O(r^2)$ edges that can instead be generated during relaxation.
- **Floyd-Warshall:** Treat all relevant coordinates as graph vertices and compute every-pair distances in $O(r^3)$ time and $O(r^2)$ space.
- **Repeated Bellman-Ford relaxation:** Relax every road from every road destination until stable. It is easier to derive but can also require cubic time.
- A special road is directed; a cheap road from the target toward the start provides no reverse shortcut.
- A road whose stated cost exceeds the Manhattan distance between its endpoints can be capped or ignored without changing the optimum.
- Ordinary movement may be needed both before entering a special road and after leaving the final one.
- Duplicate road destinations are harmless because the distance map retains only the cheapest discovered arrival.
- Cycles cannot improve a settled route because every ordinary and special-road cost is positive.
