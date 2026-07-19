## General
**Represent only changes in brightness**

A lamp covering the inclusive interval `[left, right]` raises brightness by
one starting at `left`. Its contribution remains active at `right` and ends
immediately afterward, so record `+1` at `left` and `-1` at `right + 1`.
Combining equal event positions prevents coincident lamp boundaries from
requiring any special case.

**Sweep events from left to right**

Sort the event positions and maintain the sum of all changes seen so far.
After applying the change at a position, that sum is the brightness beginning
at that position and continuing until the next event. If it exceeds the best
brightness recorded so far, store the current position.

Event positions are processed in increasing order, and the answer changes only
for a strictly larger brightness. Therefore, the first position recorded for
any brightness is its smallest occurrence. Every lamp is included exactly
between its start event and its end event, so the running sum equals the true
brightness throughout the sweep. The stored position is consequently the
smallest position attaining the global maximum.

## Complexity detail
There are at most $2N$ distinct event positions. Building their changes takes
$O(N)$ time, sorting them takes $O(N\log N)$ time, and the sweep takes $O(N)$
time. The event map and sorted keys use $O(N)$ space.

## Alternatives and edge cases
- **Ordered event map:** Inserting changes into a balanced ordered map performs
  the same sweep online, with $O(N\log N)$ time and $O(N)$ space.
- **Scan every integer position:** Testing each coordinate and recounting all
  lamps is correct but can depend on an enormous coordinate span and take
  quadratic or worse time.
- A zero-range lamp illuminates its center only; placing its removal event at
  `position + 1` preserves that endpoint.
- Multiple changes at one coordinate must be combined before comparing the
  resulting brightness.
- Updating the answer on an equal brightness would incorrectly replace the
  smallest maximizer with a later position.
- Negative positions and intervals crossing zero require no separate handling.
