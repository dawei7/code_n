## General

Represent every task as two events for its employee: a $+1$ delta at `start_time` and a $-1$ delta at `end_time`. Aggregate all deltas that share an employee and timestamp before computing a running sum. After the aggregate event at time $t$, that sum is exactly the number of tasks active on the half-open span beginning at $t$.

**Why aggregation handles endpoint ties.** A task ending at $t$ is not concurrent with one starting at $t$. Combining all $-1$ and $+1$ changes at the same coordinate applies both boundary changes before the following positive-length span. No artificial concurrency spike can arise from an arbitrary ordering of equal timestamps.

**Recover both requested measures from one timeline.** Partition by employee and order the distinct event times. A cumulative sum of `delta` gives `active_tasks` after each event, while `LEAD(event_time)` gives the next coordinate. Whenever `active_tasks > 0`, the entire span from the current coordinate to the next is covered by at least one task, so add its length once. Spans with zero active tasks are gaps and contribute nothing. The maximum cumulative count is the employee's peak concurrency.

Group the annotated timeline by employee. Sum the covered seconds, divide by 3600, and floor only after the complete union duration has been accumulated. Taking the maximum active count and sorting by `employee_id` completes the required result.

Every task contributes one start and one end event. Between consecutive distinct event times the active set cannot change, so the sweep accounts for every covered instant exactly once and examines every possible concurrency level. This proves both aggregates simultaneously.

## Complexity detail

Let $n$ be the number of rows in `Tasks`. The event relation contains $2n$ rows. Grouping and ordering those events for the window functions costs $O(n\log n)$ time in the general case; the remaining scans and aggregations are linear. A database engine may exploit a suitable employee-and-time index, but the bound does not assume one.

The raw events, grouped coordinates, and window results may each materialize $O(n)$ rows, so auxiliary working space is $O(n)$.

## Alternatives and edge cases

- **Correlated active-count query:** Counting covering tasks separately at every distinct event time is correct, but may rescan the task table for each coordinate and take $O(n^2)$ time.
- **Merge intervals plus a second overlap query:** Sorting and merging intervals can compute union duration, but concurrency still needs a separate sweep or join; the unified event timeline derives both results from the same state.
- **Expand time into fixed units:** Generating one row per minute or second is both inefficient and incorrect for arbitrary `DATETIME` precision.
- Aggregate equal timestamps before the running sum; ordering individual tied start and end rows can invent a transient peak that exists for no positive-length interval.
- A task ending exactly when another starts does not overlap it, although the union duration remains continuous.
- Sum all covered seconds before flooring to hours; flooring each task or each disjoint component separately loses valid partial hours.
- Multiple employees must be partitioned independently, even when they share timestamps or task IDs.
- Physical row order is irrelevant because every window explicitly orders event coordinates.

