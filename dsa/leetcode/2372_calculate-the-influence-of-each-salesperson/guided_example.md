# Guided Example: Calculate the Influence of Each Salesperson

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Salesperson": [{"salesperson_id": 1, "name": "Alice"}, {"salesperson_id": 2, "name": "Bob"}, {"salesperson_id": 3, "name": "Jerry"}], "Customer": [{"customer_id": 1, "salesperson_id": 1}, {"customer_id": 2, "salesperson_id": 1}, {"customer_id": 3, "salesperson_id": 2}], "Sales": [{"sale_id": 1, "customer_id": 2, "price": 892}, {"sale_id": 2, "customer_id": 1, "price": 354}, {"sale_id": 3, "customer_id": 3, "price": 988}, {"sale_id": 4, "customer_id": 3, "price": 856}]}}`
- **Required output:** `{"columns": ["salesperson_id", "name", "total"], "rows": [[1, "Alice", 1246], [2, "Bob", 1844], [3, "Jerry", 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Salesperson`

The objective is to compute `{"columns": ["salesperson_id", "name", "total"], "rows": [[1, "Alice", 1246], [2, "Bob", 1844], [3, "Jerry", 0]]}` from `{"tables": {"Salesperson": [{"salesperson_id": 1, "name": "Alice"}, {"salesperson_id": 2, "name": "Bob"}, {"salesperson_id": 3, "name": "Jerry"}], "Customer": [{"customer_id": 1, "salesperson_id": 1}, {"customer_id": 2, "salesperson_id": 1}, {"customer_id": 3, "salesperson_id": 2}], "Sales": [{"sale_id": 1, "customer_id": 2, "price": 892}, {"sale_id": 2, "customer_id": 1, "price": 354}, {"sale_id": 3, "customer_id": 3, "price": 988}, {"sale_id": 4, "customer_id": 3, "price": 856}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow the ownership chain

The value attributed to a salesperson does not appear directly in `Salesperson`. The three tables form a chain:



A salesperson owns zero or more customers through `Customer.salesperson_id`. Each customer may then have zero or more sales through `Sales.customer_id`. The required total for one salesperson is the sum of `Sales.price` over every sale made by every customer assigned to that salesperson.

The result must also contain salespeople who have no customers or whose customers have no sales. That requirement determines the join direction and join type.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Salesperson": [{"salesperson_id": 1, "name": "Alice"}, {"salesperson_id": 2, "name": "Bob"}, {"salesperson_id": 3, "name": "Jerry"}], "Customer": [{"customer_id": 1, "salesperson_id": 1}, {"customer_id": 2, "salesperson_id": 1}, {"customer_id": 3, "salesperson_id": 2}], "Sales": [{"sale_id": 1, "customer_id": 2, "price": 892}, {"sale_id": 2, "customer_id": 1, "price": 354}, {"sale_id": 3, "customer_id": 3, "price": 988}, {"sale_id": 4, "customer_id": 3, "price": 856}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Begin with every salesperson

The query starts from `Salesperson AS sp`. This makes the salesperson table the preserved side of the operation. The first join is:



A left join emits matching customer rows when they exist. When a salesperson has no customer, it still emits one row containing the salesperson columns and `NULL` for the customer columns. An inner join would discard that salesperson completely, making it impossible to report the required zero.

The second join is also a left join:



For a customer with several sales, this expands into one joined row per sale. For a customer with no sales—or for the null placeholder produced because there was no customer—it preserves the chain with null sales columns. This second preservation is important: using an inner join here would also remove salespeople whose customers have not purchased anything.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregate all expanded rows back to one salesperson

After the joins, one salesperson may appear on many rows: once for each sale reachable through their customers. The query groups by:



In MySQL, `1` is a positional reference to the first expression in the `SELECT` list, which is `sp.salesperson_id`. It is equivalent here to `GROUP BY sp.salesperson_id`.

The selected `name` is functionally determined by the unique `salesperson_id` in the `Salesperson` table. Thus, every joined row in one group carries the same name, and returning that name alongside the aggregate is unambiguous.

Within each group, `SUM(price)` adds every non-null sale price. If one customer has multiple sales, every sale row contributes. If a salesperson has multiple customers, the rows from all those customers share the salesperson group and contribute to the same sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["salesperson_id", "name", "total"], "rows": [[1, "Alice", 1246], [2, "Bob", 1844], [3, "Jerry", 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Salesperson": [{"salesperson_id": 1, "name": "Alice"}, {"salesperson_id": 2, "name": "Bob"}, {"salesperson_id": 3, "name": "Jerry"}], "Customer": [{"customer_id": 1, "salesperson_id": 1}, {"customer_id": 2, "salesperson_id": 1}, {"customer_id": 3, "salesperson_id": 2}], "Sales": [{"sale_id": 1, "customer_id": 2, "price": 892}, {"sale_id": 2, "customer_id": 1, "price": 354}, {"sale_id": 3, "customer_id": 3, "price": 988}, {"sale_id": 4, "customer_id": 3, "price": 856}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["salesperson_id", "name", "total"], "rows": [[1, "Alice", 1246], [2, "Bob", 1844], [3, "Jerry", 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Inner joins:** They incorrectly remove salespeople without customers or without completed sales, violating the zero-total requirement.
- **Correlated subquery per salesperson:** It can calculate each total but may repeat lookup work and is less direct than one joined aggregation.
- **Pre-aggregate sales by customer:** Summing per customer before joining is valid and may reduce intermediate rows, but the current query already expresses the required logic clearly.
- **`COUNT` instead of `SUM`:** Counting sales would measure transactions, not the prices paid.
- **A salesperson with no customers:** Both left joins preserve a null chain and `COALESCE` returns zero.
- **A customer with no sales:** The customer is present but contributes no numeric price; the salesperson still remains in the result.
- **Several sales by one customer:** Each sale price appears on a separate joined row and all are included.
- **Several customers per salesperson:** Grouping by salesperson merges their sale rows into one total.
- **`GROUP BY 1`:** The positional `1` refers to `sp.salesperson_id`, not a constant group shared by the whole table.
- **Output order:** No ordering is promised or needed because any order is accepted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+C+R)$. Let $S$ be the number of salesperson rows, $C$ the number of customer rows, and $R$ the number of sales rows. The manifest reports $O((S+C+R)\log(S+C+R))$ time and $O(S+C+R)$ space.
- **Auxiliary Space Complexity:** $O(S+C+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
