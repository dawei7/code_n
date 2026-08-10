## General

**Enumerate time-feasible walks, not only simple paths**

The route may revisit nodes and edges. A simple-path algorithm would miss valid solutions such as returning through an already visited node to reach zero.

The source performs depth-first search over every walk whose accumulated travel time does not exceed `maxTime`. The degree bound of four and minimum edge time of ten keep the search depth small.

**Build an undirected weighted graph**

For edge `[u,v,t]`, the source appends `(v,t)` to `g[u]` and `(u,t)` to `g[v]`.

This permits travel in both directions with the same cost, matching the graph contract.

**Track time and current quality separately**

`dfs(u,cost,value)` means the walk is currently at node `u`, has spent `cost` seconds, and has collected unique-node quality `value`.

For each adjacent edge with time `t`, recursion is allowed only when `cost+t <= maxTime`. This ensures no explored state violates the time budget.

The method does not require using all available time. Any return to zero within the budget is a valid candidate.

**Add a node's value only on its first current-walk visit**

Boolean array `vis` records whether a node has appeared anywhere on the current recursion path.

If neighbor `v` is already visited, the recursive walk moves there without changing quality. If it is new, the source sets `vis[v]=True`, adds `values[v]`, recurses, and resets the flag afterward.

This exactly implements “unique nodes visited”: repeated visits are allowed, but a node's value contributes once per complete walk.

**Why backtracking the flag is necessary**

Two sibling DFS branches represent different candidate walks. A node visited in one branch must not appear permanently collected in another branch that did not traverse it.

Resetting `vis[v]` after the recursive call restores the state belonging to the parent walk. A node already marked before the edge is not toggled, so its earlier first visit remains recorded until the recursion unwinds past that first visit.

**Initialize node zero correctly**

The walk begins at zero, so `vis[0]=True` and initial quality is `values[0]`.

Even if later moves return to zero many times, its value is never added again. This is the same unique-node rule used for every other vertex.

**Update the answer only at a valid endpoint**

At the start of every DFS call, the source checks `u == 0`. Only then does it update `ans` with current quality.

A walk ending elsewhere is not valid even if it has high collected value. It may still be extended, because a later edge sequence could return to zero within the time budget.

The initial zero-length walk is also a valid candidate and establishes at least `values[0]`, although `ans` begins at zero.

**Trace a revisiting path**

For `0 -> 1 -> 0 -> 3 -> 0`, node zero is marked throughout. Node one is marked and adds its value on the first edge, then unmarked after the branch eventually unwinds. Within that branch, returning to zero adds nothing.

Continuing to node three marks it and adds its value. When the walk returns to zero within time, the candidate contains values of zero, one, and three exactly once.

**Why exhaustive DFS is complete**

At each state, the loop considers every adjacent edge that fits the remaining budget. Therefore every time-feasible sequence of edge choices from zero appears as one recursion path.

Every valid walk is among these paths, and its quality state is exact by the visit-marker invariant. The answer examines it whenever it returns to zero.

Conversely, every answer candidate comes from a real walk beginning at zero, ending at zero, and respecting the time check. Taking the maximum yields precisely the requested quality.

**Why the bounded depth matters**

Every traversed edge costs at least ten seconds and `maxTime<=100`. Thus a walk contains at most

$$
L=\left\lfloor\frac{\texttt{maxTime}}{\text{minimum edge time}}\right\rfloor
$$

edges, at most ten under the constraints. Cycles cannot make recursion infinite.

## Complexity detail

Let $N$ be nodes, $E$ edges, $D\le4$ maximum degree, and $L$ the maximum number of edges fitting in the time budget. Graph construction costs $O(N+E)$.

The DFS search tree has worst-case size $O(D^L)$, so total time is $O(N+E+4^L)$. The graph and visited array use $O(N+E)$ space, while recursion uses $O(L)$ stack space. Total is $O(N+E+L)$.

## Alternatives and edge cases

- **Shortest-return pruning:** Precompute shortest time from each node to zero and stop branches that cannot return; improves actual search but is absent from the source.
- **Simple-path DFS:** Incorrect because revisiting nodes and edges is allowed and often required.
- **Disconnected nodes:** Never reached from zero and correctly contribute nothing.
- **Zero-value node:** Visiting it changes no quality but may enable routes.
- **Repeated node:** Its value is not added again while its visit flag is active.
- **Return to zero early:** Produces a candidate and may still be extended for a better later return.
- **Use less than `maxTime`:** Fully valid; exact budget exhaustion is not required.
- **Edge exactly fills budget:** Traversal is allowed by `<=`.
- **No edges:** The zero-length walk returns quality `values[0]`.
- **Backtracking:** New-node flags must be reset between sibling walks.
- **Bounded degree and edge count:** Make exhaustive walk enumeration practical.
- **Input preservation:** The method builds a separate adjacency list.
