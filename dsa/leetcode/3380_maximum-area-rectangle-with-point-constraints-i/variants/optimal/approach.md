## General

**Treat each point pair as possible opposite corners.** An axis-aligned rectangle is determined by two diagonal corners with different $x$- and $y$-coordinates. The nested loops consider every unordered pair once by pairing current point with `points[:i]`.

For a pair, the source normalizes bounds:

$$
x_{\min}=\min(x_1,x_2),\quad x_{\max}=\max(x_1,x_2),
$$

and similarly for $y$. This makes the later test independent of which diagonal orientation was selected.

The code does not explicitly reject pairs sharing a row or column. Such degenerate boxes cannot contain four unique corner points, so `check` returns false through its final corner count.

**Scan the inclusive bounding box.** `check(x1,y1,x2,y2)` examines every given point. A point outside at least one bound is irrelevant and skipped.

For a point inside or on the box, the only allowed locations are the four corner combinations. Condition

`(x == x1 or x == x2) and (y == y1 or y == y2)`

recognizes those combinations and increments `cnt`. Any other point is either strictly inside or lies on a non-corner border position, both forbidden by the statement, so the function immediately returns false.

**Require all four corners.** After the scan, `cnt == 4` proves that four unique input points occupy the four corner combinations. Points are globally unique, so the count cannot be inflated by duplicate copies of one coordinate.

This corner-count test replaces a separate hash lookup for the other two corners. The manifest says corners are verified by hash lookup, but the exact source uses only this full scan.

When width and height are positive, there are exactly four possible endpoint combinations, so a count of four also proves that none is missing. When either dimension is zero, there are only two distinct combinations, making four impossible under the uniqueness guarantee.

**Why an accepted box is a valid rectangle.** Four distinct corner points imply both width and height are positive. The early rejection guarantees no fifth point lies anywhere in the inclusive rectangle. Therefore all geometric requirements hold.

**Why every valid rectangle is considered.** A valid rectangle has two diagonal pairs. At least one—and actually both—appears among the unordered point pairs. Normalizing either diagonal produces its exact bounds, and `check` accepts because precisely its four corners lie in the box. The area is therefore offered to `ans`.

**Compute and maximize area.** For accepted bounds, area is

`(x4 - x3) * (y4 - y3)`.

`ans` starts at `-1`, the required result when no candidate succeeds. Every real rectangle has positive area, so the sentinel cannot conflict with an accepted value.

**Trace an interior obstruction.** With four corners at $(1,1),(1,3),(3,1),(3,3)$ and extra point $(2,2)$, a diagonal pair produces bounds $[1,3]\times[1,3]$. The fifth point is within all bounds but has neither boundary $x$ nor boundary $y$, so `check` returns false before area update.

**Trace a border obstruction.** A point $(1,2)$ has boundary $x=1$ but non-endpoint $y=2$. The corner predicate requires both a boundary $x$ and endpoint $y$, so it is rejected just like an interior point.

**The exact implementation is exhaustive rather than hash-assisted.** Each candidate pair triggers a scan of the full point list. The small constraint $n\le10$ makes this clear method appropriate, but the data flow differs from the manifest summary.

## Complexity detail

There are $O(n^2)$ unordered pairs, and `check` scans $O(n)$ points for each, giving $O(n^3)$ time.

Expression `points[:i]` creates a temporary slice for each outer iteration. Its maximum size is $O(n)$ and cumulative copying is $O(n^2)$, dominated by cubic checking time. Peak auxiliary space is $O(n)$ because of the slice; without slicing, indexed loops could make auxiliary space $O(1)$. The manifest's $O(n)$ space bound matches this exact Python detail.

## Alternatives and edge cases

- **Corner hash set:** It can test the other two corners in expected $O(1)$, but forbidden-point scanning still remains unless extra geometry structures are used.
- **Enumerate two x-levels and two y-levels:** It generates coordinate boxes but can examine many combinations absent from the points.
- **Prefix grid:** Coordinates are small enough for a dense count grid, though coordinate compression is more general.
- **Fewer than four points:** No check can reach corner count four, so return `-1`.
- **Pair on one vertical line:** The degenerate box has at most two unique corners and fails.
- **Pair on one horizontal line:** It fails symmetrically.
- **Interior point:** It invalidates the rectangle.
- **Non-corner border point:** It also invalidates the rectangle.
- **Point outside bounds:** It has no effect.
- **Two diagonal pairs:** The same rectangle may be checked twice, but maximum area is unchanged.
- **Unique-point guarantee:** It makes `cnt == 4` equivalent to four distinct corners.
- **Positive dimensions:** They follow implicitly from reaching four unique endpoint combinations.
- **Tied maximum areas:** Only the numeric maximum is returned.
- **No hash lookup:** The exact source discovers all corners during the scan.
- **Sentinel `-1`:** Every valid area is positive.
- **Input preservation:** Slices copy references; point coordinates are unchanged.
