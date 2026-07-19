## General
**Treat walls as segment boundaries**

Within a row, every empty cell between the same two walls sees the same horizontal enemies. The analogous statement holds for a column segment. Instead of scanning outward from every possible bomb position, count each wall-delimited segment once and reuse that count for all of its empty cells.

**Refresh row and column counts only at segment starts**

Scan the grid row by row. Recompute the current row-segment enemy count when the column is zero or the cell immediately to the left is a wall; scan right until the next wall. Maintain one cached enemy count per column, and recompute a column's current segment when the row is zero or the cell above is a wall by scanning downward to the next wall.

At an empty cell `(r,c)`, `row_hits + column_hits[c]` is exactly the number killed by a bomb there. Update the maximum only for `"0"` cells.

**Why the two cached counts include every legal target once**

A blast travels horizontally and vertically until a wall. The cached row count enumerates precisely the enemies in the empty cell's horizontal wall-delimited segment, and the cached column count does the same vertically. Their cells intersect only at the bomb position, which is empty, so no enemy is double-counted. Since every legal placement is evaluated during the scan, the largest sum is the optimal result.

**Trace the central placement**

In the first example, the empty cell at row 1, column 1 shares its horizontal segment with the enemy at column 0 and its vertical segment with enemies above and below. The wall at column 2 blocks the row's right-side enemy, so the total is exactly three.

## Complexity detail
Let `m` and `n` be the row and column counts. Although segment refreshes contain short scans, each row segment is counted once and each column segment is counted once, so the total work is $O(mn)$. The column cache uses $O(n)$ space; the row count and loop indices use $O(1)$.

## Alternatives and edge cases
- **Scan four rays from every empty cell:** is easy to derive but can cost $O(mn(m+n))$ on a wall-free grid.
- **Four directional prefix matrices:** answers each placement in constant time after preprocessing but uses $O(mn)$ extra space.
- **Count all rows and columns globally:** fails when walls split a line into independent blast segments.
- A wall stops both horizontal and vertical propagation and is never counted.
- An enemy cell cannot be selected as the bomb location.
- A grid with no empty cells returns `0`.
- Empty rows or an empty grid are handled as having no legal placement.
