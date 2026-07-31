## General

The difficult part is that overlapping area belongs to the union only once. Between two consecutive horizontal square edges, the set of active squares is unchanged, so the union width on the x-axis is constant and the union area of that band is simply width times height. This suggests sweeping upward through every bottom and top edge.

Compress all square left and right x-coordinates. A segment-tree node represents an interval between compressed coordinates, stores how many active square intervals completely cover it, and stores its union-covered width. A positive cover count makes the whole node interval covered. Otherwise a leaf has width zero, while an internal node obtains its width from its two children. Adding or removing one square interval therefore updates the global union width in $O(\log n)$ time.

Before applying the events at a height `y`, the tree describes the active x-union throughout the band from `previous_y` to `y`. Record that band together with the union area accumulated below it, then apply every event sharing `y`. Once the sweep has the total union area, scan the recorded nonempty bands from bottom to top. In the first band whose upper boundary reaches half the total, linear interpolation by its constant width gives the exact balancing height. Using `>=` selects the top of the current band when half the area is reached exactly, which is also the minimum point of any following empty gap.

## Complexity detail

Let $n$ be the number of squares. There are $2n$ x-coordinates and $2n$ horizontal events. Coordinate sorting and event sorting take $O(n\log n)$ time. Each event performs one $O(\log n)$ segment-tree update, and the final band scan is $O(n)$, so total time is $O(n\log n)$. Coordinates, events, bands, and the segment tree occupy $O(n)$ space.

## Alternatives and edge cases

- **Rebuilding the active union:** Sorting and merging every active x-interval at every event height is correct but can require $O(n^2\log n)$ time.
- **Binary search with repeated union sweeps:** Computing the clipped union area from scratch for each candidate height adds a precision-search factor and repeats the expensive geometric work.
- **Summing square strips:** Adding each square's strip independently double-counts overlaps and solves Separate Squares I rather than this union-area version.
- **Several events at one height:** Area must be accumulated before processing the whole event group; zero-height transitions contribute no area.
- **Vertical gaps:** Empty bands are omitted, and reaching half the area at the preceding band's top returns the lowest balancing line.
- **Contained or duplicate squares:** Coverage counts prevent removals from uncovering an interval still covered by another active square.
- **Touching edges:** Shared boundaries have zero area and do not create overlap.
