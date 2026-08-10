## General

**A cut depends only on rectangle projections.** Horizontal cuts care about each rectangle's y-interval `[y1,y2]`. A cut is valid when no projection spans across it. Vertical cuts use x-intervals in the same way.

The source builds start/end events for both axes. Marker one is a start and marker zero is an end.

**Sweep how many projections overlap.** `overlap` increments at a start and decrements at an end. Whenever it becomes zero, one connected group of projected intervals has finished.

Variable `lines` therefore counts disjoint unions of projections along that axis, not literal line intersections despite the helper's name.

**Why three groups are equivalent to two cuts.** If projections form at least three separated groups, place one cut after the first group and another after the second. Each of the first two sections contains its completed group, and the last contains remaining groups. No rectangle crosses a cut.

Conversely, two valid cuts creating three nonempty rectangle sections imply the projections can be partitioned into at least three groups with zero overlap between consecutive sections. Thus `lines >= 3` is necessary and sufficient.

The groups need not each contain exactly one rectangle. Several overlapping projections may form one group and occupy the same section. What matters is that there are at least three nonempty groups that can be distributed across the three ordered sections.

**End events must precede starts at the same coordinate.** Events sort by `(coordinate,marker)`, and zero sorts before one. If one rectangle ends exactly where another begins, processing the end first lets `overlap` reach zero and records a group boundary.

A cut on that shared coordinate does not pass through either rectangle's interior: one lies entirely on one side and the other on the other side. Reversing tie order would merge them and miss valid cuts.

**Check both orientations independently.** Y events determine whether two horizontal cuts work. X events determine vertical cuts. Logical OR returns true if either orientation has at least three groups; the cuts may not mix orientations.

**Trace touching bands.** Intervals `[0,2]`, `[2,4]`, and `[4,5]` produce end-before-start zero points at two and four, yielding three groups and two valid boundary cuts.

**Trace overlapping projections.** Intervals `[0,4]`, `[1,2]`, and `[5,6]` produce only two groups. The nested second interval ends while the first is still active, so `overlap` does not reach zero there. Only after coordinate four does the first group close. One separation is insufficient for two cuts.

**Why counting zero transitions is easier than storing merged intervals.** The active count already represents the union status of every interval seen so far. A transition to zero is exactly the end of a merged component, so no explicit current-start/current-end pair is needed.

**Overlapping projections may belong to non-overlapping rectangles.** Two rectangles separated horizontally can overlap in y. They merge into one y group, preventing a horizontal separation between them, but may remain separable through x projections. This is why both axes are tested.

**Grid size `n` is unused.** Only relative rectangle endpoints determine gaps. Bounds guarantee coordinates lie inside the grid, but the existence test needs no dense grid representation and remains independent of coordinate magnitude up to $10^9$.

**Why the sweep exactly counts projection components.** Sorted interval endpoints maintain the number of currently active intervals. It reaches zero exactly when no earlier projection extends into the next coordinate region. Every zero therefore closes one maximal overlapping/touching group under the chosen boundary convention.

## Complexity detail

For $r$ rectangles, each axis list contains $2r$ events. Sorting both costs $O(r\log r)$ time, and both sweeps cost $O(r)$. Total time is $O(r\log r)$.

The two event lists use $O(r)$ space. The helper uses constant counters. The source does not mutate `rectangles`, unlike an in-place projection-sort alternative.

## Alternatives and edge cases

- **Sort intervals by start and merge:** It yields the same group count and is the editorial's formulation.
- **Try coordinate cuts directly:** Coordinates may reach $10^9$, so dense scanning is impossible.
- **Exactly three groups:** Two cuts separate them directly.
- **More than three groups:** Choose cuts so all three sections remain nonempty; extra groups can share a section.
- **Several rectangles per group:** They may overlap in projection and remain in one section.
- **Only two groups:** One gap cannot create three nonempty sections.
- **Touching endpoints:** End-before-start treats the shared boundary as cuttable.
- **Overlapping projections:** They remain one group until all active intervals end.
- **Nested interval:** Its end does not close the group while an outer projection remains active.
- **Horizontal success:** X grouping becomes irrelevant because OR short-circuits conceptually.
- **Vertical success:** Y may fail while x succeeds.
- **Non-overlapping 2D rectangles:** Their projections can still overlap on one axis.
- **Large grid size:** It does not affect event count or runtime.
- **Helper name:** `countLineIntersections` actually counts completed projection groups.
- **Unused `n`:** It is part of the contract but unnecessary to the algorithm.
- **Input preservation:** Only new event tuples are sorted.
