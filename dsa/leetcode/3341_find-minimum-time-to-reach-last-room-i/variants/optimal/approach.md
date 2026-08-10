## General

**Model earliest arrival times as shortest-path distances.** Each room is a graph vertex with edges to up to four wall-sharing neighbors. The cost of moving to a neighbor depends on both current time and that neighbor's opening time, so ordinary breadth-first search is insufficient even though every physical move itself lasts one second.

`dist[i][j]` stores the earliest known time at which the tourist can be inside room $(i,j)$. The start is reachable at time zero. Every other distance begins at infinity.

**Derive one relaxation.** Suppose current room is reached at time $d$. Movement into neighbor $(x,y)$ cannot start before `moveTime[x][y]`. If the tourist arrives early, waiting in the current room is allowed. The earliest departure is therefore

$$
\max(d,\texttt{moveTime}[x][y]).
$$

The move takes one second, so candidate arrival is

$$
t=\max(d,\texttt{moveTime}[x][y])+1.
$$

The source uses `dist[i][j]` in this formula after rejecting stale heap entries; it equals the finalized current key at useful pops.

**Use Dijkstra because later arrival never helps.** The transition function is nondecreasing in current time: starting from a later arrival cannot produce an earlier neighbor arrival. This FIFO property makes Dijkstra's greedy extraction valid even though edge waiting costs are time-dependent.

The min-heap stores tuples `(time,row,column)`, ordered first by time. Whenever a relaxation improves a neighbor, its distance and a new heap entry are recorded. Old larger entries may remain. If popped time exceeds the current distance, the stale entry is skipped.

**Generate four directions compactly.** `dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` yield `(-1,0),(0,1),(1,0),(0,-1)`: up, right, down, and left. Bounds checks discard moves outside the grid.

**Why early return is safe.** Dijkstra pops states in nondecreasing time. The first popped target time is the minimum possible arrival, so the method returns immediately. The target check occurs before the stale-entry check, but a stale target entry with larger time cannot be the first target pop: its newer smaller entry would have a smaller heap key and be popped first. Thus the order remains safe.
Assume a popped non-stale room has minimum possible arrival among unsettled rooms. Any alternative path to it must pass through another unsettled predecessor with arrival no smaller than the heap minimum; the nondecreasing transition cannot improve the popped time. Its distance is final. Relaxing all neighbors considers every path extension. Induction finalizes rooms in correct order, and the first finalized target is optimal.

The loop is written `while 1` rather than checking heap non-emptiness. A rectangular grid is connected and waiting makes every room eventually reachable, so a target entry is guaranteed and the heap cannot empty first.

The source assumes `inf`, `heappop`, `heappush`, and `pairwise` are imported.

## Complexity detail

There are $V=nm$ rooms and fewer than $4V$ directed neighbor relaxations. Each successful relaxation pushes one heap entry, and heap operations cost $O(\log V)$. The conventional bound is $O(nm\log(nm))$ time.

The distance matrix uses $O(nm)$ space. The heap may contain $O(nm)$ entries up to constant-factor duplicates, so total auxiliary space is $O(nm)$.

## Alternatives and edge cases

- **Breadth-first search:** It fails because opening-time waits make effective edge arrival costs unequal.
- **Bellman-Ford:** It can handle general weights but would be vastly slower than needed; all transitions satisfy Dijkstra's monotonicity.
- **Explicit visited matrix:** It can finalize each node once. The stale-distance comparison already provides equivalent lazy handling.
- **Neighbor already open:** Candidate is current time plus one.
- **Neighbor opens later:** The tourist waits until its opening time and then spends one second moving.
- **Starting room's opening time:** The start is given at time zero, so `moveTime[0][0]` is not used as an entry restriction.
- **Large opening values:** Python integers and the heap support them without overflow.
- **Multiple optimal paths:** Only the earliest time matters; predecessor reconstruction is unnecessary.
- **Stale heap entry:** It is skipped unless it is the target, where a smaller target entry necessarily would have returned first.
- **Connected grid:** Four-direction adjacency guarantees reachability in a nonempty rectangle.
- **Direction tuple:** `pairwise` requires a modern Python import from `itertools`.
- **Waiting:** It occurs implicitly through `max` and does not require adding wait edges.
- **One-second movement:** The `+1` is applied after waiting, meaning opening time is the earliest departure-to-room time under the examples.
- **Why destination opening controls the edge:** The current room is already occupied legally. Only the room being entered imposes a new opening constraint, so `moveTime[i][j]` is not rechecked on departure.
- **No benefit from deliberate extra waiting:** Because every later transition is nondecreasing in arrival time, waiting beyond the earliest permitted departure cannot improve any future arrival.
- **Heap tuple tie-breaking:** Equal times are then ordered by row and column automatically. This affects processing order only, not computed distances.
- **Relax from finalized time:** After the stale check, using `dist[i][j]` rather than local `d` yields the same value and preserves the formula's state meaning.
