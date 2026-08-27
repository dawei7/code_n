# Guided Example: Sellers With No Sales

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customer": [{"customer_id": 101, "customer_name": "Alice"}, {"customer_id": 102, "customer_name": "Bob"}], "Orders": [{"order_id": 1, "sale_date": "2020-03-01", "order_cost": 1500, "customer_id": 101, "seller_id": 1}, {"order_id": 2, "sale_date": "2020-05-25", "order_cost": 2400, "customer_id": 102, "seller_id": 2}, {"order_id": 3, "sale_date": "2019-05-25", "order_cost": 800, "customer_id": 101, "seller_id": 3}, {"order_id": 4, "sale_date": "2020-09-13", "order_cost": 1000, "customer_id": 101, "seller_id": 2}, {"order_id": 5, "sale_date": "2019-02-11", "order_cost": 700, "customer_id": 101, "seller_id": 2}], "Seller": [{"seller_id": 1, "seller_name": "Daniel"}, {"seller_id": 2, "seller_name": "Elizabeth"}, {"seller_id": 3, "seller_name": "Frank"}]}}`
- **Required output:** `{"columns": ["seller_name"], "rows": [["Frank"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customer`

The objective is to compute `{"columns": ["seller_name"], "rows": [["Frank"]]}` from `{"tables": {"Customer": [{"customer_id": 101, "customer_name": "Alice"}, {"customer_id": 102, "customer_name": "Bob"}], "Orders": [{"order_id": 1, "sale_date": "2020-03-01", "order_cost": 1500, "customer_id": 101, "seller_id": 1}, {"order_id": 2, "sale_date": "2020-05-25", "order_cost": 2400, "customer_id": 102, "seller_id": 2}, {"order_id": 3, "sale_date": "2019-05-25", "order_cost": 800, "customer_id": 101, "seller_id": 3}, {"order_id": 4, "sale_date": "2020-09-13", "order_cost": 1000, "customer_id": 101, "seller_id": 2}, {"order_id": 5, "sale_date": "2019-02-11", "order_cost": 700, "customer_id": 101, "seller_id": 2}], "Seller": [{"seller_id": 1, "seller_name": "Daniel"}, {"seller_id": 2, "seller_name": "Elizabeth"}, {"seller_id": 3, "seller_name": "Frank"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from every seller

The result must include sellers who made no 2020 sale, including sellers with no orders at all. The query therefore starts from `Seller` and uses:

`LEFT JOIN Orders USING (seller_id)`.

A left join preserves every seller. Sellers with orders produce one joined row per order. A seller without any order still produces one null-extended joined row whose order columns, including `sale_date`, are `NULL`.

The `Customer` table is irrelevant because the result depends only on seller identity and order dates; no customer information is selected or filtered.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customer": [{"customer_id": 101, "customer_name": "Alice"}, {"customer_id": 102, "customer_name": "Bob"}], "Orders": [{"order_id": 1, "sale_date": "2020-03-01", "order_cost": 1500, "customer_id": 101, "seller_id": 1}, {"order_id": 2, "sale_date": "2020-05-25", "order_cost": 2400, "customer_id": 102, "seller_id": 2}, {"order_id": 3, "sale_date": "2019-05-25", "order_cost": 800, "customer_id": 101, "seller_id": 3}, {"order_id": 4, "sale_date": "2020-09-13", "order_cost": 1000, "customer_id": 101, "seller_id": 2}, {"order_id": 5, "sale_date": "2019-02-11", "order_cost": 700, "customer_id": 101, "seller_id": 2}], "Seller": [{"seller_id": 1, "seller_name": "Daniel"}, {"seller_id": 2, "seller_name": "Elizabeth"}, {"seller_id": 3, "seller_name": "Frank"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group all records for one seller

`GROUP BY seller_id` collects a seller’s joined order rows into one group. Since `Seller.seller_id` is unique, it functionally determines one `seller_name`, so selecting the name is well-defined in MySQL.

Grouping is necessary because the condition concerns whether any order in the entire seller history occurred during 2020.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `GROUP BY seller_id` collects a seller’s joined order rows i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turn the year test into a numeric count

MySQL evaluates the Boolean expression:

`YEAR(sale_date) = 2020`

as one when true and zero when false. `SUM` over that expression therefore counts the seller’s 2020 order rows.

An order in 2019 or 2021 contributes zero. An order on any date from January 1 through December 31, 2020 contributes one because `YEAR` returns 2020.

The exact order count is not requested; only whether the count is zero matters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["seller_name"], "rows": [["Frank"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customer": [{"customer_id": 101, "customer_name": "Alice"}, {"customer_id": 102, "customer_name": "Bob"}], "Orders": [{"order_id": 1, "sale_date": "2020-03-01", "order_cost": 1500, "customer_id": 101, "seller_id": 1}, {"order_id": 2, "sale_date": "2020-05-25", "order_cost": 2400, "customer_id": 102, "seller_id": 2}, {"order_id": 3, "sale_date": "2019-05-25", "order_cost": 800, "customer_id": 101, "seller_id": 3}, {"order_id": 4, "sale_date": "2020-09-13", "order_cost": 1000, "customer_id": 101, "seller_id": 2}, {"order_id": 5, "sale_date": "2019-02-11", "order_cost": 700, "customer_id": 101, "seller_id": 2}], "Seller": [{"seller_id": 1, "seller_name": "Daniel"}, {"seller_id": 2, "seller_name": "Elizabeth"}, {"seller_id": 3, "seller_name": "Frank"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["seller_name"], "rows": [["Frank"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`NOT EXISTS` anti-join:** Select sellers for w:** - **`NOT EXISTS` anti-join:** Select sellers for whom no correlated order has a 2020 date. It directly expresses absence and avoids aggregation.
- **`NOT IN` subquery:** It can exclude seller IDs found in 2020 orders, but nullable subquery values can create three-valued-logic hazards unless the key is guaranteed non-null.
- **Left join only 2020 orders and test null:** Put the date predicate in the join condition, then keep sellers with a null joined order ID. This is another clean anti-join formulation.
- **Filter non-2020 rows in `WHERE`:** This is incorrect for sellers having both 2020 and other-year orders, because it removes evidence of the disqualifying sale while leaving another row.
- **Seller with no orders:** The left join preserves the seller, and `COALESCE` turns the null aggregate into zero.
- **Only sales before 2020:** Every Boolean contributes zero, so the seller is included.
- **Only sales after 2020:** The same zero aggregate includes the seller.
- **At least one 2020 sale:** The aggregate is positive, excluding the seller regardless of other dates.
- **Several 2020 sales:** Each contributes one, but any positive total has the same exclusion effect.
- **Boundary dates:** `YEAR` classifies both `2020-01-01` and `2020-12-31` as 2020.
- **Functional dependency:** Unique `seller_id` determines `seller_name`. Stricter portable SQL can group by both columns explicitly.
- **Required ordering:** `ORDER BY 1` sorts the only selected column ascending; no tie-breaking is necessary for identical names unless the schema permits them.
- **Unused customer table:** Customer data cannot change whether a seller made a 2020 sale, so excluding it is intentional.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((s+r)\log(s+r))$. Let $S$ be the number of sellers and $R$ the number of orders.
- **Auxiliary Space Complexity:** $O(s+r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
