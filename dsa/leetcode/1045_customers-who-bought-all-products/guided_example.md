# Guided Example: Customers Who Bought All Products

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customer": [{"customer_id": 1, "product_key": 5}, {"customer_id": 2, "product_key": 6}, {"customer_id": 3, "product_key": 5}, {"customer_id": 3, "product_key": 6}, {"customer_id": 1, "product_key": 6}], "Product": [{"product_key": 5}, {"product_key": 6}]}}`
- **Required output:** `{"columns": ["customer_id"], "rows": [[1], [3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customer`

The objective is to compute `{"columns": ["customer_id"], "rows": [[1], [3]]}` from `{"tables": {"Customer": [{"customer_id": 1, "product_key": 5}, {"customer_id": 2, "product_key": 6}, {"customer_id": 3, "product_key": 5}, {"customer_id": 3, "product_key": 6}, {"customer_id": 1, "product_key": 6}], "Product": [{"product_key": 5}, {"product_key": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “all products” into equal distinct counts

The `Product` table defines the complete required set. Its `product_key` is a primary key, so each required product appears exactly once.

For one customer, collect the distinct `product_key` values appearing in `Customer`. Because `Customer.product_key` references `Product.product_key`, every counted non-null key belongs to the required product set.

The customer bought every product exactly when the size of this distinct purchased set equals the number of rows in `Product`.

This is a relational-division question expressed through grouping and counting.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customer": [{"customer_id": 1, "product_key": 5}, {"customer_id": 2, "product_key": 6}, {"customer_id": 3, "product_key": 5}, {"customer_id": 3, "product_key": 6}, {"customer_id": 1, "product_key": 6}], "Product": [{"product_key": 5}, {"product_key": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group rows by customer

The query selects `customer_id` from `Customer` and uses `GROUP BY 1`.

In MySQL, positional grouping expression `1` refers to the first selected expression, which is `customer_id`. Every row for the same customer is placed in one group.

Writing `GROUP BY customer_id` would be equivalent and more explicit. The exact source uses the concise positional form.

Only IDs that appear in `Customer` form groups. There is no separate customer master table in the schema, so the query cannot report an ID that has no purchase row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query selects `customer_id` from `Customer` and uses `GR... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `DISTINCT` is essential

The `Customer` table may contain duplicate rows. If a customer bought product five and that row appears three times, ordinary `COUNT(product_key)` would count three purchases even though only one distinct product was covered.

`COUNT(DISTINCT product_key)` collapses repeated keys within each customer group. It measures coverage of different products, not transaction-row volume.

Without `DISTINCT`, duplicates could make an incomplete customer's count equal the product total and produce a false positive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id"], "rows": [[1], [3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customer": [{"customer_id": 1, "product_key": 5}, {"customer_id": 2, "product_key": 6}, {"customer_id": 3, "product_key": 5}, {"customer_id": 3, "product_key": 6}, {"customer_id": 1, "product_key": 6}], "Product": [{"product_key": 5}, {"product_key": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id"], "rows": [[1], [3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Double `NOT EXISTS`:** Select customers for wh:** - **Double `NOT EXISTS`:** Select customers for whom there does not exist a product lacking a matching purchase row. This expresses universal quantification directly and does not depend on count equality.
- **Cross join then find missing pairs:** Generate every customer-product pair, subtract purchased pairs, and exclude customers with missing rows. It mirrors relational division but can create a very large intermediate table.
- **Join to `Product` before counting:** This is safer if referential integrity is absent or invalid product keys can appear. Under the stated foreign key, it is redundant.
- **Count without `DISTINCT`:** This is incorrect because duplicate `Customer` rows can inflate a customer's coverage.
- **Count distinct products in `Product`:** `COUNT(DISTINCT product_key)` would equal `COUNT(1)` because `product_key` is a primary key, so the simpler row count is sufficient.
- **Duplicate purchase rows:** They collapse inside `COUNT(DISTINCT ...)` and do not affect qualification.
- **Customer missing one product:** Its distinct count is strictly below the product total and it is excluded.
- **Customer buying every product:** Its distinct set equals the required set and it is returned once.
- **Result ordering:** No ordering clause is necessary because any order is accepted.
- **`GROUP BY 1` portability:** Positional grouping is supported by MySQL here, but `GROUP BY customer_id` is clearer and more portable across SQL styles.
- **Null product key:** It is ignored by the distinct count and cannot falsely satisfy a required product.
- **Foreign-key dependence:** Count equality proves set equality only because purchased keys belong to the product set.
- **No customer master table:** The query's candidate IDs come only from `Customer`, which is all the schema makes available.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of rows in `Customer` and `Q` the number of rows in `Product`.
- **Auxiliary Space Complexity:** $O(R + Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
