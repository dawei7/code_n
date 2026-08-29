# Guided Example: Compute the Rank as a Percentage

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Students": [{"student_id": 2, "department_id": 2, "mark": 650}, {"student_id": 8, "department_id": 2, "mark": 650}, {"student_id": 7, "department_id": 1, "mark": 920}, {"student_id": 1, "department_id": 1, "mark": 610}, {"student_id": 3, "department_id": 1, "mark": 530}]}}`
- **Required output:** `{"columns": ["student_id", "department_id", "percentage"], "rows": [[7, 1, 0.0], [1, 1, 50.0], [3, 1, 100.0], [2, 2, 0.0], [8, 2, 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Students`

The objective is to compute `{"columns": ["student_id", "department_id", "percentage"], "rows": [[7, 1, 0.0], [1, 1, 50.0], [3, 1, 100.0], [2, 2, 0.0], [8, 2, 0.0]]}` from `{"tables": {"Students": [{"student_id": 2, "department_id": 2, "mark": 650}, {"student_id": 8, "department_id": 2, "mark": 650}, {"student_id": 7, "department_id": 1, "mark": 920}, {"student_id": 1, "department_id": 1, "mark": 610}, {"student_id": 3, "department_id": 1, "mark": 530}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute rank and department size as window values

Each student's percentage depends on other rows in the same department but must still return one row per student. Window functions are designed for this: they calculate partition-level information without collapsing rows through grouping.

The query uses two window expressions partitioned by `department_id`:

- `RANK()` supplies the student's descending-mark rank;
- `COUNT(1)` supplies the department's total student count.

Every source row remains in the output with its own `student_id` and `department_id`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Students": [{"student_id": 2, "department_id": 2, "mark": 650}, {"student_id": 8, "department_id": 2, "mark": 650}, {"student_id": 7, "department_id": 1, "mark": 920}, {"student_id": 1, "department_id": 1, "mark": 610}, {"student_id": 3, "department_id": 1, "mark": 530}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank marks from highest to lowest

`RANK() OVER (PARTITION BY department_id ORDER BY mark DESC)` restarts ranking for every department and places higher marks first.

The highest mark receives rank one. Equal marks receive the same rank because `RANK` assigns ties identically. Ranks after a tie contain gaps, matching the positional definition of rank. For example, marks `90,90,80` receive ranks `1,1,3`.

Using `DENSE_RANK` would be wrong when a lower mark follows a tie because it would produce `1,1,2` and a different percentage.

This distinction is part of the formula rather than a cosmetic display choice. The numerator measures how many ranking positions precede the student, including positions occupied by tied students. After two students tie for first, the next student is in the third positional slot, so `rank - 1` must be two. Compressing that student to dense rank two would incorrectly claim that only one position precedes them and would understate their percentage.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Translate the rank into the requested scale

The formula is

`(rank - 1) * 100 / (department_count - 1)`.

Subtracting one makes the highest rank zero. Dividing by one less than the group size spreads positional ranks across a scale whose last unique position is 100.

The multiplication by 100 occurs before division in the expression, producing a percentage rather than a fraction. MySQL performs the numeric calculation and `ROUND(..., 2)` rounds it to two decimal places.

Students tied on a mark share a rank and therefore share the same percentage.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["student_id", "department_id", "percentage"], "rows": [[7, 1, 0.0], [1, 1, 50.0], [3, 1, 100.0], [2, 2, 0.0], [8, 2, 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Students": [{"student_id": 2, "department_id": 2, "mark": 650}, {"student_id": 8, "department_id": 2, "mark": 650}, {"student_id": 7, "department_id": 1, "mark": 920}, {"student_id": 1, "department_id": 1, "mark": 610}, {"student_id": 3, "department_id": 1, "mark": 530}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["student_id", "department_id", "percentage"], "rows": [[7, 1, 0.0], [1, 1, 50.0], [3, 1, 100.0], [2, 2, 0.0], [8, 2, 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **MySQL `PERCENT_RANK`:** This window function directly computes `(rank-1)/(rows-1)` and could be multiplied by 100, often with the single-row case already defined as zero.
- **Correlated subqueries:** Count higher marks and department size per student. This can repeat scans and requires careful tie handling.
- **`DENSE_RANK`:** It removes gaps after ties and does not match the specified rank formula.
- **`ROW_NUMBER`:** It gives different ranks to tied marks, violating the tie rule.
- **Global rank without partition:** Students from different departments would compete incorrectly.
- **Global count denominator:** Percentages must use department size, not total table size.
- **One student:** Division by zero becomes null and `COALESCE` returns zero.
- **All students tied:** Everyone has rank one and percentage zero.
- **Tie below the top:** Tied students share the same percentage, and later ranks skip positions.
- **Negative or unusual marks:** Descending numeric ordering still defines rank; the schema uses integers without requiring positivity.
- **Rounding:** `ROUND(...,2)` is applied after the full percentage calculation.
- **Any output order:** No final sort is necessary.
- **Unique student IDs:** Each source row corresponds to one output student.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let `n` be the number of students. Ranking generally requires ordering rows within departments, giving `O(n \log n)` time under comparison sorting. Counting partitions and evaluating expressions add linear work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
