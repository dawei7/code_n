## General

**Separate space from time.** The required brightness is identical at every covered time, and bulb states at different times do not constrain one another. The minimum energy is therefore

$$
(\text{minimum bulbs per active time})
\cdot
(\text{number of active time units}).
$$

**Find the minimum bulb count.** One bulb illuminates at most three positions, so illuminating `brightness` distinct positions requires at least `ceil(brightness / 3)` bulbs. That bound is attainable: place bulbs along a consecutive portion of the line so that their length-three neighborhoods cover successive positions. Because `brightness <= n`, the block can be shifted away from an endpoint when necessary, and its final bulb can cover a shorter remainder of one or two positions. Thus `(brightness + 2) // 3` is both a lower bound and an achievable count.

**Count active times once.** Sort `intervals` by start time. Maintain the inclusive component `[current_start, current_end]` formed by all intervals processed into it. A next interval whose start is at most `current_end` overlaps the component, so only a farther end can extend it. When the next start lies beyond `current_end`, the current component is final and contributes `current_end - current_start + 1` time units. Starting a new component and adding the last one after the sweep counts every covered integer time exactly once.

Multiplying the proven minimum bulb count by that union size is feasible by reusing an optimal bulb placement at every active time. Any schedule must pay at least that many bulbs at each of those times, so no smaller total energy is possible.

## Complexity detail

Let $m=\texttt{intervals.length}$. Sorting takes $O(m\log m)$ time, and the merge sweep takes $O(m)$ time. Python's in-place sort may use $O(m)$ temporary memory in the worst case; the sweep itself uses $O(1)$ additional state. The manifest therefore records $O(m)$ auxiliary space.

The benchmark uses disjoint intervals in reverse start order at 32, 128, and 512 intervals. This exercises both sorting and the full merge sweep. A correct quadratic implementation that incrementally merges each unsorted interval returns every expected answer but must fail the scaling verdict.

## Alternatives and edge cases

- **Event sweep:** Sorting start and end events can also measure the covered union in $O(m\log m)$ time, but direct interval merging has fewer states because only coverage presence matters.
- **Incremental unsorted union:** Inserting each interval into a maintained disjoint list is correct, but repeated scans and list reconstruction can take $O(m^2)$ time.
- **Enumerating time units:** Adding every covered integer to a set is invalid for the full contract because one interval may span up to $10^9+1$ time units.
- **Inclusive endpoints:** A finalized interval `[start, end]` contributes `end - start + 1`, not `end - start`.
- **Shared endpoints:** Intervals such as `[1,3]` and `[3,5]` overlap at time `3`, which must be counted once.
- **Nested and duplicate intervals:** Neither adds active time beyond the containing component.
- **Adjacent intervals:** `[0,2]` and `[3,5]` do not overlap, but treating them as separate components still yields the correct total of six integer times.
- **Line boundaries:** A bulb at an endpoint illuminates only two positions, yet a consecutive placement can always realize `ceil(brightness / 3)` because `brightness` never exceeds `n`.
