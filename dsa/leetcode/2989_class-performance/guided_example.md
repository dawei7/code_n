# Guided Example: Class Performance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Scores": [{"student_id": 309, "student_name": "Owen", "assignment1": 88, "assignment2": 47, "assignment3": 87}, {"student_id": 321, "student_name": "Claire", "assignment1": 98, "assignment2": 95, "assignment3": 37}, {"student_id": 338, "student_name": "Julian", "assignment1": 100, "assignment2": 64, "assignment3": 43}, {"student_id": 423, "student_name": "Peyton", "assignment1": 60, "assignment2": 44, "assignment3": 47}, {"student_id": 896, "student_name": "David", "assignment1": 32, "assignment2": 37, "assignment3": 50}, {"student_id": 235, "student_name": "Camila", "assignment1": 31, "assignment2": 53, "assignment3": 69}]}}`
- **Required output:** `{"columns": ["difference_in_score"], "rows": [[111]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Scores`

The objective is to compute `{"columns": ["difference_in_score"], "rows": [[111]]}` from `{"tables": {"Scores": [{"student_id": 309, "student_name": "Owen", "assignment1": 88, "assignment2": 47, "assignment3": 87}, {"student_id": 321, "student_name": "Claire", "assignment1": 98, "assignment2": 95, "assignment3": 37}, {"student_id": 338, "student_name": "Julian", "assignment1": 100, "assignment2": 64, "assignment3": 43}, {"student_id": 423, "student_name": "Peyton", "assignment1": 60, "assignment2": 44, "assignment3": 47}, {"student_id": 896, "student_name": "David", "assignment1": 32, "assignment2": 37, "assignment3": 50}, {"student_id": 235, "student_name": "Camila", "assignment1": 31, "assignment2": 53, "assignment3": 69}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute a comparable total for every student

The performance value for one student is the sum of exactly three assignments:

`assignment1 + assignment2 + assignment3`.

The task is not asking for the difference between the best and worst score on each assignment. It first combines each student’s three columns into one row-level total, then compares those totals across students.

The query embeds the same row expression inside two aggregate functions:

- `MAX(total expression)` finds the highest student total;
- `MIN(total expression)` finds the lowest student total.

Subtracting the second from the first gives the requested spread.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Scores": [{"student_id": 309, "student_name": "Owen", "assignment1": 88, "assignment2": 47, "assignment3": 87}, {"student_id": 321, "student_name": "Claire", "assignment1": 98, "assignment2": 95, "assignment3": 37}, {"student_id": 338, "student_name": "Julian", "assignment1": 100, "assignment2": 64, "assignment3": 43}, {"student_id": 423, "student_name": "Peyton", "assignment1": 60, "assignment2": 44, "assignment3": 47}, {"student_id": 896, "student_name": "David", "assignment1": 32, "assignment2": 37, "assignment3": 50}, {"student_id": 235, "student_name": "Camila", "assignment1": 31, "assignment2": 53, "assignment3": 69}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the aggregation returns one row

There is no `GROUP BY`. SQL therefore treats the entire `Scores` relation as one aggregate group and emits one result row. `student_id` and `student_name` do not appear because the output needs the numeric difference, not the identities of the highest and lowest students.

The alias `difference_in_score` gives the sole output column its required name. Since the result contains one row, “any order” requires no `ORDER BY`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | There is no `GROUP BY`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the sample arithmetic

For the sample students, the query conceptually derives totals 222, 230, 207, 151, 119, and 153. `MAX` returns 230 and `MIN` returns 119. Their difference is 111.

The database may evaluate the row expression twice, once for each aggregate, but no derived table is logically necessary. Both aggregates process the same input rows.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["difference_in_score"], "rows": [[111]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Scores": [{"student_id": 309, "student_name": "Owen", "assignment1": 88, "assignment2": 47, "assignment3": 87}, {"student_id": 321, "student_name": "Claire", "assignment1": 98, "assignment2": 95, "assignment3": 37}, {"student_id": 338, "student_name": "Julian", "assignment1": 100, "assignment2": 64, "assignment3": 43}, {"student_id": 423, "student_name": "Peyton", "assignment1": 60, "assignment2": 44, "assignment3": 47}, {"student_id": 896, "student_name": "David", "assignment1": 32, "assignment2": 37, "assignment3": 50}, {"student_id": 235, "student_name": "Camila", "assignment1": 31, "assignment2": 53, "assignment3": 69}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["difference_in_score"], "rows": [[111]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort students by total:** Reading the first an:** - **Sort students by total:** Reading the first and last totals works but costs $O(R\log R)$ rather than a linear aggregate.
- **Pair every student:** Comparing all pairs is $O(R^2)$ and unnecessary because extrema determine the largest difference.
- **Sum column-wise maxima:** This may combine scores belonging to different students and is incorrect.
- **Use a derived total CTE:** It can improve readability, then apply `MAX(total)-MIN(total)`; the exact query inlines the expression.
- **One student:** Maximum and minimum are the same total, so the difference is zero.
- **Tied highest or lowest totals:** Aggregate values remain the same; identities and tie counts are not requested.
- **Negative assignment values:** Even if allowed, max-minus-min logic would remain valid, though the stated educational scores are ordinary integers.
- **Null assignments:** The exact SQL would exclude that row’s null total from aggregates; it relies on complete score data.
- **No output sorting:** A one-row result already satisfies “any order.”
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of students. A streaming aggregate computes each total and updates both extrema once, giving $O(R)$ logical time. The calculation uses constant arithmetic per row.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
