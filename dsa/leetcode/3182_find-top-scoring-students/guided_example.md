# Guided Example: Find Top Scoring Students

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A"}, {"student_id": 1, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "B"}, {"student_id": 2, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 104, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 104, "semester": "Fall 2023", "grade": "B"}]}}`
- **Required output:** `{"columns": ["student_id"], "rows": [[1], [3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `students`

The objective is to compute `{"columns": ["student_id"], "rows": [[1], [3]]}` from `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A"}, {"student_id": 1, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "B"}, {"student_id": 2, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 104, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 104, "semester": "Fall 2023", "grade": "B"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create one required row per student-course pair

`students JOIN courses USING (major)` pairs every student with every course offered by that student's major.

This turns the universal requirement “all major courses” into rows that can be checked by aggregation. A student with two required courses receives two base rows.

The left join to `enrollments` uses both `student_id` and `course_id`. A completed enrollment attaches its grade. A missing course enrollment keeps the required row but supplies null enrollment columns, which is why a left join is necessary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A"}, {"student_id": 1, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "B"}, {"student_id": 2, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 104, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 104, "semester": "Fall 2023", "grade": "B"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compare A rows with all required joined rows

MySQL expression `grade = 'A'` evaluates to 1 for A, 0 for another non-null grade, and null for missing enrollment.

`SUM(grade = 'A')` counts A enrollment rows. `COUNT(major)` counts every joined row because `major` comes from required student/course data and is non-null.

Equality holds only when every counted row contributes one—meaning every required joined record has grade A and none is missing or non-A.

Grouping by `student_id` makes this test independent per student. `ORDER BY 1` returns passing IDs ascending.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Example

For a major with courses 101 and 102:

- grades A and A yield sum 2 and count 2, so student passes;
- grades A and B yield 1 versus 2, so fails;
- enrollment only in 101 with A leaves course 102 null, yielding sum 1 versus count 2, so fails.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id"], "rows": [[1], [3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A"}, {"student_id": 1, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "B"}, {"student_id": 2, "course_id": 102, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 3, "course_id": 104, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "A"}, {"student_id": 4, "course_id": 104, "semester": "Fall 2023", "grade": "B"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id"], "rows": [[1], [3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Double NOT EXISTS:** Select a student for whom no required course lacks an A. This expresses universal logic directly.
- **Count distinct required courses:** Compare major course count with distinct courses having at least one A; this supports the “ever achieved A” interpretation.
- **Inner join enrollments:** Incorrect for detecting missing courses because absent rows disappear instead of causing failure.
- **Missing required course:** Left-join null makes the student fail.
- **One B attempt:** Exact query fails even if another semester has A.
- **Several A attempts:** They duplicate numerator and denominator equally and still pass.
- **Major with no courses:** Student disappears in the initial inner join.
- **Student not enrolled anywhere:** Required rows remain with null grades and fail.
- **Course IDs globally unique:** The enrollment join uses student and course and does not need major again.
- **Boolean SUM:** Relies on MySQL treating true as 1 and false as 0.
- **Null grade:** It cannot contribute an A and prevents equality through the counted required row.
- **Final ordering:** Positional `ORDER BY 1` sorts student IDs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be total joined-row volume across required courses and enrollment attempts.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
