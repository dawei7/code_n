## General
**Model complete rolls as weighted edges**

The ball may choose a new direction only after it stops. Treat each open cell that can be reached as a stopping state, and connect it to the stopping cell obtained by rolling left, right, up, or down. The weight of an edge is the number of cells crossed. A route's total edge weight is therefore exactly its traveled distance.

**Precompute every wall-bounded endpoint**

Four linear sweeps record the farthest open cell reachable from each cell in each direction. In a left-to-right row sweep, a cell inherits its predecessor's left endpoint when that predecessor is open; otherwise it is its own endpoint. Reverse the sweep for right endpoints and repeat by column for up and down. This makes each later graph transition constant time instead of rescanning a corridor.

**Use Dijkstra because rolls have unequal lengths**

Store the best known distance to every cell and process `(distance, row, column)` entries from a min-heap. From a current cell, relax the four precomputed endpoints using their coordinate difference as the edge weight. Ignore stale heap entries whose distance no longer matches the table.

**Why the first popped destination is optimal**

Every edge weight is nonnegative. Dijkstra removes states in nondecreasing route distance, so when the destination's current entry is removed, no unprocessed route can reach it more cheaply. Each relaxed edge represents one legal complete roll, and every legal sequence of rolls is a path in this graph. If the heap empties first, no sequence can stop there; merely rolling through the destination never creates a destination state.

## Complexity detail
The four endpoint sweeps take $O(rows \cdot cols)$ time. The graph has at most `rows * cols` states and four outgoing edges per state; heap relaxations take $O(rows \cdot cols \log(rows \cdot cols))$ time. Endpoint tables, distances, and the heap use $O(rows \cdot cols)$ space.

## Alternatives and edge cases
- **Roll step by step during Dijkstra:** is correct and commonly used, but can rescan long corridors from many stopping states.
- **Linear-scan Dijkstra:** preserves correctness but selecting the next unsettled state can take quadratic time in the number of reachable cells.
- **Breadth-first search:** minimizes the number of rolls rather than their unequal traveled lengths, so it can return a nonminimum distance.
- **Queue-based repeated relaxation:** can be correct but lacks Dijkstra's efficient nondecreasing-distance finalization.
- **Start equals destination:** has distance `0` without a roll.
- **Pass through destination:** does not count unless the ball stops there.
- **Unreachable stopping cell:** requires returning `-1` even if it is open.
- **Zero-length direction:** an endpoint equal to the current cell adds no useful edge.
