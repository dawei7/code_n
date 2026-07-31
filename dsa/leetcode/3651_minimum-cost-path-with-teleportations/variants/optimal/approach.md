## General

Let $P=mn$ be the number of cells. Maintain `costs[r][c]` as the cheapest way to reach a cell using at most the current number of teleportations, after all right/down continuations have been considered.

**Close normal moves in topological order.** Right and down edges form a directed acyclic graph ordered from top-left to bottom-right. A row-major sweep can therefore relax each cell from its top and left neighbors, adding the destination value. Starting from cost zero at `(0, 0)` gives the no-teleport layer.

**Compress every legal teleport transition.** For a new teleport layer, a destination of value $v$ may use any prior-layer source whose value is at least $v$. Sort all cells by value descending once. While sweeping that order, maintain the minimum prior-layer cost among all sources seen so far. Process equal-valued cells as one group: first add every source cost in the group to the running minimum, then assign that minimum to every destination in the group. This preserves the inclusive `<=` rule between equal values.

Copy the prior costs before applying teleport transitions so paths using fewer teleports remain available. After initializing all zero-cost teleport destinations, run the normal-move closure again. Repeating this process `k` times produces the optimum using at most `k` teleportations.

## Complexity detail

Sorting the $P=mn$ cells takes $O(P\log P)$ time once. Each of the `k` layers performs one value sweep and one grid sweep, both $O(P)$, for total time $O(P\log P+kP)$. The sorted cells and two cost grids use $O(P)$ auxiliary space.

The benchmark defines size $N=P$ using square grids with 16, 64, and 256 cells, spanning 16x, and fixes `k = 2`. The accepted grouped sweep is $O(N\log N)$. A correct transition that checks every source for every destination costs $O(kN^2)$ and must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Explicit teleport graph:** Adding an edge for every legal source-destination pair creates $O(P^2)$ edges and is too large at the maximum grid size.
- **Dijkstra on `(cell, teleports)` states:** It is correct with implicit transitions, but scanning all legal teleport destinations from each state still becomes quadratic without the value-order aggregation.
- **No teleportations:** The initial right/down dynamic program directly gives the answer.
- **Equal cell values:** A teleport between them is legal, so all members of an equal-value group must see one another's source minimum.
- **Zero-valued cells:** Normal entry can cost zero, and teleport comparisons remain inclusive.
- **Unused allowance:** Copying the preceding layer ensures the optimum may use fewer than `k` teleports.
