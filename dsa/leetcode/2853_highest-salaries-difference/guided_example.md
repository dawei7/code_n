# Guided Example: Highest Salaries Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salaries": [{"emp_name": "Kathy", "department": "Engineering", "salary": 50000}, {"emp_name": "Roy", "department": "Marketing", "salary": 30000}, {"emp_name": "Charles", "department": "Engineering", "salary": 45000}, {"emp_name": "Jack", "department": "Engineering", "salary": 85000}, {"emp_name": "Benjamin", "department": "Marketing", "salary": 34000}, {"emp_name": "Anthony", "department": "Marketing", "salary": 42000}, {"emp_name": "Edward", "department": "Engineering", "salary": 102000}, {"emp_name": "Terry", "department": "Engineering", "salary": 44000}, {"emp_name": "Evelyn", "department": "Marketing", "salary": 53000}, {"emp_name": "Arthur", "department": "Engineering", "salary": 32000}]}}`
- **Required output:** `{"columns": ["salary_difference"], "rows": [[49000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Salaries`

The objective is to compute `{"columns": ["salary_difference"], "rows": [[49000]]}` from `{"tables": {"Salaries": [{"emp_name": "Kathy", "department": "Engineering", "salary": 50000}, {"emp_name": "Roy", "department": "Marketing", "salary": 30000}, {"emp_name": "Charles", "department": "Engineering", "salary": 45000}, {"emp_name": "Jack", "department": "Engineering", "salary": 85000}, {"emp_name": "Benjamin", "department": "Marketing", "salary": 34000}, {"emp_name": "Anthony", "department": "Marketing", "salary": 42000}, {"emp_name": "Edward", "department": "Engineering", "salary": 102000}, {"emp_name": "Terry", "department": "Engineering", "salary": 44000}, {"emp_name": "Evelyn", "department": "Marketing", "salary": 53000}, {"emp_name": "Arthur", "department": "Engineering", "salary": 32000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Compute a maximum salary for every department first.** The inner query groups `Salaries` by `department` and returns one value `s = MAX(salary)` per department.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salaries": [{"emp_name": "Kathy", "department": "Engineering", "salary": 50000}, {"emp_name": "Roy", "department": "Marketing", "salary": 30000}, {"emp_name": "Charles", "department": "Engineering", "salary": 45000}, {"emp_name": "Jack", "department": "Engineering", "salary": 85000}, {"emp_name": "Benjamin", "department": "Marketing", "salary": 34000}, {"emp_name": "Anthony", "department": "Marketing", "salary": 42000}, {"emp_name": "Edward", "department": "Engineering", "salary": 102000}, {"emp_name": "Terry", "department": "Engineering", "salary": 44000}, {"emp_name": "Evelyn", "department": "Marketing", "salary": 53000}, {"emp_name": "Arthur", "department": "Engineering", "salary": 32000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For Engineering, this row is the greatest engineering salary. For Marketing, it is the greatest marketing salary. The primary key on employee name and department prevents duplicate identity rows but is not needed for the maximum itself.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Turn two maxima into an absolute difference.** If the inner result contains exactly the Engineering and Marketing maxima, the larger one is `MAX(s)` and the smaller is `MIN(s)`. Their difference is nonnegative and equals the absolute difference:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["salary_difference"], "rows": [[49000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salaries": [{"emp_name": "Kathy", "department": "Engineering", "salary": 50000}, {"emp_name": "Roy", "department": "Marketing", "salary": 30000}, {"emp_name": "Charles", "department": "Engineering", "salary": 45000}, {"emp_name": "Jack", "department": "Engineering", "salary": 85000}, {"emp_name": "Benjamin", "department": "Marketing", "salary": 34000}, {"emp_name": "Anthony", "department": "Marketing", "salary": 42000}, {"emp_name": "Edward", "department": "Engineering", "salary": 102000}, {"emp_name": "Terry", "department": "Engineering", "salary": 44000}, {"emp_name": "Evelyn", "department": "Marketing", "salary": 53000}, {"emp_name": "Arthur", "department": "Engineering", "salary": 32000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["salary_difference"], "rows": [[49000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation:** Compute `MAX(CASE WHEN department = 'Engineering' THEN salary END)` and the analogous Marketing maximum, then apply `ABS` to their difference. This explicitly follows the requirement and matches the manifest.
- **Filter the grouped subquery:** Restrict to the two named departments before grouping, then `MAX(s) - MIN(s)` is safe.
- **Two scalar subqueries:** Query each department maximum separately and subtract with `ABS`. It is clear but may scan the table twice without optimization.
- **Engineering maximum is larger:** Outer max-minus-min returns Engineering minus Marketing.
- **Marketing maximum is larger:** The extrema reverse roles automatically and still return the absolute difference.
- **Equal maxima:** Both extrema are equal and the result is zero.
- **Multiple employees tied for maximum:** `MAX` returns the salary once; employee identity is irrelevant.
- **Additional department:** The exact unfiltered query can be wrong if its maximum changes the outer minimum or maximum.
- **Existence of both named departments:** It prevents a missing required maximum but does not by itself exclude unrelated groups.
- **One output row:** No result ordering is needed.
- **Manifest mismatch:** Conditional one-scan aggregation is the robust alternative, not the exact grouped-all-departments source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $S$ be the number of salary rows and $D$ the number of departments.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
