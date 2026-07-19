## General
**Process friends in chronological order**

Attach each friend's original index to that friend's interval, then sort the
records by arrival time. This produces the exact order in which chair choices
must be made while preserving the identity of `targetFriend`.

Maintain an occupied min-heap of pairs `(leaving, chair)`. Before handling an
arrival at time $t$, remove every occupied entry whose leaving time is at most
$t$ and insert its chair into an available-chair min-heap. Using “at most” is
essential: it makes a chair reusable when a departure and arrival occur at the
same moment.

**Assign the smallest possible chair**

If the available heap is nonempty, remove its smallest chair. Otherwise, use
the next chair number that has never been assigned and advance that number.
Return immediately when the arriving friend is `targetFriend`; later events
cannot change the chair already assigned.

Every chair in the available heap has been released, and every smaller chair
absent from that heap is still occupied. When no released chair exists, the
never-used chair is the smallest number beyond all chairs allocated so far.
Thus each assignment is precisely the smallest unoccupied chair required by
the rules, including the target's assignment.

## Complexity detail
Sorting $N$ arrival records costs $O(N\log N)$. Each processed friend enters
and leaves the occupied heap at most once and each chair enters and leaves the
available heap at most once; every heap operation costs $O(\log N)$. The total
time is therefore $O(N\log N)$. The sorted records and two heaps together use
$O(N)$ auxiliary space.

## Alternatives and edge cases
- **Ordered event simulation:** Sort separate arrival and departure events and
  maintain an ordered set of free chairs. This can meet the same asymptotic
  bound, but departures must be ordered before arrivals at equal timestamps.
- **Linear chair search:** Track occupancy in an array and scan from chair 0
  for every arrival. It is straightforward but can require $O(N^2)$ time when
  many friends overlap.
- A chair whose friend leaves at time $t$ is available to a friend arriving at
  time $t$.
- Several friends may share a leaving time, so all qualifying occupied-heap
  entries must be released before assigning a chair.
- Original friend indices do not describe arrival order; sorting must retain
  each index to recognize `targetFriend`.
- When every earlier friend is still present, the target receives the next
  previously unused chair.
- When the target arrives first, the answer is chair 0.
