# Guided Example: Find Cutoff Score for Each School

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Schools": [{"school_id": 11, "capacity": 151}, {"school_id": 5, "capacity": 48}, {"school_id": 9, "capacity": 9}, {"school_id": 10, "capacity": 99}], "Exam": [{"score": 975, "student_count": 10}, {"score": 966, "student_count": 60}, {"score": 844, "student_count": 76}, {"score": 749, "student_count": 76}, {"score": 744, "student_count": 100}]}}`
- **Required output:** `{"columns": ["school_id", "score"], "rows": [[5, 975], [9, -1], [10, 749], [11, 744]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Schools`

The objective is to compute `{"columns": ["school_id", "score"], "rows": [[5, 975], [9, -1], [10, 749], [11, 744]]}` from `{"tables": {"Schools": [{"school_id": 11, "capacity": 151}, {"school_id": 5, "capacity": 48}, {"school_id": 9, "capacity": 9}, {"school_id": 10, "capacity": 99}], "Exam": [{"score": 975, "student_count": 10}, {"score": 966, "student_count": 60}, {"score": 844, "student_count": 76}, {"score": 749, "student_count": 76}, {"score": 744, "student_count": 100}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate capacity into a join condition

An `Exam` row says that `student_count` students earned at least its `score`. If a school uses that score as its cutoff, every one of those students might apply. The cutoff is safe exactly when

`school.capacity >= exam.student_count`.

The query places this condition directly in the join between `Schools` and `Exam`. For each school, the matching exam rows are precisely the score thresholds whose possible applicant count does not exceed capacity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Schools": [{"school_id": 11, "capacity": 151}, {"school_id": 5, "capacity": 48}, {"school_id": 9, "capacity": 9}, {"school_id": 10, "capacity": 99}], "Exam": [{"score": 975, "student_count": 10}, {"score": 966, "student_count": 60}, {"score": 844, "student_count": 76}, {"score": 749, "student_count": 76}, {"score": 744, "student_count": 100}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a left join is required

Some school may be too small even for the highest recorded cutoff. Such a school has no feasible `Exam` row, but it must still appear in the result with score -1.

An inner join would discard it completely. `LEFT JOIN` instead retains one synthetic row for the school and fills the exam-side columns with SQL `NULL` when no score matches. This preserves every `school_id` for grouping and fallback handling.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Some school may be too small even for the highest recorded c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the smallest feasible score

The exam data is monotone: as score increases, `student_count` cannot increase. Once a threshold is feasible, higher thresholds are also no more demanding, although they may allow fewer students to apply.

Schools first want to maximize the number of possible applicants. Lowering the cutoff can only keep or increase that number, so the lowest feasible score is an optimal choice. If several scores have the same student count, the explicit tie rule also chooses the smallest score. Thus `MIN(score)` over all feasible joined rows implements both priorities.

For capacity 99 in the example, scores 975, 966, 844, and 749 are feasible, while 744 would allow 100 students and is not. The minimum feasible score is 749.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["school_id", "score"], "rows": [[5, 975], [9, -1], [10, 749], [11, 744]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Schools": [{"school_id": 11, "capacity": 151}, {"school_id": 5, "capacity": 48}, {"school_id": 9, "capacity": 9}, {"school_id": 10, "capacity": 99}], "Exam": [{"score": 975, "student_count": 10}, {"score": 966, "student_count": 60}, {"score": 844, "student_count": 76}, {"score": 749, "student_count": 76}, {"score": 744, "student_count": 100}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["school_id", "score"], "rows": [[5, 975], [9, -1], [10, 749], [11, 744]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated subquery:** Select `MIN(score)` fro:** - **Correlated subquery:** Select `MIN(score)` from `Exam` under each school's capacity and coalesce null to -1; this states the per-school search directly.
- **Cross join then filter:** Correct but materializes or reasons about all $SE$ pairs before filtering.
- **Rank by student count then score:** More general if monotonicity were absent, but unnecessary under the guaranteed ordering relationship.
- **Inner join:** Incorrectly removes schools that have no feasible score.
- **No feasible exam row:** The synthetic null row becomes -1.
- **Every exam row feasible:** The smallest score in the table is selected.
- **Capacity exactly equals student count:** It is feasible because the join uses `>=`.
- **Equal student counts at different scores:** The smallest feasible score satisfies the tie rule.
- **Unique school IDs:** Ensure one capacity and one aggregate group per school.
- **Unique score values:** Prevent duplicate threshold rows in `Exam`.
- **Monotone exam data:** Makes minimum feasible score consistent with maximizing possible applicants.
- **Any output order:** No `ORDER BY` is required.
- **No table mutation:** The query only joins and aggregates existing rows.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(SE)$. Let $S$ be the number of schools and $E$ the number of exam rows. Logically, the inequality join may test up to $SE$ school-score pairs, so the manifest's $O(SE)$ time is an appropriate worst-case query-level bound.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
