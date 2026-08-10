## General

**Water above a bar is limited from both sides.** At position $i$, define:

$$
L_i=\max_{j\le i}\texttt{height}[j],
\qquad
R_i=\max_{j\ge i}\texttt{height}[j].
$$

The water surface cannot exceed the tallest boundary available on the left or the tallest boundary on the right. Therefore its height is $\min(L_i,R_i)$, and water stored above the current bar is

$$
\min(L_i,R_i)-\texttt{height}[i].
$$

Because both running maxima include the current bar, the minimum is never below the current height, so this quantity is nonnegative without a separate `GREATEST(...,0)`.

**Compute the left maximum with a window.** In CTE `T`,

`MAX(height) OVER (ORDER BY id) AS l`

uses the rows from the start through the current sequential `id` under MySQL's default ordered window frame. Since `id` is unique, `l` is the tallest bar at or left of the current position.

**Compute the right maximum by reversing order.** The second expression orders `id DESC`. In that ordering, rows preceding the current row are geometrically to its right. The running maximum is therefore the tallest bar at or right of the current position, stored as `r`.

No self-join is needed: the window engine derives both boundary arrays while retaining one output row per original bar.

**Sum each position's water.** The outer query applies `LEAST(l,r) - height` and sums it. Every bar has width one, so height difference equals volume at that position. Adding all positions produces the total trapped water.

**A trace of one basin.** For heights `[2,0,1,3]`:

- left maxima are `[2,2,2,3]`;
- right maxima are `[3,3,3,3]`;
- bounded levels are `[2,2,2,3]`;
- water amounts are `[0,2,1,0]`.

The total is three. The first and last positions cannot hold exterior water because one limiting side equals their own height.

**Why local neighbor comparisons are insufficient.** A low bar can hold water because of distant walls even if an adjacent bar is also low. Running maxima retain the strongest boundary anywhere on each side rather than looking at only immediate neighbors.

**Why sequential IDs matter.** The source treats increasing `id` as physical left-to-right order. The reference guarantees sequential order, so no coordinate gaps or duplicate positions complicate the unit-width interpretation.
Any water above $i$ must be contained by some left bar and some right bar, so it cannot exceed the smaller side maximum. Conversely, filling to that smaller maximum is supported on both sides by bars reaching at least that height; lower intermediate bars form the basin. The formula is therefore exact at each position, and summing disjoint unit-width columns gives the exact total.

**Empty-table caveat.** `SUM` over no rows returns null rather than zero. Typical problem inputs contain at least one height row, but the local excerpt does not show a nonempty constraint. The exact source has no `COALESCE` for an empty table.

## Complexity detail

For $N$ bars, the two window functions require ordering by `id` in opposite directions. A typical database plan costs $O(N\log N)$ time and $O(N)$ temporary space. A clustered or indexed `id` may help one direction, though the reverse window or engine materialization can still require work.

The final aggregation is $O(N)$. Logical intermediate CTE output has $N$ rows with two additional maxima.

The query is read-only and returns one aggregate row.

## Alternatives and edge cases

- **Correlated subqueries for each side maximum:** They express the formula directly but may rescan large portions of the table for every bar, causing quadratic work.
- **Self joins and grouping:** Joining all left and right candidates creates large intermediate relations; window maxima are much cleaner.
- **Two-pointer algorithm outside SQL:** In an imperative language it reaches $O(N)$ time and $O(1)$ space, but relational SQL naturally favors windows.
- **Monotonically increasing heights:** Right boundaries never create a basin, so every contribution is zero.
- **Monotonically decreasing heights:** The symmetric result is also zero.
- **Flat plateau:** Both maxima equal the bar height and no water is stored.
- **Interior zero height:** It can hold water up to the smaller surrounding maximum.
- **Current bar included in maxima:** This guarantees nonnegative contributions automatically.
- **Sequential IDs:** Their ordering defines adjacent unit-width bars; the formula relies on it.
- **Empty table:** The exact aggregate returns null, not zero.
- **Width-one assumption:** Each row represents exactly one horizontal unit, so no multiplication by an interval width is needed. Nonuniform or missing positions would require using coordinate differences.
- **Boundary bars:** At the global tallest bar, both directional maxima equal its own height and contribution is zero. Exterior endpoints likewise cannot trap water beyond the landscape.
- **Multiple equal maxima:** Window functions retain the same boundary height across the plateau; basins between equal peaks are handled without selecting a unique wall.
- **No negative correction required:** Since both running maxima include the current row, `LEAST(l,r)` is always at least `height`.
