# Guided Example: Students and Examinations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Students": [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}, {"student_id": 13, "student_name": "John"}, {"student_id": 6, "student_name": "Alex"}], "Subjects": [{"subject_name": "Math"}, {"subject_name": "Physics"}, {"subject_name": "Programming"}], "Examinations": [{"student_id": 1, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Programming"}, {"student_id": 2, "subject_name": "Programming"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Programming"}, {"student_id": 13, "subject_name": "Physics"}, {"student_id": 2, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Math"}]}}`
- **Required output:** `{"columns": ["student_id", "student_name", "subject_name", "attended_exams"], "rows": [[1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Physics", 0], [2, "Bob", "Programming", 1], [6, "Alex", "Math", 0], [6, "Alex", "Physics", 0], [6, "Alex", "Programming", 0], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Students`

The objective is to compute `{"columns": ["student_id", "student_name", "subject_name", "attended_exams"], "rows": [[1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Physics", 0], [2, "Bob", "Programming", 1], [6, "Alex", "Math", 0], [6, "Alex", "Physics", 0], [6, "Alex", "Programming", 0], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}` from `{"tables": {"Students": [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}, {"student_id": 13, "student_name": "John"}, {"student_id": 6, "student_name": "Alex"}], "Subjects": [{"subject_name": "Math"}, {"subject_name": "Physics"}, {"subject_name": "Programming"}], "Examinations": [{"student_id": 1, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Programming"}, {"student_id": 2, "subject_name": "Programming"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Programming"}, {"student_id": 13, "subject_name": "Physics"}, {"student_id": 2, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Math"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Begin with every student-subject combination

The result must contain a row even when a student attended a subject's exam zero times. Starting from `Examinations` cannot naturally produce combinations that have no rows there. The query instead builds the complete set of required combinations first, then attaches matching attendance records.

In MySQL, `Students JOIN Subjects` without an `ON` or `USING` condition acts as a cross join. Every student is paired with every subject. If there are $S$ students and $U$ subjects, this stage produces exactly $S\cdot U$ rows, including pairs with no attendance.

The selected `student_name` travels with its student's primary-key row, while `subject_name` comes from the unique subject row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Students": [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}, {"student_id": 13, "student_name": "John"}, {"student_id": 6, "student_name": "Alex"}], "Subjects": [{"subject_name": "Math"}, {"subject_name": "Physics"}, {"subject_name": "Programming"}], "Examinations": [{"student_id": 1, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Programming"}, {"student_id": 2, "subject_name": "Programming"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Programming"}, {"student_id": 13, "subject_name": "Physics"}, {"student_id": 2, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Math"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Preserve zero-attendance pairs with a left join

The query left-joins `Examinations AS e` with `USING (student_id, subject_name)`. For a student-subject pair, every examination record with both matching fields joins to it. Because `Examinations` may contain duplicates, repeated attendance rows are deliberately preserved: each row represents one attendance.

If no examination record matches, the left join still emits the student-subject pair and fills columns from alias `e` with `NULL`. This placeholder is why an inner join would be wrong: an inner join would discard every zero-attendance combination.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query left-joins `Examinations AS e` with `USING (studen... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count a nullable examination column rather than all rows

The expression `COUNT(e.student_id)` counts only non-null values from the examination side. For a real matching attendance row, `e.student_id` is present and contributes one. For the placeholder row created by a missing match, it is `NULL` and contributes zero.

Using `COUNT(*)` in this exact join would incorrectly return one for a student-subject pair with no examination, because the preserved left-side placeholder is still a row. Qualifying the column with `e.` is equally important: the unqualified cross-product `student_id` is never null and would also count the placeholder.

For Alice and Math in the example, three matching examination rows join and the count is three. For Bob and Physics, no row matches, the left join produces one null examination placeholder, and `COUNT(e.student_id)` returns zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "student_name", "subject_name", "attended_exams"], "rows": [[1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Physics", 0], [2, "Bob", "Programming", 1], [6, "Alex", "Math", 0], [6, "Alex", "Physics", 0], [6, "Alex", "Programming", 0], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Students": [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}, {"student_id": 13, "student_name": "John"}, {"student_id": 6, "student_name": "Alex"}], "Subjects": [{"subject_name": "Math"}, {"subject_name": "Physics"}, {"subject_name": "Programming"}], "Examinations": [{"student_id": 1, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Programming"}, {"student_id": 2, "subject_name": "Programming"}, {"student_id": 1, "subject_name": "Physics"}, {"student_id": 1, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Math"}, {"student_id": 13, "subject_name": "Programming"}, {"student_id": 13, "subject_name": "Physics"}, {"student_id": 2, "subject_name": "Math"}, {"student_id": 1, "subject_name": "Math"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "student_name", "subject_name", "attended_exams"], "rows": [[1, "Alice", "Math", 3], [1, "Alice", "Physics", 2], [1, "Alice", "Programming", 1], [2, "Bob", "Math", 1], [2, "Bob", "Physics", 0], [2, "Bob", "Programming", 1], [6, "Alex", "Math", 0], [6, "Alex", "Physics", 0], [6, "Alex", "Programming", 0], [13, "John", "Math", 1], [13, "John", "Physics", 1], [13, "John", "Programming", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pre-aggregate examinations first:** Group `Exa:** - **Pre-aggregate examinations first:** Group `Examinations` by student and subject, cross join the dimension tables, then left join the compact counts and use `IFNULL(..., 0)`. This can reduce intermediate duplicates while producing the same result.
- **Start from `Examinations`:** It omits student-subject pairs with zero attendance and cannot meet the output contract by itself.
- **Inner join examinations:** It similarly removes every zero-count pair.
- **`COUNT(*)` after a left join:** It counts the placeholder row and incorrectly reports one instead of zero.
- **Duplicate examination rows:** They represent repeated attendances and must each contribute one; the exact query preserves and counts them.
- **Student with no examinations:** The cross join still produces every subject, each with count zero.
- **Subject with no examinations:** Every student still receives a row for that subject with zero.
- **No examination rows at all:** The result remains the full student-subject product with all counts zero.
- **Ordinal grouping:** `GROUP BY 1, 3` depends on select-list positions; explicit column names can be clearer during future query edits.
- **Functional dependency:** Selecting `student_name` is safe because primary-key `student_id` uniquely determines it.
- **Required order:** Removing `ORDER BY` would leave row order unspecified and violate this problem's explicit sorting requirement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R+E)$. Let $S$ be the number of students, $U$ the number of subjects, $E$ the number of examination rows, and $R=S\cdot U$ the mandatory number of result combinations. An efficient hash- or index-assisted plan can form and aggregate matches in $O(R+E)$ time before ordering. Since the output itself has $R$ rows, $\Omega(R)$ work is unavoidable.
- **Auxiliary Space Complexity:** $O(R+E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
