## General
**Sweep attendance days in increasing order.** Sort events by start day. Maintain an index into that ordering and a min-heap containing the end days of every event that has started but has not been attended.

If the heap is empty, jump the current day directly to the next event's start; empty calendar gaps never help. Push every event whose start is at most the current day, then remove heap entries whose end is before the day because those events have expired.

**Attend the event with the earliest deadline.** If an active event remains, remove the smallest end day, attend that event today, increment the answer, and advance one day. Choosing the earliest deadline cannot reduce the achievable total: if an optimal schedule instead attends a later-ending active event today, swap the earliest-ending event into today. The displaced event can use the day originally assigned to the earlier-ending event, because it started no later than today and ends at least as late. Thus an optimal schedule always exists with the greedy choice.

The sweep repeats until neither unseen nor active events remain, so every counted event has a distinct valid day and the exchange argument proves the count is maximum.

## Complexity detail
Sorting costs $O(n \log n)$. Each event is pushed into and removed from the heap at most once, adding $O(n \log n)$ time. The sorted list and heap hold at most $n$ events, giving $O(n)$ auxiliary space when the input is not reused.

## Alternatives and edge cases
- **Repeated linear deadline selection:** Scanning all remaining events to choose one each day is correct with the same greedy rule but costs $O(n^2)$ time.
- **Sort only by end day:** Assigning each event its first free valid day can also be implemented with a successor structure, but a naive search for free days may be slow.
- **Identical one-day events:** At most one can be attended because they share their only valid day.
- **Large gaps between events:** Jumping directly to the next start avoids iterating unused days.
- **Expired events:** They must be removed before choosing today's event.
- **Nested intervals:** The earliest-ending active interval must take priority over a more flexible event.
