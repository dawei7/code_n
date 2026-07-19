## General
**Choose a column maximum.** Binary-search the column range. In the middle column, scan all $m$ rows and select a row containing that column's maximum. Because vertically adjacent values are unequal, this cell is strictly larger than its existing upper and lower neighbors.

**Follow a larger horizontal neighbor.** Compare the selected value with the cells immediately left and right, using $-1$ beyond a boundary. If it exceeds both, it is also horizontally dominant and therefore is a peak. If the right neighbor is larger, discard the middle column and everything left of it; repeatedly moving toward larger values on that side must eventually reach a peak. Otherwise the left neighbor is larger, and the symmetric argument permits discarding the middle and right side.

Each decision preserves at least one peak in the retained columns. The interval shrinks by half, and selecting a column maximum guarantees that the returned coordinate satisfies all four strict comparisons.

## Complexity detail
Let $m$ and $n$ be the row and column counts. Each of $O(\log n)$ binary-search iterations scans one full column in $O(m)$ time, for $O(m\log n)$ total time. Only indices and neighboring values are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Scan every cell:** Checking all four neighbors finds a valid peak but costs $O(mn)$ time and violates the requested bound.
- **Binary-search rows:** The transposed method scans a row maximum per iteration and runs in $O(n\log m)$ time.
- **Multiple peaks:** Any valid coordinate is correct; output must be validated semantically rather than against one fixed reference coordinate.
- **Single cell:** With only the $-1$ perimeter as neighbors, `[0, 0]` is a peak.
- **Single row or column:** The same search reduces to the ordinary one-dimensional peak argument.
- **Strictness guarantee:** Adjacent inequality prevents a column maximum from tying its vertical neighbor and avoids plateaus during directional reasoning.
