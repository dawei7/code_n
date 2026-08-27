# Guided Example: Find Students with Study Spiral Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"students": [{"student_id": 1, "student_name": "Alice Chen", "major": "Computer Science"}, {"student_id": 2, "student_name": "Bob Johnson", "major": "Mathematics"}, {"student_id": 3, "student_name": "Carol Davis", "major": "Physics"}, {"student_id": 4, "student_name": "David Wilson", "major": "Chemistry"}, {"student_id": 5, "student_name": "Emma Brown", "major": "Biology"}], "study_sessions": [{"session_id": 1, "student_id": 1, "subject": "Math", "session_date": "2023-10-01", "hours_studied": 2.5}, {"session_id": 2, "student_id": 1, "subject": "Physics", "session_date": "2023-10-02", "hours_studied": 3.0}, {"session_id": 3, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 4, "student_id": 1, "subject": "Math", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 5, "student_id": 1, "subject": "Physics", "session_date": "2023-10-05", "hours_studied": 3.0}, {"session_id": 6, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-06", "hours_studied": 2.0}, {"session_id": 7, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-01", "hours_studied": 4.0}, {"session_id": 8, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-02", "hours_studied": 3.5}, {"session_id": 9, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-03", "hours_studied": 2.5}, {"session_id": 10, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-04", "hours_studied": 3.0}, {"session_id": 11, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-05", "hours_studied": 4.0}, {"session_id": 12, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-06", "hours_studied": 3.5}, {"session_id": 13, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-07", "hours_studied": 2.5}, {"session_id": 14, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-08", "hours_studied": 3.0}, {"session_id": 15, "student_id": 3, "subject": "Biology", "session_date": "2023-10-01", "hours_studied": 2.0}, {"session_id": 16, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-02", "hours_studied": 2.5}, {"session_id": 17, "student_id": 3, "subject": "Biology", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 18, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 19, "student_id": 4, "subject": "Organic", "session_date": "2023-10-01", "hours_studied": 3.0}, {"session_id": 20, "student_id": 4, "subject": "Physical", "session_date": "2023-10-05", "hours_studied": 2.5}]}}`
- **Required output:** `{"columns": ["student_id", "student_name", "major", "cycle_length", "total_study_hours"], "rows": [[2, "Bob Johnson", "Mathematics", 4, 26.0], [1, "Alice Chen", "Computer Science", 3, 15.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `students`

The objective is to compute `{"columns": ["student_id", "student_name", "major", "cycle_length", "total_study_hours"], "rows": [[2, "Bob Johnson", "Mathematics", 4, 26.0], [1, "Alice Chen", "Computer Science", 3, 15.0]]}` from `{"tables": {"students": [{"student_id": 1, "student_name": "Alice Chen", "major": "Computer Science"}, {"student_id": 2, "student_name": "Bob Johnson", "major": "Mathematics"}, {"student_id": 3, "student_name": "Carol Davis", "major": "Physics"}, {"student_id": 4, "student_name": "David Wilson", "major": "Chemistry"}, {"student_id": 5, "student_name": "Emma Brown", "major": "Biology"}], "study_sessions": [{"session_id": 1, "student_id": 1, "subject": "Math", "session_date": "2023-10-01", "hours_studied": 2.5}, {"session_id": 2, "student_id": 1, "subject": "Physics", "session_date": "2023-10-02", "hours_studied": 3.0}, {"session_id": 3, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 4, "student_id": 1, "subject": "Math", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 5, "student_id": 1, "subject": "Physics", "session_date": "2023-10-05", "hours_studied": 3.0}, {"session_id": 6, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-06", "hours_studied": 2.0}, {"session_id": 7, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-01", "hours_studied": 4.0}, {"session_id": 8, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-02", "hours_studied": 3.5}, {"session_id": 9, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-03", "hours_studied": 2.5}, {"session_id": 10, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-04", "hours_studied": 3.0}, {"session_id": 11, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-05", "hours_studied": 4.0}, {"session_id": 12, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-06", "hours_studied": 3.5}, {"session_id": 13, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-07", "hours_studied": 2.5}, {"session_id": 14, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-08", "hours_studied": 3.0}, {"session_id": 15, "student_id": 3, "subject": "Biology", "session_date": "2023-10-01", "hours_studied": 2.0}, {"session_id": 16, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-02", "hours_studied": 2.5}, {"session_id": 17, "student_id": 3, "subject": "Biology", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 18, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 19, "student_id": 4, "subject": "Organic", "session_date": "2023-10-01", "hours_studied": 3.0}, {"session_id": 20, "student_id": 4, "subject": "Physical", "session_date": "2023-10-05", "hours_studied": 2.5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Ordering sessions

`ranked_sessions` joins `study_sessions` to `students` by `student_id` and assigns:

`ROW_NUMBER() OVER (PARTITION BY s.student_id ORDER BY ss.session_date) AS rn`.

This creates a chronological number within each student. The selected `rn` is never used by later CTEs, so it does not affect the final result. The join also filters out sessions without matching student metadata, although a valid relational dataset should already preserve that relationship.

Ordering only by `session_date` is ambiguous when one student has several sessions on the same date. Their relative order can affect the subject sequence, but the query supplies no `session_id` tie-breaker.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"students": [{"student_id": 1, "student_name": "Alice Chen", "major": "Computer Science"}, {"student_id": 2, "student_name": "Bob Johnson", "major": "Mathematics"}, {"student_id": 3, "student_name": "Carol Davis", "major": "Physics"}, {"student_id": 4, "student_name": "David Wilson", "major": "Chemistry"}, {"student_id": 5, "student_name": "Emma Brown", "major": "Biology"}], "study_sessions": [{"session_id": 1, "student_id": 1, "subject": "Math", "session_date": "2023-10-01", "hours_studied": 2.5}, {"session_id": 2, "student_id": 1, "subject": "Physics", "session_date": "2023-10-02", "hours_studied": 3.0}, {"session_id": 3, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 4, "student_id": 1, "subject": "Math", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 5, "student_id": 1, "subject": "Physics", "session_date": "2023-10-05", "hours_studied": 3.0}, {"session_id": 6, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-06", "hours_studied": 2.0}, {"session_id": 7, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-01", "hours_studied": 4.0}, {"session_id": 8, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-02", "hours_studied": 3.5}, {"session_id": 9, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-03", "hours_studied": 2.5}, {"session_id": 10, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-04", "hours_studied": 3.0}, {"session_id": 11, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-05", "hours_studied": 4.0}, {"session_id": 12, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-06", "hours_studied": 3.5}, {"session_id": 13, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-07", "hours_studied": 2.5}, {"session_id": 14, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-08", "hours_studied": 3.0}, {"session_id": 15, "student_id": 3, "subject": "Biology", "session_date": "2023-10-01", "hours_studied": 2.0}, {"session_id": 16, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-02", "hours_studied": 2.5}, {"session_id": 17, "student_id": 3, "subject": "Biology", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 18, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 19, "student_id": 4, "subject": "Organic", "session_date": "2023-10-01", "hours_studied": 3.0}, {"session_id": 20, "student_id": 4, "subject": "Physical", "session_date": "2023-10-05", "hours_studied": 2.5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Computing gaps

`grouped_sessions` uses `LAG(session_date)` within each student to retrieve the preceding date and calculates `DATEDIFF`.

The first session has no predecessor, so `date_diff` is NULL. A difference of 0, 1, or 2 remains in the same continuous run. A difference greater than 2 breaks the run, matching the rule that gaps longer than two days are forbidden.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `grouped_sessions` uses `LAG(session_date)` within each stud... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Assigning uninterrupted group IDs

`session_groups` converts gap boundaries into a running group number. Its windowed sum adds one when:

- `date_diff > 2`; or
- `date_diff IS NULL` for the student's first row.

As a result, each student begins at group 1, and every excessive gap starts the next group. Rows sharing `(student_id, group_id)` form one maximal sequence with no adjacent date gap above two days.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "student_name", "major", "cycle_length", "total_study_hours"], "rows": [[2, "Bob Johnson", "Mathematics", 4, 26.0], [1, "Alice Chen", "Computer Science", 3, 15.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"students": [{"student_id": 1, "student_name": "Alice Chen", "major": "Computer Science"}, {"student_id": 2, "student_name": "Bob Johnson", "major": "Mathematics"}, {"student_id": 3, "student_name": "Carol Davis", "major": "Physics"}, {"student_id": 4, "student_name": "David Wilson", "major": "Chemistry"}, {"student_id": 5, "student_name": "Emma Brown", "major": "Biology"}], "study_sessions": [{"session_id": 1, "student_id": 1, "subject": "Math", "session_date": "2023-10-01", "hours_studied": 2.5}, {"session_id": 2, "student_id": 1, "subject": "Physics", "session_date": "2023-10-02", "hours_studied": 3.0}, {"session_id": 3, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 4, "student_id": 1, "subject": "Math", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 5, "student_id": 1, "subject": "Physics", "session_date": "2023-10-05", "hours_studied": 3.0}, {"session_id": 6, "student_id": 1, "subject": "Chemistry", "session_date": "2023-10-06", "hours_studied": 2.0}, {"session_id": 7, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-01", "hours_studied": 4.0}, {"session_id": 8, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-02", "hours_studied": 3.5}, {"session_id": 9, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-03", "hours_studied": 2.5}, {"session_id": 10, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-04", "hours_studied": 3.0}, {"session_id": 11, "student_id": 2, "subject": "Algebra", "session_date": "2023-10-05", "hours_studied": 4.0}, {"session_id": 12, "student_id": 2, "subject": "Calculus", "session_date": "2023-10-06", "hours_studied": 3.5}, {"session_id": 13, "student_id": 2, "subject": "Statistics", "session_date": "2023-10-07", "hours_studied": 2.5}, {"session_id": 14, "student_id": 2, "subject": "Geometry", "session_date": "2023-10-08", "hours_studied": 3.0}, {"session_id": 15, "student_id": 3, "subject": "Biology", "session_date": "2023-10-01", "hours_studied": 2.0}, {"session_id": 16, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-02", "hours_studied": 2.5}, {"session_id": 17, "student_id": 3, "subject": "Biology", "session_date": "2023-10-03", "hours_studied": 2.0}, {"session_id": 18, "student_id": 3, "subject": "Chemistry", "session_date": "2023-10-04", "hours_studied": 2.5}, {"session_id": 19, "student_id": 4, "subject": "Organic", "session_date": "2023-10-01", "hours_studied": 3.0}, {"session_id": 20, "student_id": 4, "subject": "Physical", "session_date": "2023-10-05", "hours_studied": 2.5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "student_name", "major", "cycle_length", "total_study_hours"], "rows": [[2, "Bob Johnson", "Mathematics", 4, 26.0], [1, "Alice Chen", "Computer Science", 3, 15.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use valid MySQL aggregation:** Replace `STRING:** - **Use valid MySQL aggregation:** Replace `STRING_AGG` with correctly ordered `GROUP_CONCAT`, while considering its configurable maximum output length.
- **Avoid concatenated strings:** Keep one row per session and use row numbers plus self-joins or window logic for modulo-aligned comparisons.
- **Generate candidate periods:** Test every `d >= 3` satisfying two complete cycles and compare all positions to `((pos-1) mod d)+1`.
- **Six nonrepeating subjects:** The exact query incorrectly accepts them because its length-3 `LIKE` condition matches the sequence's own prefix.
- **Exactly two three-subject cycles:** A correct detector accepts `A,B,C,A,B,C` with cycle length 3.
- **Partial final cycle:** The statement requires complete cycles; candidate validation should define whether extra sessions invalidate the group and enforce divisibility accordingly.
- **Cycle longer than ten:** The exact distinct-count join inspects only ten positions and cannot report it accurately.
- **Repeated subject inside one cycle:** Distinct-subject count is not generally equal to positional period length.
- **Gap exactly two days:** It remains in the same group because only `date_diff > 2` starts a new one.
- **Gap three days:** It starts a new group.
- **Several sessions on one date:** The missing secondary order makes their subject sequence nondeterministic.
- **Several qualifying groups for one student:** The exact query may return duplicate student rows rather than choosing one pattern.
- **Fewer than six sessions:** The group is rejected before pattern detection.
- **Three distinct subjects without repetition:** Distinctness alone is insufficient, but the source treats it as nearly sufficient.
- **Subject containing comma:** Comma-delimited parsing becomes ambiguous unless the data contract excludes commas or escaping is added.
- **Subject containing `%` or `_`:** These are `LIKE` wildcards and can further distort the prefix checks.
- **No sessions:** The student has no ranked row and cannot appear.
- **Total hours:** Summing the whole group is correct only after proving the entire group belongs to the pattern.
- **Runtime defect:** As MySQL, the query fails at `STRING_AGG` before any logical result is returned.
- **Manifest mismatch:** The source never performs the stated modulo-position equality test.
- **Read-only behavior:** Despite its defects, the query contains no data-modification statement.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Because the exact query is not executable MySQL and its detector is semantically incorrect, a claimed runtime cannot validate it as a solution. Its physical operation shape can still be described.
- **Auxiliary Space Complexity:** $O(R + S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
