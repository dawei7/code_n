## General

**Record changes only at endpoints**

Between consecutive building endpoints, the set of active buildings is constant. Its count and sum of heights are constant, so the integer average is constant.

For building `[start,end,height]`, the source records:

- count change +1 at start and -1 at end in `cnt`;
- height-sum change +height at start and -height at end in `d`.

This is a difference-map sweep line. It avoids visiting every coordinate up to $10^8$.

**Maintain the active aggregate**

`m` is the number of buildings active immediately to the right of the last processed endpoint, and `s` is their total height. `last` is that endpoint.

When the loop reaches next coordinate `k`, the values of `s` and `m` describe interval `[last,k)`. The source emits that interval before applying events at `k`.

This order matches half-open semantics: a building ending at `k` is still active throughout the interval leading up to `k`, while a building starting at `k` becomes active only to its right.

If one building ends exactly where another begins, the interval before the coordinate is emitted using the old building. Then both endpoint deltas are applied together, removing the old height and adding the new one for the following interval. There is no zero-width segment at the shared coordinate, and no moment when both buildings are incorrectly counted over a positive-length interval.

**Skip uncovered gaps**

If `m==0`, no building covers `[last,k)`, so the source emits nothing. It still updates `last=k` after processing events.

This retained gap boundary later prevents equal-average occupied regions on opposite sides of an empty gap from being merged.

**Compute the required integer average**

For a covered interval, `avg = s // m` computes integer division of total heights by active building count. All heights are positive, so Python floor division matches the stated integer average.

The average may remain unchanged even when the active set changes at an endpoint. Output must use the minimum number of segments, so such adjacent pieces should be combined.

**Merge only equal and contiguous segments**

The source extends the last result when:

- its average equals `avg`; and
- its right endpoint equals `last`.

The second condition proves there is no uncovered gap between pieces. Extension changes only the previous right endpoint to `k`.

Otherwise it appends `[last,k,avg]` as a new segment.

**Trace an active-set change with the same average**

For buildings `[1,3,2]`, `[2,5,3]`, and `[2,8,3]`, interval one to two has average two. Interval two to three has heights two, three, and three, whose integer average is also two. Although coverage changes at two, equal adjacent averages let these become one segment `[1,3,2]`.

At three the first building ends, leaving average three. Later endpoint five changes the active count but not average, so coverage through eight merges into one `[3,8,3]` segment.

**Why every elementary interval is correct**

Sorted endpoint coordinates partition the line into intervals on which no building begins or ends. The active difference sums therefore represent exactly all buildings covering each interval. Dividing their height sum by count gives its required average.

Because the maps aggregate all events at the same coordinate, their input order cannot affect the sweep. Several starts, several ends, or a mixture at one point produce one net count and height transition after the preceding interval has been handled.

The sweep emits every covered elementary interval and no uncovered one. Merging preserves values and coverage while combining exactly those adjacent intervals that can share one description. The result is correct and has the minimum number of segments.

**Why endpoint maps stay aligned**

Every start and end updates both `cnt` and `d`. Even if height deltas cancel to zero at a coordinate, accessing `d[coordinate]` created the key, so iterating sorted `d.items()` still visits all count-change endpoints.

## Complexity detail

Let $B$ be the number of buildings and $E\le2B$ the number of distinct endpoints. Recording events takes $O(B)$ expected time. Sorting endpoints costs $O(E\log E)=O(B\log B)$, and the sweep is linear.

The two maps and output use $O(B)$ space. Scalar sweep state is $O(1)$.

## Alternatives and edge cases

- **Coordinate-by-coordinate simulation:** Impossible when endpoints reach $10^8$; only event coordinates matter.
- **Store active heights in a multiset:** Unnecessary because only their sum and count determine the average.
- **Sort explicit start/end events:** Equivalent to difference maps but must combine simultaneous events before describing the next interval.
- **Several events at one coordinate:** Dictionary accumulation applies their net effect together.
- **No active building:** Omit the interval from output.
- **Equal averages across an endpoint:** Merge when segments are contiguous.
- **Equal averages across an empty gap:** Do not merge; the endpoint-contiguity check prevents it.
- **Half-open boundary:** Emit the preceding interval before applying current deltas.
- **Single building:** Produces its original interval and height.
- **Complete overlap:** Sum heights and divide by active count.
- **Integer division:** `s // m` implements the specified truncation for positive heights.
- **Any output order:** The source returns sorted street order, which is valid.
- **Input preservation:** It builds event maps without sorting or modifying `buildings`.
