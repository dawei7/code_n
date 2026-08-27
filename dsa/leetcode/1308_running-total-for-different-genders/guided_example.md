# Guided Example: Running Total for Different Genders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Scores": [{"player_name": "Aron", "gender": "F", "day": "2020-01-01", "score_points": 17}, {"player_name": "Alice", "gender": "F", "day": "2020-01-07", "score_points": 23}, {"player_name": "Bajrang", "gender": "M", "day": "2020-01-07", "score_points": 7}, {"player_name": "Khali", "gender": "M", "day": "2019-12-25", "score_points": 11}, {"player_name": "Slaman", "gender": "M", "day": "2019-12-30", "score_points": 13}, {"player_name": "Joe", "gender": "M", "day": "2019-12-31", "score_points": 3}, {"player_name": "Jose", "gender": "M", "day": "2019-12-18", "score_points": 2}, {"player_name": "Priya", "gender": "F", "day": "2019-12-31", "score_points": 23}, {"player_name": "Priyanka", "gender": "F", "day": "2019-12-30", "score_points": 17}]}}`
- **Required output:** `{"columns": ["gender", "day", "total"], "rows": [["F", "2019-12-30", 17], ["F", "2019-12-31", 40], ["F", "2020-01-01", 57], ["F", "2020-01-07", 80], ["M", "2019-12-18", 2], ["M", "2019-12-25", 13], ["M", "2019-12-30", 26], ["M", "2019-12-31", 29], ["M", "2020-01-07", 36]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Scores`

The objective is to compute `{"columns": ["gender", "day", "total"], "rows": [["F", "2019-12-30", 17], ["F", "2019-12-31", 40], ["F", "2020-01-01", 57], ["F", "2020-01-07", 80], ["M", "2019-12-18", 2], ["M", "2019-12-25", 13], ["M", "2019-12-30", 26], ["M", "2019-12-31", 29], ["M", "2020-01-07", 36]]}` from `{"tables": {"Scores": [{"player_name": "Aron", "gender": "F", "day": "2020-01-01", "score_points": 17}, {"player_name": "Alice", "gender": "F", "day": "2020-01-07", "score_points": 23}, {"player_name": "Bajrang", "gender": "M", "day": "2020-01-07", "score_points": 7}, {"player_name": "Khali", "gender": "M", "day": "2019-12-25", "score_points": 11}, {"player_name": "Slaman", "gender": "M", "day": "2019-12-30", "score_points": 13}, {"player_name": "Joe", "gender": "M", "day": "2019-12-31", "score_points": 3}, {"player_name": "Jose", "gender": "M", "day": "2019-12-18", "score_points": 2}, {"player_name": "Priya", "gender": "F", "day": "2019-12-31", "score_points": 23}, {"player_name": "Priyanka", "gender": "F", "day": "2019-12-30", "score_points": 17}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separating the two teams

The expression begins with

`SUM(score_points) OVER (PARTITION BY gender ...)`.

`PARTITION BY gender` creates an independent window partition for each distinct gender. Female rows contribute only to female totals, and male rows contribute only to male totals. The running accumulation restarts when the partition changes.

This partitioning is different from `GROUP BY gender`. A grouped query would reduce each gender to one row, losing the per-day results. The window aggregate keeps the original `gender` and `day` row while attaching a cumulative sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Scores": [{"player_name": "Aron", "gender": "F", "day": "2020-01-01", "score_points": 17}, {"player_name": "Alice", "gender": "F", "day": "2020-01-07", "score_points": 23}, {"player_name": "Bajrang", "gender": "M", "day": "2020-01-07", "score_points": 7}, {"player_name": "Khali", "gender": "M", "day": "2019-12-25", "score_points": 11}, {"player_name": "Slaman", "gender": "M", "day": "2019-12-30", "score_points": 13}, {"player_name": "Joe", "gender": "M", "day": "2019-12-31", "score_points": 3}, {"player_name": "Jose", "gender": "M", "day": "2019-12-18", "score_points": 2}, {"player_name": "Priya", "gender": "F", "day": "2019-12-31", "score_points": 23}, {"player_name": "Priyanka", "gender": "F", "day": "2019-12-30", "score_points": 17}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Putting dates in accumulation order

Inside each partition, `ORDER BY gender, day` determines the order used by the window calculation. Because every row in a partition already has the same `gender`, the first ordering key is redundant there. `ORDER BY day` would define the same within-gender sequence.

For one gender, the earliest date comes first. Its window includes its own score, so its total equals that first score. The next date includes both the first and second rows, and so on.

For example, female scores $17$, $23$, $17$, and $23$ in ascending date order produce totals $17$, $40$, $57$, and $80$. The value $57$ is not the score for one day; it is $17+23+17$ through that date.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Inside each partition, `ORDER BY gender, day` determines the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The implicit window frame

MySQL supplies a default frame when an aggregate window has `ORDER BY` and no explicit frame clause. Conceptually, the cumulative frame extends from the beginning of the partition through the current ordering value.

The schema declares `(gender, day)` as a primary key, so no gender has two rows on the same day. As a result, peer-row differences between a `RANGE` frame and a `ROWS` frame do not affect this dataset: within a gender, each day identifies one row.

An explicit form such as

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

would make the running-row intent clearer. Under the key guarantee, it produces the same totals as the exact source.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["gender", "day", "total"], "rows": [["F", "2019-12-30", 17], ["F", "2019-12-31", 40], ["F", "2020-01-01", 57], ["F", "2020-01-07", 80], ["M", "2019-12-18", 2], ["M", "2019-12-25", 13], ["M", "2019-12-30", 26], ["M", "2019-12-31", 29], ["M", "2020-01-07", 36]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Scores": [{"player_name": "Aron", "gender": "F", "day": "2020-01-01", "score_points": 17}, {"player_name": "Alice", "gender": "F", "day": "2020-01-07", "score_points": 23}, {"player_name": "Bajrang", "gender": "M", "day": "2020-01-07", "score_points": 7}, {"player_name": "Khali", "gender": "M", "day": "2019-12-25", "score_points": 11}, {"player_name": "Slaman", "gender": "M", "day": "2019-12-30", "score_points": 13}, {"player_name": "Joe", "gender": "M", "day": "2019-12-31", "score_points": 3}, {"player_name": "Jose", "gender": "M", "day": "2019-12-18", "score_points": 2}, {"player_name": "Priya", "gender": "F", "day": "2019-12-31", "score_points": 23}, {"player_name": "Priyanka", "gender": "F", "day": "2019-12-30", "score_points": 17}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["gender", "day", "total"], "rows": [["F", "2019-12-30", 17], ["F", "2019-12-31", 40], ["F", "2020-01-01", 57], ["F", "2020-01-07", 80], ["M", "2019-12-18", 2], ["M", "2019-12-25", 13], ["M", "2019-12-30", 26], ["M", "2019-12-31", 29], ["M", "2020-01-07", 36]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated subquery:** For each row, sum same-:** - **Correlated subquery:** For each row, sum same-gender scores with dates at or before the current date. It is logically direct but can approach $O(n^2)$ without effective indexing or optimizer rewriting.
- **Self-join and group:** Joining each row to all earlier same-gender rows and grouping by the current row also works, but creates a large intermediate relation.
- **Explicit `ROWS` frame:** Adding `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` makes cumulative semantics explicit and avoids peer-group surprises if uniqueness changes.
- **Required outer ordering:** The exact source needs final `ORDER BY gender, day`. Window-local order alone is not a result-order guarantee.
- **Redundant gender window key:** Inside a `gender` partition, ordering by `gender` adds no distinction. Keeping it is harmless but less concise than ordering by `day` alone.
- **First date for a gender:** Its frame contains only itself, so total equals that row's score.
- **Only one row for a gender:** That row remains in the output and its total equals its score.
- **Different genders on nearby dates:** Partitioning prevents one team's scores from entering the other team's total.
- **Unique date within gender:** The composite primary key ensures no tied `day` peers in one partition, so implicit `RANGE` and explicit cumulative `ROWS` agree.
- **Negative score outside the likely scenario:** `SUM` would still compute an arithmetic running total, which could decrease. The algorithm does not require monotone scores.
- **No guaranteed natural order:** Table storage and index choice do not replace an outer `ORDER BY` when ordering is part of the answer contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the number of rows in `Scores`. A typical execution plan must arrange rows by the partition and ordering keys `(gender, day)`. Without a supporting access order, sorting costs $O(n\log n)$ time. After ordering, the database can maintain a running sum in one pass, costing $O(n)$ additional time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
