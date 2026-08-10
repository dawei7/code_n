## General

This problem combines three details that an ordinary maze BFS does not handle:

1. one instruction rolls through multiple cells, so graph edges have different distances;
2. the ball falls into the hole immediately, even before reaching a wall;
3. equal-distance routes must be compared by their complete instruction strings.

The source models each cell where the ball can stop—or the hole where it disappears—as a graph node. It maintains the best known pair for each node:

`(traveled distance, instruction string)`.

A pair is better when its distance is smaller, or when distances tie and its string is lexicographically smaller.

**Distance and path tables.** `dist[i][j]` begins at infinity, meaning the cell has not been reached. `path[i][j]` begins as `None`. At the ball position, distance is zero and the path is the empty string because no cell has been traversed and no instruction has been issued.

The queue contains coordinates whose outgoing rolls should be reconsidered. Unlike an ordinary unweighted BFS, queue order alone does not prove shortest distance because one roll may travel one cell and another may travel many. Instead, this code uses repeated relaxation: whenever a better distance/path pair is found for a node, that node is enqueued so its improved value can propagate to neighbors.

Because queue entries contain only coordinates, popping a duplicate coordinate reads its latest `dist` and `path` values from the tables. Stale queued copies may cause extra work, but they do not propagate stale costs.

**Simulate one instruction exactly.** From stop `(i, j)`, the code considers up, down, left, and right. For direction vector `(a, b)` and letter `d`, it starts at `x = i`, `y = j`, and `step = dist[i][j]`.

The rolling loop checks that the next cell is inside the maze and open. It also checks that the current cell is not already the hole. When movement succeeds, `x` and `y` advance by one and `step` increases by one, matching the definition that distance counts every entered empty space.

The hole check is intentionally on the current position. If the next cell is the hole, the loop is allowed to move into it and increment distance. On the following condition check, `(x, y)` equals the hole, so rolling stops immediately even if open cells remain before the wall. This exactly models falling into the hole.

If no hole is encountered, the loop stops at the last open cell before a wall or boundary. That cell is the next legal direction-choice node.

**Relax by distance first, path second.** The candidate instruction string is `path[i][j] + d`. The endpoint is improved when

- `step < dist[x][y]`, or
- `step == dist[x][y]` and the candidate string is lexicographically smaller than `path[x][y]`.

On improvement, both tables are updated together. If the endpoint is not the hole, it is enqueued because its better pair may improve later nodes. The hole is not enqueued: the game ends upon entering it, so it has no outgoing moves.

The direction iteration order `u, d, l, r` is not lexicographic order. That does not determine the answer because every equal-distance relaxation explicitly compares full candidate strings. A later-discovered string such as one beginning with `d` can replace an earlier larger one and be propagated again.

**Why repeated relaxation reaches the optimum.** Every legal roll creates an edge with nonnegative length equal to the cells traveled and a one-character label. The relaxation rule is the standard shortest-path rule extended with a lexicographic tie-breaker. Whenever a node's stored pair improves, its outgoing edges are reconsidered. When the queue finally empties, no edge can produce a shorter path or an equally short but lexicographically smaller path. The stored pair at every reachable node is therefore optimal under the required ordering.

This is closer to a queue-based Bellman-Ford/SPFA-style process than to plain BFS. Positive roll lengths prevent distance improvements from cycling forever. Equal-distance path improvements also move strictly downward in lexicographic order among the finite relevant route strings, so the process converges.

A blocked direction leaves `(x, y) = (i, j)` and adds a letter without adding distance. Such a self-candidate cannot improve the cell's own current path because the current path is a strict prefix of the longer candidate and is lexicographically smaller. It is therefore ignored.

For the example with two routes of distance six, the tables may learn either route first. When the alternative `"lul"` reaches the hole with the same distance as `"ul"`, string comparison selects `"lul"` because `'l' < 'u'`. Thus discovery order does not control the answer.

After the queue drains, `path[rh][ch]` is the best instruction string or remains `None` if the hole is unreachable. The return expression uses `path[rh][ch] or 'impossible'`. A successful path is nonempty because the ball and hole start at different cells, so only `None` selects the fallback.

**Implementation fidelity.** The manifest describes precomputed endpoints and lexicographically keyed Dijkstra search. The exact source does neither: it rolls on demand and uses a FIFO deque with repeated relaxations, not a priority heap. The conceptual shortest-path goal is the same, but the implementation behavior and complexity must be analyzed as queue relaxation.

## Complexity detail

Let $V = RC$ be the number of grid cells, $E <= 4V$ the implicit roll edges, $L = \max(R,C)$ the maximum cells scanned by one roll, and $p$ a bound on stored instruction-string length. A heap-based Dijkstra implementation would have the manifest's logarithmic priority-queue factor. This source has no heap.

For the exact queue-relaxation implementation, a conservative Bellman-Ford-style bound allows $O(VE)$ successful/repeated edge-processing rounds. Each generated edge may scan $O(L)$ cells and compare or concatenate strings costing up to $O(p)$, yielding a conservative $O(VE(L+p))$ time bound. Actual behavior is often much better, but the manifest's $O(Vp\log V)$ form is not directly justified by this code.

The `dist` table uses $O(V)$ numeric storage and `path` stores up to $O(Vp)$ characters. The coordinate queue may contain duplicates because there is no in-queue set; usual working behavior is dominated by the tables, though a conservative transient queue bound must account for repeated improvements. A heap-based Dijkstra version gives a cleaner $O(Vp)$-style storage analysis.

## Alternatives and edge cases

- **Priority-queue Dijkstra:** Order entries by `(distance, path)` and finalize the first optimal hole entry. This matches the editorial and manifest more directly and gives predictable logarithmic queue operations.
- **Precompute roll endpoints:** Directional sweeps can avoid rescanning corridors, but hole interception must still stop a roll early.
- **Plain BFS:** It is incorrect because roll edges have unequal traveled distances; few instructions do not necessarily mean short distance.
- **Hole before a wall:** The loop must stop as soon as the ball enters the hole, not at the corridor endpoint.
- **Equal distance:** Replace a stored path only when the new complete string is lexicographically smaller.
- **Blocked direction:** It creates a zero-distance self-edge with a longer path and cannot improve the current pair.
- **Unreachable hole:** Its path remains `None` and the method returns `"impossible"`.
- **Queue duplicates:** They may repeat work, but each pop reads the newest table values rather than stale values embedded in the entry.
- **Direction order:** Correctness does not rely on iteration order because tie-breaking is explicit.
