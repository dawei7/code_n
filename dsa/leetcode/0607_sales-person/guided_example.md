# Guided Example: Sales Person

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"SalesPerson": [{"sales_id": 1, "name": "Alice", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}, {"sales_id": 2, "name": "Bob", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}], "Company": [{"com_id": 1, "name": "RED", "city": "A"}, {"com_id": 2, "name": "BLUE", "city": "B"}], "Orders": [{"order_id": 1, "order_date": "2021-01-01", "com_id": 1, "sales_id": 1, "amount": 100}, {"order_id": 2, "order_date": "2021-01-02", "com_id": 2, "sales_id": 2, "amount": 200}]}}`
- **Required output:** `{"columns": ["name"], "rows": [["Bob"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `SalesPerson`

The objective is to compute `{"columns": ["name"], "rows": [["Bob"]]}` from `{"tables": {"SalesPerson": [{"sales_id": 1, "name": "Alice", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}, {"sales_id": 2, "name": "Bob", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}], "Company": [{"com_id": 1, "name": "RED", "city": "A"}, {"com_id": 2, "name": "BLUE", "city": "B"}], "Orders": [{"order_id": 1, "order_date": "2021-01-01", "com_id": 1, "sales_id": 1, "amount": 100}, {"order_id": 2, "order_date": "2021-01-02", "com_id": 2, "sales_id": 2, "amount": 200}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why the query starts from `SalesPerson`

`SalesPerson AS s` is the complete universe of people who may need to appear. The first left join:



attaches all orders for a salesperson. If none exist, the salesperson row remains and order columns become `NULL`. An inner join would discard no-order salespersons even though they clearly had no RED order and should be returned.

The second left join attaches each order’s company through `com_id`:



Foreign keys guarantee valid IDs for real orders. The left form continues preserving the already retained salesperson row when there is no order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"SalesPerson": [{"sales_id": 1, "name": "Alice", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}, {"sales_id": 2, "name": "Bob", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}], "Company": [{"com_id": 1, "name": "RED", "city": "A"}, {"com_id": 2, "name": "BLUE", "city": "B"}], "Orders": [{"order_id": 1, "order_date": "2021-01-01", "com_id": 1, "sales_id": 1, "amount": 100}, {"order_id": 2, "order_date": "2021-01-02", "com_id": 2, "sales_id": 2, "amount": 200}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collapsing all orders per salesperson

`GROUP BY sales_id` creates one group per salesperson after joining. A person with several orders has several joined rows in the same group; a person with no orders has one synthetic left-join row.

Selecting `s.name` is sound because `sales_id` is the primary key of `SalesPerson`, so it determines exactly one name. Some SQL systems require the name in the grouping list for strict portability, but MySQL recognizes the functional dependency.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Counting RED orders with a Boolean sum

In MySQL, `c.name = 'RED'` behaves as one for a RED company and zero for another non-null company name. Summing it gives the number of RED-related joined order rows.

Three cases matter:

- at least one RED order: the sum is positive;
- orders exist, but none target RED: every comparison is zero, so the sum is zero;
- no orders: `c.name` is `NULL`, comparison is `NULL`, and `SUM` over only null values returns `NULL`.

The predicate:



maps the no-order null sum to zero. Therefore, both “no orders” and “only non-RED orders” qualify, while any RED order disqualifies the entire group.

`HAVING` is the correct clause because the decision depends on an aggregate over all rows in a salesperson’s group. A row-level `WHERE c.name != 'RED'` would be wrong: a salesperson with one RED and one GREEN order would retain the GREEN row and falsely appear eligible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name"], "rows": [["Bob"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"SalesPerson": [{"sales_id": 1, "name": "Alice", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}, {"sales_id": 2, "name": "Bob", "salary": 50000, "commission_rate": 10, "hire_date": "2020-01-01"}], "Company": [{"com_id": 1, "name": "RED", "city": "A"}, {"com_id": 2, "name": "BLUE", "city": "B"}], "Orders": [{"order_id": 1, "order_date": "2021-01-01", "com_id": 1, "sales_id": 1, "amount": 100}, {"order_id": 2, "order_date": "2021-01-02", "com_id": 2, "sales_id": 2, "amount": 200}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name"], "rows": [["Bob"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`NOT EXISTS` correlated subquery:** For each salesperson, reject if an order joined to company RED exists. It directly expresses the anti-condition and can short-circuit after one match.
- **`NOT IN` of RED salesperson IDs:** Works when the subquery cannot return `NULL`. `NOT EXISTS` is safer under nullable data.
- **Filter non-RED rows in `WHERE`:** Incorrect because it can hide a RED row while leaving another order from the same salesperson.
- **Inner join:** Incorrectly removes salespersons with no orders.
- **One RED among many orders:** Positive Boolean sum excludes the salesperson.
- **Only non-RED orders:** Sum is zero and the salesperson qualifies.
- **No orders:** Left join preserves the person; null sum becomes zero.
- **Several companies named RED:** Every matching order contributes one; the condition still behaves correctly.
- **Duplicate names:** Selection is by salesperson groups, so distinct people with the same display name may yield repeated name values; do not add `DISTINCT` without a requirement.
- **Functional dependency:** Grouping by primary key `sales_id` determines `s.name` in MySQL.
- **No required order:** Avoid unnecessary `ORDER BY`.
- **Why `COALESCE` matters:** `NULL = 0` is unknown, so no-order groups would otherwise fail the `HAVING` test.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((S + C + O) \log(S + C + O))$. Let $S$, $O$, and $C$ be row counts for `SalesPerson`, `Orders`, and `Company`. With hash/indexed joins, processing can be expected linear in $S+O+C$, followed by grouping over joined rows. Sort-based joins or aggregation can require $O((S+O+C)\log(S+O+C))$, matching the conservative manifest.
- **Auxiliary Space Complexity:** $O(S + C + O)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
