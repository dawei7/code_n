## General

Sort both schedules. Process buses in departure order while one pointer marks
the earliest passenger who has not boarded. For each bus, advance that pointer
at most `capacity` times while the next passenger arrived no later than the
departure.

**Only the last bus determines the latest candidate**

After all buses are processed, inspect how many existing passengers boarded
the final bus. If it has a spare seat, arriving at its departure time is as
late as any successful arrival could be. If it is full, you must precede the
last passenger who boarded it, so start one minute before that passenger's
arrival.

**Retreat through occupied arrival times**

Store every existing arrival in a set. While the candidate is occupied,
decrement it. Each rejected minute belongs to a distinct passenger, so this
retreat takes at most $p$ successful set lookups.

The chronological simulation assigns every existing passenger to exactly the
same earliest bus as the boarding rule. In the spare-seat case, the final
departure is feasible and no later bus exists. In the full case, arriving no
later than just before its last boarder displaces that passenger and secures a
seat. Retreating changes only collisions with forbidden existing times and
preserves the ordering needed to board, so the first unoccupied candidate is
both feasible and maximal.

## Complexity detail

Sorting costs $O(b\log b+p\log p)$ time. The boarding pointer and final retreat
are linear, so sorting dominates. The occupied-time set and Python's in-place
sorting storage use $O(b+p)$ space.

## Alternatives and edge cases

- **Binary search an arrival time:** Feasibility can be simulated for each
  guess, but proving monotonicity around forbidden passenger times and
  repeating the simulation adds avoidable complexity.
- **Linear-list collision checks:** Testing each decremented candidate against
  the passenger list costs $O(p)$ per check and can become $O(p^2)$.
- **Final bus has room:** Begin at its departure time, not at the last
  passenger's time.
- **Final bus is full:** Begin strictly before the last passenger who boarded;
  arriving simultaneously with any passenger is forbidden.
- **Consecutive occupied times:** Continue decrementing through the entire
  run; the answer is allowed to be earlier than all given times.
