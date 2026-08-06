## General

**Treat all gates as one BFS frontier**

Enqueue all gates at distance zero. Expand them together in breadth-first order. When an adjacent cell is still `INF`,
assign the current distance plus one and enqueue it.

Every dequeued cell already has its shortest distance to any gate. Unvisited `INF` cells have not yet been reached by a
path as short as the current BFS frontier.

**First arrival is the nearest gate distance**

Multi-source BFS is equivalent to adding a virtual source with zero-cost initialization at every gate. Its layers
contain cells at increasing distance from the closest source, so the first path reaching a room is shortest. Assigning
distance when enqueued prevents a later path of equal or greater length from changing it, while walls are never
enqueued.

## Complexity detail

The initial grid scan takes $O(mn)$ time. Each reachable non-wall cell is then enqueued at most once and checks four
neighbors, so total time remains $O(mn)$. In the widest frontier, the deque can contain $O(mn)$ cells, which is the
auxiliary-space bound.

## Alternatives and edge cases

- **Run BFS from every empty room:** can take $O((mn)^2)$.
- **Run BFS separately from every gate:** also repeats visits and requires taking a minimum across searches.
- **No gates:** the initial queue is empty, so every empty room remains `INF`.
- **All gates or walls:** no `INF` neighbor is ever enqueued and the grid remains unchanged.
- **Unreachable room:** walls prevent any BFS arrival, so its `INF` marker is preserved.
- **Defensive empty grid:** the app-local guard returns immediately, although the source contract requires positive
  dimensions.
