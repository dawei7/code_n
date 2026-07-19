## General
**Compress intervals by their left endpoint**

For every tap, clip its coverage to `[0, n]`. In an array `farthest`, record at each integer left endpoint the greatest right endpoint reached by any tap starting there. Keeping only the greatest endpoint loses no useful choice because a shorter interval with the same start can never improve a cover.

**Advance coverage in greedy layers**

Scan positions from left to right while maintaining `current_end`, the farthest point covered by the taps already committed, and `next_end`, the farthest point reachable by opening one more tap whose interval begins no later than the current scan position.

When the scan reaches `current_end`, the current set cannot progress farther without another tap. Commit the candidate that produced `next_end`, increment the count, and make that endpoint the new boundary. If `next_end` does not move past the scan position, there is an uncovered gap and the answer is `-1`.

At each boundary, every interval eligible to continue the cover has already been examined. Choosing the one reaching farthest cannot use more taps than choosing a shorter eligible interval, because it leaves a superset of the garden available to the remaining choices. Repeating this exchange argument gives a minimum-cardinality cover.

## Complexity detail
Creating `farthest` scans $n+1$ taps, and the greedy pass scans $n$ positions, for $O(n)$ time. The endpoint array uses $O(n)$ space.

## Alternatives and edge cases
- **Sort all intervals:** Standard greedy interval covering after sorting by left endpoint takes $O(n\log n)$ time and is correct, but integer endpoints make the linear bucketed form possible.
- **Dynamic programming:** A minimum-tap value for every prefix can be computed, but a direct transition over covering taps may take $O(n^2)$ time.
- **Zero-radius taps:** They cover no positive length and cannot bridge a gap.
- **One tap covers all:** The first greedy commitment reaches `n`, so the answer is 1.
- **Touching endpoints:** Intervals ending and beginning at the same coordinate maintain continuous coverage.
- **Uncovered gap:** Return `-1` as soon as no eligible interval extends the current boundary.
