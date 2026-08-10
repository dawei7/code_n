## General

All sources begin at time zero, and every spread crosses one orthogonal grid edge per time step. This is exactly the setting for multi-source breadth-first search.

The complication is the tie rule. A cell reached by several colors during the same time step must receive the greatest of those colors. The source processes one complete BFS layer at a time, gathers every proposal for the next layer in a dictionary, and commits colors only after all proposals from the current layer have been seen.

**Distance determines the arrival time**

In an obstacle-free rectangular grid, the shortest number of orthogonal moves from source $(r_s,c_s)$ to cell $(r,c)$ is the Manhattan distance

$$
|r-r_s|+|c-c_s|.
$$

Because all sources start together and colors advance one edge per step, a cell's first coloring time is its minimum Manhattan distance to any source.

Sources farther away cannot overwrite it later, because spreading applies only to uncolored cells. Among sources at the same minimum distance, all arrivals occur simultaneously, and the maximum source color must win.

The BFS does not calculate these distances explicitly. Layer number represents time, and the per-layer maximum aggregation implements the equal-distance tie rule.

**Initializing all sources as one layer**

The answer matrix `ans` begins with zeros. Every source coordinate receives its positive initial color.

The source then sets

```text
q = sources
```

so the initial frontier contains all time-zero cells. Starting with every source in one queue is what makes the search multi-source rather than running one flood fill after another. Sequential single-source fills would incorrectly let whichever source ran first claim cells before simultaneous competitors were considered.

The value zero safely means “uncolored” because every allowed source color is positive.

**Enumerating four orthogonal neighbors**

The tuple

```text
dirs = (-1, 0, 1, 0, -1)
```

contains the coordinate offsets in cyclic form. Consecutive pairs are

$$
(-1,0),\ (0,1),\ (1,0),\ (0,-1),
$$

representing up, right, down, and left.

For every current frontier entry $(r,c,\text{color})$, the source checks those four neighbors. It discards:

- coordinates outside rows $0..n-1$ or columns $0..m-1$; and
- cells whose `ans` entry is already nonzero.

The second rule enforces first-arrival permanence. A cell colored in an earlier BFS layer has a strictly shorter route from some source and cannot be changed by a later arrival.

**Why proposals are not written immediately**

Within one time step, iteration order must not decide ties. Suppose two frontier cells propose colors 3 and 5 for the same still-uncolored neighbor. If color 3 were written to `ans` immediately, the later proposal would see an already-colored cell and be ignored, producing the wrong result.

Instead, `vis[(x, y)]` stores the greatest proposal seen for each next-layer coordinate:

$$
\texttt{vis}[(x,y)]
=
\max(\text{existing proposal},\text{current color}).
$$

The `defaultdict(int)` initial value is zero, smaller than every legal color. Multiple proposals from the same or different colors collapse into one coordinate entry holding the correct maximum.

Only after every current-layer node has proposed does the source copy `vis` entries into `ans` and form the next frontier. This is a faithful simulation of simultaneous spreading.

**Why every committed cell has its final color**

Assume `q` contains exactly the cells first colored at time $t$, with their final tie-resolved colors. Every uncolored neighbor is reachable at time $t+1$. The dictionary sees all such edges from the entire layer and assigns each coordinate the maximum color among all time-$t$ predecessors.

Could another source also arrive at time $t+1$ through a different shortest path? Its time-$t$ predecessor is also in `q`, so its proposal is included. Could a higher color arrive later? Yes, but later arrival cannot color an already-colored cell under the rules.

Thus the committed `vis` entries are exactly the cells first colored at time $t+1$, and their stored colors are final. This establishes the same property for the next layer.

Since the grid is connected through orthogonal moves and at least one source exists, repeated layers eventually color every cell.

**A tie example**

In a $3\times3$ grid with color 1 at $(0,0)$ and color 2 at $(2,2)$, cells $(0,2)$, $(1,1)$, and $(2,0)$ are distance two from both sources.

They remain uncolored through time one. During the time-two proposal phase, each receives proposals 1 and 2 before any result is committed. `vis` keeps 2, so all three receive the required maximum color.

**The observable queue alias**

The assignment `q = sources` does not copy the list. Both names refer to the same list object. At the end of every layer, the source calls `q.clear()` and appends the next frontier into that same object.

After the final frontier is processed, `q.clear()` leaves it empty and no next entries are appended. Therefore the caller-provided `sources` list is emptied as a side effect. This does not change the returned grid, but it is part of the exact checked-in implementation and callers cannot rely on retaining their input list.

## Complexity detail

Let $V=nm$ be the number of cells. Every cell enters a frontier at most once because it is committed to `ans` only while uncolored. When active, it inspects four neighbors. The total graph work is

$$
O(V+4V)=O(nm).
$$

A coordinate may receive several proposals in one layer, but a grid cell has at most four neighbors, so this remains constant work per grid edge.

The output matrix uses $O(nm)$ space. The current frontier and the `vis` proposal dictionary can each contain $O(nm)$ cells in the worst case, although they are replaced layer by layer. Total auxiliary storage is

$$
O(nm).
$$

The number and magnitude of colors do not affect the asymptotic cost. A tie is resolved with one integer `max` operation.

The source reuses `sources` as frontier storage rather than allocating a separate initial queue, but that saves only a constant-factor allocation and causes the input-mutation behavior described above.

## Alternatives and edge cases

- **Immediate neighbor coloring:** Writing proposals directly into `ans` makes results depend on frontier iteration order and violates simultaneous maximum-color tie resolution.
- **Priority queue by distance and color:** Ordering states by minimum distance and then maximum color can solve the same nearest-source problem, but costs $O(nm\log(nm))$ instead of layered linear BFS.
- **Run one BFS per source:** This repeats grid work and requires later distance comparisons; multi-source initialization shares the traversal.
- **Single source:** No ties are possible, and its color eventually fills the connected grid.
- **Source coordinates are distinct:** Initialization never needs to resolve two colors already occupying the same cell.
- **Adjacent sources:** Each is already colored at time zero and cannot be overwritten by the other at time one.
- **Equal-distance tie:** `vis` keeps the numerically largest proposal, regardless of proposal order.
- **Later higher color:** It cannot replace a cell claimed earlier because spreading targets only uncolored cells.
- **Positive-color guarantee:** `ans[x][y] == 0` unambiguously means uncolored; allowing source color zero would break this test.
- **One-row or one-column grid:** The same four-direction loop works; out-of-bounds checks discard the unavailable directions.
- **Input-list destruction:** Because `q` aliases `sources` and is repeatedly cleared, `sources` is empty when the method returns.
- **Required helpers:** Standalone execution needs `defaultdict` and `pairwise` from the Python standard library.
