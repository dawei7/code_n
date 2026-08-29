## General

This maze forms a weighted graph of stopping positions. From one stop, choosing a direction rolls through zero or more open cells until the next wall; the endpoint is another node, and the number of cells crossed is that edge's weight. The task asks for minimum traveled distance, not the fewest direction choices, so edge weights must be accumulated.

`dist[i][j]` stores the shortest distance currently known from `start` to a stop at `(i, j)`. Every entry begins at infinity except the start, whose distance is zero. The queue begins with the start coordinates.

**Generate the four direction vectors compactly.** `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce

`(-1, 0), (0, 1), (1, 0), (0, -1)`,

which represent up, right, down, and left. This avoids maintaining two separate direction arrays.

**Roll to the actual next decision point.** When coordinate `(i, j)` is dequeued, one direction starts with `x = i`, `y = j`, and `k = dist[i][j]`. The inner loop looks one cell ahead. While that cell is in bounds and open, the ball moves there and `k` increases by one.

When the loop stops, `(x, y)` is the last open cell before a wall or boundary. No intermediate cell is enqueued because the ball cannot change direction there. If the destination was merely crossed and the ball continued, it is not treated as reached; only an endpoint can receive a finite stopping distance.

If a wall is immediately adjacent, no movement occurs. The endpoint equals the current node and `k` equals its current distance. The strict improvement condition fails, so no useless self-edge is enqueued.

**Relax an endpoint whenever a shorter route is found.** If `k < dist[x][y]`, this roll has produced a better route to the endpoint. The code replaces the stored distance and appends the endpoint to the queue. Its outgoing rolls must be reconsidered because the lower distance may improve other nodes.

If the candidate equals or exceeds the stored distance, it is discarded. Future travel from the same endpoint depends only on position, so starting there with a no-better distance cannot lead to a better final route.

Unlike ordinary unweighted BFS, a cell is not marked permanently visited when first discovered. A route with more roll instructions may still have fewer traveled cells and improve it later. Re-enqueuing on strict improvements is what makes this FIFO relaxation work on weighted roll edges.

Queue entries contain only coordinates, not a frozen distance. If the same coordinate is queued multiple times and its table value improves before an older copy is popped, that pop uses the newest `dist[i][j]`. This may repeat work but cannot propagate an obsolete larger distance.

**Why the final distances are correct.** Every legal complete roll is generated from its start node with the exact number of crossed cells. Whenever a known shortest candidate plus an edge improves an endpoint, relaxation records and propagates it. The queue stops only when no stored improvement remains unprocessed. At that fixed point, every reachable graph edge satisfies the shortest-path inequality, so no route can produce a distance smaller than the stored value.

All edge weights are nonnegative integers, and every successful roll has positive length. Strictly decreasing distance updates cannot continue forever in the finite graph, so the process terminates.

After relaxation finishes, infinity at the destination means no sequence of complete rolls stops there, and the source returns `-1`. Otherwise the finite table value is the minimum traveled distance.

For the example route with roll lengths `1, 1, 3, 1, 2, 2, 2`, the algorithm adds those edge weights through successive table relaxations to obtain twelve. It does not count seven instructions as the distance.

**Implementation fidelity.** The manifest summary describes precomputed roll endpoints and heap-based Dijkstra. The exact source has neither endpoint tables nor a priority heap. It computes rolls on demand and uses a FIFO deque with repeated relaxation, corresponding to the editorial's queue-based accepted approach. The high-level weighted-graph model is shared, but the mechanics and strict complexity differ.

## Complexity detail

Let $R$ and $C$ be the grid dimensions, $V = RC$, and $L = \max(R,C)$. One expansion examines four rolls, each scanning at most $L$ cells. If every stop were expanded only once, this gives the editorial's $O(RCL)$ rolling bound.

Because the exact FIFO implementation can re-enqueue a stop whenever its distance improves, a conservative queue-relaxation analysis permits repeated edge processing. With at most $E <= 4V$ implicit edges, a Bellman-Ford-style upper bound is $O(VE L)$ in the worst case. Actual maze behavior is commonly much better, but the manifest's $O(V\log V)$ bound belongs to heap Dijkstra with constant-time or precomputed edge generation, not directly to this source.

The distance matrix uses $O(RC)$ space. The queue stores coordinates and can contain repeated entries transiently; standard practical storage is linear in reachable states, while the absence of an in-queue guard allows duplicate pending coordinates. No path strings are stored.

## Alternatives and edge cases

- **Heap-based Dijkstra:** Pop the smallest current distance first and ignore stale heap entries. With cached or efficiently generated endpoints, this matches the manifest and gives a cleaner shortest-path bound.
- **Precompute roll endpoints and lengths:** Directional sweeps replace repeated corridor scans with constant-time edge lookup at an $O(RC)$ storage cost.
- **Plain visited BFS:** Marking a node final on first discovery is incorrect because roll edges have unequal weights.
- **Destination crossed but not stopped on:** It receives no relaxation unless it is the wall-stopped endpoint.
- **Blocked direction:** The candidate is a zero-length self-edge and cannot strictly improve its current distance.
- **Unreachable destination:** Infinity remains in its table cell and is converted to `-1`.
- **Several routes to one stop:** Only strictly shorter distances trigger re-enqueueing; equal distances need no path tie-breaking in this problem.
- **Queue duplicates:** They affect efficiency rather than correctness because popped coordinates read current table distances.
- **Start and destination distinction:** The contract says they differ; if equal, the initialized zero would naturally be returned.
