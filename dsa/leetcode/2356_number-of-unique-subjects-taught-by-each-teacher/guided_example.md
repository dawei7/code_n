# Guided Example: Number of Unique Subjects Taught by Each Teacher

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teacher": [{"teacher_id": 1, "subject_id": 2, "dept_id": 3}, {"teacher_id": 1, "subject_id": 2, "dept_id": 4}, {"teacher_id": 1, "subject_id": 3, "dept_id": 3}, {"teacher_id": 2, "subject_id": 1, "dept_id": 1}, {"teacher_id": 2, "subject_id": 2, "dept_id": 1}, {"teacher_id": 2, "subject_id": 3, "dept_id": 1}, {"teacher_id": 2, "subject_id": 4, "dept_id": 1}]}}`
- **Required output:** `{"columns": ["teacher_id", "cnt"], "rows": [[1, 2], [2, 4]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teacher`

The objective is to compute `{"columns": ["teacher_id", "cnt"], "rows": [[1, 2], [2, 4]]}` from `{"tables": {"Teacher": [{"teacher_id": 1, "subject_id": 2, "dept_id": 3}, {"teacher_id": 1, "subject_id": 2, "dept_id": 4}, {"teacher_id": 1, "subject_id": 3, "dept_id": 3}, {"teacher_id": 2, "subject_id": 1, "dept_id": 1}, {"teacher_id": 2, "subject_id": 2, "dept_id": 1}, {"teacher_id": 2, "subject_id": 3, "dept_id": 1}, {"teacher_id": 2, "subject_id": 4, "dept_id": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be counted

Every input row is a teaching assignment containing a `teacher_id`, a `subject_id`, and a `dept_id`. The requested output has one row per teacher and reports how many different subjects that teacher teaches. The important word is *different*: two assignments can have the same teacher and subject but different departments. Those rows describe the same subject for this question and must contribute only one to the teacher's count.

For example, suppose a teacher has the following subject values across four rows:



There are four assignments, but only the two distinct subject identifiers `2` and `3`. The answer for that teacher is therefore `2`. The department is useful in the source table's primary key, but it is deliberately absent from the quantity being counted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teacher": [{"teacher_id": 1, "subject_id": 2, "dept_id": 3}, {"teacher_id": 1, "subject_id": 2, "dept_id": 4}, {"teacher_id": 1, "subject_id": 3, "dept_id": 3}, {"teacher_id": 2, "subject_id": 1, "dept_id": 1}, {"teacher_id": 2, "subject_id": 2, "dept_id": 1}, {"teacher_id": 2, "subject_id": 3, "dept_id": 1}, {"teacher_id": 2, "subject_id": 4, "dept_id": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Partitioning rows with `GROUP BY`

SQL aggregate functions turn several input rows into a summarized output row. Before counting anything, the query must specify which input rows belong to the same summary. The clause



does that partitioning. In MySQL, `1` in this context is a positional reference to the first expression in the `SELECT` list. The first selected expression is `teacher_id`, so `GROUP BY 1` is a compact spelling of `GROUP BY teacher_id`.

After grouping, all rows with the same `teacher_id` are processed together, and different teachers cannot affect one another. SQL produces exactly one aggregate result row for each teacher identifier present in `Teacher`. No separate join, subquery, or temporary result is needed because all necessary information already appears in this one table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Counting subjects rather than assignments

Within each teacher's group, the expression



first collapses repeated `subject_id` values and then counts the remaining values. Plain `COUNT(subject_id)` would count assignment rows, so it would incorrectly count the same subject more than once when that teacher teaches it in multiple departments. Including `dept_id` in the distinct expression would also answer a different question: it would count distinct subject-department assignments instead of distinct subjects.

The table contract makes `subject_id` an integer and uses `(subject_id, dept_id)` as its primary key. In a normal SQL table, primary-key columns cannot be `NULL`. Consequently, the usual detail that `COUNT` ignores `NULL` values does not change this problem's result. Every assignment contributes a real subject identifier to its teacher's distinct-value set.

The aggregate is named with



because the output contract requires the count column to be called `cnt`. An alias changes only the result column's label; it does not affect grouping or counting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["teacher_id", "cnt"], "rows": [[1, 2], [2, 4]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teacher": [{"teacher_id": 1, "subject_id": 2, "dept_id": 3}, {"teacher_id": 1, "subject_id": 2, "dept_id": 4}, {"teacher_id": 1, "subject_id": 3, "dept_id": 3}, {"teacher_id": 2, "subject_id": 1, "dept_id": 1}, {"teacher_id": 2, "subject_id": 2, "dept_id": 1}, {"teacher_id": 2, "subject_id": 3, "dept_id": 1}, {"teacher_id": 2, "subject_id": 4, "dept_id": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["teacher_id", "cnt"], "rows": [[1, 2], [2, 4]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Plain `COUNT(subject_id)`:** This counts rows rather than unique subjects and fails whenever the same teacher teaches one subject in more than one department.
- **Distinct teacher-subject subquery:** One can first select distinct `(teacher_id, subject_id)` pairs and then count rows per teacher. It is logically correct but adds an unnecessary query layer because `COUNT(DISTINCT subject_id)` expresses the operation directly.
- **Grouping by `teacher_id, subject_id`:** This produces one row per teacher-subject pair rather than the required one row per teacher unless another aggregation stage is added.
- **Including `dept_id` in the count:** Departments do not define uniqueness in the requested answer. Counting subject-department pairs would overcount subjects taught across multiple departments.
- **`GROUP BY 1` versus an explicit name:** `GROUP BY teacher_id` is more self-documenting and equivalent here. The exact solution uses `GROUP BY 1`, whose `1` refers to the first selected expression, not to the literal number one as a group key.
- **A teacher with one assignment:** Its group contains one subject, so the distinct count is `1`.
- **Repeated subject across departments:** All occurrences share a `subject_id` and collapse to one value before counting, which is the central edge case.
- **Different teachers teaching the same subject:** Grouping separates their rows first, so each teacher independently receives credit for that subject.
- **Output order:** Without `ORDER BY`, database row order is unspecified, but the statement explicitly accepts any order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of rows in `Teacher`. The manifest states $O(R \log R)$ time and $O(R)$ space. A standard way for a database engine to execute grouped distinct aggregation is to sort or otherwise organize the rows by the grouping key and distinct value. Sorting $R$ records takes $O(R \log R)$ time, after which a scan can identify changes in teacher and subject. Internal temporary structures or the sorted working set may occupy $O(R)$ space.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
