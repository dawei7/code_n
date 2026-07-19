## General
**Flood inward from every escape boundary**

All boundary cells can release water directly, so mark them visited and insert them into one min-heap keyed by their effective boundary height. This creates a multi-source frontier around the unprocessed interior.

**Always expand the lowest known containment wall**

Pop the frontier cell with minimum effective height. For each unvisited neighbor, that wall can hold water up to its height. If the neighbor's terrain is lower, add the difference to the volume. The neighbor then joins the frontier at `max(wall_height, terrain_height)` because trapped water raises its effective surface to the wall.

**Why a later route cannot lower a finalized level**

The heap processes effective boundaries in nondecreasing order. When a cell is first reached from the minimum frontier, every alternate path to the exterior must cross either that frontier height or a boundary not yet popped and therefore no lower. Its assigned level is thus the minimum possible maximum elevation on any escape path—the exact water surface limit for that cell.

**Visit each cell only once**

Mark a neighbor when it enters the heap, not when it leaves. Its first candidate comes from the globally smallest available boundary and is already optimal by the minimax argument, so duplicate entries and later relaxation are unnecessary.

## Complexity detail
Let `r` and `c` be the matrix dimensions. Each of the `rc` cells enters and leaves the heap once, with $O(\log(rc))$ heap work, for $O(rc \log(rc))$ time. The heap and visited matrix use $O(rc)$ space.

## Alternatives and edge cases
- **Independent minimax search from every interior cell:** computes correct escape levels but repeats graph work and can take $O((rc)^2 \log(rc))$ time.
- **Iterative level-by-level flooding:** can revisit the grid once per height level and depends on the numeric height range.
- **Apply one-dimensional trapping by rows and columns:** is incorrect because water can escape along winding two-dimensional paths.
- Fewer than three rows or columns cannot enclose water.
- Boundary cells never trap water above themselves.
- A low boundary leak can drain an otherwise high basin.
- Nested terrain walls are handled by propagated effective heights.
