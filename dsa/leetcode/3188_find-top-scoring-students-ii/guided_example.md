# Guided Example: Find Top Scoring Students II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 105, "name": "Machine Learning", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 106, "name": "Probability", "credits": 3, "major": "Mathematics", "mandatory": "No"}, {"course_id": 107, "name": "Operating Systems", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 108, "name": "Statistics", "credits": 3, "major": "Mathematics", "mandatory": "No"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 102, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 105, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 107, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 2, "course_id": 102, "semester": "Spring 2023", "grade": "B", "GPA": 3}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 104, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 106, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 108, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "B", "GPA": 3}, {"student_id": 4, "course_id": 104, "semester": "Spring 2023", "grade": "B", "GPA": 3}]}}`
- **Required output:** `{"columns": ["student_id"], "rows": [[1], [3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `students`

The objective is to compute `{"columns": ["student_id"], "rows": [[1], [3]]}` from `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 105, "name": "Machine Learning", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 106, "name": "Probability", "credits": 3, "major": "Mathematics", "mandatory": "No"}, {"course_id": 107, "name": "Operating Systems", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 108, "name": "Statistics", "credits": 3, "major": "Mathematics", "mandatory": "No"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 102, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 105, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 107, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 2, "course_id": 102, "semester": "Spring 2023", "grade": "B", "GPA": 3}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 104, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 106, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 108, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "B", "GPA": 3}, {"student_id": 4, "course_id": 104, "semester": "Spring 2023", "grade": "B", "GPA": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Treat the requirements as two different scopes.** A qualifying student must satisfy one condition over all enrollment records and several conditions over courses offered by that student's own major. The SQL keeps these scopes separate:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 105, "name": "Machine Learning", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 106, "name": "Probability", "credits": 3, "major": "Mathematics", "mandatory": "No"}, {"course_id": 107, "name": "Operating Systems", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 108, "name": "Statistics", "credits": 3, "major": "Mathematics", "mandatory": "No"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 102, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 105, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 107, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 2, "course_id": 102, "semester": "Spring 2023", "grade": "B", "GPA": 3}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 104, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 106, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 108, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "B", "GPA": 3}, {"student_id": 4, "course_id": 104, "semester": "Spring 2023", "grade": "B", "GPA": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the common table expression `T` computes average GPA from every row in `enrollments`, including courses outside the student's major;
- the outer query joins each remaining student to the complete course catalog for that student's major, then compares those required catalog rows with the student's matching enrollment rows.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - the common table expression `T` computes average GPA from ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This separation prevents a common mistake: if GPA were averaged only after joining courses by major, out-of-major courses would disappear even though the statement explicitly includes them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id"], "rows": [[1], [3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 1, "name": "Alice", "major": "Computer Science"}, {"student_id": 2, "name": "Bob", "major": "Computer Science"}, {"student_id": 3, "name": "Charlie", "major": "Mathematics"}, {"student_id": 4, "name": "David", "major": "Mathematics"}], "courses": [{"course_id": 101, "name": "Algorithms", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 102, "name": "Data Structures", "credits": 3, "major": "Computer Science", "mandatory": "Yes"}, {"course_id": 103, "name": "Calculus", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 104, "name": "Linear Algebra", "credits": 4, "major": "Mathematics", "mandatory": "Yes"}, {"course_id": 105, "name": "Machine Learning", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 106, "name": "Probability", "credits": 3, "major": "Mathematics", "mandatory": "No"}, {"course_id": 107, "name": "Operating Systems", "credits": 3, "major": "Computer Science", "mandatory": "No"}, {"course_id": 108, "name": "Statistics", "credits": 3, "major": "Mathematics", "mandatory": "No"}], "enrollments": [{"student_id": 1, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 102, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 105, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 1, "course_id": 107, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 2, "course_id": 101, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 2, "course_id": 102, "semester": "Spring 2023", "grade": "B", "GPA": 3}, {"student_id": 3, "course_id": 103, "semester": "Fall 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 104, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 106, "semester": "Spring 2023", "grade": "A", "GPA": 4}, {"student_id": 3, "course_id": 108, "semester": "Fall 2023", "grade": "B", "GPA": 3.5}, {"student_id": 4, "course_id": 103, "semester": "Fall 2023", "grade": "B", "GPA": 3}, {"student_id": 4, "course_id": 104, "semester": "Spring 2023", "grade": "B", "GPA": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id"], "rows": [[1], [3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Conditional aggregation with explicit distinct:** - **Conditional aggregation with explicit distinct course IDs:** Counting `COUNT(DISTINCT CASE WHEN ... THEN course_id END)` can express “two different elective courses” and protect the quantity test from repeated-semester duplicates. It is more verbose and may cost additional deduplication work, but it better matches the literal course-count requirement.
- **Relational division with `NOT EXISTS`:** A student can be rejected when there exists a mandatory course in the major for which no A enrollment exists. This often makes the “all required courses” meaning explicit and avoids comparing aggregate counts, though the optimizer and indexes determine performance.
- **Separate requirement CTEs:** One CTE can count mandatory catalog courses by major, another can aggregate a student's major-course results, and another can calculate GPA. Joining those summaries yields clearer named quantities at the cost of a longer query.
- **Outside-major enrollments:** They intentionally affect `AVG(GPA)` in `T` but never count as mandatory or elective courses for the student's major.
- **Untaken electives:** The left join keeps their catalog rows, but `grade IS NOT NULL` and `grade IN ('A', 'B')` are not true. They contribute to neither elective count, which is correct because only at least two electives—not all electives—are required.
- **Missing mandatory enrollment:** The catalog row survives, the mandatory denominator increases, and no A is counted. The student therefore fails.
- **Low mandatory grade:** Any mandatory joined row whose grade is not A prevents equality. The query requires exactly grade A, not merely a GPA threshold.
- **Elective grade below B:** A non-null grade outside A/B appears in the left elective count but not the right one, so even one such row rejects the student. This means the query interprets the grade condition as applying to every enrolled in-major elective, not merely to two qualifying electives.
- **Repeated semesters are a semantic limitation:** The enrollment primary key includes `semester`, so one student may have multiple rows for the same course. The exact query counts rows, not distinct `course_id` values. Two attempts at the same elective can satisfy the “at least two” sum even though they are only one elective course. It also requires every joined attempt of an elective to be A or B and every joined attempt of a mandatory course to be A. Those behaviors are stricter in grade handling and looser in distinct-course counting than a natural reading of the requirement.
- **Case sensitivity of `mandatory`:** The schema describes enum literals `'Yes'` and `'No'`, while the source compares `'yes'` and `'no'`. Typical MySQL text collations are case-insensitive, under which these compare equal. Under a case-sensitive collation, neither comparison matches, the elective count cannot reach two, and the query is incorrect. The exact solution therefore depends on the judge's collation behavior.
- **Null GPA or grade values:** `AVG` ignores null GPA values, and `SUM` ignores null boolean results. The source assumes the problem's intended enrollment facts are populated. If nulls are allowed beyond missing rows introduced by the left join, the effective semantics should be reviewed explicitly.
- **Major with no catalog courses:** The inner `JOIN courses USING (major)` produces no outer group for that student, so the student cannot appear. This is reasonable for the given qualification model but is an exact consequence of the join.
- **Ordering:** `ORDER BY 1` refers to the first selected expression. It works here because only `student_id` is selected, though spelling out `ORDER BY student_id` would be more self-documenting.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of enrollment rows and let $j$ be the number of rows produced by joining GPA-qualified students to their major's courses and then to matching enrollments. The precise physical cost depends on the database engine, indexes, join plan, grouping strategy, and whether sorting or hashing implements each aggregation.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
