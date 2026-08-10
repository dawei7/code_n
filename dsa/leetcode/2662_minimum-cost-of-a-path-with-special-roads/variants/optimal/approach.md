## General

**Walking can connect any relevant points directly**

Ordinary movement from point $P$ to point $Q$ costs Manhattan distance:

$$
d(P,Q)=|x_P-x_Q|+|y_P-y_Q|.
$$

This metric obeys the triangle inequality. Any all-walking route through intermediate points costs at least direct walking between its endpoints.

Therefore, useful route structure alternates:

1. walk directly to a special-road entrance;
2. take that directed road to its exit;
3. repeat, or walk directly to the final target.

The only positions that need to become graph states are the original start and special-road exit coordinates. From any such state, the algorithm can walk to every road entrance on demand.

**Use Dijkstra because transition costs are nonnegative**

Heap `q` begins with state:

`(0, startX, startY)`.

Tuple first component is total cost to reach the coordinate. The min-heap always pops the smallest tentative distance.

All Manhattan distances and special-road costs are nonnegative, so Dijkstra's finalization argument applies.

**Finalize each coordinate once**

Several roads may end at the same coordinate, and many different sequences can reach one exit.

Set `vis` stores coordinates already popped and finalized. When a duplicate heap entry appears later, it is skipped.

The first pop of $(x,y)$ has minimum possible cost $d$: any undiscovered alternative route would have to extend a heap state with distance at least $d$ by nonnegative cost and cannot improve it.

**Always consider walking to the target**

From finalized coordinate $(x,y)$ at cost $d$, a complete route may stop using special roads and walk directly to target.

Its total is:

$$
d+\operatorname{Manhattan}((x,y),\texttt{target}).
$$

The solution minimizes `ans` with this candidate at every finalized state.

This includes the no-special-road route when the start state is popped.

**Create transitions through every special road**

For road:

$$
(x_1,y_1)\to(x_2,y_2)
\quad\text{with cost }c,
$$

from current state $(x,y)$ the route cost is:

$$
d
+|x-x_1|+|y-y_1|
+c.
$$

The heap entry ends at road exit $(x_2,y_2)$.

Direction is respected: the transition always walks to the stored entrance and arrives at the stored exit. The algorithm never automatically adds the reverse road.

**Why entrances do not need permanent states**

Suppose an optimal route walks from one road exit to an entrance, perhaps passing through other coordinates without using a road.

By Manhattan triangle inequality, replacing that walking segment with direct walking to the same entrance is no more expensive. Nothing special happens at arbitrary intermediate coordinates.

The transition formula already includes this direct cost. Hence storing every entrance or every grid coordinate as a separate Dijkstra node adds no new route.

**Why all useful road sequences are represented**

Take any route using special roads $R_1,R_2,\ldots,R_t$.

Starting at `start`, the heap transition for $R_1$ includes walking to its entrance and riding to its exit. From that exit state, the transition for $R_2$ does the same, and so on.

After $R_t$, the `ans` update represents final walking to target.

Thus every possible road sequence corresponds to a path in the implicit state graph. Conversely, every heap transition describes a legal walk-plus-road move, so no invalid candidate is introduced.

**Expensive roads are harmless**

A special road may cost more than simply walking from its entrance to its exit. The exact code still pushes it.

Dijkstra and the direct-walk candidates ensure such a dominated choice cannot lower `ans`. Filtering these roads could improve constants but is unnecessary for correctness.

**Trace the first example**

From start $(1,1)$, direct walking to target $(4,5)$ costs seven, so initial `ans` becomes seven.

Transition through first road walks one step to $(1,2)$, pays road cost two, and reaches $(3,3)$ for cost three.

From there, using the second road requires one walking step to $(3,4)$ plus road cost one, reaching target for total five.

When that target coordinate is popped, direct remaining distance is zero and `ans` becomes five.


The implicit graph has nonnegative edges from every state to every special-road exit, plus conceptual direct edges to target. Dijkstra finalizes each reachable state at minimum cost.

The route-representation argument proves every legal original route maps to an implicit path of no greater cost, while every implicit path is legal. Therefore, minimizing target completion over finalized states gives exactly the original problem optimum.

## Complexity detail

Let $r$ be the number of special roads. There are at most $r+1$ distinct state coordinates: start and road exits.

Each finalized state scans all $r$ roads and pushes up to $r$ entries, for $O(r^2)$ heap entries. Heap operations cost $O(\log(r^2))=O(\log r)$, so time is $O(r^2\log r)$.

The heap may hold $O(r^2)$ entries, while `vis` holds $O(r)$ coordinates. Total space is $O(r^2)$.

## Alternatives and edge cases

- **Explicit complete graph of relevant coordinates:** Build road transitions first, then run Dijkstra; equivalent but stores edges eagerly.
- **Bellman–Ford-style relaxation:** Nonnegative weights make Dijkstra preferable.
- **Coordinate-grid search:** Impossible over the large continuous rectangle and unnecessary under Manhattan distance.
- **No useful special road:** Initial direct-walk candidate remains optimal.
- **Road ending at target:** Its popped state's remaining Manhattan distance is zero.
- **Road pointing away:** Direction is honored; reverse travel is ordinary Manhattan walking.
- **Repeated exit coordinates:** `vis` finalizes the coordinate only once at minimum cost.
- **Road cost exceeds walking:** It is dominated but harmless.
- **Use road multiple times:** Implicit transitions allow it, though positive costs mean useless cycles cannot improve a shortest path.
- **Start equals an exit:** Duplicate coordinate entries are safely skipped after finalization.
