## General

**View the line as unit segments**

Integer endpoints divide each requested interval into unit segments
`start, start + 1, ..., end - 1`. The answer for a day is the number of these
segments that have not been painted earlier.

**Maintain the next unpainted successor**

Use a dictionary as a disjoint-set successor structure. An absent coordinate
is still unpainted. Once coordinate `x` is painted, store a link from `x` to a
later coordinate. A path-compressed `find(x)` follows these links and returns
the first unpainted coordinate at or after `x`.

For a day `[start, end)`, first find the unpainted coordinate at `end`; every
new segment painted during this day can safely link directly to that successor.
Starting from `find(start)`, count a segment, remember the next unpainted
coordinate, link the current segment past the completed interval, and continue
until the successor is at least `end`.

Every counted segment is inside the current interval and was unpainted, so it
contributes exactly one unit of new area. Every unpainted segment in the
interval is reached in increasing order, while stored links skip all previously
painted segments. The daily count is therefore exact, and no unit segment is
counted on two days.

## Complexity detail

Let $n$ be the number of days and let $p$ be the total number of distinct unit
segments ever painted. Each segment is inserted once, and path-compressed
successor operations take amortized inverse-Ackermann time. The total time is
$O((n+p)\alpha(p))$ and the dictionary uses $O(p)$ space. Here
$p \le 5\cdot10^4$ because of the coordinate bound.

## Alternatives and edge cases

- **Scan every requested coordinate:** A painted set is simple and correct, but
  repeatedly traversing heavily overlapping intervals can take time
  proportional to the sum of all interval lengths.
- **Segment tree:** Range queries and updates give $O(n\log C)$ time over
  coordinate bound $C$, but require a more elaborate tree and lazy state.
- **Ordered disjoint intervals:** Maintaining the painted union supports sparse
  coordinates, though splitting and merging intervals is more intricate.
- Intervals are half-open, so `[a, b)` and `[b, c)` touch without overlapping.
- A fully contained or repeated interval contributes zero.
- Coordinate `50000` is a valid exclusive endpoint and successor sentinel.
