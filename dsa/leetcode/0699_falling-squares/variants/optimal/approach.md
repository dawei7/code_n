## General
**Compress the only coordinates where height can change**

Treat a square as the half-open interval `[left, left + side)`. Collect and sort every left and right edge. Between two consecutive edges, the set of covering squares cannot change, so one compressed elementary interval can represent that whole span.

**Query the supporting height**

Build a segment tree over the elementary intervals. Before dropping a square, query the maximum stored height across all compressed intervals it covers. Adding its side length to that base gives the square's top height.

**Assign the new top across the footprint**

After landing, the entire footprint's visible height becomes that top value. Perform a range-assignment update in the tree. A lazy assignment marker lets a fully covered node adopt the height without descending to every elementary interval; pending assignments are pushed only when a later operation needs its children.

**Maintain the reported skyline maximum**

The new global maximum is the greater of the previous answer and the new square's top. Append it after every update.

**Why the range operations model every fall**

The query returns the highest top among exactly the earlier squares with positive-width overlap, which is the first surface the falling square reaches. Assigning that landing height across its whole footprint records its new exposed top. Induction over the drop order therefore keeps every compressed interval's height and every reported maximum correct.

## Complexity detail
At most `2n` distinct edges create $O(n)$ elementary intervals. Sorting them costs $O(n \log n)$. Each square performs one range-maximum query and one lazy range assignment, each $O(\log n)$, for $O(n \log n)$ total time. The coordinate map and segment tree use $O(n)$ space.

## Alternatives and edge cases
- **Scan all previous squares:** compute the base by testing overlap with every earlier square; it is straightforward and correct but takes $O(n^2)$ time.
- **Dynamic segment tree:** operate on the original coordinate range and create nodes on demand; it avoids compression but has a larger constant and depends on the coordinate bound.
- **Ordered disjoint intervals:** split a skyline map at square edges, query covered pieces, and merge equal neighbors; careful splitting and assignment are required.
- Half-open intervals ensure squares that only share an edge do not support one another.
- A square may overlap several stacks and lands on the tallest one across its footprint.
- Later squares may be narrower, wider, or exactly coincident with earlier squares.
- The output is a running global maximum, so it never decreases.
