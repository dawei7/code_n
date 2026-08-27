# Guided Example: Highest Grade For Each Student

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Enrollments": [{"student_id": 2, "course_id": 2, "grade": 95}, {"student_id": 2, "course_id": 3, "grade": 95}, {"student_id": 1, "course_id": 1, "grade": 90}, {"student_id": 1, "course_id": 2, "grade": 99}, {"student_id": 3, "course_id": 1, "grade": 80}, {"student_id": 3, "course_id": 2, "grade": 75}, {"student_id": 3, "course_id": 3, "grade": 82}]}}`
- **Required output:** `{"columns": ["student_id", "course_id", "grade"], "rows": [[1, 2, 99], [2, 2, 95], [3, 3, 82]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Enrollments`

The objective is to compute `{"columns": ["student_id", "course_id", "grade"], "rows": [[1, 2, 99], [2, 2, 95], [3, 3, 82]]}` from `{"tables": {"Enrollments": [{"student_id": 2, "course_id": 2, "grade": 95}, {"student_id": 2, "course_id": 3, "grade": 95}, {"student_id": 1, "course_id": 1, "grade": 90}, {"student_id": 1, "course_id": 2, "grade": 99}, {"student_id": 3, "course_id": 1, "grade": 80}, {"student_id": 3, "course_id": 2, "grade": 75}, {"student_id": 3, "course_id": 3, "grade": 82}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define one complete priority order per student

For each student, the desired row is determined by two priorities. A larger grade is always better. When grades tie, a smaller course ID is better.

The window ordering writes these rules directly:

`ORDER BY grade DESC, course_id`

`DESC` puts the maximum grade first. Course ID uses ascending order by default, so the smallest tied course comes first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Enrollments": [{"student_id": 2, "course_id": 2, "grade": 95}, {"student_id": 2, "course_id": 3, "grade": 95}, {"student_id": 1, "course_id": 1, "grade": 90}, {"student_id": 1, "course_id": 2, "grade": 99}, {"student_id": 3, "course_id": 1, "grade": 80}, {"student_id": 3, "course_id": 2, "grade": 75}, {"student_id": 3, "course_id": 3, "grade": 82}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank rows without collapsing their columns

A grouped `MAX(grade)` could find the best grade, but it would not by itself identify which course should be returned. The query needs the complete enrollment row after applying both priorities.

`RANK() OVER (PARTITION BY student_id ... )` keeps every original row and adds its position within that student’s ordered enrollments. `PARTITION BY student_id` restarts ranking for each student, preventing one student’s grades from affecting another’s selection.

The best row in every partition receives `rk = 1`. The outer query filters to those rows and selects the original `student_id`, `course_id`, and `grade`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A grouped `MAX(grade)` could find the best grade, but it wou... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why rank one is unique here

`RANK` normally gives the same rank to rows tied on every ordering expression. In this query, a tie would require equal grade and equal course ID for the same student.

The composite primary key `(student_id, course_id)` forbids two rows with the same student and course. Therefore, no two rows within one partition can tie on both ordering expressions. Exactly one row receives rank one for each represented student.

This is why `RANK`, `ROW_NUMBER`, and `DENSE_RANK` would all select the same single winner under the source constraints, although their behavior differs for true ordering ties.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "course_id", "grade"], "rows": [[1, 2, 99], [2, 2, 95], [3, 3, 82]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Enrollments": [{"student_id": 2, "course_id": 2, "grade": 95}, {"student_id": 2, "course_id": 3, "grade": 95}, {"student_id": 1, "course_id": 1, "grade": 90}, {"student_id": 1, "course_id": 2, "grade": 99}, {"student_id": 3, "course_id": 1, "grade": 80}, {"student_id": 3, "course_id": 2, "grade": 75}, {"student_id": 3, "course_id": 3, "grade": 82}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "course_id", "grade"], "rows": [[1, 2, 99], [2, 2, 95], [3, 3, 82]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`ROW_NUMBER`:** Assign row numbers with the sa:** - **`ROW_NUMBER`:** Assign row numbers with the same partition and ordering, then keep one. It communicates the one-winner intent directly and is equivalent under the composite primary key.
- **Maximum-grade CTE plus join:** Find `MAX(grade)` per student, join back to matching rows, then take the minimum course ID among ties. This works but needs multiple logical stages.
- **Correlated subquery:** Reject a row when a better grade or equal grade with smaller course exists. It expresses dominance directly but is usually harder to read and optimize.
- **Group only by student with arbitrary course:** Incorrect because SQL cannot safely associate an unaggregated course ID with the maximum grade.
- **One enrollment:** That row is rank one and is returned.
- **Several equal maximum grades:** The smallest course ID wins through the second ordering key.
- **Smaller course with lower grade:** It does not win because grade has higher priority.
- **Negative or null grades:** Null is explicitly forbidden; numeric grade ordering is therefore unambiguous.
- **Duplicate student-course row:** The primary key forbids it, which guarantees a unique complete ordering.
- **Students with different enrollment counts:** Partitioning handles each independently, including students with only one course.
- **Final ordering:** The outer `ORDER BY` is necessary because window ordering alone does not promise result-table order.
- **Empty table:** No partitions or winner rows are created.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R \log R)$. Let $R$ be the number of enrollment rows. A typical database plan sorts rows by student ID, descending grade, and course ID to evaluate the window. General comparison sorting costs $O(R\log R)$ time.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
