## General
**Measure what each later attack newly contributes**

An attack at time `t` covers `duration` units, ending just before `t + duration`. For consecutive attack times, the earlier interval contributes only until the next attack begins or until its full duration ends, whichever occurs first.

**Add capped gaps**

For each adjacent pair, add `min(duration, next_time - current_time)`. A small gap counts only the non-overlapping prefix before the poison is refreshed; a gap at least as large as the duration counts the entire earlier interval.

**Account for the last attack**

No later attack truncates the final interval, so add one full `duration` after processing all gaps. If the series is empty, there is no final interval and the answer is zero.

**Why no time unit is double-counted**

The capped contribution assigned to each attack ends at or before the next attack time. These contributions are disjoint and together cover the union through the final start; the last full interval covers the remaining suffix. Their sum is exactly the poison-interval union length.

## Complexity detail
The algorithm scans $n - 1$ adjacent gaps once, giving $O(n)$ time. A running total and the current gap use $O(1)$ extra space.

## Alternatives and edge cases
- **Track the current interval end:** add only the extension beyond the previous end; this is another linear interval-union formulation.
- **Store every poisoned time unit:** is correct for integer time but can require $O(n \cdot duration)$ time and space.
- **Single attack:** contributes exactly one full duration.
- **Overlapping attacks:** count only the gap before the refresh.
- **Touching intervals:** a gap equal to `duration` contributes two non-overlapping full intervals.
- **Repeated timestamp:** adds zero for that gap because the poison merely restarts immediately.
- **Duration one:** every distinct attack time contributes one unit.
