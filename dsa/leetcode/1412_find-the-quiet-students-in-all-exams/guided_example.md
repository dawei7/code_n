# Guided Example: Find the Quiet Students in All Exams

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Student": [{"student_id": 1, "student_name": "Daniel"}, {"student_id": 2, "student_name": "Jade"}, {"student_id": 3, "student_name": "Stella"}, {"student_id": 4, "student_name": "Jonathan"}, {"student_id": 5, "student_name": "Will"}], "Exam": [{"exam_id": 10, "student_id": 1, "score": 70}, {"exam_id": 10, "student_id": 2, "score": 80}, {"exam_id": 10, "student_id": 3, "score": 90}, {"exam_id": 20, "student_id": 1, "score": 80}, {"exam_id": 30, "student_id": 1, "score": 70}, {"exam_id": 30, "student_id": 3, "score": 80}, {"exam_id": 30, "student_id": 4, "score": 90}, {"exam_id": 40, "student_id": 1, "score": 60}, {"exam_id": 40, "student_id": 2, "score": 70}, {"exam_id": 40, "student_id": 4, "score": 80}]}}`
- **Required output:** `{"columns": ["student_id", "student_name"], "rows": [[2, "Jade"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Student`

The objective is to compute `{"columns": ["student_id", "student_name"], "rows": [[2, "Jade"]]}` from `{"tables": {"Student": [{"student_id": 1, "student_name": "Daniel"}, {"student_id": 2, "student_name": "Jade"}, {"student_id": 3, "student_name": "Stella"}, {"student_id": 4, "student_name": "Jonathan"}, {"student_id": 5, "student_name": "Will"}], "Exam": [{"exam_id": 10, "student_id": 1, "score": 70}, {"exam_id": 10, "student_id": 2, "score": 80}, {"exam_id": 10, "student_id": 3, "score": 90}, {"exam_id": 20, "student_id": 1, "score": 80}, {"exam_id": 30, "student_id": 1, "score": 70}, {"exam_id": 30, "student_id": 3, "score": 80}, {"exam_id": 30, "student_id": 4, "score": 90}, {"exam_id": 40, "student_id": 1, "score": 60}, {"exam_id": 40, "student_id": 2, "score": 70}, {"exam_id": 40, "student_id": 4, "score": 80}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn “never highest or lowest” into per-exam ranks

A student qualifies only if two conditions both hold:

1. The student took at least one exam.
2. Across every exam they took, their score was neither a lowest score nor a highest score.

The word “every” makes this easier to solve by first marking violations on individual Exam rows and then grouping those rows by student. If the grouped student has zero lowest-score violations and zero highest-score violations, every participation was quiet.

The common table expression `T` creates those row-level markers through two window ranks:



and



`PARTITION BY exam_id` restarts each ranking for each exam. Scores from exam 10 must never be compared with scores from exam 20, even if the numerical values overlap.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Student": [{"student_id": 1, "student_name": "Daniel"}, {"student_id": 2, "student_name": "Jade"}, {"student_id": 3, "student_name": "Stella"}, {"student_id": 4, "student_name": "Jonathan"}, {"student_id": 5, "student_name": "Will"}], "Exam": [{"exam_id": 10, "student_id": 1, "score": 70}, {"exam_id": 10, "student_id": 2, "score": 80}, {"exam_id": 10, "student_id": 3, "score": 90}, {"exam_id": 20, "student_id": 1, "score": 80}, {"exam_id": 30, "student_id": 1, "score": 70}, {"exam_id": 30, "student_id": 3, "score": 80}, {"exam_id": 30, "student_id": 4, "score": 90}, {"exam_id": 40, "student_id": 1, "score": 60}, {"exam_id": 40, "student_id": 2, "score": 70}, {"exam_id": 40, "student_id": 4, "score": 80}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why two directions are needed

For `rk1`, ascending order puts the smallest score first, so `rk1 = 1` means the row holds a lowest score in that exam. For `rk2`, descending order puts the largest score first, so `rk2 = 1` means the row holds a highest score.

These are independent conditions. A middle score has both ranks greater than one. A minimum but nonmaximum score has `rk1 = 1` only. A maximum but nonminimum score has `rk2 = 1` only. In a one-participant exam, the same score is both minimum and maximum, so both ranks are one.

Using `RANK` rather than `ROW_NUMBER` is essential for ties. If three students share the lowest score, all three receive ascending rank one and all three must be disqualified. `ROW_NUMBER` would arbitrarily assign only one of them position one and could falsely treat the other tied students as quiet. The same reasoning applies to tied maximum scores.

The CTE retains `student_id` along with both ranks. It does not need `exam_id` in its output because the window computation has already encoded whether that particular participation was extreme.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For `rk1`, ascending order puts the smallest score first, so... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why joining from `T` excludes nonparticipants

The main query uses:



`T` contains one row for every Exam participation and no row for a student who never took an exam. Because this is an inner join, only identifiers present in `T` can reach the result. The contract's “took at least one exam” requirement is therefore satisfied automatically.

`USING (student_id)` is shorthand for equality between the same-named identifier columns. It also exposes a single merged `student_id` column, which makes the later selection concise. The join obtains `student_name` from the Student table.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "student_name"], "rows": [[2, "Jade"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Student": [{"student_id": 1, "student_name": "Daniel"}, {"student_id": 2, "student_name": "Jade"}, {"student_id": 3, "student_name": "Stella"}, {"student_id": 4, "student_name": "Jonathan"}, {"student_id": 5, "student_name": "Will"}], "Exam": [{"exam_id": 10, "student_id": 1, "score": 70}, {"exam_id": 10, "student_id": 2, "score": 80}, {"exam_id": 10, "student_id": 3, "score": 90}, {"exam_id": 20, "student_id": 1, "score": 80}, {"exam_id": 30, "student_id": 1, "score": 70}, {"exam_id": 30, "student_id": 3, "score": 80}, {"exam_id": 30, "student_id": 4, "score": 90}, {"exam_id": 40, "student_id": 1, "score": 60}, {"exam_id": 40, "student_id": 2, "score": 70}, {"exam_id": 40, "student_id": 4, "score": 80}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "student_name"], "rows": [[2, "Jade"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Per-exam `MIN` and `MAX` subquery:** Compute b:** - **Per-exam `MIN` and `MAX` subquery:** Compute both extremes for each exam, join them back to Exam, and reject students with a matching extreme. This is correct but requires another aggregation and join.
- **`NOT EXISTS` disqualifier:** Select participating students for whom no Exam row equals its exam's minimum or maximum. This can read naturally but may involve correlated work unless the optimizer rewrites it well.
- **Conditional aggregation without ranks:** Window `MIN(score)` and `MAX(score)` values can be attached to each row, followed by Boolean sums. It handles ties correctly and expresses the same idea.
- **`ROW_NUMBER`:** This is incorrect when scores tie because only one tied row gets number one. `RANK` marks every student at an extreme.
- **Student with no exams:** The inner join from `T` excludes the student, as required.
- **Only participant in an exam:** The student is both lowest and highest and must be disqualified.
- **All scores tied in an exam:** Every participant receives rank one in both directions, so none can be quiet across that exam.
- **Tie only at one extreme:** Every student sharing that minimum or maximum is disqualified, while strict middle scores remain eligible.
- **Quiet in one exam but extreme in another:** Group-level sums detect the single violation and exclude the student.
- **Ordinal syntax:** `GROUP BY 1` and `ORDER BY 1` refer to the first selected column. Naming `student_id` explicitly would be more self-documenting but is logically equivalent here.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S \log S)$. Let $E$ be the number of Exam rows and $S$ the number of Student rows. Computing the two window rankings requires organizing rows by exam and score. A comparison-sort execution plan takes $O(E \log E)$ time in the general case. The join and per-student grouping scan or hash their inputs in expected $O(E+S)$ time, and the final sort of at most $S$ result groups is bounded by $O(S \log S)$.
- **Auxiliary Space Complexity:** $O(E+S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
