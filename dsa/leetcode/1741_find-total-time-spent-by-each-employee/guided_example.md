# Guided Example: Find Total Time Spent by Each Employee

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employees": [{"emp_id": 1, "event_day": "2020-11-28", "in_time": 4, "out_time": 32}, {"emp_id": 1, "event_day": "2020-11-28", "in_time": 55, "out_time": 200}, {"emp_id": 1, "event_day": "2020-12-03", "in_time": 1, "out_time": 42}, {"emp_id": 2, "event_day": "2020-11-28", "in_time": 3, "out_time": 33}, {"emp_id": 2, "event_day": "2020-12-09", "in_time": 47, "out_time": 74}]}}`
- **Required output:** `{"columns": ["day", "emp_id", "total_time"], "rows": [["2020-11-28", 1, 173], ["2020-11-28", 2, 30], ["2020-12-03", 1, 41], ["2020-12-09", 2, 27]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employees`

The objective is to compute `{"columns": ["day", "emp_id", "total_time"], "rows": [["2020-11-28", 1, 173], ["2020-11-28", 2, 30], ["2020-12-03", 1, 41], ["2020-12-09", 2, 27]]}` from `{"tables": {"Employees": [{"emp_id": 1, "event_day": "2020-11-28", "in_time": 4, "out_time": 32}, {"emp_id": 1, "event_day": "2020-11-28", "in_time": 55, "out_time": 200}, {"emp_id": 1, "event_day": "2020-12-03", "in_time": 1, "out_time": 42}, {"emp_id": 2, "event_day": "2020-11-28", "in_time": 3, "out_time": 33}, {"emp_id": 2, "event_day": "2020-12-09", "in_time": 47, "out_time": 74}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify what one input row contributes

Each row of `Employees` records one uninterrupted visit to the office. The visit begins at `in_time` and ends at `out_time`, measured as minute positions within the same `event_day`. Because `in_time < out_time`, the duration contributed by that row is exactly:

$$
\texttt{out\_time}-\texttt{in\_time}.
$$

The task is not asking for one result per visit. It asks for one result per employee per day, and an employee may have several visits on the same day. Therefore the durations of rows that share both `emp_id` and `event_day` must be added together.

The exact SQL solution expresses this in a single aggregation query:

`SUM(out_time - in_time)` calculates and accumulates the row durations, while `GROUP BY 1, 2` partitions rows according to the first two expressions in the `SELECT` list.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employees": [{"emp_id": 1, "event_day": "2020-11-28", "in_time": 4, "out_time": 32}, {"emp_id": 1, "event_day": "2020-11-28", "in_time": 55, "out_time": 200}, {"emp_id": 1, "event_day": "2020-12-03", "in_time": 1, "out_time": 42}, {"emp_id": 2, "event_day": "2020-11-28", "in_time": 3, "out_time": 33}, {"emp_id": 2, "event_day": "2020-12-09", "in_time": 47, "out_time": 74}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the output columns before grouping

The first selected expression is `event_day AS day`. The stored date is preserved, but the result column receives the required name `day`. The second selected expression is `emp_id`. The third is the aggregate `SUM(out_time - in_time) AS total_time`.

SQL ordinal grouping makes `GROUP BY 1, 2` refer to those first and second selected expressions. In this query, that means grouping by `event_day` and `emp_id`. It does not mean grouping by literal numeric values one and two, and it does not include `total_time` in the key.

Using both key columns is essential. Grouping only by employee would incorrectly combine visits from different days. Grouping only by day would combine different employees. The pair `(event_day, emp_id)` describes exactly one requested output group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How aggregation processes a group

Conceptually, the database begins with an empty accumulator for every distinct employee-day pair. For each input row, it computes the duration and adds it to the accumulator associated with that row's pair.

For employee one on 2020-11-28 in the example, the two row contributions are:

- `32 - 4 = 28` minutes.
- `200 - 55 = 145` minutes.

Both rows have the same day and employee identifier, so `SUM` combines them into `28 + 145 = 173`. The visit on 2020-12-03 belongs to a different key and therefore produces a separate total of 41. Rows belonging to employee two use different keys even when the day matches employee one's day.

The guarantee that visits do not overlap is useful domain information, but the query does not need interval merging. The requested definition explicitly says that the time for each entry is `out_time - in_time`, and non-overlap guarantees that summing these durations does not double-count office time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["day", "emp_id", "total_time"], "rows": [["2020-11-28", 1, 173], ["2020-11-28", 2, 30], ["2020-12-03", 1, 41], ["2020-12-09", 2, 27]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employees": [{"emp_id": 1, "event_day": "2020-11-28", "in_time": 4, "out_time": 32}, {"emp_id": 1, "event_day": "2020-11-28", "in_time": 55, "out_time": 200}, {"emp_id": 1, "event_day": "2020-12-03", "in_time": 1, "out_time": 42}, {"emp_id": 2, "event_day": "2020-11-28", "in_time": 3, "out_time": 33}, {"emp_id": 2, "event_day": "2020-12-09", "in_time": 47, "out_time": 74}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["day", "emp_id", "total_time"], "rows": [["2020-11-28", 1, 173], ["2020-11-28", 2, 30], ["2020-12-03", 1, 41], ["2020-12-09", 2, 27]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit grouping names:** `GROUP BY event_day, emp_id` is equivalent here and can be safer during query maintenance because reordering the `SELECT` list cannot silently change its meaning.
- **Window function:** `SUM(...) OVER (PARTITION BY ...)` would repeat a daily total on every visit row unless followed by deduplication, so ordinary grouping is simpler.
- **Correlated subquery:** Recomputing the sum for each employee-day pair is more verbose and may repeatedly scan the same rows.
- **Application-side aggregation:** Fetching all visits and grouping them in application code moves work and data transfer out of the database without improving the result.
- **Several visits on one day:** All durations for the same employee-day key are added into one row.
- **Same day, different employees:** `emp_id` keeps their totals separate.
- **Same employee, different days:** `event_day` keeps their totals separate.
- **Single visit:** Its group total is simply `out_time - in_time`.
- **No overlapping events:** Direct summation is valid; interval union or overlap correction is unnecessary.
- **Boundary minute values:** Values from 1 through 1440 are ordinary integers, and the strict endpoint order keeps every duration positive.
- **Output order:** Omitting `ORDER BY` is intentional because any row order is accepted.
- **Alias requirement:** `event_day AS day` supplies the requested result-column name without changing the stored date values.
- **Ordinal syntax:** `GROUP BY 1, 2` is concise but depends on MySQL's interpretation of select-list positions.
- **Primary key semantics:** Different `in_time` values allow multiple rows in one employee-day group, which is why aggregation remains necessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(G)$. Let $R$ be the number of input rows and $G$ the number of distinct `(event_day, emp_id)` groups. Conceptually, the database reads each row, computes one constant-time subtraction, and updates one group accumulator. With hash aggregation, this is expected $O(R)$ time and $O(G)$ working space, matching the manifest.
- **Auxiliary Space Complexity:** $O(G)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
