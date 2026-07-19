## General
**Record only color changes**

For a segment `[start, end, color]`, add `color` to the change stored at
`start` and subtract it from the change stored at `end`. Between consecutive
coordinates that have changes, no segment begins or ends, so the active color
set and its sum remain constant.

**Sweep every recorded boundary**

Visit all change coordinates in increasing order while carrying the current
mixed-color sum. Before applying the change at the current coordinate, the
carried sum describes the half-open span from the previous coordinate to the
current one. Emit that span when the sum is positive; a zero sum identifies an
unpainted gap.

Apply the current net change only after considering the preceding span. This
ordering implements the half-open endpoint rule: colors ending at a coordinate
do not cover what follows, while colors starting there do.

Every emitted span has no internal color-set boundary and is therefore
uniform. Conversely, every input endpoint remains a sweep coordinate, even
when its net numeric change is zero. Thus adjacent regions with different
color sets are kept separate despite equal sums, and all painted points appear
in exactly one result span.

## Complexity detail
Building the difference map takes $O(N)$ time and stores at most $2N$
coordinates. Sorting those coordinates costs $O(N\log N)$, and the sweep is
linear in their count. The total time is $O(N\log N)$ and the difference map,
sorted coordinates, and result use $O(N)$ space.

## Alternatives and edge cases
- **Endpoint-by-endpoint rescanning:** Sort every distinct endpoint, then scan
  all input segments to find the colors covering each consecutive span. It is
  correct but can take $O(N^2)$ time.
- **Coordinate array:** Apply differences in an array of size $10^5+1$ and
  sweep the complete coordinate domain. This avoids sorting but ties work and
  storage to the coordinate bound rather than the actual number of endpoints.
- Several segments may start or end at one coordinate; their changes must be
  combined before the next span is evaluated.
- A segment ending where another begins does not overlap the new segment.
- Unpainted gaps have a carried sum of zero and must not appear in the result.
- Equal mixed-color sums on adjacent spans cannot be merged when the active
  color sets differ.
- A single input segment is returned unchanged apart from its result shape.
