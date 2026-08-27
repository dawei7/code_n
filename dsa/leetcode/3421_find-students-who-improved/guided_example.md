# Guided Example: Find Students Who Improved

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Scores": [{"student_id": 101, "subject": "Math", "score": 70, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 101, "subject": "Physics", "score": 65, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Physics", "score": 60, "exam_date": "2023-02-15"}, {"student_id": 102, "subject": "Math", "score": 80, "exam_date": "2023-01-15"}, {"student_id": 102, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 103, "subject": "Math", "score": 90, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 75, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 85, "exam_date": "2023-02-15"}]}}`
- **Required output:** `{"columns": ["student_id", "subject", "first_score", "latest_score"], "rows": [[101, "Math", 70, 85], [102, "Math", 80, 85], [104, "Physics", 75, 85]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Scores`

The objective is to compute `{"columns": ["student_id", "subject", "first_score", "latest_score"], "rows": [[101, "Math", 70, 85], [102, "Math", 80, 85], [104, "Physics", 75, 85]]}` from `{"tables": {"Scores": [{"student_id": 101, "subject": "Math", "score": 70, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 101, "subject": "Physics", "score": 65, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Physics", "score": 60, "exam_date": "2023-02-15"}, {"student_id": 102, "subject": "Math", "score": 80, "exam_date": "2023-01-15"}, {"student_id": 102, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 103, "subject": "Math", "score": 90, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 75, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 85, "exam_date": "2023-02-15"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Compare chronological endpoints within each student-subject history.** Improvement is not based on the minimum and maximum scores, nor on any pair of consecutive exams. For every distinct `(student_id, subject)` group, the query must identify the score on the earliest date and the score on the latest date, then keep the group only when the latter is strictly larger.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Scores": [{"student_id": 101, "subject": "Math", "score": 70, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 101, "subject": "Physics", "score": 65, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Physics", "score": 60, "exam_date": "2023-02-15"}, {"student_id": 102, "subject": "Math", "score": 80, "exam_date": "2023-01-15"}, {"student_id": 102, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 103, "subject": "Math", "score": 90, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 75, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 85, "exam_date": "2023-02-15"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The first common table expression, `RankedScores`, keeps every row from `Scores` and adds two independent row numbers.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first common table expression, `RankedScores`, keeps eve... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

`PARTITION BY student_id, subject ORDER BY exam_date ASC`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "subject", "first_score", "latest_score"], "rows": [[101, "Math", 70, 85], [102, "Math", 80, 85], [104, "Physics", 75, 85]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Scores": [{"student_id": 101, "subject": "Math", "score": 70, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 101, "subject": "Physics", "score": 65, "exam_date": "2023-01-15"}, {"student_id": 101, "subject": "Physics", "score": 60, "exam_date": "2023-02-15"}, {"student_id": 102, "subject": "Math", "score": 80, "exam_date": "2023-01-15"}, {"student_id": 102, "subject": "Math", "score": 85, "exam_date": "2023-02-15"}, {"student_id": 103, "subject": "Math", "score": 90, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 75, "exam_date": "2023-01-15"}, {"student_id": 104, "subject": "Physics", "score": 85, "exam_date": "2023-02-15"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "subject", "first_score", "latest_score"], "rows": [[101, "Math", 70, 85], [102, "Math", 80, 85], [104, "Physics", 75, 85]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Aggregate minimum and maximum score:** `MIN(sc:** - **Aggregate minimum and maximum score:** `MIN(score)` and `MAX(score)` do not identify scores on the first and latest dates. A student could peak in the middle and later decline.
- **Aggregate endpoint dates then join:** Finding `MIN(exam_date)` and `MAX(exam_date)` per group and joining those dates back to `Scores` is also correct, but requires additional grouped and keyed joins.
- **`FIRST_VALUE` and `LAST_VALUE`:** Window endpoint functions can solve the problem, but `LAST_VALUE` is easy to misuse because its default frame often ends at the current row rather than the partition's final row.
- **Only one exam:** The row receives both endpoint ranks but fails strict improvement, correctly excluding it.
- **Equal first and latest scores:** Equality is not improvement, so `>` rather than `>=` is required.
- **Intermediate scores:** They do not affect qualification. Only the earliest and latest chronological scores matter.
- **Several subjects:** Partitioning by both columns prevents one subject's dates or scores from influencing another.
- **Unique dates:** The composite primary key removes endpoint ties within a group. Without that guarantee, an additional deterministic tie rule would be required.
- **Date text format:** Chronological correctness assumes a lexicographically sortable date representation such as `YYYY-MM-DD`. Arbitrary localized date strings should be converted to a date type before ordering.
- **Output ordering:** `ORDER BY 1, 2` is correct but positional. Naming `student_id, subject` explicitly would be more resistant to future select-list reordering.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of rows in `Scores`. Computing each partitioned row number generally requires ordering rows by the partition keys and exam date. In a straightforward plan, window sorting costs $O(r\log r)$ time and $O(r)$ working or materialization space. Both window expressions share compatible partition keys and opposite date direction; the exact number of physical sorts depends on the MySQL optimizer.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
