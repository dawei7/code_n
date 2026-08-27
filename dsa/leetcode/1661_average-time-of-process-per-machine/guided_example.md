# Guided Example: Average Time of Process per Machine

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activity": [{"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712}, {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.52}, {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.14}, {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.12}, {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.55}, {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.55}, {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.43}, {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.42}, {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.1}, {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512}, {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.5}, {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.0}]}}`
- **Required output:** `{"columns": ["machine_id", "processing_time"], "rows": [[0, 0.894], [1, 0.995], [2, 1.456]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activity`

The objective is to compute `{"columns": ["machine_id", "processing_time"], "rows": [[0, 0.894], [1, 0.995], [2, 1.456]]}` from `{"tables": {"Activity": [{"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712}, {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.52}, {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.14}, {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.12}, {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.55}, {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.55}, {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.43}, {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.42}, {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.1}, {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512}, {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.5}, {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert each activity row into a signed contribution

For one process, processing time is

$$
\text{end timestamp} - \text{start timestamp}.
$$

The SQL query turns this subtraction into an aggregation-friendly sum. Its `CASE` expression produces `-timestamp` for a `'start'` row and `timestamp` for an `'end'` row. Therefore the two rows for one machine-process pair contribute

$$
-\text{start} + \text{end}
= \text{end} - \text{start},
$$

which is exactly that process’s duration.

The table contract is essential here. The composite primary key ensures at most one row of each activity type for a given machine and process, and the guarantee supplies both one `'start'` and one `'end'`. Consequently every process contributes exactly two rows and exactly one signed duration.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activity": [{"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712}, {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.52}, {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.14}, {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.12}, {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.55}, {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.55}, {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.43}, {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.42}, {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.1}, {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512}, {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.5}, {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Grouping produces one result row per machine

`FROM Activity` scans the activity records. `GROUP BY 1` is MySQL’s positional grouping syntax: `1` refers to the first select-list expression, which is `machine_id`. It is therefore equivalent to `GROUP BY machine_id`.

Inside each machine group, the `CASE` expression evaluates every row, `AVG` combines the signed timestamps, and multiplication by two converts the row average to the process average. Because no `process_id` appears in the final grouping, the output contains one row for each distinct machine.

The problem allows any output order, so the absence of `ORDER BY` is correct. SQL does not promise a particular order without that clause, but none is required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `FROM Activity` scans the activity records.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Round only the completed average

`ROUND(..., 3)` surrounds the complete value after averaging and multiplying. This rounds the final processing time to three decimal places, as requested. Rounding individual process durations or individual timestamps first could accumulate avoidable error, so placing `ROUND` at the outside is the correct numerical order.

The alias `processing_time` gives the calculated column its required output name. The other selected column already has the required name `machine_id`.

For machine zero in the example, the signed values are `-0.712`, `1.520`, `-3.140`, and `4.120`. Their sum is `1.788` and their row average is `0.447`. Multiplying by two gives `0.894`, which is also the average of the two durations `0.808` and `0.980`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["machine_id", "processing_time"], "rows": [[0, 0.894], [1, 0.995], [2, 1.456]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activity": [{"machine_id": 0, "process_id": 0, "activity_type": "start", "timestamp": 0.712}, {"machine_id": 0, "process_id": 0, "activity_type": "end", "timestamp": 1.52}, {"machine_id": 0, "process_id": 1, "activity_type": "start", "timestamp": 3.14}, {"machine_id": 0, "process_id": 1, "activity_type": "end", "timestamp": 4.12}, {"machine_id": 1, "process_id": 0, "activity_type": "start", "timestamp": 0.55}, {"machine_id": 1, "process_id": 0, "activity_type": "end", "timestamp": 1.55}, {"machine_id": 1, "process_id": 1, "activity_type": "start", "timestamp": 0.43}, {"machine_id": 1, "process_id": 1, "activity_type": "end", "timestamp": 1.42}, {"machine_id": 2, "process_id": 0, "activity_type": "start", "timestamp": 4.1}, {"machine_id": 2, "process_id": 0, "activity_type": "end", "timestamp": 4.512}, {"machine_id": 2, "process_id": 1, "activity_type": "start", "timestamp": 2.5}, {"machine_id": 2, "process_id": 1, "activity_type": "end", "timestamp": 5.0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["machine_id", "processing_time"], "rows": [[0, 0.894], [1, 0.995], [2, 1.456]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Self-join start and end rows:** Alias `Activit:** - **Self-join start and end rows:** Alias `Activity` twice, join on both `machine_id` and `process_id`, filter one alias to `'start'` and the other to `'end'`, then average `end.timestamp - start.timestamp` by machine. This is explicit and does not need the factor two, but requires a join.
- **Two-stage aggregation:** First group by machine and process to sum signed timestamps into durations, then average those durations by machine. It mirrors the definition closely but adds a derived-table stage.
- **Conditional sums divided by process count:** Sum end timestamps minus start timestamps and divide by `COUNT(DISTINCT process_id)`. This is clear but distinct counting may cost more than exploiting the guaranteed two-row structure.
- **Missing one activity row:** The `* 2` derivation would be invalid if a process lacked a start or end. The input guarantee rules this out.
- **Duplicate activity row:** The composite primary key prevents duplicate start or duplicate end records for one machine-process pair.
- **Zero-duration process:** Since start may equal end, its signed contribution can be zero. It still counts as one process through its two rows and is correctly included in the average.
- **Several machines:** `GROUP BY 1` isolates their aggregates; timestamps from different machines can never mix.
- **Different process counts outside the narrative:** The formula still works because each group’s `AVG` uses that machine’s own number of rows.
- **Floating-point timestamps:** Rounding happens once after aggregation. Exact internal representation and half-way rounding behavior follow MySQL’s numeric rules for the expression types.
- **Output ordering:** No `ORDER BY` is needed because the contract explicitly accepts any order.
- **Ordinal grouping syntax:** `GROUP BY 1` is concise but can become fragile if the select-list order changes. `GROUP BY machine_id` is a more self-documenting equivalent.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let `R` be the number of rows in `Activity` and `M` the number of distinct machines. Conceptually, each row is read once, its `CASE` value is computed in constant time, and it updates one group aggregate. With hash aggregation, this is expected $O(R)$ time and $O(M)$ aggregation space.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
