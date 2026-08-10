## General

**Use the API to discard large empty regions**

Checking every integer coordinate would exceed the four-hundred-call limit. The API is powerful because one call answers whether an entire inclusive rectangle contains at least one ship. The solution recursively divides only rectangles known to contain ships, while empty rectangles stop immediately.

Function `dfs(topRight, bottomLeft)` first extracts inclusive bounds `x1, y1, x2, y2`. Some quadrants of a thin rectangle can be invalid, so `x1 > x2 or y1 > y2` returns zero before calling the API. This ordering avoids unauthorized or meaningless queries with reversed corners.

For a valid rectangle, `sea.hasShips` is called. A false result proves the count is zero and prunes every coordinate inside. If the rectangle is one point and the API has returned true, that point contains exactly one ship because the contract allows at most one per integer point.

**Partition an inclusive rectangle without gaps or overlaps**

For a nonempty rectangle containing more than one point, midpoint coordinates are floor averages. The four recursive rectangles are:

- northeast: from `(midx + 1, midy + 1)` to the original top right;
- northwest: from `(x1, midy + 1)` to `(midx, y2)`;
- southwest: from the original bottom left to `(midx, midy)`;
- southeast: from `(midx + 1, y1)` to `(x2, midy)`.

The `+1` boundaries are essential for inclusive coordinates. Every x-coordinate belongs either to the left half through `midx` or the right half starting at `midx + 1`, and the same holds for y. Combining those choices creates four disjoint quadrants whose union is the original rectangle.

When one dimension has length one, two quadrant descriptions become invalid. The initial bound check returns zero for them without consuming API calls, while the valid halves still cover the rectangle.

**Why summing recursive answers is correct**

An empty rectangle returns zero by authoritative API evidence. A nonempty single point returns one. Otherwise, every ship belongs to exactly one of the four disjoint quadrants. By recursively counting each quadrant and summing `a + b + c + d`, the algorithm counts every ship once and none twice.

The recursion eventually terminates because every valid child is strictly smaller in at least one non-single dimension. Repeated halving reaches individual points.

The method never tries to inspect hidden ship coordinates directly. `Point` objects only describe query corners, and `hasShips` is the sole observation of the sea, respecting the interactive contract.

**Corner order is part of every recursive call**

Each call receives the upper-right point first and lower-left point second, matching the API. The four constructions preserve that order for valid quadrants. For example, the northwest region uses upper right `(midx, y2)` and lower left `(x1, midy + 1)`. When a dimension is too thin, those values may reverse, but the explicit invalid-bound test catches that before constructing an API query. Keeping coordinate meaning consistent is especially important here because swapping two `Point` arguments could make an empty region appear ordered incorrectly or ask the hidden service about the wrong rectangle.

**Why the query budget remains small**

An empty quadrant ends after one API call. Only quadrants containing ships keep branching. With at most `s = 10` ships, at most `s` regions at a given sufficiently separated level can be nonempty. Each nonempty region creates four child calls, while side lengths halve at every level.

With coordinate span at most about one thousand per dimension, recursion depth is around ten. The resulting bound is on the order of four times the number of ships times the logarithmic depth, within the stated four-hundred-call budget; the tighter distribution analysis in the editorial gives fewer than that maximum for the allowed domain.

## Complexity detail

Let $s$ be the number of ships and let $C$ be the larger inclusive side length. Empty input still causes one API query. In general, only branches containing ships continue for $O(\log C)$ levels, with a constant number of empty siblings per continuing branch. Time and API calls are $O(1+s\log C)$, commonly written $O(s\log C)$ when $s>0$.

The recursive call stack follows one quadrant at a time and has depth $O(\log C)$. Aside from stack frames and constant-size `Point` objects, no growing structure is retained, so auxiliary space is $O(\log C)$.

The method's meaningful cost is API calls rather than arithmetic. Each call performs constant local computation under the interactive model.

## Alternatives and edge cases

- **Check every coordinate:** It is exact but may require about a million API calls and violates the limit.
- **Split into two rectangles:** Binary partitioning is also possible; four-way splitting halves both dimensions together and matches the sparse two-dimensional geometry well.
- **Call API before validating bounds:** This can send reversed rectangles created by thin quadrants and must be avoided.
- **Empty target rectangle:** Public corners are ordered, but recursive empty quadrants correctly return zero without an API call.
- **No ships:** The initial `hasShips` call is false, so the answer is zero immediately.
- **Single-point recursive region:** A true API result means exactly one ship; further subdivision is unnecessary.
- **Ship on a midpoint boundary:** Inclusive half definitions assign it to exactly one side because the other begins at midpoint plus one.
- **One-row or one-column region:** Invalid quadrants vanish, and valid halves continue reducing the remaining dimension.
- **Ships on outer boundaries:** `hasShips` includes rectangle boundaries, and the partition covers them.
- **API call limit:** Pruning empty regions is essential; recursion without the initial existence query would still explore every point.
