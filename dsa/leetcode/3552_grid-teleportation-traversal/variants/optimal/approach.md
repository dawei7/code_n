## General

The grid defines a graph with two edge weights. Entering an orthogonally adjacent non-obstacle cell costs one move, while jumping between equal portal letters costs zero. Ordinary breadth-first search cannot represent both weights faithfully, but 0–1 BFS can: append cost-one neighbors to the back of a deque and cost-zero portal destinations to its front. The first time a cell is removed from the deque, its distance is minimal.

Precompute the coordinates for every portal letter. When a portal cell is finalized, prepend every coordinate with that letter at the current distance, then remove the letter from the map. Suppose this is the first finalized cell with that letter and has distance $d$. Any later arrival at the same letter has distance at least $d$, so teleporting from it cannot improve any destination beyond the zero-cost transitions already offered from distance $d$. Expanding the group once therefore preserves every shortest path while preventing repeated scans of a large portal group.

Normal moves remain available from portal cells, so using a portal is optional. Finalizing a cell only when it is popped also handles the case where a cost-one route enqueues it before a later zero-cost route reaches it.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Preprocessing visits all $mn$ cells. Each traversable cell is finalized once, each of its at most four grid edges is considered once during finalization, and each portal coordinate is expanded once because its letter group is removed after use. The total time is $O(mn)$ and the portal map, deque, and finalized set require $O(mn)$ space.

## Alternatives and edge cases

- **Dijkstra's algorithm:** A heap also handles edge weights zero and one correctly, but adds an unnecessary $O(\log(mn))$ factor to queue operations.
- **Repeated portal expansion:** Scanning every same-letter coordinate whenever that letter is encountered is correct but can take $O((mn)^2)$ time when many cells share one letter.
- **Plain FIFO BFS:** Treating portal jumps like ordinary moves overcounts them; placing zero-cost transitions at the deque front is essential.
- **Single cell:** The start is already the destination, so the answer is zero regardless of whether the cell is empty or a portal.
- **Portal at the start:** It may be activated before any adjacent move, as in the first sample.
- **Optional teleportation:** The search also enqueues adjacent cells, so it does not force a portal jump that would be unhelpful.
- **Obstacle destination:** If the bottom-right cell is `'#'`, it cannot be entered and the answer is `-1` unless the grid contains only the starting cell, which is guaranteed not to be an obstacle.
- **Several copies of one letter:** A single activation may jump to any copy; expanding all of them at the same distance models that choice simultaneously.
