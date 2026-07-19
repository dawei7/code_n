## General
**Treat all gates as one BFS frontier**

Enqueue all gates at distance zero. Expand them together in breadth-first order. When an adjacent cell is still `INF`, assign the current distance plus one and enqueue it.

Every dequeued cell already has its shortest distance to any gate. Unvisited `INF` cells have not yet been reached by a path as short as the current BFS frontier.

**First arrival is the nearest gate distance**

Multi-source BFS is equivalent to adding a virtual source with zero-cost initialization at every gate. Its layers contain cells at increasing distance from the closest source, so the first path reaching a room is shortest. Assigning distance when enqueued prevents a later path of equal or greater length from changing it, while walls are never enqueued.

## Complexity detail
Each cell is enqueued at most once and checks four neighbors, giving $O(mn)$ time. The queue may contain $O(mn)$ cells.

## Alternatives and edge cases
- **Run BFS from every empty room:** can take $O((mn)^2)$.
- With no gates, empty rooms stay `INF`; walls can make rooms permanently unreachable.
