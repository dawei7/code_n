## General

**This is a shortest-path problem with time-dependent entry rules**

Each cell is a graph vertex, and edges connect orthogonally adjacent cells. Moving across one edge takes one second. Unlike an ordinary unweighted grid, a neighbor cannot be entered before its `grid` value.

A breadth-first search is insufficient because reaching a neighbor may effectively cost more than one second when its opening time is in the future. Dijkstra's algorithm is appropriate: it repeatedly finalizes the cell with the smallest known arrival time and relaxes time-dependent moves to its neighbors.

**Why the initial impossibility check is necessary**

The traveler cannot stand still. At time zero, the only possible first moves are right to $(0,1)$ or down to $(1,0)$; dimensions are at least two in both directions.

If both cells require a time greater than one, neither can be entered at time one. There is no previously visited edge along which to move back and forth, so time cannot be consumed. The start is permanently trapped, and the solution returns $-1$.

If at least one neighbor opens by time one, the traveler can make a first move. From then on, an already traversed edge provides a two-second waiting cycle: move to the previous cell and back. This makes every sufficiently late time of the correct parity attainable.

**Why waiting changes time only by even amounts**

Suppose the current cell is reached at time $t$. A direct move to a neighbor would arrive at `t + 1`. Since waiting in place is forbidden, extra time is spent through back-and-forth moves. Each round trip adds two seconds.

Therefore possible arrival times at that neighbor have the same parity as $t+1$:

$$
t+1,\ t+3,\ t+5,\ldots
$$

If the neighbor's opening time is $g$ and $t+1\ge g$, direct arrival works. Otherwise the earliest legal arrival is the smallest value at least $g$ with the same parity as $t+1$.

**Derive the parity adjustment**

The code begins with `nt = t + 1`. When `nt < grid[x][y]`, it replaces it by

`grid[x][y] + (grid[x][y] - nt) % 2`.

Let $g=\texttt{grid[x][y]}$. If $g-nt$ is even, $g$ has the same parity as the direct arrival, so arrival exactly at $g$ is reachable. The remainder is zero.

If $g-nt$ is odd, $g$ has the wrong parity. The next time $g+1$ has the correct parity, and the remainder is one. This formula therefore produces precisely the earliest feasible arrival.

For example, if direct arrival would be time $4$ and the gate is $7$, reachable times are $4,6,8,\ldots$, so the first legal one is $8$. The difference $7-4$ is odd, and the formula adds one.

**Dijkstra state and relaxation**

`dist[i][j]` stores the smallest discovered arrival time for each cell. It starts at infinity except `dist[0][0] = 0`. The heap stores triples `(time,row,column)` and always pops the smallest time first.

For each of the four directions encoded by adjacent pairs from `dirs = (-1,0,1,0,-1)`, the algorithm checks bounds, computes the earliest parity-compatible arrival, and updates the neighbor only if that time improves `dist`.

The direction pairs are $(-1,0)$, $(0,1)$, $(1,0)$, and $(0,-1)$, covering up, right, down, and left.

**Why the first popped destination time is optimal**

The effective move from a state reached at time $t$ never arrives before $t+1$, so edge travel respects nonnegative elapsed time. Dijkstra's ordering applies: when a cell is popped with its smallest possible heap time, no later path can produce a smaller arrival that was not already scheduled.

The code does not explicitly discard stale heap entries whose time exceeds `dist[i][j]`. Processing such an entry is harmless because its neighbor arrivals cannot improve already discovered routes in a way that violates Dijkstra ordering. More importantly, if the destination has multiple entries, the smallest time is popped before any larger stale one, so returning immediately is safe.

Once the initial trap is ruled out, geometric grid connectivity and the ability to oscillate mean all cells eventually become reachable. That is why the exact loop is written as `while 1` without an empty-heap return branch.

**Why the waiting cycle is always available after departure**

Any reached non-start cell has a predecessor used to enter it. At later times, both the current cell and that predecessor are already open because opening constraints are lower bounds, not temporary windows. Traversing the edge backward and forward is always legal and spends two seconds.

At the start, the passed initial check guarantees an accessible neighbor. A route that needs delayed departure can use that first edge as the same oscillation mechanism.

## Complexity detail

Let $N=mn$ be the number of cells. Each successful distance improvement pushes a heap entry. With four edges per cell, there are $O(N)$ relevant relaxations, and each heap operation costs $O(\log N)$. Total time is $O(mn\log(mn))$.

The distance matrix uses $O(mn)$ space, and the heap can contain $O(mn)$ entries. Direction and scalar state are constant-sized. The input grid is not modified.

## Alternatives and edge cases

- **Ordinary BFS:** It assumes every transition has identical effective cost and cannot prioritize paths with different gate-induced delays.
- **Wait in place:** The rules require a move every second, so simply replacing arrival by `max(t+1, gate)` ignores parity and can claim impossible times.
- **Time-expanded BFS:** Adding a state for every time step is far larger than computing the next legal time algebraically.
- **Both first neighbors locked:** No move at time one means no waiting cycle exists, so $-1$ is mandatory.
- **One first neighbor open:** That edge is enough to create two-second oscillations for later waits.
- **Gate already open:** When `t + 1 >= gate`, no parity adjustment is needed.
- **Wrong parity at the gate:** Arrival is delayed to `gate + 1`, not to the gate time.
- **Stale heap entries:** They may cause redundant work, but the distance comparison prevents harmful updates and the minimum destination entry pops first.
- **Input dimensions:** The direct accesses to `grid[0][1]` and `grid[1][0]` rely on the guaranteed minimum of two rows and two columns.
