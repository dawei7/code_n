# Guided Example: Median Employee Salary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Employee": [{"id": 1, "company": "A", "salary": 2341}, {"id": 2, "company": "A", "salary": 341}, {"id": 3, "company": "A", "salary": 15}, {"id": 4, "company": "A", "salary": 15314}, {"id": 5, "company": "A", "salary": 451}, {"id": 6, "company": "A", "salary": 513}, {"id": 7, "company": "B", "salary": 15}, {"id": 8, "company": "B", "salary": 13}, {"id": 9, "company": "B", "salary": 1154}, {"id": 10, "company": "B", "salary": 1345}, {"id": 11, "company": "B", "salary": 1221}, {"id": 12, "company": "B", "salary": 234}, {"id": 13, "company": "C", "salary": 2345}, {"id": 14, "company": "C", "salary": 2645}, {"id": 15, "company": "C", "salary": 2645}, {"id": 16, "company": "C", "salary": 2652}, {"id": 17, "company": "C", "salary": 65}]}}`
- **Required output:** `{"columns": ["id", "company", "salary"], "rows": [[5, "A", 451], [6, "A", 513], [12, "B", 234], [9, "B", 1154], [14, "C", 2645]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Employee`

The objective is to compute `{"columns": ["id", "company", "salary"], "rows": [[5, "A", 451], [6, "A", 513], [12, "B", 234], [9, "B", 1154], [14, "C", 2645]]}` from `{"tables": {"Employee": [{"id": 1, "company": "A", "salary": 2341}, {"id": 2, "company": "A", "salary": 341}, {"id": 3, "company": "A", "salary": 15}, {"id": 4, "company": "A", "salary": 15314}, {"id": 5, "company": "A", "salary": 451}, {"id": 6, "company": "A", "salary": 513}, {"id": 7, "company": "B", "salary": 15}, {"id": 8, "company": "B", "salary": 13}, {"id": 9, "company": "B", "salary": 1154}, {"id": 10, "company": "B", "salary": 1345}, {"id": 11, "company": "B", "salary": 1221}, {"id": 12, "company": "B", "salary": 234}, {"id": 13, "company": "C", "salary": 2345}, {"id": 14, "company": "C", "salary": 2645}, {"id": 15, "company": "C", "salary": 2645}, {"id": 16, "company": "C", "salary": 2652}, {"id": 17, "company": "C", "salary": 65}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The query ranks employees within each company, counts that company's rows, and keeps the one or two central ranks.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Employee": [{"id": 1, "company": "A", "salary": 2341}, {"id": 2, "company": "A", "salary": 341}, {"id": 3, "company": "A", "salary": 15}, {"id": 4, "company": "A", "salary": 15314}, {"id": 5, "company": "A", "salary": 451}, {"id": 6, "company": "A", "salary": 513}, {"id": 7, "company": "B", "salary": 15}, {"id": 8, "company": "B", "salary": 13}, {"id": 9, "company": "B", "salary": 1154}, {"id": 10, "company": "B", "salary": 1345}, {"id": 11, "company": "B", "salary": 1221}, {"id": 12, "company": "B", "salary": 234}, {"id": 13, "company": "C", "salary": 2345}, {"id": 14, "company": "C", "salary": 2645}, {"id": 15, "company": "C", "salary": 2645}, {"id": 16, "company": "C", "salary": 2652}, {"id": 17, "company": "C", "salary": 65}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

CTE `t` preserves every Employee column and adds:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `rk` from `ROW_NUMBER()`;
- `n` from a partitioned `COUNT`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "company", "salary"], "rows": [[5, "A", 451], [6, "A", 513], [12, "B", 234], [9, "B", 1154], [14, "C", 2645]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Employee": [{"id": 1, "company": "A", "salary": 2341}, {"id": 2, "company": "A", "salary": 341}, {"id": 3, "company": "A", "salary": 15}, {"id": 4, "company": "A", "salary": 15314}, {"id": 5, "company": "A", "salary": 451}, {"id": 6, "company": "A", "salary": 513}, {"id": 7, "company": "B", "salary": 15}, {"id": 8, "company": "B", "salary": 13}, {"id": 9, "company": "B", "salary": 1154}, {"id": 10, "company": "B", "salary": 1345}, {"id": 11, "company": "B", "salary": 1221}, {"id": 12, "company": "B", "salary": 234}, {"id": 13, "company": "C", "salary": 2345}, {"id": 14, "company": "C", "salary": 2645}, {"id": 15, "company": "C", "salary": 2645}, {"id": 16, "company": "C", "salary": 2652}, {"id": 17, "company": "C", "salary": 65}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "company", "salary"], "rows": [[5, "A", 451], [6, "A", 513], [12, "B", 234], [9, "B", 1154], [14, "C", 2645]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct deterministic window order:** Use `ORDER BY salary ASC, id ASC` to satisfy the explicit tie-break.
- **Aggregate then join:** Compute company counts and compare each row's relative rank through joins; it is more complex and may be slower.
- **Average the middle salaries:** That returns a numeric median, not the requested employee rows.
- **One employee:** That sole row is the median.
- **Odd company size:** Exactly one rank is selected.
- **Even company size:** Exactly two ranks are selected.
- **Equal salaries:** The exact query lacks the required ID tie-break and can be nondeterministic at boundaries.
- **Multiple companies:** Partitioning resets both row numbers and counts.
- **Output order:** No final sort is required.
- **Primary-key ID:** It provides a unique deterministic secondary key when included.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E \log E)$. Let $E$ be the total Employee rows. A typical database plan partitions and sorts rows by company and salary, costing $O(E\log E)$ comparison work in the absence of a supporting index. Window counting and filtering then take linear work.
- **Auxiliary Space Complexity:** $O(E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
