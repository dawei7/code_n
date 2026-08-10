## General

The graph is directed, and each edge has a time window rather than a fixed departure schedule. The key observation is that reaching a node earlier is never worse than reaching it later: an early traveler may wait at that node and reproduce any action available to the later traveler. Therefore, for each node, the algorithm needs only its earliest known arrival time.

This makes the problem a time-dependent version of Dijkstra's shortest-path algorithm. The priority queue always processes the not-yet-finalized node with the smallest arrival time.

**Building the directed adjacency list**

For every input edge `[source, destination, start, end]`, the source appends:

`(destination, start, end)`

to `graph[source]`. It does not add the reverse direction because the cables are directed. The adjacency list lets the main loop inspect only edges that can leave the node currently being processed.

**The meaning of `earliest`**

`earliest[v]` is the smallest arrival time at node `v` discovered so far. Initially:

- `earliest[0] = 0` because the traveler starts at node 0 at time 0;
- every other value is infinity because no route to those nodes is known.

The heap begins with `(0, 0)`. Each tuple stores arrival time first, so Python's min-heap orders entries primarily by time.

**Using one edge at the earliest possible moment**

Suppose node `u` is reached at time `time` and an outgoing edge is usable for integer departure times from `start` through `end`, inclusive.

If `time > end`, the entire availability window has already closed. Waiting only increases time, so that edge is permanently unusable from this arrival and is skipped.

Otherwise, the traveler can use the edge:

- if `time >= start`, depart immediately at `time`;
- if `time < start`, wait until `start` and then depart.

These cases combine into:

`departure = max(time, start)`.

Because the earlier guard guarantees `time <= end` and the input guarantees `start <= end`, this chosen departure also satisfies `departure <= end`. Traversal consumes one unit of time, so:

`arrival = max(time, start) + 1`.

The inclusive upper endpoint is important. Departing exactly at `end` is legal and arrives at `end + 1`.

**Relaxing an edge**

If the computed `arrival` is smaller than `earliest[neighbor]`, the algorithm has found a better route. It replaces that value and pushes `(arrival, neighbor)` into the heap.

The source does not remove the neighbor's older heap tuple. Python's standard heap has no efficient decrease-key operation. Instead, both tuples may remain until popped. The check:

`if time != earliest[node]: continue`

identifies an obsolete entry and discards it. Only the tuple matching the current best time is allowed to relax outgoing edges.

**Why an earlier arrival dominates a later one**

In a general time-dependent graph, Dijkstra can fail if leaving an edge later can somehow produce an earlier arrival in a way an early traveler cannot reproduce. That does not happen here.

If one route reaches a node at time `a` and another at time `b >= a`, the traveler from time `a` can wait `b-a` units and be in exactly the same node at time `b`. From then onward, every edge choice available to the later route is also available to the earlier route. Thus the later arrival cannot lead to a strictly better continuation that was unavailable from the earlier arrival.

For one particular edge, the arrival function is:

$$
A(t)=\max(t,\textit{start})+1
$$

for `t <= end`. This function never decreases as `t` increases. Arriving earlier either gives the same edge arrival after waiting for `start` or an earlier immediate departure.

**Why the heap order finalizes a node**

When a current tuple `(time, node)` is removed from the heap, every remaining candidate route has arrival time at least `time`. Any alternative route to `node` would have to pass through one of those not-earlier states. Since edge traversal and waiting cannot move time backward, that alternative cannot arrive before `time`.

Therefore, the current earliest time is final in the same sense as ordinary Dijkstra. Each finalized node's outgoing edges can be relaxed safely, and the destination may be returned as soon as its current tuple is popped.

**Early return at the destination**

The condition `if node == n - 1: return time` appears after stale-entry rejection. Therefore, it never returns an obsolete destination time. The first current destination entry popped is the globally minimum arrival time, so scanning the rest of the graph would not improve the answer.

**Following the first example**

At node 0 and time 0, edge `0 -> 1` is open from 0 through 1. The traveler departs at `max(0, 0) = 0` and arrives at node 1 at time 1.

At node 1, edge `1 -> 2` opens at time 2. Since the traveler arrives at 1, the formula waits implicitly:

`max(1, 2) + 1 = 3`.

The destination is inserted with time 3 and returned when popped. There is no need to represent each one-second wait as a separate graph state.

**When no route exists**

If all reachable states have been processed and the heap becomes empty, no sequence of waits and valid directed edges reaches node `n - 1`. The source then returns `-1`. Waiting cannot help an edge whose `end` is already earlier than the current time, and it cannot create an outgoing edge where none exists.

## Complexity detail

Let `n` be the number of nodes and `m` the number of directed edges. Building the adjacency list takes `O(n+m)` time and `O(n+m)` space.

Each node's outgoing list is scanned when its current earliest entry is finalized, so the total number of edge examinations is `O(m)`. A successful relaxation pushes one heap entry, and there can be `O(m)` such entries, including entries that later become stale. Heap insertion and removal therefore cost `O(\log m)` in the tight implementation-level bound. Total time is:

$$
O((n+m)\log m).
$$

The manifest states `O((n+m)\log n)`, the common bound for Dijkstra with a heap whose active entries are treated as node-bounded or with an indexed decrease-key structure. This exact Python implementation retains stale tuples, so its heap can be edge-bounded; `O((n+m)\log m)` is the safer faithful statement. Under a simple graph where `m` is polynomial in `n`, the logarithms are asymptotically equivalent.

The adjacency list stores `O(n+m)` data, `earliest` stores `O(n)` values, and the heap may hold `O(m)` tuples. Total auxiliary space is `O(n+m)`.

## Alternatives and edge cases

- **Explicit time-expanded graph:** Creating a state for every node and time is infeasible because availability endpoints can be as large as `10^9`. The arrival formula handles waiting symbolically.
- **Breadth-first search:** Edge traversal takes one unit, but forced waiting varies by edge and current arrival time, so the effective transition costs are not uniform.
- **Bellman-Ford:** It could repeatedly relax temporal edges but would be much slower; the nondecreasing arrival property permits Dijkstra.
- **Indexed priority queue:** A true decrease-key heap can maintain one active entry per node and support the manifest's conventional `\log n` heap factor.
- **Node 0 is the destination:** When `n = 1`, the initial tuple is already the target and the result is 0.
- **No outgoing edge from the start:** Unless `n = 1`, the queue empties and the result is `-1`.
- **Arrive before an edge opens:** `max(time, start)` waits exactly as long as necessary.
- **Arrive exactly at `end`:** The edge remains usable because the window is inclusive.
- **Arrive after `end`:** The source skips the edge because no amount of further waiting can reopen it.
- **Self-loops:** The constraints exclude them, but they would not improve an earliest time because traversal adds one.
- **Several edges to the same neighbor:** Each is tested independently; a later discovery may improve `earliest` and make an earlier heap entry stale.
- **Directedness:** A listed edge from `u` to `v` gives no route from `v` to `u` unless another edge explicitly provides it.
- **Cycles:** Every traversal increases time by one, and only strictly better arrival labels are pushed, so cycles cannot cause endless improvements.
- **Large time endpoints:** Python integers represent them exactly, and the algorithm never iterates through each waiting second.
- **Stale destination entry:** Stale tuples are rejected before the destination check, preventing a premature nonoptimal return.
- **Input preservation:** The solution builds a separate adjacency list and does not sort or mutate `edges`.
