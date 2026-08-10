## General

**Water is limited by the lowest escape boundary**

In one dimension, left and right maxima are enough. In a two-dimensional grid, water can escape along many winding paths to the outside, so four independent directional maxima do not solve the problem.

The key is to flood inward from the outer boundary. Every boundary cell can leak directly out of the map and therefore cannot hold water above its own terrain. As interior cells are reached, the lowest currently known enclosing boundary determines how high water can stand there.

A min-heap always processes the lowest effective boundary cell first. This is analogous to Dijkstra’s algorithm, but the path cost is the maximum height encountered along an escape path rather than a sum of edge weights.

**What a heap height means**

Each heap entry is `(h, row, column)`. The value `h` is not always the cell’s original terrain height. It is the effective boundary level carried into that cell:

- if the terrain is at least the incoming boundary, `h` is the terrain height;
- if the terrain is lower, water fills it to the incoming boundary, so `h` is that water-surface height.

This effective height is what can constrain neighboring cells. A filled depression behaves like boundary at its water surface, not like a hole at its original floor.

**Initialize every outer cell**

The nested initialization loops push every cell in the first row, last row, first column, or last column. They also mark it visited.

Because each coordinate is encountered once by the nested loops, corners are pushed only once even though each corner satisfies two boundary conditions.

These cells begin with their terrain heights. They form the initial frontier between the known outside and the unprocessed interior. Starting anywhere else would assume a containment level before proving how that region connects to an escape edge.

**Always expand the lowest frontier first**

The heap pops the entry with smallest `h`. Suppose it pops cell `(i, j)` with effective height `h`. For every unvisited orthogonal neighbor `(x, y)`, compare terrain `heightMap[x][y]` with `h`.

If the neighbor is lower than `h`, water is trapped there up to level `h`. Its contribution is

$$
h-\texttt{heightMap}[x][y].
$$

If the neighbor is at least `h`, it holds no water from this boundary. The expression

```text
max(0, h - heightMap[x][y])
```

handles both cases and is added to `ans`.

The neighbor then joins the heap with effective height

$$
\max(h,\text{terrain height}).
$$

This carries the current wall level across a low cell and raises the frontier when a taller cell is encountered.

**Why a low cell does not lower the future boundary**

Imagine a basin floor of height two behind an enclosing wall of height five. The floor traps three units of water. After filling, adjacent cells do not see an escape route of height two through that floor; they see water standing at height five. Pushing the neighbor with raw height two would incorrectly let later water leak through it.

Using `max(h, terrain)` records the stabilized surface or wall height and preserves containment for further inward expansion.

**Why the minimum heap order is essential**

A cell’s water level is governed by the lowest possible maximum height along any path from that cell to the outer boundary. If there is an escape path whose highest barrier is three, a different surrounding wall of height ten cannot make the cell hold water to ten; it leaks along the lower path.

Processing the smallest frontier first ensures the first route that reaches a cell has the smallest attainable escape-boundary level. A higher frontier cannot later improve that level.

This is the minimax counterpart of Dijkstra’s rule: when the smallest tentative effective height is popped, it is final.

**Why marking visited on insertion is safe**

The exact code marks a neighbor visited as soon as it is pushed, not when it is later popped.

At discovery time, the parent is the globally smallest heap frontier. Any other undiscovered route to the same cell must pass through a frontier whose effective height is no smaller. Taking `max` with the cell’s fixed terrain cannot make that alternative candidate lower. Thus the first inserted effective height is already minimal, and duplicate insertions are unnecessary.

Marking immediately also guarantees every cell contributes water at most once.

**Direction encoding**

`dirs = (-1, 0, 1, 0, -1)` combined with `pairwise(dirs)` produces:

```text
(-1, 0), (0, 1), (1, 0), (0, -1)
```

These are up, right, down, and left. Diagonal cells do not share an edge and are not direct water-flow neighbors.

Bounds checks ensure only coordinates inside the matrix are considered, and `not vis[x][y]` prevents reprocessing.

**A small basin example**

Consider

```text
3 3 3
3 1 3
3 3 3
```

All eight boundary cells enter the heap at height three. When any adjacent boundary cell is popped, it discovers the center terrain at height one. The center traps `3 - 1 = 2` units and enters the heap at effective height three. No other route can lower that level, and the final answer is two.

If one boundary value were zero, that low boundary would pop first and propagate a low escape level inward. The center would not be incorrectly filled behind the higher walls because water can escape through the zero opening.

**The boundary invariant**

At every point, visited cells have finalized minimum escape-boundary levels. Heap entries form the active boundary between finalized and unvisited cells, keyed by those effective levels.

Popping the minimum and relaxing each unvisited neighbor finalizes the least possible maximum barrier to that neighbor. The water above it is exactly the positive difference between that finalized level and its terrain. Pushing the maximum of terrain and incoming level preserves the correct boundary for subsequent cells.

Eventually every cell is visited. Boundary cells contribute zero, and every interior cell contributes exactly its stable trapped depth. Summing these depths gives the total volume because each unit cell has area one.

## Complexity detail

Let $r$ be the number of rows, $c$ the number of columns, and $N=rc$ the number of cells.

Every cell is marked once and pushed into the heap once. It is also popped once, and at most four neighbors are examined. Heap insertion and removal cost $O(\log N)$, so total time is

$$
O(N\log N)=O(rc\log(rc)).
$$

The visited matrix contains $N$ Booleans. The heap can also contain $O(N)$ entries. Auxiliary space is $O(N)=O(rc)$.

The result may sum water across many cells, but Python integers avoid overflow. In fixed-width languages, the maximum possible volume should be checked against the chosen integer type.

## Alternatives and edge cases

- **Four directional maxima:** The 1D trapping-water technique does not capture winding escape paths in two dimensions. A cell can leak around a high wall through a lower route.

- **Repeated global relaxation:** One could iteratively lower tentative water levels until stable, but this revisits cells many times. The min-heap finalizes levels in the correct order.

- **Minimax Dijkstra formulation:** Define each cell’s cost as the minimum possible maximum terrain height on a path to the boundary. Standard Dijkstra relaxation uses `max(current_cost, neighbor_height)`. This is exactly the effective-height algorithm described here.

- **Single row or single column:** Every cell is on the boundary, so all are initially visited and no water is added.

- **Two rows or two columns:** Again, there is no fully enclosed interior cell, so the result is zero.

- **Flat map:** Every effective height equals terrain height, and every contribution is zero.

- **Low opening in the border:** It enters the heap early and propagates the true spill level, preventing overcounting behind taller boundary sections.

- **Tall interior peak:** Its terrain exceeds the incoming boundary, so it traps no water and enters the frontier at its own taller height.

- **Multiple ponds:** The same global heap handles disconnected depressions; each cell is governed by its own minimum escape path.

- **Mark on push:** This is safe because the first discovery comes from the globally lowest frontier. Marking later would permit duplicate heap entries and require stale-entry checks.

- **No input mutation:** Effective heights live in heap entries; the original `heightMap` remains unchanged.

- **`pairwise` dependency:** The exact source relies on `itertools.pairwise` being available in the execution environment to turn the compact direction tuple into four moves.
