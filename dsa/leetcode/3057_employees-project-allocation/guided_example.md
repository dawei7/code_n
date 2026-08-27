# Guided Example: Employees Project Allocation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Project": [{"project_id": 1, "employee_id": 1, "workload": 45}, {"project_id": 1, "employee_id": 2, "workload": 90}, {"project_id": 2, "employee_id": 3, "workload": 12}, {"project_id": 2, "employee_id": 4, "workload": 68}], "Employees": [{"employee_id": 1, "name": "Khaled", "team": "A"}, {"employee_id": 2, "name": "Ali", "team": "B"}, {"employee_id": 3, "name": "John", "team": "B"}, {"employee_id": 4, "name": "Doe", "team": "A"}]}}`
- **Required output:** `{"columns": ["employee_id", "project_id", "employee_name", "project_workload"], "rows": [[2, 1, "Ali", 90], [4, 2, "Doe", 68]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Project`

The objective is to compute `{"columns": ["employee_id", "project_id", "employee_name", "project_workload"], "rows": [[2, 1, "Ali", 90], [4, 2, "Doe", 68]]}` from `{"tables": {"Project": [{"project_id": 1, "employee_id": 1, "workload": 45}, {"project_id": 1, "employee_id": 2, "workload": 90}, {"project_id": 2, "employee_id": 3, "workload": 12}, {"project_id": 2, "employee_id": 4, "workload": 68}], "Employees": [{"employee_id": 1, "name": "Khaled", "team": "A"}, {"employee_id": 2, "name": "Ali", "team": "B"}, {"employee_id": 3, "name": "John", "team": "B"}, {"employee_id": 4, "name": "Doe", "team": "A"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**First compute the benchmark for every team.** The CTE `T` joins `Project` to `Employees` by `employee_id` so each workload gains its employee's team. It groups by team and computes `AVG(workload)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Project": [{"project_id": 1, "employee_id": 1, "workload": 45}, {"project_id": 1, "employee_id": 2, "workload": 90}, {"project_id": 2, "employee_id": 3, "workload": 12}, {"project_id": 2, "employee_id": 4, "workload": 68}], "Employees": [{"employee_id": 1, "name": "Khaled", "team": "A"}, {"employee_id": 2, "name": "Ali", "team": "B"}, {"employee_id": 3, "name": "John", "team": "B"}, {"employee_id": 4, "name": "Doe", "team": "A"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The resulting CTE has one row per represented team:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The resulting CTE has one row per represented team:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Employees without a project row contribute no workload and therefore do not enter the average. This follows the source model, where workload is stored only in `Project`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["employee_id", "project_id", "employee_name", "project_workload"], "rows": [[2, 1, "Ali", 90], [4, 2, "Doe", 68]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Project": [{"project_id": 1, "employee_id": 1, "workload": 45}, {"project_id": 1, "employee_id": 2, "workload": 90}, {"project_id": 2, "employee_id": 3, "workload": 12}, {"project_id": 2, "employee_id": 4, "workload": 68}], "Employees": [{"employee_id": 1, "name": "Khaled", "team": "A"}, {"employee_id": 2, "name": "Ali", "team": "B"}, {"employee_id": 3, "name": "John", "team": "B"}, {"employee_id": 4, "name": "Doe", "team": "A"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["employee_id", "project_id", "employee_name", "project_workload"], "rows": [[2, 1, "Ali", 90], [4, 2, "Doe", 68]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window average:** Join allocations to employee:** - **Window average:** Join allocations to employees once, compute `AVG(workload) OVER (PARTITION BY team)`, then filter in an outer query. This matches the manifest but not the exact source.
- **Correlated subquery:** Recompute a team's average for each employee. It is correct with optimization but can repeat work and be harder to reason about.
- **Workload equals average:** It is excluded because the predicate is strictly greater.
- **One employee in a team:** Their workload equals the team's average, so that team contributes no result.
- **Employees without projects:** They do not participate because both paths begin from `Project`.
- **Project with missing employee:** The inner join removes it; ordinary foreign-key integrity should prevent this.
- **Several teams with equal averages:** Comparisons remain independent because joining uses team identity, not average value.
- **Decimal average:** MySQL preserves fractional averages, so an integer workload is compared with the true non-rounded team mean.
- **Manifest mismatch:** The exact SQL uses grouped aggregation and a rejoin, not a window function.
- **Ordering:** Ordinals 1 and 2 correctly implement employee then project ascending.
- **Why the average is not rounded:** Filtering against the full `AVG` result preserves the true strict comparison. Rounding a team average first could incorrectly include or exclude a workload near the boundary.
- **Team with no allocated employee:** It has no row in CTE `T` and cannot produce an output employee, which is consistent because no project workload exists to evaluate.
- **Name is descriptive only:** Employee identity and joining use `employee_id`. Duplicate employee names across teams or within a team cannot merge rows or alter averages.
- **Strict team isolation:** The CTE key prevents an employee from being compared with a global company average or another team's workload distribution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $P$ be project rows and $E$ employee rows. With indexed employee identifiers, both joins are approximately linear in the matched rows. Grouping team workloads is $O(P)$ expected with hash aggregation, while final output ordering can cost $O(Q\log Q)$ for $Q$ qualifying rows. A broad bound is $O(P+E+Q\log Q)$.
- **Auxiliary Space Complexity:** $O(Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
