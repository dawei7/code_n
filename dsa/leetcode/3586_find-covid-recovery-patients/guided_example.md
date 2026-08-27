# Guided Example: Find COVID Recovery Patients

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"patients": [{"patient_id": 1, "patient_name": "Alice Smith", "age": 28}, {"patient_id": 2, "patient_name": "Bob Johnson", "age": 35}, {"patient_id": 3, "patient_name": "Carol Davis", "age": 42}, {"patient_id": 4, "patient_name": "David Wilson", "age": 31}, {"patient_id": 5, "patient_name": "Emma Brown", "age": 29}], "covid_tests": [{"test_id": 1, "patient_id": 1, "test_date": "2023-01-15", "result": "Positive"}, {"test_id": 2, "patient_id": 1, "test_date": "2023-01-25", "result": "Negative"}, {"test_id": 3, "patient_id": 2, "test_date": "2023-02-01", "result": "Positive"}, {"test_id": 4, "patient_id": 2, "test_date": "2023-02-05", "result": "Inconclusive"}, {"test_id": 5, "patient_id": 2, "test_date": "2023-02-12", "result": "Negative"}, {"test_id": 6, "patient_id": 3, "test_date": "2023-01-20", "result": "Negative"}, {"test_id": 7, "patient_id": 3, "test_date": "2023-02-10", "result": "Positive"}, {"test_id": 8, "patient_id": 3, "test_date": "2023-02-20", "result": "Negative"}, {"test_id": 9, "patient_id": 4, "test_date": "2023-01-10", "result": "Positive"}, {"test_id": 10, "patient_id": 4, "test_date": "2023-01-18", "result": "Positive"}, {"test_id": 11, "patient_id": 5, "test_date": "2023-02-15", "result": "Negative"}, {"test_id": 12, "patient_id": 5, "test_date": "2023-02-20", "result": "Negative"}]}}`
- **Required output:** `{"columns": ["patient_id", "patient_name", "age", "recovery_time"], "rows": [[1, "Alice Smith", 28, 10], [3, "Carol Davis", 42, 10], [2, "Bob Johnson", 35, 11]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `patients`

The objective is to compute `{"columns": ["patient_id", "patient_name", "age", "recovery_time"], "rows": [[1, "Alice Smith", 28, 10], [3, "Carol Davis", 42, 10], [2, "Bob Johnson", 35, 11]]}` from `{"tables": {"patients": [{"patient_id": 1, "patient_name": "Alice Smith", "age": 28}, {"patient_id": 2, "patient_name": "Bob Johnson", "age": 35}, {"patient_id": 3, "patient_name": "Carol Davis", "age": 42}, {"patient_id": 4, "patient_name": "David Wilson", "age": 31}, {"patient_id": 5, "patient_name": "Emma Brown", "age": 29}], "covid_tests": [{"test_id": 1, "patient_id": 1, "test_date": "2023-01-15", "result": "Positive"}, {"test_id": 2, "patient_id": 1, "test_date": "2023-01-25", "result": "Negative"}, {"test_id": 3, "patient_id": 2, "test_date": "2023-02-01", "result": "Positive"}, {"test_id": 4, "patient_id": 2, "test_date": "2023-02-05", "result": "Inconclusive"}, {"test_id": 5, "patient_id": 2, "test_date": "2023-02-12", "result": "Negative"}, {"test_id": 6, "patient_id": 3, "test_date": "2023-01-20", "result": "Negative"}, {"test_id": 7, "patient_id": 3, "test_date": "2023-02-10", "result": "Positive"}, {"test_id": 8, "patient_id": 3, "test_date": "2023-02-20", "result": "Negative"}, {"test_id": 9, "patient_id": 4, "test_date": "2023-01-10", "result": "Positive"}, {"test_id": 10, "patient_id": 4, "test_date": "2023-01-18", "result": "Positive"}, {"test_id": 11, "patient_id": 5, "test_date": "2023-02-15", "result": "Negative"}, {"test_id": 12, "patient_id": 5, "test_date": "2023-02-20", "result": "Negative"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Earliest positive

`first_positive` filters rows to `result='Positive'` and groups by patient. `MIN(test_date)` gives one anchor date per patient.

Patients with only negative or inconclusive tests create no row and cannot enter the result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"patients": [{"patient_id": 1, "patient_name": "Alice Smith", "age": 28}, {"patient_id": 2, "patient_name": "Bob Johnson", "age": 35}, {"patient_id": 3, "patient_name": "Carol Davis", "age": 42}, {"patient_id": 4, "patient_name": "David Wilson", "age": 31}, {"patient_id": 5, "patient_name": "Emma Brown", "age": 29}], "covid_tests": [{"test_id": 1, "patient_id": 1, "test_date": "2023-01-15", "result": "Positive"}, {"test_id": 2, "patient_id": 1, "test_date": "2023-01-25", "result": "Negative"}, {"test_id": 3, "patient_id": 2, "test_date": "2023-02-01", "result": "Positive"}, {"test_id": 4, "patient_id": 2, "test_date": "2023-02-05", "result": "Inconclusive"}, {"test_id": 5, "patient_id": 2, "test_date": "2023-02-12", "result": "Negative"}, {"test_id": 6, "patient_id": 3, "test_date": "2023-01-20", "result": "Negative"}, {"test_id": 7, "patient_id": 3, "test_date": "2023-02-10", "result": "Positive"}, {"test_id": 8, "patient_id": 3, "test_date": "2023-02-20", "result": "Negative"}, {"test_id": 9, "patient_id": 4, "test_date": "2023-01-10", "result": "Positive"}, {"test_id": 10, "patient_id": 4, "test_date": "2023-01-18", "result": "Positive"}, {"test_id": 11, "patient_id": 5, "test_date": "2023-02-15", "result": "Negative"}, {"test_id": 12, "patient_id": 5, "test_date": "2023-02-20", "result": "Negative"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Earliest later negative

The second CTE joins every test `t` to that patient’s positive anchor `p` with:

`t.test_date > p.first_positive_date`.

The strict greater-than condition excludes negatives before the infection evidence and negatives on the same date.

After filtering `t.result='Negative'`, `MIN(t.test_date)` selects the first qualifying recovery evidence. Inconclusive and later positive tests neither qualify nor prevent a later negative.

Grouping produces at most one recovery date per patient. A positive-only patient has no row in this CTE.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The second CTE joins every test `t` to that patient’s positi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Final joins

An inner join between the two CTEs keeps only patients having both an earliest positive and a later negative. Joining `patients` attaches name and age.

`DATEDIFF(first_negative_date,first_positive_date)` returns elapsed calendar days. Because the negative date is strictly later, recovery time is positive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["patient_id", "patient_name", "age", "recovery_time"], "rows": [[1, "Alice Smith", 28, 10], [3, "Carol Davis", 42, 10], [2, "Bob Johnson", 35, 11]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"patients": [{"patient_id": 1, "patient_name": "Alice Smith", "age": 28}, {"patient_id": 2, "patient_name": "Bob Johnson", "age": 35}, {"patient_id": 3, "patient_name": "Carol Davis", "age": 42}, {"patient_id": 4, "patient_name": "David Wilson", "age": 31}, {"patient_id": 5, "patient_name": "Emma Brown", "age": 29}], "covid_tests": [{"test_id": 1, "patient_id": 1, "test_date": "2023-01-15", "result": "Positive"}, {"test_id": 2, "patient_id": 1, "test_date": "2023-01-25", "result": "Negative"}, {"test_id": 3, "patient_id": 2, "test_date": "2023-02-01", "result": "Positive"}, {"test_id": 4, "patient_id": 2, "test_date": "2023-02-05", "result": "Inconclusive"}, {"test_id": 5, "patient_id": 2, "test_date": "2023-02-12", "result": "Negative"}, {"test_id": 6, "patient_id": 3, "test_date": "2023-01-20", "result": "Negative"}, {"test_id": 7, "patient_id": 3, "test_date": "2023-02-10", "result": "Positive"}, {"test_id": 8, "patient_id": 3, "test_date": "2023-02-20", "result": "Negative"}, {"test_id": 9, "patient_id": 4, "test_date": "2023-01-10", "result": "Positive"}, {"test_id": 10, "patient_id": 4, "test_date": "2023-01-18", "result": "Positive"}, {"test_id": 11, "patient_id": 5, "test_date": "2023-02-15", "result": "Negative"}, {"test_id": 12, "patient_id": 5, "test_date": "2023-02-20", "result": "Negative"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["patient_id", "patient_name", "age", "recovery_time"], "rows": [[1, "Alice Smith", 28, 10], [3, "Carol Davis", 42, 10], [2, "Bob Johnson", 35, 11]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated subqueries:** Find each patient’s m:** - **Correlated subqueries:** Find each patient’s minimum positive and then a correlated minimum negative. It is readable but may repeat scans without good indexes.
- **Window functions:** Ordered conditional dates can solve the problem, but two grouped anchors express the definition directly.
- **Negative before positive:** It is ignored by the strict date join.
- **Negative on the same date:** It is not “later” and is excluded.
- **Multiple positives:** Only the earliest anchors recovery, even if a later positive occurs before the negative.
- **Multiple later negatives:** MIN selects the earliest one.
- **Inconclusive tests:** They are ignored in both CTE filters.
- **Only positive:** Missing second-CTE row excludes the patient.
- **Only negative:** Missing first-CTE row excludes the patient.
- **No tests:** The patient never appears in either aggregate.
- **Equal recovery times:** Name ascending resolves the specified tie.
- **Date arithmetic:** DATEDIFF uses dates rather than subtracting day-of-month numbers, so month and year boundaries work.
- **Inner joins:** They naturally enforce the requirement for catalog identity and both test types.
- **Strict result spelling:** The source compares exact strings `Positive` and `Negative` as provided by the schema.
- **Same-name patients:** They remain separate by unique patient ID even though final tie order is not fully determined.
- **Why the earliest positive is computed first:** Searching for any positive-negative pair and minimizing their gap would answer a different question. The required recovery clock is anchored to the patient’s first positive even when a later positive would yield a shorter interval.
- **Aggregation grain:** Both CTEs group by patient ID, never patient name. Names need not be unique, and grouping by them could merge different people’s medical histories into a false recovery sequence.
- **Positive after recovery:** A later positive does not change the first recovery interval defined by the statement. Once the earliest later negative is selected, subsequent tests are outside this calculation.
- **Database date semantics:** `test_date` is a date rather than a timestamp, so strict comparison and `DATEDIFF` operate in whole calendar days. If time-of-day ordering mattered, the schema and expression would need timestamp precision.
- **Returned age:** Age is read from the patient catalog at query time and does not participate in recovery qualification. Tests establish eligibility and duration; the catalog join supplies descriptive fields only after those medical-date aggregates are fixed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T log T + P log P)$. Let `T` be test rows and `P` patient rows. Filtering and grouping tests can require `O(T\log T)` with sort aggregation, while indexed/hash plans may approach linear expected work. Patient joining and final ordering contribute up to `O(P\log P)`.
- **Auxiliary Space Complexity:** $O(T + P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
