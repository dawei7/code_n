# Guided Example: Server Utilization Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Servers": [{"server_id": 3, "status_time": "2023-11-04 16:29:47", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:49:47", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-25 01:37:08", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-25 03:50:08", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-13 03:05:31", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-13 11:10:31", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-29 15:11:17", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-29 15:42:17", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-20 00:31:44", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-20 07:03:44", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-20 00:27:11", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-20 01:41:11", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-04 23:16:48", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:15:48", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-30 15:09:18", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-30 20:48:18", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-25 21:09:06", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-26 04:58:06", "session_status": "stop"}, {"server_id": 5, "status_time": "2023-11-16 19:42:22", "session_status": "start"}, {"server_id": 5, "status_time": "2023-11-16 21:08:22", "session_status": "stop"}]}}`
- **Required output:** `{"columns": ["total_uptime_days"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Servers`

The objective is to compute `{"columns": ["total_uptime_days"], "rows": [[1]]}` from `{"tables": {"Servers": [{"server_id": 3, "status_time": "2023-11-04 16:29:47", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:49:47", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-25 01:37:08", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-25 03:50:08", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-13 03:05:31", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-13 11:10:31", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-29 15:11:17", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-29 15:42:17", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-20 00:31:44", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-20 07:03:44", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-20 00:27:11", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-20 01:41:11", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-04 23:16:48", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:15:48", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-30 15:09:18", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-30 20:48:18", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-25 21:09:06", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-26 04:58:06", "session_status": "stop"}, {"server_id": 5, "status_time": "2023-11-16 19:42:22", "session_status": "start"}, {"server_id": 5, "status_time": "2023-11-16 21:08:22", "session_status": "stop"}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Turn every start row into one complete running interval

The table records events, not durations. A row whose `session_status` is `'start'` tells us when a server began running, while the corresponding `'stop'` row tells us when that run ended. Therefore, the useful quantity is the difference between two consecutive timestamps belonging to the same server.

The query first builds the common table expression `T`. For every row, `LEAD(status_time)` looks one row ahead and copies that later timestamp into `next_status_time`. Two clauses define exactly what “one row ahead” means:

- `PARTITION BY server_id` keeps different servers completely separate. The next event for server 3 can never be borrowed from server 4.
- `ORDER BY status_time` puts each server's events in chronological order before choosing the next one.

Suppose one server has these events:

| `session_status` | `status_time` | `next_status_time` |
|---|---|---|
| `start` | 08:00 | 10:30 |
| `stop` | 10:30 | 13:00 |
| `start` | 13:00 | 14:15 |
| `stop` | 14:15 | `NULL` |

Only the first and third rows describe the beginnings of running intervals. Their next timestamps are exactly their matching stop times, so their durations are 2.5 hours and 1.25 hours. The values generated for stop rows are irrelevant.

This explains why the outer query applies `WHERE session_status = 'start'` only after `LEAD` has been evaluated in the CTE. Filtering starts before evaluating the window would remove all stop rows. Then a start row would look ahead to the next start, which would measure downtime and running time together and produce a wrong answer. Keeping all events during the window calculation preserves the start-to-stop adjacency; filtering afterward selects only actual uptime intervals.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Servers": [{"server_id": 3, "status_time": "2023-11-04 16:29:47", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:49:47", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-25 01:37:08", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-25 03:50:08", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-13 03:05:31", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-13 11:10:31", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-29 15:11:17", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-29 15:42:17", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-20 00:31:44", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-20 07:03:44", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-20 00:27:11", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-20 01:41:11", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-04 23:16:48", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:15:48", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-30 15:09:18", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-30 20:48:18", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-25 21:09:06", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-26 04:58:06", "session_status": "stop"}, {"server_id": 5, "status_time": "2023-11-16 19:42:22", "session_status": "start"}, {"server_id": 5, "status_time": "2023-11-16 21:08:22", "session_status": "stop"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Measure in seconds, add globally, and round only once

For every retained start row, `TIMESTAMPDIFF(SECOND, status_time, next_status_time)` measures the complete interval in seconds. `SUM` then combines intervals from every server because the requested result is total fleet uptime, not one result per `server_id`.

It is important to sum the raw seconds before converting to days. Rounding each session separately would discard partial days that can combine into a full day. For example, two 18-hour sessions contribute 36 hours in total, which contains one full day. If each session were independently rounded down, both would become zero and that day would be lost.

There are 86,400 seconds in a day, so the query divides the grand total by `86400`. `FLOOR` removes the remaining fractional day and implements “rounded down to the nearest number of full days.” For 129,600 accumulated seconds, the division gives 1.5 and `FLOOR` returns 1.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why each running second is counted exactly once

Under the table contract, events for a server form complete start/stop sessions in chronological order. Consider any such session. Its start event receives the immediately following stop timestamp from `LEAD`, so the query includes that session's entire duration. No other retained row can include the same session: the stop row is filtered out, and the next start begins a different interval. Thus every complete running interval contributes once and only once.

The partition boundary matters at the end of a server's history. The last row has no later row in its partition, so `LEAD` produces `NULL`. With properly paired sessions, that final event is a stop and is filtered out. A malformed unmatched final start would create a `NULL` duration, which `SUM` ignores rather than inventing an ending time. The problem's event guarantees are what make the intended pairing valid.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["total_uptime_days"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Servers": [{"server_id": 3, "status_time": "2023-11-04 16:29:47", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:49:47", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-25 01:37:08", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-25 03:50:08", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-13 03:05:31", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-13 11:10:31", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-29 15:11:17", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-29 15:42:17", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-20 00:31:44", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-20 07:03:44", "session_status": "stop"}, {"server_id": 1, "status_time": "2023-11-20 00:27:11", "session_status": "start"}, {"server_id": 1, "status_time": "2023-11-20 01:41:11", "session_status": "stop"}, {"server_id": 3, "status_time": "2023-11-04 23:16:48", "session_status": "start"}, {"server_id": 3, "status_time": "2023-11-05 01:15:48", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-30 15:09:18", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-30 20:48:18", "session_status": "stop"}, {"server_id": 4, "status_time": "2023-11-25 21:09:06", "session_status": "start"}, {"server_id": 4, "status_time": "2023-11-26 04:58:06", "session_status": "stop"}, {"server_id": 5, "status_time": "2023-11-16 19:42:22", "session_status": "start"}, {"server_id": 5, "status_time": "2023-11-16 21:08:22", "session_status": "stop"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["total_uptime_days"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Signed timestamp aggregation:** Add every stop timestamp and subtract every start timestamp, then convert the resulting total duration. This can avoid explicitly pairing rows when sessions are guaranteed balanced, but timestamp arithmetic is less direct and still relies on the event contract.
- **Self-join with row numbers:** Number starts and stops per server and join matching sequence numbers. It makes pairing visible, but requires more machinery and usually the same ordering work as `LEAD`.
- **Correlated next-stop lookup:** For every start, search for the earliest later stop of the same server. This is intuitive but may perform repeated index searches and is easier to get wrong when several sessions exist.
- **Filter placement:** The `session_status = 'start'` condition must remain outside the CTE that computes `LEAD`. Applying it before the window calculation changes “next event” into “next start.”
- **Multiple servers:** Partitioning is essential. Without `PARTITION BY server_id`, a late event from one server could be paired with an early event from another.
- **Several short sessions:** Durations must be added before `FLOOR`. Fractional days from separate sessions are allowed to combine into full days.
- **Session crossing midnight:** Nothing special is needed. `TIMESTAMPDIFF` measures elapsed seconds across dates correctly.
- **Last stop event:** Its `next_status_time` is `NULL`, but the stop row is removed by the outer filter.
- **Unmatched final start:** The exact query silently excludes its `NULL` duration through SQL aggregate semantics. The intended data contract should prevent this malformed history; the query does not choose an artificial end time.
- **Empty input:** If the table were empty, `SUM` would return `NULL` and so would the final expression. The problem normally supplies valid session data; returning zero for a potentially empty table would require `COALESCE`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r \log r)$. Let $r$ be the number of rows in `Servers`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
