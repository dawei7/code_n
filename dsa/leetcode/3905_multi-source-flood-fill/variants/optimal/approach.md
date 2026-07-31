## General

**Keep one frontier for each simultaneous time step**

All source cells are colored at time zero, so they form the initial frontier. A multi-source breadth-first traversal advances exactly one grid edge per time step: the current frontier contains the cells that were most recently colored, and its uncolored neighbors are the only cells that can be colored next.

The tie rule prevents assigning a neighbor as soon as the first frontier cell reaches it. Instead, collect the proposed color for every still-uncolored neighbor in `next_colors`. If several current cells offer colors to the same coordinate, retain their maximum. Only after the entire current frontier has been processed are those winning colors written to the grid and their coordinates made the next frontier. This delayed write models simultaneous spreading exactly.

**Why every final color is correct**

Breadth-first layers visit cells in nondecreasing distance from the complete source set. Consequently, the first layer that can reach an uncolored cell is its earliest possible coloring time. Every predecessor capable of reaching it at that same time belongs to the current frontier, so taking the maximum proposal applies the required tie rule across all simultaneous arrivals. Once the layer is committed, the cell is colored and later layers correctly leave it unchanged.

Each new frontier is one step farther from the sources. Because the grid is connected and at least one source exists, the process eventually colors every cell. When no proposals remain, the stored matrix is therefore the requested final state.

## Complexity detail

Let $V=n\cdot m$ be the number of cells. Each cell enters one frontier once, and its at most four incident grid edges are inspected once when that cell is processed. The total time is $O(V)$, equivalently $O(nm)$.

The returned grid, the current frontier, and the next-layer proposal map can each contain $O(V)$ entries, giving $O(V)$ auxiliary space beyond the returned matrix as well.

## Alternatives and edge cases

- **Assign on first discovery:** A normal visited check without layer-wide aggregation can make the result depend on queue order and lose a larger color arriving during the same time step.
- **Priority queue by distance and color:** Ordering states by earliest distance and then largest color can reproduce the rule, but introduces an unnecessary $O(V\log V)$ factor on an unweighted grid.
- **Compare every cell with every source:** Manhattan distances characterize the earliest arrivals, but scanning all sources per cell costs $O(V\lvert\texttt{sources}\rvert)$ time.
- **Repeated full-grid simulation:** Copying or scanning the entire grid at each time step is correct when carefully synchronized, but can require $O(V(n+m))$ work on a long thin grid.
- **Already colored cells:** Sources and cells filled during earlier steps are permanent; only cells with value `0` may accept proposals.
- **Equal-time competition:** The maximum color matters only among arrivals in the earliest step. A numerically larger color arriving later cannot replace an existing color.
- **Adjacent sources:** Distinct neighboring sources keep their own initial colors even when one color value is larger.
- **Single source or single cell:** One source eventually fills the connected grid with its color, and a one-cell grid is already complete.
- **Grid boundaries:** Neighbor generation must reject rows outside `[0, n)` and columns outside `[0, m)`; diagonal cells are not adjacent.
