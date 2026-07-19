## General
**View downward gravity before rotation**

After a clockwise rotation, falling downward corresponds to moving right in
each original row. Obstacles divide a row into independent segments: stones
within one segment pack against its right boundary without crossing an
obstacle.

**Write settled cells directly into rotated coordinates**

Create an $n \times m$ result filled with empty cells. Scan each original row
from right to left while tracking the rightmost available landing column.
When an obstacle appears at column `c`, place it at its rotated coordinate and
reset the landing column to `c - 1`. When a stone appears, place it at the
rotated coordinate corresponding to the current landing column, then decrement
that pointer. Empty cells need no action.

The scan encounters stones from rightmost to leftmost, so each stone receives
the rightmost unoccupied cell in its obstacle-delimited segment. That is
exactly where gravity leaves the stones. Original coordinate $(r,c)$ maps to
rotated coordinate $(c,m-1-r)$, so writing every obstacle and settled stone
through this mapping constructs the required orientation without a second
matrix rotation.

## Complexity detail
Every one of the $N=mn$ source cells is inspected once and every nonempty
result cell is written once, for $O(N)$ time. The returned $n \times m$ matrix
uses $O(N)$ space; aside from that output, the landing pointer and loop indices
use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Settle then rotate:** modifying a copy row by row and rotating it afterward
  is also $O(N)$, but it performs two distinct matrix passes.
- **Move each stone one cell repeatedly:** this direct simulation is correct
  but can take $O(mn^2)$ time when many stones cross long empty suffixes.
- Obstacles reset the landing pointer and can never be overwritten or crossed.
- A row containing only empty cells remains empty after rotation.
- One-row and one-column boxes still swap dimensions according to the same
  coordinate mapping.
