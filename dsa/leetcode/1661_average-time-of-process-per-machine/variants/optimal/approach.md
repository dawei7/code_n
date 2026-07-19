## General
**Pair the two events for each process.** Filter one alias of `Activity` to `start` rows and join it to an `end` alias on both `machine_id` and `process_id`. Including the event-type conditions ensures each process contributes exactly one matched pair.

**Aggregate durations at machine level.** For every joined pair, subtract the start timestamp from the end timestamp. Group by `machine_id` and apply `AVG` to these differences, which is equivalent to total processing time divided by the number of processes on that machine.

**Apply the output contract.** Round the aggregate to three decimal places and alias it as `processing_time`. No `ORDER BY` is required because the result may be returned in any order.

**Why the average is exact.** The composite-key guarantee provides one start and one end event per machine-process pair, so the join neither loses nor duplicates a process. Each joined difference is precisely that process's duration, and grouping contains exactly the processes belonging to one machine. Their arithmetic mean is therefore the requested machine average.

## Complexity detail
With indexes or a hash join on the machine-process key, the two filtered event streams and grouped durations require $O(R)$ expected work. Join and aggregation state may require $O(R)$ auxiliary storage in the worst case. The exact result has a worst-case $\Omega(R)$ input lower bound because changing any activity timestamp can change its machine's output.

## Alternatives and edge cases
- **Conditional aggregation:** Group by machine and process, subtract a conditional start value from a conditional end value, then average in an outer query. This avoids a self-join but requires two aggregation levels.
- **Sign-based aggregation:** Treat end timestamps as positive and start timestamps as negative, then exploit the equal event count. This is concise but depends more subtly on the guaranteed one-to-one event structure.
- **Join only on machine:** This creates a Cartesian pairing among that machine's processes and produces incorrect durations.
- Machine and process identifiers need not be consecutive or globally unique.
- A machine with one process returns that process's duration directly.
- Fractional timestamps must be subtracted before averaging and rounded only after the average is computed.
- Different machines may reuse the same `process_id`; `machine_id` must remain part of the join key.
- Output ordering is intentionally unspecified.
