## General

**Union area requires horizontal coverage, not summed square widths.** In this version, overlapping regions count only once. At a fixed height between square edges, the covered horizontal cross-section is the union of active x-intervals. If its union width is $W$ and the scan rises by height $\Delta y$, the new covered area is $W\Delta y$.

The source creates two events per square:

- at its bottom $y_1$, add interval $[x_1,x_2)$;
- at its top $y_2$, remove that interval.

Events are sorted by height. Between consecutive event heights, the active interval set and union width are constant.

**Compress x-coordinates into elementary intervals.** Only square left and right edges can change union structure. Sorting all distinct x-coordinates gives `st`. Segment-tree leaf $i$ represents continuous interval

$$
[\texttt{st}[i],\texttt{st}[i+1]).
$$

A square interval $[x_1,x_2)$ therefore updates leaf-index range `d[x1]` through `d[x2] - 1`.

**What each segment-tree node stores.** `cnt` is the number of range updates that fully cover the node's coordinate interval. `length` is the union-covered length inside it.

During `pushup`:

- if `cnt` is nonzero, the entire node interval is covered, so length is its right coordinate minus left coordinate;
- if it is an uncovered leaf, length is zero;
- otherwise, coverage comes from descendants, so length is the sum of child lengths.

Coverage counts rather than Booleans are essential because overlapping squares may add the same x-range several times. Removing one square must not uncover a region still covered by another.

The root property `tree.length` is the active union width across all x.

**First sweep: calculate total union area.** Before applying an event at height $y$, the current tree describes coverage from prior height `y0` up to $y$. The source adds

`(y - y0) * tree.length`

to `area`, then applies the event and advances `y0`. Events sharing a height create zero-height strips between them, so their internal ordering adds no area.

After all top events, every interval has been removed and the tree is empty again. This conveniently prepares the same tree for a second sweep without rebuilding it.

**Second sweep: locate half the area.** Set `target = area / 2` and reset accumulated area and height. For each next strip, compute its area

`t = (y - y0) * tree.length`.

If `area + t >= target`, the dividing line lies in this strip. Union width is constant there, so the exact vertical offset needed is

$$
\frac{\textit{target}-\textit{area}}{\texttt{tree.length}}.
$$

The method returns `y0` plus this offset. Otherwise, it consumes the strip, applies the event, and continues.

If half the area occurs exactly at a strip's top, the condition returns that boundary before applying the event. This also guarantees the minimum value when a zero-width vertical gap follows: the source does not enter the plateau and divide by zero.

**Why two sweeps are necessary in this implementation.** The target depends on total union area, which is unknown until all strips are integrated. One could record every strip during the first sweep, but the source instead replays sorted events. Since the first pass restores an empty tree, replay is simple and keeps only events plus the tree.
Coordinate compression preserves every point where horizontal coverage can change. The segment-tree invariant makes the root equal to exact union width after each event group. Integrating constant-width strips yields exact union area. The second sweep finds the first strip reaching half and linearly interpolates within it, so below and above union areas are equal and the returned coordinate is minimal.

## Complexity detail

There are $2n$ events and at most $2n$ distinct x-coordinates. Sorting costs $O(n\log n)$. Each event is applied once in each of two sweeps, and a range update costs $O(\log n)$, so total time is $O(n\log n)$.

Events, compressed coordinates, the index map, and the segment tree all use $O(n)$ space, matching the manifest.

## Alternatives and edge cases

- **Sum active square widths:** This double-counts horizontal overlap and is correct only for version I.
- **Binary search height with union-area checks:** Each check would need expensive union computation unless additional preprocessing is built.
- **Record strips in one sweep:** Saving cumulative area and width per strip avoids replay but still uses $O(n)$ additional records.
- **Overlapping identical squares:** Coverage counts rise above one and prevent premature uncovering during removals.
- **Same-height events:** Zero strip height makes their internal sort order irrelevant to area.
- **Vertical gap at exactly half:** Returning at the preceding positive strip's endpoint gives the minimum valid height.
- **Half-open x-intervals:** Shared edges have zero area and are neither lost nor double-counted.
- **One square:** Union area is ordinary square area, and interpolation returns its vertical midpoint.
- **Tree reset:** Processing every add and matching remove leaves the tree empty after the first sweep.
- **Division by union width:** The crossing strip has positive area unless target is already reached at its lower edge, which the previous strip returns at its endpoint.
