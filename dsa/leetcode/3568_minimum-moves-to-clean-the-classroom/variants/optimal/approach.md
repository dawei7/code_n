## General

The shortest route cannot be described by position alone. Reaching the same cell with different remaining energy or a different set of collected litter can change what is possible next. The source therefore runs breadth-first search over states containing:

- current row and column;
- current energy;
- a bitmask of litter items still uncollected.

Every move has cost one, so the first BFS layer containing a state with no remaining litter gives the minimum number of moves.

**Assigning a bit to each litter cell**

The initial grid scan finds the unique starting coordinate and numbers the `L` litter cells from zero through `L-1`. `d[i][j]` stores the bit index for a litter cell.

The starting mask is

`(1 << L) - 1`,

whose lowest `L` bits are all one. A one means that litter remains. On entering litter cell `(x,y)`, the update

`nxt_mask &= ~(1 << d[x][y])`

clears its bit. Visiting the same cell again leaves the bit zero, so litter is collected only once.

If the initial scan finds no litter, the answer is immediately zero. No movement is required, and avoiding state allocation is especially useful because the full visited structure is large.

**Why all three state dimensions matter**

Two visits to the same coordinate and mask are not necessarily equivalent if one has more energy. The higher-energy visit can reach farther before needing a reset.

Likewise, equal position and energy do not make states equivalent when their masks differ. One route may already have collected litter that another still needs.

The exact visited key is therefore `(row,column,remaining_energy,remaining_mask)`. The four-dimensional `vis` array marks each such combination once.

The manifest summary says the source retains only the greatest remaining energy for each position-mask pair. That dominance optimization is not implemented. The exact source allocates and tracks every energy value from zero through the maximum separately. A higher energy can dominate a lower one at the same position and mask, but the current code does not exploit that fact.

**BFS layers represent move counts**

`q` contains all states at the current distance `ans`. At the start, it holds the starting state with full energy and all litter bits set, while `ans=0`.

For each iteration:

- `t=q` freezes the current layer;
- `q=[]` becomes the next layer;
- every legal one-step successor is appended to the new `q`;
- after the layer is exhausted, `ans` increments.

Thus every state in `t` was reached in exactly `ans` moves. States are never mixed across distances.

The mask is checked before energy:

`if mask == 0: return ans`.

This ordering is important. The final move may collect the last litter while reducing energy to zero. That state is still a successful answer and must be returned even though it cannot make another ordinary move.

**Energy transitions**

A state with `cur_energy <= 0` cannot leave its current cell, so the source skips expansion.

For a legal neighboring cell:

- if it is `R`, `nxt_energy` becomes the full original `energy`;
- otherwise, `nxt_energy = cur_energy - 1`.

Moving costs one unit, but stepping onto a reset area immediately restores the capacity regardless of the arrival amount. In particular, a student with one unit left may enter `R` and continue with full energy.

The source never leaves a reset cell represented with zero energy: entering it always stores the full value. A zero-energy non-reset state can occur after moving onto ordinary space or the final litter, and it cannot continue.

Reset cells can be visited repeatedly because they do not have collection bits and their behavior depends only on the state’s other dimensions.

**Legal movement**

The direction array generates the four orthogonal neighbors. A successor must be inside the grid and not equal to obstacle `X`. The starting cell, empty cells, litter cells, and reset cells are all traversable.

After energy and mask updates, a successor is appended only if the exact state has not been seen. Since future behavior depends only on these state components, revisiting an identical state cannot reveal a new route. BFS reached it at an equal or smaller number of moves already.

**Why the first completed state is optimal**

All edges in the state graph represent one physical move and have equal cost. BFS examines states in nondecreasing move count. Therefore, when a zero mask is found in layer `ans`, no route with fewer moves remains unexplored.

Different routes may reach the same litter set at different positions and energies; all are represented when distinct. The first completed one across this full state graph is the global minimum, not merely a shortest route for one chosen litter order.

If the queue empties, every reachable state has been explored without clearing the mask. No legal route can collect all litter, so the source returns `-1`.

**A reset example**

Suppose a route reaches a reset cell with one unit remaining. The move into that cell creates a state with full capacity, not zero. From there, BFS can continue toward distant litter.

This modeling also prevents an invalid shortcut: future sale-like resources do not exist here, and energy is restored only when the destination character is exactly `R`.

## Complexity detail

Let `L` be the number of litter cells and `E` the maximum energy. There are at most

$$
mn(E+1)2^L
$$

distinct states. Each examines at most four neighbors, so worst-case time is `O(mnE2^L)`.

The four-dimensional visited structure explicitly allocates one Boolean slot for every such combination, and the BFS frontier can also contain a large fraction of the state space. Space is `O(mnE2^L)`.

This matches the manifest bounds, but not its dominance-summary wording. If only the greatest energy for each `(cell,mask)` were retained, state storage could fall toward `O(mn2^L)`; the exact implementation does not do that.

At maximum constraints, the explicit Python nested-list representation can be memory-heavy because Boolean list entries are object references rather than packed bits. The asymptotic bound captures this large product, and a dominance table or compact array would be a practical improvement.

## Alternatives and edge cases

- **Dominance pruning by maximum energy:** At the same position and mask, a state with more remaining energy can reproduce every continuation available to one with less. Storing only the maximum energy can reduce memory and repeated work; this is advertised by the manifest but absent from the source.
- **Shortest paths between special cells plus subset DP:** One can precompute energy-aware reachability among start, litter, and reset locations, then solve a smaller mask problem. Reusable resets make the compressed transitions more subtle than ordinary pairwise distances.
- **Priority-queue search:** Dijkstra’s algorithm is unnecessary because every physical move costs one; BFS has simpler ordering and lower overhead.
- **No litter:** The source returns zero before allocating the state space.
- **Last litter reached with zero energy:** Success is checked before expansion eligibility, so the route is accepted.
- **Zero energy away from a reset:** The state cannot move and is safely discarded.
- **Entering a reset with one energy:** The destination immediately restores full capacity, allowing further movement.
- **Repeated reset visits:** They are allowed; only an identical full state is suppressed by `vis`.
- **Litter revisited:** Its bit is already clear, so the mask remains unchanged.
- **Obstacle-separated litter:** If no state can reach it, BFS exhausts and returns `-1`.
- **Start next to litter:** The first next-layer state clears that bit and may finish in one move.
- **Different litter orders:** The mask lets BFS explore all reachable orders without prescribing one.
- **Exactly ten litter cells:** The mask has 1024 possibilities, which is why the energy and grid dimensions make careful state representation important.
- **Input preservation:** Litter collection is represented in the mask; the immutable classroom strings are never modified.
