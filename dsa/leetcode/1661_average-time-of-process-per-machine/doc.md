# Average Time of Process per Machine

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1661 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/average-time-of-process-per-machine/) |

## Problem Description
### Goal
The `Activity` table records when each process starts and ends on a factory machine. Every `(machine_id, process_id)` pair has exactly one `start` row and one `end` row, and the start timestamp is earlier. All machines run the same number of processes.

For each machine, calculate every process duration as its end timestamp minus its start timestamp, then average those durations. Return one row per machine with the average named `processing_time` and rounded to three decimal places. Result rows may appear in any order.

### Function Contract
**Input table**

`Activity`

| Column | Type | Meaning |
|---|---|---|
| `machine_id` | integer | Machine identifier. |
| `process_id` | integer | Process identifier within the machine. |
| `activity_type` | enum | Either `start` or `end`. |
| `timestamp` | float | Event time in seconds. |

The composite key is `(machine_id, process_id, activity_type)`. Let $R$ be the number of rows in `Activity`.

**Return value**

Return columns `machine_id` and `processing_time`, with one row per machine and the average duration rounded to three decimal places.

### Examples
**Example 1**

For machine 0, processes lasting `1.520 - 0.712` and `4.120 - 3.140` seconds have average duration `0.894`. Applying the same calculation to machines 1 and 2 produces:

- Output: `[[0, 0.894], [1, 0.995], [2, 1.456]]`

### Required Complexity
- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Pair the two events for each process.** Filter one alias of `Activity` to `start` rows and join it to an `end` alias on both `machine_id` and `process_id`. Including the event-type conditions ensures each process contributes exactly one matched pair.

**Aggregate durations at machine level.** For every joined pair, subtract the start timestamp from the end timestamp. Group by `machine_id` and apply `AVG` to these differences, which is equivalent to total processing time divided by the number of processes on that machine.

**Apply the output contract.** Round the aggregate to three decimal places and alias it as `processing_time`. No `ORDER BY` is required because the result may be returned in any order.

**Why the average is exact.** The composite-key guarantee provides one start and one end event per machine-process pair, so the join neither loses nor duplicates a process. Each joined difference is precisely that process's duration, and grouping contains exactly the processes belonging to one machine. Their arithmetic mean is therefore the requested machine average.

#### Complexity detail

With indexes or a hash join on the machine-process key, the two filtered event streams and grouped durations require $O(R)$ expected work. Join and aggregation state may require $O(R)$ auxiliary storage in the worst case. The exact result has a worst-case $\Omega(R)$ input lower bound because changing any activity timestamp can change its machine's output.

#### Alternatives and edge cases

- **Conditional aggregation:** Group by machine and process, subtract a conditional start value from a conditional end value, then average in an outer query. This avoids a self-join but requires two aggregation levels.
- **Sign-based aggregation:** Treat end timestamps as positive and start timestamps as negative, then exploit the equal event count. This is concise but depends more subtly on the guaranteed one-to-one event structure.
- **Join only on machine:** This creates a Cartesian pairing among that machine's processes and produces incorrect durations.
- Machine and process identifiers need not be consecutive or globally unique.
- A machine with one process returns that process's duration directly.
- Fractional timestamps must be subtracted before averaging and rounded only after the average is computed.
- Different machines may reuse the same `process_id`; `machine_id` must remain part of the join key.
- Output ordering is intentionally unspecified.

</details>
