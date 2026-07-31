## General

**Respect original-start priority with sorting.** Sort meetings by their unique
start times. Delayed meetings never overtake a later original meeting because
the sorted loop assigns each meeting before considering the next one.

**Separate the two room orderings.** An `available_rooms` min-heap stores room
numbers, making its root the lowest-numbered free room. An `occupied_rooms`
min-heap stores `(finish_time, room_number)`. Its root is the room that becomes
free first, with room number resolving simultaneous finishes.

**Release every room available at the current start.** Before assigning a
meeting `[start,end)`, move all occupied entries with finish time at most
`start` into the available heap. The non-strict comparison implements the
half-open interval rule. If a room is available, choose its smallest number
and keep the original end time.

**Delay without changing duration.** If no room is available, remove the
earliest `(finish, room)` from the occupied heap. The meeting begins at
`finish` and its new end is `finish + (end - start)`. Push the resulting
occupied entry and increment that room's count.

At every sorted meeting, the heaps expose exactly the room required by the
allocation rules. The computed finish time is either the original end or the
earliest possible delayed start plus the unchanged duration. Induction over
the sorted meetings therefore shows that the simulation matches the mandated
schedule. Finally, the first index attaining the maximum count supplies the
required lowest-numbered tie break.

## Complexity detail

Let $m$ be the number of meetings and $n$ the number of rooms. Sorting costs
$O(m\log m)$. Each meeting causes a constant number of heap operations, and
each occupied entry is released at most once, for $O(m\log n)$ additional
time. Total time is $O(m\log m+m\log n)$. The sorted meeting list uses
$O(m)$ space and the heaps and counts use $O(n)$, for $O(m+n)$ auxiliary
space.

## Alternatives and edge cases

- **Scan every room:** Keeping only room finish times and linearly searching
  for the required room is correct but costs $O(mn)$ after sorting.
- **Single event heap:** Free and busy rooms obey different primary orderings,
  so combining them without careful state handling makes tie rules harder to
  preserve.
- **Half-open endpoints:** A room with finish time equal to the next start is
  already unused and must be released before assignment.
- **Simultaneous finishes:** When no room was free at the original start, the
  lower-numbered room wins among equal earliest finish times.
- **Several newly free rooms:** Release all rooms ending by `start` before
  selecting the smallest room number; releasing only one can choose wrongly.
- **Delayed meeting duration:** Delay changes both endpoints by the same
  amount and must not retain the original absolute end time.
- **Unsorted input:** Original-start priority is defined independently of the
  order in which the pairs are supplied.
- **Usage-count tie:** Returning the first index of the maximum count enforces
  the lowest-room-number rule.
