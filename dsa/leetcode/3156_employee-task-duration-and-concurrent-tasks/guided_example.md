# Guided Example: Employee Task Duration and Concurrent Tasks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tasks": [{"task_id": 1, "employee_id": 1001, "start_time": "2023-05-01 08:00:00", "end_time": "2023-05-01 09:00:00"}, {"task_id": 2, "employee_id": 1001, "start_time": "2023-05-01 08:30:00", "end_time": "2023-05-01 10:30:00"}, {"task_id": 3, "employee_id": 1001, "start_time": "2023-05-01 11:00:00", "end_time": "2023-05-01 12:00:00"}, {"task_id": 7, "employee_id": 1001, "start_time": "2023-05-01 13:00:00", "end_time": "2023-05-01 15:30:00"}, {"task_id": 4, "employee_id": 1002, "start_time": "2023-05-01 09:00:00", "end_time": "2023-05-01 10:00:00"}, {"task_id": 5, "employee_id": 1002, "start_time": "2023-05-01 09:30:00", "end_time": "2023-05-01 11:30:00"}, {"task_id": 6, "employee_id": 1003, "start_time": "2023-05-01 14:00:00", "end_time": "2023-05-01 16:00:00"}]}}`
- **Required output:** `{"columns": ["employee_id", "total_task_hours", "max_concurrent_tasks"], "rows": [[1001, 6, 2], [1002, 2, 2], [1003, 2, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tasks`

The objective is to compute `{"columns": ["employee_id", "total_task_hours", "max_concurrent_tasks"], "rows": [[1001, 6, 2], [1002, 2, 2], [1003, 2, 1]]}` from `{"tables": {"Tasks": [{"task_id": 1, "employee_id": 1001, "start_time": "2023-05-01 08:00:00", "end_time": "2023-05-01 09:00:00"}, {"task_id": 2, "employee_id": 1001, "start_time": "2023-05-01 08:30:00", "end_time": "2023-05-01 10:30:00"}, {"task_id": 3, "employee_id": 1001, "start_time": "2023-05-01 11:00:00", "end_time": "2023-05-01 12:00:00"}, {"task_id": 7, "employee_id": 1001, "start_time": "2023-05-01 13:00:00", "end_time": "2023-05-01 15:30:00"}, {"task_id": 4, "employee_id": 1002, "start_time": "2023-05-01 09:00:00", "end_time": "2023-05-01 10:00:00"}, {"task_id": 5, "employee_id": 1002, "start_time": "2023-05-01 09:30:00", "end_time": "2023-05-01 11:30:00"}, {"task_id": 6, "employee_id": 1003, "start_time": "2023-05-01 14:00:00", "end_time": "2023-05-01 16:00:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Split time only where activity can change

For one employee, the set of active tasks can change only at a task start or task end. Between two consecutive distinct boundary timestamps, no task begins or ends, so concurrency is constant throughout that entire elementary interval.

CTE `T` collects all starts and ends as the common column `st`. `UNION DISTINCT` removes duplicate boundaries, including times when several tasks begin or end together.

CTE `P` partitions boundaries by `employee_id`, orders them chronologically, and uses `LEAD(st)` to create the next boundary `ed`. Each row now represents elementary interval `[st, ed]` between adjacent event times. The final boundary has no successor and receives `NULL`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tasks": [{"task_id": 1, "employee_id": 1001, "start_time": "2023-05-01 08:00:00", "end_time": "2023-05-01 09:00:00"}, {"task_id": 2, "employee_id": 1001, "start_time": "2023-05-01 08:30:00", "end_time": "2023-05-01 10:30:00"}, {"task_id": 3, "employee_id": 1001, "start_time": "2023-05-01 11:00:00", "end_time": "2023-05-01 12:00:00"}, {"task_id": 7, "employee_id": 1001, "start_time": "2023-05-01 13:00:00", "end_time": "2023-05-01 15:30:00"}, {"task_id": 4, "employee_id": 1002, "start_time": "2023-05-01 09:00:00", "end_time": "2023-05-01 10:00:00"}, {"task_id": 5, "employee_id": 1002, "start_time": "2023-05-01 09:30:00", "end_time": "2023-05-01 11:30:00"}, {"task_id": 6, "employee_id": 1003, "start_time": "2023-05-01 14:00:00", "end_time": "2023-05-01 16:00:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count tasks covering each elementary interval

CTE `S` joins each interval to every task of the same employee. Conditions

`P.st >= Tasks.start_time`

and

`P.ed <= Tasks.end_time`

retain a task only when it covers the complete elementary interval. Because all start and end times are boundaries, a task cannot cover merely part of such an interval. Coverage is all or nothing.

Grouping back by the three `P` columns counts the retained tasks. `concurrent_count` is therefore the number of simultaneously active tasks during that positive-duration segment.

Intervals not covered by any task disappear through the inner join. This is exactly what total active duration needs: idle gaps should not be added.

The last `P` row has `ed = NULL`. Comparisons involving that null are unknown, so it also produces no `S` row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregate union duration and maximum concurrency

Every surviving elementary interval belongs to the union of the employee's task intervals. The intervals are disjoint except at boundaries, so summing their durations counts each active second once, even if many tasks overlap there.

`TIMEDIFF(ed, st)` obtains the interval duration, `TIME_TO_SEC` converts it to seconds, and division by 3600 expresses hours. `SUM` combines all active segments. `FLOOR` is applied after the sum so partial hours from different segments can combine before the final downward rounding.

`MAX(concurrent_count)` returns the largest number of covering tasks among all elementary intervals.

The outer grouping produces one row per employee, and `ORDER BY 1` sorts by the first selected column, `employee_id`, ascending.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "total_task_hours", "max_concurrent_tasks"], "rows": [[1001, 6, 2], [1002, 2, 2], [1003, 2, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tasks": [{"task_id": 1, "employee_id": 1001, "start_time": "2023-05-01 08:00:00", "end_time": "2023-05-01 09:00:00"}, {"task_id": 2, "employee_id": 1001, "start_time": "2023-05-01 08:30:00", "end_time": "2023-05-01 10:30:00"}, {"task_id": 3, "employee_id": 1001, "start_time": "2023-05-01 11:00:00", "end_time": "2023-05-01 12:00:00"}, {"task_id": 7, "employee_id": 1001, "start_time": "2023-05-01 13:00:00", "end_time": "2023-05-01 15:30:00"}, {"task_id": 4, "employee_id": 1002, "start_time": "2023-05-01 09:00:00", "end_time": "2023-05-01 10:00:00"}, {"task_id": 5, "employee_id": 1002, "start_time": "2023-05-01 09:30:00", "end_time": "2023-05-01 11:30:00"}, {"task_id": 6, "employee_id": 1003, "start_time": "2023-05-01 14:00:00", "end_time": "2023-05-01 16:00:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "total_task_hours", "max_concurrent_tasks"], "rows": [[1001, 6, 2], [1002, 2, 2], [1003, 2, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Signed event sweep:** Emit +1 at starts and -1 at ends, aggregate equal timestamps, and use cumulative concurrency. It can compute active duration and peak in $O(r\log r)$ without the quadratic containment join.
- **Merge intervals only:** Sorting and merging yields union duration but does not by itself preserve maximum concurrency.
- **Sum task durations:** Incorrect because overlap would be counted multiple times.
- **Duplicate boundary times:** `UNION DISTINCT` ensures they define one boundary rather than zero-length repeated segments.
- **Idle gaps:** They have no covering joined task and are excluded from total duration.
- **Nested tasks:** The inner segments receive higher covering counts while union duration remains counted once.
- **Back-to-back tasks:** They form continuous active duration but no positive-duration concurrency of two.
- **Several tasks with identical intervals:** Each joins the same segments, so concurrency equals their multiplicity.
- **Partial hours:** Durations are summed before `FLOOR` so fractions can combine.
- **Final boundary:** Its null `ed` cannot form a segment and drops from the containment join.
- **Employees remain separate:** Every window and join is partitioned or keyed by `employee_id`.
- **Long MySQL time differences:** `TIMEDIFF`/`TIME_TO_SEC` behavior should be checked if task spans exceed MySQL's TIME range; the local statement provides no such extreme example.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r^2+r\log r)$. Let $r$ be the number of task rows and $b$ the number of distinct employee-boundary rows, with $b\le2r$.
- **Auxiliary Space Complexity:** $O(r^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
