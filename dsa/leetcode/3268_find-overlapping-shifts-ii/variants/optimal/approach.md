## General

Let $m$ be the number of rows in `EmployeeShifts`.

**Build a timeline per employee and start date**

Turn every shift into a `+1` event at `start_time` and a `-1` event at `end_time`. Partition by `employee_id` and the date of the shift's start. At equal timestamps, order end events before start events so adjacent shifts are never counted as simultaneously active.

**Track concurrency and the next boundary**

A cumulative window sum of event deltas gives `active_shifts` immediately after each event. A `LEAD(event_time)` window supplies the next boundary. The active count stays constant throughout the interval from the current event to that next event, so its maximum over the timeline is the employee's peak concurrency.

**Integrate all pairwise overlaps**

If $a$ shifts are active over an interval of $t$ minutes, exactly $\binom{a}{2} = a(a-1)/2$ distinct shift pairs overlap throughout that interval. Add

$$
t \cdot \frac{a(a-1)}{2}
$$

for every consecutive-event interval, then sum across all start dates belonging to the employee. This equals summing each pair's intersection length, because a pair contributes one unit at precisely the instants when both members are active.

The event sum changes concurrency at every boundary exactly as the original intervals do. End-before-start ordering enforces strict overlap, date partitioning enforces eligibility, and the active-pair identity counts every overlapping pair once per minute. Aggregating the peak and the integral therefore produces both requested metrics, including peak one and duration zero for a lone shift.

## Complexity detail

The event relation contains $2m$ rows. Partitioned event ordering costs $O(m \log m)$ time in the general case; the window scans and final aggregation are linear. Event and window state use $O(m)$ space.

## Alternatives and edge cases

- **Self-join every shift pair:** Directly summing pair intersections is correct but can take $O(m^2)$ time for one employee and date.
- **Sum the time with at least two active shifts:** This undercounts intervals shared by three or more shifts because each active pair must contribute separately.
- **Process starts before ends at a tie:** That incorrectly treats endpoint-touching shifts as overlapping.
- A single shift yields maximum one and duration zero.
- Three simultaneous shifts contribute three pair-minutes for every elapsed minute.
- Shifts with different start dates are partitioned separately even if their datetime intervals cross midnight and intersect.
- A shift may end after midnight while remaining in the partition determined by its start date.
- Peak concurrency is the maximum across an employee's dates, while pairwise durations are summed across those dates.
- Result rows include every employee and are ordered by `employee_id` ascending.
