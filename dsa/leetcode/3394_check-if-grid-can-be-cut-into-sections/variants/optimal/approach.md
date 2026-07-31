## General

**Reduce a cut direction to interval groups.** For vertical cuts, project every rectangle onto the x-axis as `[start_x, end_x]`; for horizontal cuts, use `[start_y, end_y]`. Two projections whose interiors overlap cannot be separated by a cut of that orientation. Conversely, a boundary between two disjoint projection groups is a legal full-grid cut because it crosses no rectangle interior.

Sort one axis's intervals by their starting coordinate and merge overlapping interiors. Maintain the farthest `current_end` in the active group. An interval with `start < current_end` overlaps that group and extends its end when necessary. If `start >= current_end`, it begins a new group: equality is deliberately separate because a cut may lie on touching rectangle boundaries.

**Why three groups are exactly the target.** Each merged projection group is indivisible under cuts of this orientation. If at least three groups exist, place one cut between the first and second groups and another between the second and third; any later groups remain in the third section. All three sections contain rectangles, and no rectangle is split. If fewer than three groups exist, two cuts cannot produce three nonempty sections without dividing a group, which would intersect at least one rectangle. Testing x projections and then y projections therefore covers every allowed pair of cuts.

The coordinate `n` bounds the input but does not affect the decision: only the relative projection endpoints determine whether legal separating boundaries exist.

## Complexity detail

Let $r$ be the number of rectangles. Creating and sorting one projection costs $O(r\log r)$ time, and its merge scan costs $O(r)$. At most two axes are checked, so the total time is $O(r\log r)$. The sorted interval list uses $O(r)$ auxiliary space.

The benchmark defines `size` as $r$ and uses 24, 48, and 96 rectangles. Their x projections all overlap while their y projections are disjoint, forcing both sorts. The accepted-class merge scan stays linear after sorting. A correct slower baseline compares every interval pair to build projection connectivity, completes all tiers, and fails only the scaling verdict.

## Alternatives and edge cases

- **Sweep events:** Sorting starts and ends can also count zero-active gaps, but equal-coordinate event ordering must allow a cut where one rectangle ends and another begins.
- **Pairwise projection graph:** Connecting every pair of overlapping projections and counting components is correct but requires $O(r^2)$ comparisons.
- **Search arbitrary grid coordinates:** The grid may be as large as $10^9$, and only rectangle endpoints can change whether a cut is legal.
- **Touching boundaries:** Intervals `[a, b]` and `[b, c]` belong to separate groups because a cut at $b$ crosses neither interior.
- **Overlapping chains:** Even when the first and last projections do not overlap, intermediate overlaps can make all of them one indivisible merged group.
- **Exactly two groups:** One legal boundary produces only two nonempty sections, so the answer remains `False`.
- **More than three groups:** Two cuts can isolate the first two groups and leave every remaining group in the third section.
- **Large coordinates:** Sorting endpoints is independent of coordinate magnitude; no coordinate-sized array is needed.
