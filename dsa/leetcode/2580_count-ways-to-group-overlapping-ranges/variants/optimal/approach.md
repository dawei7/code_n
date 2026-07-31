## General

Regard each range as a vertex and connect two vertices when their closed intervals overlap. The grouping rule forces every connected component of this overlap graph to remain intact: direct overlap forces two ranges together, and that equality propagates through any chain of overlaps.

**Finding components without building the graph:** Sort the ranges by start coordinate. While scanning, maintain `current_end`, the farthest end reached by the current merged component. If the next start is at most `current_end`, that range overlaps the merged union and belongs to the same component; extend `current_end` when necessary. If the next start is greater than `current_end`, no earlier interval can reach it, so a new component begins.

The strict comparison is important. Because ranges are closed, intervals ending and starting at the same coordinate overlap and remain in one component.

**Counting assignments:** Different components contain no overlapping pair and can choose groups independently. Each component has two choices: place all of its ranges in group one or place them in group two. Starting with one assignment and multiplying by two whenever a component begins therefore computes $2^k$, where $k$ is the number of components. Reducing after each multiplication keeps the result modulo $10^9+7$.

The scan neither separates connected ranges nor merges disconnected ones: every range whose start lies within the current merged end has an overlap chain into that component, while a start beyond that end cannot overlap any previously sorted range. Thus the counted boundaries are exactly the graph components, and the independent two-way choices give precisely all valid assignments.

## Complexity detail

Let $n$ be the number of ranges. Sorting costs $O(n \log n)$ time and the component scan costs $O(n)$ time. Python's in-place sort may use $O(n)$ auxiliary space in the worst case, which determines the stated $O(n)$ space bound.

## Alternatives and edge cases

- **All-pairs graph plus disjoint set union:** Testing every pair and unioning overlaps is correct, but requires $O(n^2)$ overlap checks and cannot handle $10^5$ ranges.
- **Event sweep:** Start and end events can count connected unions, but sorting the intervals directly is simpler and avoids tie-order mistakes for closed endpoints.
- **Touching endpoints:** `[a, b]` and `[b, c]` overlap at `b`, so a new component starts only when the next start is strictly greater than `current_end`.
- **Transitive overlap:** Two ranges need not intersect directly to be forced together when a chain of intermediate overlaps connects them.
- **Possibly empty groups:** Assigning every component to the same labeled group is valid, which is why the two all-in-one assignments are counted.
