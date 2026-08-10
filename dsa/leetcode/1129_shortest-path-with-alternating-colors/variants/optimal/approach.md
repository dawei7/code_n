## General

**A node alone is not enough state**

Whether an outgoing edge is legal depends on the previous edge color. Reaching node five after red is different from reaching node five after blue.

The BFS state is therefore `(node, color)`, where `color` represents the color of the edge used to reach that state, or equivalently determines which color must be used next after toggling.

**Build separate adjacency lists**

`g[0]` stores red outgoing neighbors and `g[1]` stores blue outgoing neighbors. Parallel and self edges are preserved in the lists because the graph permits them.

The queue starts with `(0,0)` and `(0,1)`. These two conceptual states allow the first real edge to be either color. Both have distance zero because no edge has yet been taken.

**Process BFS by distance layers**

`d` is the current edge count. The snapshot `len(q)` fixes one layer, so states appended during processing wait for the next distance.

When state `i,c` is dequeued, the code writes `ans[i] = d` only if that node has no answer yet. BFS layer order guarantees this first node-level answer is the shortest alternating path regardless of ending color.

It records the colored state in `vis`, flips `c` with XOR one, and follows only adjacency edges of the opposite color. Each enqueued state therefore extends a valid alternating path by one edge.

**Why two colored arrivals may both matter**

Finding a short path to a node ending in red does not make an arrival ending in blue redundant. They enable different next edge colors and may reach different future nodes.

Visited identity must include both node and color. A node-only visited set could discard the only state capable of taking a needed next edge.

**Shortest-path correctness**

Every queued state corresponds to an alternating path because initialization is neutral and every transition flips color. BFS processes paths in nondecreasing edge count.

Thus, the first time a node appears in any ending-color state, `d` is the minimum length among all alternating paths to it. Unreached nodes retain initial `-1`. Node zero receives zero from the initial layer.

**Duplicate-state limitation in the exact code**

The implementation adds a state to `vis` only when it is dequeued, not when enqueued. Parallel edges or converging paths can enqueue the same state several times before its first dequeue.

More importantly, when a duplicate is later dequeued after already being visited, the code does not skip expansion. It adds the state to the set again, flips color, and scans its outgoing edges again. Neighbors not yet dequeued can consequently be enqueued repeatedly.

The answer remains shortest because only the first BFS-layer arrival sets it, and every duplicate path in a layer is still alternating. However, the exact operation count can exceed the manifest’s $O(n+r+b)$ bound and in path-rich graphs may reflect many duplicate path expansions.

To guarantee linear graph work, mark `(neighbor, next_color)` visited when enqueueing it, including both initial states, or skip any dequeued state already processed before scanning its edges.

Marking at enqueue time is preferable because it prevents duplicate queue storage as well as duplicate expansion. The first enqueue is already at minimum BFS distance, so suppressing later enqueues cannot discard a shorter path.

## Complexity detail

The intended colored-state graph has $2n$ vertices and $O(r+b)$ transitions. A standard enqueue-once BFS takes $O(n+r+b)$ time and space.

The exact protected code can place duplicate states in the queue and re-expand them, so that linear time bound is not guaranteed by its control flow. Its adjacency storage is $O(r+b)$ and visited set is $O(n)$, while queue size can exceed $O(n)$ due to duplicates.

The manifest describes the corrected standard BFS rather than the strict worst case of this implementation.

## Alternatives and edge cases

- **Enqueue-time visited marking:** The standard repair that ensures each colored state enters the queue once.
- **Distance matrix:** Store separate red-ending and blue-ending distances, then take the minimum per node.
- **Dijkstra:** Correct but unnecessary because every edge has unit length.
- **Node-only BFS:** Incorrect because previous color changes future legality.
- **No edges:** Node zero is zero and every other answer stays `-1`.
- **Only same-color chain:** At most its first edge can be used because colors fail to alternate.
- **Parallel edges:** They may enqueue duplicate states in the exact code but do not change shortest distance.
- **Self-edge:** It is legal only when its color alternates with the prior edge and may change the usable ending color at the same node.
- **Both colors to one node:** Both states should be explored because they enable different next colors.
- **Cycle:** Colored visited state prevents endlessly discovering new semantic states, though duplicate expansion remains possible.
- **Unreachable node:** Its initialized `-1` is returned.
- **Start node:** Its shortest path length is zero without traversing an edge.
