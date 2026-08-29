# Guided Example: Find Consistently Improving Employees

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"employees": [{"employee_id": 1, "name": "Alice Johnson"}, {"employee_id": 2, "name": "Bob Smith"}, {"employee_id": 3, "name": "Carol Davis"}, {"employee_id": 4, "name": "David Wilson"}, {"employee_id": 5, "name": "Emma Brown"}], "performance_reviews": [{"review_id": 1, "employee_id": 1, "review_date": "2023-01-15", "rating": 2}, {"review_id": 2, "employee_id": 1, "review_date": "2023-04-15", "rating": 3}, {"review_id": 3, "employee_id": 1, "review_date": "2023-07-15", "rating": 4}, {"review_id": 4, "employee_id": 1, "review_date": "2023-10-15", "rating": 5}, {"review_id": 5, "employee_id": 2, "review_date": "2023-02-01", "rating": 3}, {"review_id": 6, "employee_id": 2, "review_date": "2023-05-01", "rating": 2}, {"review_id": 7, "employee_id": 2, "review_date": "2023-08-01", "rating": 4}, {"review_id": 8, "employee_id": 2, "review_date": "2023-11-01", "rating": 5}, {"review_id": 9, "employee_id": 3, "review_date": "2023-03-10", "rating": 1}, {"review_id": 10, "employee_id": 3, "review_date": "2023-06-10", "rating": 2}, {"review_id": 11, "employee_id": 3, "review_date": "2023-09-10", "rating": 3}, {"review_id": 12, "employee_id": 3, "review_date": "2023-12-10", "rating": 4}, {"review_id": 13, "employee_id": 4, "review_date": "2023-01-20", "rating": 4}, {"review_id": 14, "employee_id": 4, "review_date": "2023-04-20", "rating": 4}, {"review_id": 15, "employee_id": 4, "review_date": "2023-07-20", "rating": 4}, {"review_id": 16, "employee_id": 5, "review_date": "2023-02-15", "rating": 3}, {"review_id": 17, "employee_id": 5, "review_date": "2023-05-15", "rating": 2}]}}`
- **Required output:** `{"columns": ["employee_id", "name", "improvement_score"], "rows": [[2, "Bob Smith", 3], [1, "Alice Johnson", 2], [3, "Carol Davis", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `employees`

The objective is to compute `{"columns": ["employee_id", "name", "improvement_score"], "rows": [[2, "Bob Smith", 3], [1, "Alice Johnson", 2], [3, "Carol Davis", 2]]}` from `{"tables": {"employees": [{"employee_id": 1, "name": "Alice Johnson"}, {"employee_id": 2, "name": "Bob Smith"}, {"employee_id": 3, "name": "Carol Davis"}, {"employee_id": 4, "name": "David Wilson"}, {"employee_id": 5, "name": "Emma Brown"}], "performance_reviews": [{"review_id": 1, "employee_id": 1, "review_date": "2023-01-15", "rating": 2}, {"review_id": 2, "employee_id": 1, "review_date": "2023-04-15", "rating": 3}, {"review_id": 3, "employee_id": 1, "review_date": "2023-07-15", "rating": 4}, {"review_id": 4, "employee_id": 1, "review_date": "2023-10-15", "rating": 5}, {"review_id": 5, "employee_id": 2, "review_date": "2023-02-01", "rating": 3}, {"review_id": 6, "employee_id": 2, "review_date": "2023-05-01", "rating": 2}, {"review_id": 7, "employee_id": 2, "review_date": "2023-08-01", "rating": 4}, {"review_id": 8, "employee_id": 2, "review_date": "2023-11-01", "rating": 5}, {"review_id": 9, "employee_id": 3, "review_date": "2023-03-10", "rating": 1}, {"review_id": 10, "employee_id": 3, "review_date": "2023-06-10", "rating": 2}, {"review_id": 11, "employee_id": 3, "review_date": "2023-09-10", "rating": 3}, {"review_id": 12, "employee_id": 3, "review_date": "2023-12-10", "rating": 4}, {"review_id": 13, "employee_id": 4, "review_date": "2023-01-20", "rating": 4}, {"review_id": 14, "employee_id": 4, "review_date": "2023-04-20", "rating": 4}, {"review_id": 15, "employee_id": 4, "review_date": "2023-07-20", "rating": 4}, {"review_id": 16, "employee_id": 5, "review_date": "2023-02-15", "rating": 3}, {"review_id": 17, "employee_id": 5, "review_date": "2023-05-15", "rating": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Ranking reviews per employee

`ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC)` assigns:

- `rn=1` to the latest review;
- `rn=2` to the second latest;
- `rn=3` to the third latest.

Ranking restarts independently for every employee.

Only rows two and three will be aggregated later, because each holds one comparison to the review immediately newer than itself.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"employees": [{"employee_id": 1, "name": "Alice Johnson"}, {"employee_id": 2, "name": "Bob Smith"}, {"employee_id": 3, "name": "Carol Davis"}, {"employee_id": 4, "name": "David Wilson"}, {"employee_id": 5, "name": "Emma Brown"}], "performance_reviews": [{"review_id": 1, "employee_id": 1, "review_date": "2023-01-15", "rating": 2}, {"review_id": 2, "employee_id": 1, "review_date": "2023-04-15", "rating": 3}, {"review_id": 3, "employee_id": 1, "review_date": "2023-07-15", "rating": 4}, {"review_id": 4, "employee_id": 1, "review_date": "2023-10-15", "rating": 5}, {"review_id": 5, "employee_id": 2, "review_date": "2023-02-01", "rating": 3}, {"review_id": 6, "employee_id": 2, "review_date": "2023-05-01", "rating": 2}, {"review_id": 7, "employee_id": 2, "review_date": "2023-08-01", "rating": 4}, {"review_id": 8, "employee_id": 2, "review_date": "2023-11-01", "rating": 5}, {"review_id": 9, "employee_id": 3, "review_date": "2023-03-10", "rating": 1}, {"review_id": 10, "employee_id": 3, "review_date": "2023-06-10", "rating": 2}, {"review_id": 11, "employee_id": 3, "review_date": "2023-09-10", "rating": 3}, {"review_id": 12, "employee_id": 3, "review_date": "2023-12-10", "rating": 4}, {"review_id": 13, "employee_id": 4, "review_date": "2023-01-20", "rating": 4}, {"review_id": 14, "employee_id": 4, "review_date": "2023-04-20", "rating": 4}, {"review_id": 15, "employee_id": 4, "review_date": "2023-07-20", "rating": 4}, {"review_id": 16, "employee_id": 5, "review_date": "2023-02-15", "rating": 3}, {"review_id": 17, "employee_id": 5, "review_date": "2023-05-15", "rating": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing chronological improvement while sorting backward

The window order is newest to oldest. For a row, `LAG(rating)` returns the rating on the preceding row in that order, which is the next newer review chronologically.

The source calculates:

`delta = newer_rating - current_older_rating`.

For `rn=2`, delta is latest minus second-latest. For `rn=3`, delta is second-latest minus third-latest.

Both deltas must be positive for ratings to increase strictly from oldest to newest.

The latest row `rn=1` has no previous row in this descending order, so its lag and delta are null. It is intentionally excluded before grouping.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Selecting exactly the two needed comparisons

`WHERE rn > 1 AND rn <= 3` keeps rows with rank two and three.

An employee with at least three reviews contributes exactly two rows. Someone with only two reviews contributes only rank two; someone with one contributes none.

Older reviews beyond the latest three are ignored, even if they break or strengthen a longer trend.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "name", "improvement_score"], "rows": [[2, "Bob Smith", 3], [1, "Alice Johnson", 2], [3, "Carol Davis", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"employees": [{"employee_id": 1, "name": "Alice Johnson"}, {"employee_id": 2, "name": "Bob Smith"}, {"employee_id": 3, "name": "Carol Davis"}, {"employee_id": 4, "name": "David Wilson"}, {"employee_id": 5, "name": "Emma Brown"}], "performance_reviews": [{"review_id": 1, "employee_id": 1, "review_date": "2023-01-15", "rating": 2}, {"review_id": 2, "employee_id": 1, "review_date": "2023-04-15", "rating": 3}, {"review_id": 3, "employee_id": 1, "review_date": "2023-07-15", "rating": 4}, {"review_id": 4, "employee_id": 1, "review_date": "2023-10-15", "rating": 5}, {"review_id": 5, "employee_id": 2, "review_date": "2023-02-01", "rating": 3}, {"review_id": 6, "employee_id": 2, "review_date": "2023-05-01", "rating": 2}, {"review_id": 7, "employee_id": 2, "review_date": "2023-08-01", "rating": 4}, {"review_id": 8, "employee_id": 2, "review_date": "2023-11-01", "rating": 5}, {"review_id": 9, "employee_id": 3, "review_date": "2023-03-10", "rating": 1}, {"review_id": 10, "employee_id": 3, "review_date": "2023-06-10", "rating": 2}, {"review_id": 11, "employee_id": 3, "review_date": "2023-09-10", "rating": 3}, {"review_id": 12, "employee_id": 3, "review_date": "2023-12-10", "rating": 4}, {"review_id": 13, "employee_id": 4, "review_date": "2023-01-20", "rating": 4}, {"review_id": 14, "employee_id": 4, "review_date": "2023-04-20", "rating": 4}, {"review_id": 15, "employee_id": 4, "review_date": "2023-07-20", "rating": 4}, {"review_id": 16, "employee_id": 5, "review_date": "2023-02-15", "rating": 3}, {"review_id": 17, "employee_id": 5, "review_date": "2023-05-15", "rating": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "name", "improvement_score"], "rows": [[2, "Bob Smith", 3], [1, "Alice Johnson", 2], [3, "Carol Davis", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation after row numbering:** One can place latest, second, and third ratings into columns with CASE expressions, then compare them. The delta method is compact and makes the score telescope naturally.
- **Self-join reviews by dates:** Repeatedly finding the three latest rows per employee is more complex and can multiply rows.
- **Exactly three reviews:** Both required delta rows exist and are evaluated normally.
- **Fewer than three reviews:** COUNT is below two, so the employee is excluded.
- **More than three reviews:** Rows older than rank three are filtered out.
- **Equal adjacent ratings:** Delta zero fails strict improvement.
- **A decrease followed by a large rise:** One delta is negative, so a positive overall latest-minus-earliest difference alone is not enough.
- **Negative improvement score:** Such an employee necessarily fails MIN(delta)>0 and is excluded.
- **Tied scores:** Name ascending decides their output order.
- **Duplicate names:** The specified keys provide no further ordering; employee IDs remain distinct output rows.
- **Same review date:** The current source has nondeterministic relative order unless data guarantees uniqueness per employee.
- **Null ratings:** The schema narrative implies integer ratings; if null were allowed, MIN and SUM null behavior would need explicit handling.
- **Group by employee_id:** Name is functionally determined by the unique employee row; MySQL can permit selecting it under functional-dependency rules.
- **Latest-row delta:** It is null but filtered out through `rn>1` before aggregation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R + E log E)$. Let `R` be review rows and `E` employee rows. Window functions generally require arranging reviews by employee and descending date, costing `O(R\log R)` under a sort-based plan. Joining and grouping may use hashes or indexes; sorting the qualifying output costs at most `O(E\log E)`.
- **Auxiliary Space Complexity:** $O(R + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
