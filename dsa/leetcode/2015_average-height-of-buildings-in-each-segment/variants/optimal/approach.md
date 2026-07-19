## General
**Represent every boundary as a signed event.** At each building's start, add
its height to the active height sum and one to the active count. At its end,
subtract the same values. Combine all changes occurring at one coordinate,
then process the event coordinates in sorted order.

**Emit the interval before applying its right-boundary event.** Between two
consecutive event coordinates, the active set is constant. If its count is
positive, its average is `total_height // active_count`. Append that interval,
or extend the previous output segment when it ends at the current interval's
left boundary and has the same average. If the active count is zero, emit
nothing, so a gap naturally breaks later merging.

Every possible change in coverage or average occurs at a building endpoint.
The sweep therefore assigns the correct active sum and count to every maximal
elementary interval between endpoints. Merging exactly the adjacent intervals
with equal averages preserves their values and removes every unnecessary
boundary; no further merge is legal across a different average or uncovered
gap. The result consequently uses the minimum number of segments.

## Complexity detail
Here $B$ is the number of buildings. Creating at most $2B$ combined events
takes $O(B)$ work, and sorting their coordinates takes $O(B\log B)$ time. The
sweep is linear in the event count. The event map and output use $O(B)$ space.

## Alternatives and edge cases
- **Rescan every building between endpoints:** This computes correct averages
  but takes $O(B^2)$ time when there are linearly many distinct boundaries.
- **Coordinate-sized difference arrays:** Allocating through coordinate
  $10^8$ is wasteful because only building endpoints can change the answer.
- Integer division may keep an average unchanged when a building starts or
  ends; such adjacent regions still merge.
- Equal averages on opposite sides of an uncovered gap cannot merge.
- Starts and ends at the same coordinate must be combined before evaluating
  the interval to their right.
