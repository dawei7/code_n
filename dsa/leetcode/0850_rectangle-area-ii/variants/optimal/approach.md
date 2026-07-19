## General
**Sweep only where horizontal coverage can change**

Create two vertical events for every rectangle: `(x1, y1, y2, +1)` when its interval becomes active and `(x2, y1, y2, -1)` when it stops being active. Between consecutive event coordinates, the active set is unchanged. If its union covers vertical length $L$ across a horizontal width $Delta x$, that slab contributes $Delta x \cdot L$ area.

**Compress the vertical coordinates**

Collect and sort every rectangle's `y1` and `y2`. Consecutive values define elementary vertical intervals; no event begins or ends inside one of them. A segment tree over these intervals stores a cover count and the total covered length for each node.

A range update adds an event's delta to every elementary interval from `y1` through `y2`. If a tree node's cover count is positive, its entire coordinate span is covered. If the count is zero, a leaf contributes zero and an internal node contributes the sum of its children. The tree root therefore always reports the exact union length $L$ of active vertical intervals, including overlaps only once.

**Accumulate before applying the next event**

For each event at coordinate `x`, add `(x - previous_x) * covered_length` using the active set from the preceding slab, then apply the event's range update. Events sharing the same `x` add zero width between them, so their internal order cannot change the area. Every point in the rectangle union belongs to exactly one such slab and one covered vertical interval, which proves the accumulated sum is the union area.

## Complexity detail
There are $2n$ events and at most $2n$ distinct vertical coordinates. Sorting them takes $O(n\log n)$ time. Each event performs one segment-tree range update in $O(\log n)$ time, for $O(n\log n)$ overall. The events, compressed coordinates, and segment tree use $O(n)$ space.

## Alternatives and edge cases
- **Recompute active interval unions:** Sorting and merging all active vertical intervals at every event is correct but can take $O(n^2\log n)$ time.
- **Inclusion–exclusion:** Intersecting every nonempty subset counts the union exactly, but requires exponential time.
- **Compressed cell marking:** Marking every compressed two-dimensional cell is conceptually simple but can require $O(n^3)$ work when each rectangle tests many cells.
- **Nested rectangles:** Positive cover counts make a multiply covered interval contribute its geometric length only once.
- **Identical rectangles:** Repeated enter and leave events change counts but not the reported union length.
- **Shared edges or corners:** Boundaries have zero area, so touching rectangles simply contribute the sum of their interiors.
- **Large coordinates:** Coordinate compression preserves actual interval lengths; only the final area is reduced modulo $M$.
- **Events at one coordinate:** Zero slab width prevents double counting regardless of the order of starts and ends.
- **Single rectangle:** Its two events produce exactly width times height.
