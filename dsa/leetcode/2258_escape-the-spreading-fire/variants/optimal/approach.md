## General

**Compute the fire's earliest schedule once**

Run a multi-source breadth-first search beginning from every initial fire
cell. Its distance to each non-wall coordinate is the first minute fire can
occupy that coordinate. Unreached cells retain infinite arrival time. This
schedule is independent of the person's chosen wait and route.

**Test one waiting time against that schedule**

For a proposed wait, the start must still be unburned: its fire time must be
strictly greater than the wait. Then run a BFS for the person, carrying the
absolute arrival minute. An ordinary cell is usable only when the person
arrives strictly before fire. At the safehouse, equality is permitted because
the move completes before that minute's fire spread.

Recording each reached coordinate once is sufficient. BFS reaches it at the
earliest possible person time, and any later arrival has no advantage against
fixed fire deadlines.

**Search the monotone waiting boundary**

If waiting $t$ minutes is feasible, every smaller wait is also feasible by
following the same route earlier. Feasible waits therefore form an initial
interval. First test zero for the impossible sentinel and $10^9$ for the
unbounded sentinel. Otherwise, binary-search the greatest feasible integer
between them.

The fire BFS gives exact earliest hazards, and the feasibility BFS accepts
exactly the paths meeting every strict intermediate deadline and the
safehouse's inclusive deadline. Binary search then returns the final feasible
wait in the monotone interval, which is the requested maximum.

## Complexity detail

Each BFS touches at most $mn$ cells. Fire preprocessing costs $O(mn)$, and at
most $O(\log 10^9)$ feasibility searches each cost $O(mn)$, for
$O(mn\log 10^9)$ time. Fire times, visited coordinates, and BFS queues use
$O(mn)$ space.

## Alternatives and edge cases

- **Try every waiting time:** Exhaustively testing all finite candidates is correct but can require $O((mn)^2)$ time.
- **Simulate fire anew for every route:** This duplicates an invariant process and greatly increases work.
- **Joint person-and-fire simulation:** It can work, but preserving the move-before-spread order and searching the maximum wait is more error-prone.
- **Safehouse tie:** Arrival exactly when fire reaches the safehouse is successful.
- **Tie elsewhere:** Fire arrival at the same minute makes every non-safehouse cell unusable.
- **Fire reaches the start while waiting:** The person cannot begin at that wait.
- **No immediate route:** Return `-1` when wait zero fails.
- **Fire permanently separated by walls:** Return $10^9$ when an arbitrarily large wait succeeds.
- **Multiple fires:** Multi-source BFS combines all of them into the earliest arrival schedule.
