## General

**Encode the only three cell states needed**

The grid `g` begins with zeros:

- zero means empty and not yet known to be guarded;
- one means an empty cell seen by at least one guard;
- two means an obstruction, either a guard or a wall.

Both guards and walls receive value two because both stop line of sight. The separate `guards` input is retained so only actual guards cast rays.

**Generate the four cardinal directions**

`dirs = (-1, 0, 1, 0, -1)` and `pairwise(dirs)` produce:

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`.

These are north, east, south, and west. No diagonal direction is generated.

**Cast one ray until an obstruction**

For every guard and direction, `x,y` begins at the guard position. The while condition examines the next cell:

- it must remain inside the grid;
- `g[next] < 2` means it is not a guard or wall.

The ray advances and assigns `g[x][y] = 1`. A previously guarded cell already has one and may be assigned one again. It does not stop sight, which is correct: visibility from one guard is not an obstacle to another.

The loop stops at the boundary or before a value-two cell. It never overwrites guards or walls.

**Why every marked cell is guarded**

A marked cell lies on a straight cardinal ray beginning at a guard. Every cell before it on that ray passed the `< 2` test, so no wall or guard blocks the line. The guard can see the cell, making state one valid.

**Why every guarded empty cell is marked**

If an empty cell is visible from a guard, it lies in one of the four generated directions and no obstruction occurs between them. The corresponding ray advances through every intermediate cell until at least that position and sets it to one.

Thus, state zero after all rays means precisely “unoccupied and unseen.”

**Count only remaining zeros**

The final generator flattens rows and sums `v == 0`. Python Booleans contribute one for each zero state.

Value-one cells are occupied by no object but guarded, so they are excluded. Value-two guards and walls are occupied and also excluded. The result is exactly the number of unoccupied, unguarded cells.

**Why repeated rays remain linear overall**

The exact implementation casts rays from guards rather than using the editorial's four full-grid sweeps. A naive bound might multiply every guard by row and column length, but obstructions limit repetition.

Within one row, guards and walls divide empty cells into segments. A segment can be traversed horizontally only from a guard at its left boundary and/or a guard at its right boundary, at most twice. Any farther guard is blocked by the nearer boundary object. The same argument applies vertically.

Therefore, each empty cell is visited at most twice horizontally and twice vertically across all guards. Total ray work is `O(mn)` despite the per-guard loops.

**Trace obstruction behavior**

If a wall stands east of a guard, cells before the wall become one, the wall remains two, and the loop stops without marking anything beyond it.

If another guard is encountered, it similarly stops the ray. That other guard will cast its own rays separately.

**Exact implementation versus manifest summary**

The manifest summary says every row and column is swept in both directions. The stored code instead performs guarded ray casts. Both yield the same state classification and linear bound under the segment argument, but the data flow explained here matches the exact solution.

The input coordinate arrays remain unchanged.

## Complexity detail

Initializing `g` takes `O(mn)` time and space. Marking `G` guards and `W` walls takes `O(G + W)`.

By the row/column segment argument, all ray traversal is `O(mn)`. The final count is another `O(mn)` scan. Total time is `O(mn + G + W)`, which simplifies to `O(mn)` because occupied positions are bounded by grid cells.

The state grid uses `O(mn)` space. Direction and loop variables use constant additional space.

## Alternatives and edge cases

- **Four whole-grid sweeps:** Carry active visibility across rows and columns, resetting at walls and guards. It is also `O(mn)` and matches the manifest summary.
- **Cast rays without treating guards as blockers:** That violates the contract; value two stops at both object types.
- **Stop at already guarded cells:** Guarded emptiness is not an obstruction. Stopping there would miss cells farther along the same line.
- **Use a visibility set:** It can work but still needs obstacle handling and has more hashing overhead than a state grid.
- **Cell seen by several guards:** Reassigning one is harmless and it is counted as guarded once.
- **Guard surrounded by walls:** All four rays stop immediately.
- **One-row grid:** Horizontal rays work normally; vertical directions fail bounds.
- **One-column grid:** The symmetric case is handled.
- **Adjacent guard or wall:** The next-cell test stops before entering it.
- **Occupied cells:** Both guards and walls use state two and never count as unguarded.
- **No line of sight to an empty cell:** It remains zero and contributes one.
- **Input preservation:** Only the newly allocated state grid is modified.
