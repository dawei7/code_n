## General
**Interpret modifications as edge weights.** Treat every cell as a graph vertex with edges to its in-bounds orthogonal neighbors. The edge matching the cell's current sign has weight zero; each other outgoing edge has weight one because taking it requires changing that sign.

**Run 0–1 BFS.** Store the best known cost to every cell and process candidates in a deque. When relaxing a zero-weight edge, place the neighbor at the front; when relaxing a one-weight edge, place it at the back. This ordering processes lower-cost reachability before more expensive alternatives without a heap.

Every possible grid path corresponds to choosing one outgoing direction at each visited cell, and its edge-weight sum is exactly the number of signs that must change along that path. Conversely, every sequence of modified signs defining a valid path has the same graph cost. Therefore the shortest graph distance to the bottom-right cell is precisely the required minimum modification cost.

## Complexity detail
The graph has $RC$ vertices and at most $4RC$ directed edges. In 0–1 BFS each successful distance relaxation enters the deque in the standard linear-edge bound, so time is $O(RC)$. The distance matrix and deque use $O(RC)$ space.

## Alternatives and edge cases
- **Heap Dijkstra:** General nonnegative shortest path also works in $O(RC\log(RC))$ time, but it ignores the special zero-or-one weights.
- **Unsorted Dijkstra frontier:** Scan a pending list for the lowest-distance cell on every extraction. It is correct but adds substantial repeated selection work.
- **Ordinary BFS:** Counting every move equally is wrong because following an existing sign costs zero while changing it costs one.
- **Single cell:** Start and destination coincide, so no sign needs modification.
- **Sign leaves the grid:** That zero-cost edge is simply unavailable; other in-bounds directions remain weight-one choices.
- **Already valid path:** A chain of existing signs produces distance zero.
- **Several optimal paths:** Only the minimum cost is returned; the path itself need not be reconstructed.
