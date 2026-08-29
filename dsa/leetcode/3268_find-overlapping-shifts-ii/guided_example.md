# Guided Example: Find Overlapping Shifts II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 15:00:00", "end_time": "2023-10-01 23:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 16:00:00", "end_time": "2023-10-02 00:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 11:00:00", "end_time": "2023-10-01 19:00:00"}, {"employee_id": 3, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}]}}`
- **Required output:** `{"columns": ["employee_id", "max_overlapping_shifts", "total_overlap_duration"], "rows": [[1, 3, 600], [2, 2, 360], [3, 1, 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `EmployeeShifts`

The objective is to compute `{"columns": ["employee_id", "max_overlapping_shifts", "total_overlap_duration"], "rows": [[1, 3, 600], [2, 2, 360], [3, 1, 0]]}` from `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 15:00:00", "end_time": "2023-10-01 23:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 16:00:00", "end_time": "2023-10-02 00:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 11:00:00", "end_time": "2023-10-01 19:00:00"}, {"employee_id": 3, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The query computes maximum simultaneous shifts and total pairwise overlap duration through separate CTE paths, then joins their per-employee results.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 15:00:00", "end_time": "2023-10-01 23:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 16:00:00", "end_time": "2023-10-02 00:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 11:00:00", "end_time": "2023-10-01 19:00:00"}, {"employee_id": 3, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

CTE `T` collects every distinct start and end timestamp per employee. `UNION DISTINCT` removes duplicate event times. CTE `P` uses `LEAD` within each employee's ordered events to turn consecutive timestamps into elementary segments `[st,ed]`. Between two consecutive events, the set of active shifts cannot change.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

CTE `S` joins each event segment with all shifts of the same employee that cover the entire segment. Conditions `P.st >= start_time` and `P.ed <= end_time` express that coverage. `COUNT(1)` is the number of concurrent shifts on that segment. Taking `MAX(concurrent_count)` later gives the greatest simultaneous count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "max_overlapping_shifts", "total_overlap_duration"], "rows": [[1, 3, 600], [2, 2, 360], [3, 1, 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"EmployeeShifts": [{"employee_id": 1, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 15:00:00", "end_time": "2023-10-01 23:00:00"}, {"employee_id": 1, "start_time": "2023-10-01 16:00:00", "end_time": "2023-10-02 00:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}, {"employee_id": 2, "start_time": "2023-10-01 11:00:00", "end_time": "2023-10-01 19:00:00"}, {"employee_id": 3, "start_time": "2023-10-01 09:00:00", "end_time": "2023-10-01 17:00:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "max_overlapping_shifts", "total_overlap_duration"], "rows": [[1, 3, 600], [2, 2, 360], [3, 1, 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **true sweep line:** Sort start and end events per employee, update an active count, and integrate pair counts between timestamps. This can achieve $O(m\log m)$ and matches the manifest summary.
- **Window deltas:** Encode starts as plus one and ends as minus one, order end events before starts at equal timestamps, and use cumulative sums for maximum concurrency.
- **Pairwise duration self-join:** This is the exact `U` method and naturally implements pairwise total duration, but is quadratic for dense overlaps.
- **Touching shifts:** Strict `end > start` excludes zero-duration contact.
- **One shift:** Maximum concurrency is one and the left-joined duration becomes zero.
- **Three simultaneous shifts:** Maximum is three; their shared time contributes to three pair durations.
- **Duplicate event times:** `DISTINCT` creates one segment boundary while coverage counting still includes every shift.
- **Nested shifts:** Segment coverage counts all active intervals, and `LEAST` computes each pair's inner overlap correctly.
- **Repeated `U` value after join:** `AVG` preserves the single employee total; replacing it with `SUM` would overcount.
- **Cross-midnight shifts:** Full datetime comparisons handle actual overlap, but there is no explicit same-calendar-date predicate.
- **Null final `LEAD`:** It safely drops the non-segment after the last event through failed comparisons.
- **Gap between shifts:** A consecutive event segment covered by no shift produces no `S` row. This is correct because zero active shifts cannot increase an employee's maximum.
- **Pairwise versus union duration:** `U` sums each pair's intersection, not the length of time during which at least two shifts are active. Triple-overlap minutes are therefore counted three times, exactly as the example's pair list requires.
- **Why employees remain present:** Every valid shift covers the segment from its start to the next event at or before its end, so `S` supplies at least one row for an employee with shifts, including employees with no overlap.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m^2)$. Let $m$ be the number of shifts. There are at most $2m$ distinct event times. Joining event segments to shifts can examine $O(m^2)$ employee-local combinations, and the self-join can emit $\Theta(m^2)$ overlapping pairs in the worst case.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
