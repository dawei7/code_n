## General
**Why only sorted neighbors matter**

Order the positions increasingly. If two positions have another stored position between them, then at least one of the two smaller adjacent gaps is no greater than the outer pair's distance. Consequently, a globally closest pair must occur between consecutive values in sorted order.

**Expose the preceding position**

Use `LAG(x)` over `ORDER BY x` to attach each row's immediate predecessor. The first sorted row has no predecessor and contributes no pair; every other row contributes exactly one adjacent difference `x - previous_x`.

**Select the smallest adjacent gap**

Take `MIN` over those differences. Unique positions make every difference positive. Because the adjacent pairs include at least one globally closest pair and no computed difference represents anything other than a valid pair, the minimum is exactly the requested distance.

## Complexity detail
Sorting `P` positions for the window costs $O(P \log P)$ time and $O(P)$ execution space. Computing predecessor values, differences, and their minimum is linear after the sort and does not change those bounds.

## Alternatives and edge cases
- **All-pairs self-join:** compute `ABS(first.x - second.x)` for every distinct pair and take the minimum; it is direct but costs $O(P^2)$ time.
- **Correlated next-position lookup:** find the least larger value for every point; a suitable index can make this efficient, but without one repeated scans may be quadratic.
- **Procedural sorted scan:** outside SQL, sort once and scan adjacent differences with the same $O(P \log P)$ time bound.
- Negative and positive coordinates use the same sorted-difference logic.
- With exactly two positions, their one adjacent gap is returned.
- Input positions are unique, so the shortest distance cannot be zero.
- Input row order has no effect because the window defines its own ordering.
