# Guided Example: Average Salary: Departments VS Company

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salary": [{"id": 1, "employee_id": 1, "amount": 9000, "pay_date": "2017-03-31"}, {"id": 2, "employee_id": 2, "amount": 6000, "pay_date": "2017-03-31"}, {"id": 3, "employee_id": 3, "amount": 10000, "pay_date": "2017-03-31"}, {"id": 4, "employee_id": 1, "amount": 7000, "pay_date": "2017-02-28"}, {"id": 5, "employee_id": 2, "amount": 6000, "pay_date": "2017-02-28"}, {"id": 6, "employee_id": 3, "amount": 8000, "pay_date": "2017-02-28"}], "Employee": [{"employee_id": 1, "department_id": 1}, {"employee_id": 2, "department_id": 2}, {"employee_id": 3, "department_id": 2}]}}`
- **Required output:** `{"columns": ["pay_month", "department_id", "comparison"], "rows": [["2017-02", 1, "same"], ["2017-02", 2, "same"], ["2017-03", 1, "higher"], ["2017-03", 2, "lower"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Salary`

The objective is to compute `{"columns": ["pay_month", "department_id", "comparison"], "rows": [["2017-02", 1, "same"], ["2017-02", 2, "same"], ["2017-03", 1, "higher"], ["2017-03", 2, "lower"]]}` from `{"tables": {"Salary": [{"id": 1, "employee_id": 1, "amount": 9000, "pay_date": "2017-03-31"}, {"id": 2, "employee_id": 2, "amount": 6000, "pay_date": "2017-03-31"}, {"id": 3, "employee_id": 3, "amount": 10000, "pay_date": "2017-03-31"}, {"id": 4, "employee_id": 1, "amount": 7000, "pay_date": "2017-02-28"}, {"id": 5, "employee_id": 2, "amount": 6000, "pay_date": "2017-02-28"}, {"id": 6, "employee_id": 3, "amount": 8000, "pay_date": "2017-02-28"}], "Employee": [{"employee_id": 1, "department_id": 1}, {"employee_id": 2, "department_id": 2}, {"employee_id": 3, "department_id": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Identify the two averages that must be compared.** Every salary payment belongs to an employee, and every employee belongs to one department. For each reporting period and department, the output needs:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salary": [{"id": 1, "employee_id": 1, "amount": 9000, "pay_date": "2017-03-31"}, {"id": 2, "employee_id": 2, "amount": 6000, "pay_date": "2017-03-31"}, {"id": 3, "employee_id": 3, "amount": 10000, "pay_date": "2017-03-31"}, {"id": 4, "employee_id": 1, "amount": 7000, "pay_date": "2017-02-28"}, {"id": 5, "employee_id": 2, "amount": 6000, "pay_date": "2017-02-28"}, {"id": 6, "employee_id": 3, "amount": 8000, "pay_date": "2017-02-28"}], "Employee": [{"employee_id": 1, "department_id": 1}, {"employee_id": 2, "department_id": 2}, {"employee_id": 3, "department_id": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. the average of all company salary amounts in that period, and
2. the average of salary amounts for only that department in the same period.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | 1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The exact query computes both values on every joined salary row with window functions. It then keeps one distinct output row per repeated comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["pay_month", "department_id", "comparison"], "rows": [["2017-02", 1, "same"], ["2017-02", 2, "same"], ["2017-03", 1, "higher"], ["2017-03", 2, "lower"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salary": [{"id": 1, "employee_id": 1, "amount": 9000, "pay_date": "2017-03-31"}, {"id": 2, "employee_id": 2, "amount": 6000, "pay_date": "2017-03-31"}, {"id": 3, "employee_id": 3, "amount": 10000, "pay_date": "2017-03-31"}, {"id": 4, "employee_id": 1, "amount": 7000, "pay_date": "2017-02-28"}, {"id": 5, "employee_id": 2, "amount": 6000, "pay_date": "2017-02-28"}, {"id": 6, "employee_id": 3, "amount": 8000, "pay_date": "2017-02-28"}], "Employee": [{"employee_id": 1, "department_id": 1}, {"employee_id": 2, "department_id": 2}, {"employee_id": 3, "department_id": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["pay_month", "department_id", "comparison"], "rows": [["2017-02", 1, "same"], ["2017-02", 2, "same"], ["2017-03", 1, "higher"], ["2017-03", 2, "lower"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Partition by formatted month:** Replace both u:** - **Partition by formatted month:** Replace both uses of `pay_date` in the window partitions with `DATE_FORMAT(pay_date, '%Y-%m')`. This preserves the convenient window design and correctly combines payments made on different days of the same month.
- **Two grouped CTEs:** Compute one company average per month and one department average per month, then join them on `pay_month`. This mirrors the editorial, produces already-collapsed rows, and removes the need for outer `DISTINCT`.
- **Conditional comparison without floating rounding:** Compare the database's `AVG` results directly, as the source does. Manually rounding averages before comparing can turn genuinely different values into `'same'`.
- **One department in a month:** Its average equals the company average, so the label must be `'same'`.
- **One employee in a department:** The departmental average is simply that employee's payment, but it is still compared with every company payment in the period.
- **Several salary dates in one month:** This is the material trap in the exact source. Full-date partitions can produce separate statistics and contradictory duplicate month labels.
- **Missing employee record:** The foreign key excludes this case. With inconsistent data, the inner join would silently remove that salary from both averages.
- **Multiple employee rows for one identifier:** The employee primary key excludes this case. Otherwise the join would duplicate salary amounts and corrupt the averages.
- **Months with no salary rows:** They do not appear because there is no input evidence from which to form a department-month.
- **Result ordering:** The contract allows any order, so the absence of `ORDER BY` is intentional and harmless.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((S + E) \log(S + E))$. Let $S$ be the number of salary rows and $E$ the number of employee rows. The key join can be implemented with an index or hash lookup. Window functions generally require partitioning and often sorting the joined salary rows by their partition keys. `DISTINCT` may require another hash set or sort. A conservative database-independent bound is therefore $O((S+E)\log(S+E))$ time, matching the manifest.
- **Auxiliary Space Complexity:** $O(S + E)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
