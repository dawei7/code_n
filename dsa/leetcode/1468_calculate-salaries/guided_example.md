# Guided Example: Calculate Salaries

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salaries": [{"company_id": 1, "employee_id": 1, "employee_name": "Tony", "salary": 2000}, {"company_id": 1, "employee_id": 2, "employee_name": "Pronub", "salary": 21300}, {"company_id": 1, "employee_id": 3, "employee_name": "Tyrrox", "salary": 10800}, {"company_id": 2, "employee_id": 1, "employee_name": "Pam", "salary": 300}, {"company_id": 2, "employee_id": 7, "employee_name": "Bassem", "salary": 450}, {"company_id": 2, "employee_id": 9, "employee_name": "Hermione", "salary": 700}, {"company_id": 3, "employee_id": 7, "employee_name": "Bocaben", "salary": 100}, {"company_id": 3, "employee_id": 2, "employee_name": "Ognjen", "salary": 2200}, {"company_id": 3, "employee_id": 13, "employee_name": "Nyancat", "salary": 3300}, {"company_id": 3, "employee_id": 15, "employee_name": "Morninngcat", "salary": 7777}]}}`
- **Required output:** `{"columns": ["company_id", "employee_id", "employee_name", "salary"], "rows": [[1, 1, "Tony", 1020], [1, 2, "Pronub", 10863], [1, 3, "Tyrrox", 5508], [2, 1, "Pam", 300], [2, 7, "Bassem", 450], [2, 9, "Hermione", 700], [3, 7, "Bocaben", 76], [3, 2, "Ognjen", 1672], [3, 13, "Nyancat", 2508], [3, 15, "Morninngcat", 5911]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table `Salaries`:

The objective is to compute `{"columns": ["company_id", "employee_id", "employee_name", "salary"], "rows": [[1, 1, "Tony", 1020], [1, 2, "Pronub", 10863], [1, 3, "Tyrrox", 5508], [2, 1, "Pam", 300], [2, 7, "Bassem", 450], [2, 9, "Hermione", 700], [3, 7, "Bocaben", 76], [3, 2, "Ognjen", 1672], [3, 13, "Nyancat", 2508], [3, 15, "Morninngcat", 5911]]}` from `{"tables": {"Salaries": [{"company_id": 1, "employee_id": 1, "employee_name": "Tony", "salary": 2000}, {"company_id": 1, "employee_id": 2, "employee_name": "Pronub", "salary": 21300}, {"company_id": 1, "employee_id": 3, "employee_name": "Tyrrox", "salary": 10800}, {"company_id": 2, "employee_id": 1, "employee_name": "Pam", "salary": 300}, {"company_id": 2, "employee_id": 7, "employee_name": "Bassem", "salary": 450}, {"company_id": 2, "employee_id": 9, "employee_name": "Hermione", "salary": 700}, {"company_id": 3, "employee_id": 7, "employee_name": "Bocaben", "salary": 100}, {"company_id": 3, "employee_id": 2, "employee_name": "Ognjen", "salary": 2200}, {"company_id": 3, "employee_id": 13, "employee_name": "Nyancat", "salary": 3300}, {"company_id": 3, "employee_id": 15, "employee_name": "Morninngcat", "salary": 7777}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Determine one tax bracket per company.** The tax rate is not based on an individual employee's salary. It is based on the maximum salary anywhere in that employee's company. The query therefore begins by calculating one summary row per `company_id`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salaries": [{"company_id": 1, "employee_id": 1, "employee_name": "Tony", "salary": 2000}, {"company_id": 1, "employee_id": 2, "employee_name": "Pronub", "salary": 21300}, {"company_id": 1, "employee_id": 3, "employee_name": "Tyrrox", "salary": 10800}, {"company_id": 2, "employee_id": 1, "employee_name": "Pam", "salary": 300}, {"company_id": 2, "employee_id": 7, "employee_name": "Bassem", "salary": 450}, {"company_id": 2, "employee_id": 9, "employee_name": "Hermione", "salary": 700}, {"company_id": 3, "employee_id": 7, "employee_name": "Bocaben", "salary": 100}, {"company_id": 3, "employee_id": 2, "employee_name": "Ognjen", "salary": 2200}, {"company_id": 3, "employee_id": 13, "employee_name": "Nyancat", "salary": 3300}, {"company_id": 3, "employee_id": 15, "employee_name": "Morninngcat", "salary": 7777}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The derived table `t` groups `Salaries` by company and computes `MAX(salary) AS top`. If a company has many employees, `top` retains only its highest original salary. The primary key guarantees unique employee rows but is not needed for the maximum itself.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Attach the company maximum back to every employee.** The outer table alias `s` still contains one row per employee. Joining `s.company_id = t.company_id` gives each employee the `top` value for their own company.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["company_id", "employee_id", "employee_name", "salary"], "rows": [[1, 1, "Tony", 1020], [1, 2, "Pronub", 10863], [1, 3, "Tyrrox", 5508], [2, 1, "Pam", 300], [2, 7, "Bassem", 450], [2, 9, "Hermione", 700], [3, 7, "Bocaben", 76], [3, 2, "Ognjen", 1672], [3, 13, "Nyancat", 2508], [3, 15, "Morninngcat", 5911]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salaries": [{"company_id": 1, "employee_id": 1, "employee_name": "Tony", "salary": 2000}, {"company_id": 1, "employee_id": 2, "employee_name": "Pronub", "salary": 21300}, {"company_id": 1, "employee_id": 3, "employee_name": "Tyrrox", "salary": 10800}, {"company_id": 2, "employee_id": 1, "employee_name": "Pam", "salary": 300}, {"company_id": 2, "employee_id": 7, "employee_name": "Bassem", "salary": 450}, {"company_id": 2, "employee_id": 9, "employee_name": "Hermione", "salary": 700}, {"company_id": 3, "employee_id": 7, "employee_name": "Bocaben", "salary": 100}, {"company_id": 3, "employee_id": 2, "employee_name": "Ognjen", "salary": 2200}, {"company_id": 3, "employee_id": 13, "employee_name": "Nyancat", "salary": 3300}, {"company_id": 3, "employee_id": 15, "employee_name": "Morninngcat", "salary": 7777}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["company_id", "employee_id", "employee_name", "salary"], "rows": [[1, 1, "Tony", 1020], [1, 2, "Pronub", 10863], [1, 3, "Tyrrox", 5508], [2, 1, "Pam", 300], [2, 7, "Bassem", 450], [2, 9, "Hermione", 700], [3, 7, "Bocaben", 76], [3, 2, "Ognjen", 1672], [3, 13, "Nyancat", 2508], [3, 15, "Morninngcat", 5911]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Window-function maximum:** `MAX(salary) OVER (PARTITION BY company_id)` can attach the company maximum without an explicit derived-table join. It expresses the same logic compactly where supported.
- **Correlated subquery:** Compute the maximum separately for each employee row. It is readable but may repeat work unless the optimizer decorrelates it.
- **Tax each employee independently:** This is incorrect because the company's highest salary determines the rate for every employee.
- **Maximum below 1000:** Salaries remain unchanged before rounding.
- **Maximum exactly 1000:** The inclusive middle bracket applies, producing a twenty-four-percent tax.
- **Maximum exactly 10000:** It also remains in the middle bracket.
- **Maximum above 10000:** The fifty-one-percent retained factor applies company-wide.
- **One-employee company:** That employee's own salary is also the company maximum, and the normal logic works.
- **Several employees share the maximum:** `MAX` still returns one scalar summary and the join returns each employee once.
- **Fractional retained salary:** `ROUND` is applied after multiplication to produce the nearest integer.
- **Any-order output:** Omitting `ORDER BY` is correct.
- **Output alias:** `AS salary` gives the calculated value the same required column name as the original.
- **Decimal arithmetic:** The decimal literals `0.76` and `0.51` express retained percentages directly; database numeric rules determine intermediate precision before rounding.
- **Empty table:** The derived table and final result are both empty, with no invented employees.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let `E` be the number of employee rows and `C` the number of distinct companies. A conventional hash aggregation scans `E` rows and stores one maximum per company, taking expected `O(E)` time and `O(C)` space.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
