# Guided Example: Customer Order Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston", "country": "USA"}, {"customer_id": 2, "name": "Jonathan", "country": "Peru"}, {"customer_id": 3, "name": "Moustafa", "country": "Egypt"}], "Product": [{"product_id": 10, "description": "LC Phone", "price": 300}, {"product_id": 20, "description": "LC T-Shirt", "price": 10}, {"product_id": 30, "description": "LC Book", "price": 45}, {"product_id": 40, "description": "LC Keychain", "price": 2}], "Orders": [{"order_id": 1, "customer_id": 1, "product_id": 10, "order_date": "2020-06-10", "quantity": 1}, {"order_id": 2, "customer_id": 1, "product_id": 20, "order_date": "2020-07-01", "quantity": 1}, {"order_id": 3, "customer_id": 1, "product_id": 30, "order_date": "2020-07-08", "quantity": 2}, {"order_id": 4, "customer_id": 2, "product_id": 10, "order_date": "2020-06-15", "quantity": 2}, {"order_id": 5, "customer_id": 2, "product_id": 40, "order_date": "2020-07-01", "quantity": 10}, {"order_id": 6, "customer_id": 3, "product_id": 20, "order_date": "2020-06-24", "quantity": 2}, {"order_id": 7, "customer_id": 3, "product_id": 30, "order_date": "2020-06-25", "quantity": 2}, {"order_id": 9, "customer_id": 3, "product_id": 30, "order_date": "2020-05-08", "quantity": 3}]}}`
- **Required output:** `{"columns": ["customer_id", "name"], "rows": [[1, "Winston"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["customer_id", "name"], "rows": [[1, "Winston"]]}` from `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston", "country": "USA"}, {"customer_id": 2, "name": "Jonathan", "country": "Peru"}, {"customer_id": 3, "name": "Moustafa", "country": "Egypt"}], "Product": [{"product_id": 10, "description": "LC Phone", "price": 300}, {"product_id": 20, "description": "LC T-Shirt", "price": 10}, {"product_id": 30, "description": "LC Book", "price": 45}, {"product_id": 40, "description": "LC Keychain", "price": 2}], "Orders": [{"order_id": 1, "customer_id": 1, "product_id": 10, "order_date": "2020-06-10", "quantity": 1}, {"order_id": 2, "customer_id": 1, "product_id": 20, "order_date": "2020-07-01", "quantity": 1}, {"order_id": 3, "customer_id": 1, "product_id": 30, "order_date": "2020-07-08", "quantity": 2}, {"order_id": 4, "customer_id": 2, "product_id": 10, "order_date": "2020-06-15", "quantity": 2}, {"order_id": 5, "customer_id": 2, "product_id": 40, "order_date": "2020-07-01", "quantity": 10}, {"order_id": 6, "customer_id": 3, "product_id": 20, "order_date": "2020-06-24", "quantity": 2}, {"order_id": 7, "customer_id": 3, "product_id": 30, "order_date": "2020-06-25", "quantity": 2}, {"order_id": 9, "customer_id": 3, "product_id": 30, "order_date": "2020-05-08", "quantity": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combining orders with prices and customer names

An order row contains quantity, date, customer ID, and product ID, but not unit price or customer name. The query uses two inner joins:

- `Orders JOIN Product USING (product_id)` attaches the price for each ordered product.
- `JOIN Customers USING (customer_id)` attaches the customer's name.

`USING` expresses equality on the identically named key and exposes one copy of that key in the joined result. Inner joins are appropriate because an order must have matching product and customer records to calculate and report it.

For one order, spending is `quantity * price`. The query preserves every order row and later sums these products by customer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston", "country": "USA"}, {"customer_id": 2, "name": "Jonathan", "country": "Peru"}, {"customer_id": 3, "name": "Moustafa", "country": "Egypt"}], "Product": [{"product_id": 10, "description": "LC Phone", "price": 300}, {"product_id": 20, "description": "LC T-Shirt", "price": 10}, {"product_id": 30, "description": "LC Book", "price": 45}, {"product_id": 40, "description": "LC Keychain", "price": 2}], "Orders": [{"order_id": 1, "customer_id": 1, "product_id": 10, "order_date": "2020-06-10", "quantity": 1}, {"order_id": 2, "customer_id": 1, "product_id": 20, "order_date": "2020-07-01", "quantity": 1}, {"order_id": 3, "customer_id": 1, "product_id": 30, "order_date": "2020-07-08", "quantity": 2}, {"order_id": 4, "customer_id": 2, "product_id": 10, "order_date": "2020-06-15", "quantity": 2}, {"order_id": 5, "customer_id": 2, "product_id": 40, "order_date": "2020-07-01", "quantity": 10}, {"order_id": 6, "customer_id": 3, "product_id": 20, "order_date": "2020-06-24", "quantity": 2}, {"order_id": 7, "customer_id": 3, "product_id": 30, "order_date": "2020-06-25", "quantity": 2}, {"order_id": 9, "customer_id": 3, "product_id": 30, "order_date": "2020-05-08", "quantity": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filtering the relevant year

`WHERE YEAR(order_date) = 2020` removes orders outside 2020 before grouping. Orders from every month within 2020 remain at this stage, not only June and July.

Keeping other 2020 months is logically harmless because the conditional aggregates contribute zero for them. It is not the most selective physical predicate, but it does not affect correctness.

Applying `YEAR` to the column can make an ordinary date index less useful. A half-open range from January 1, 2020 through January 1, 2021 would express the same year more directly for index access. An even narrower June-through-August range would suffice for this particular result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `WHERE YEAR(order_date) = 2020` removes orders outside 2020 ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Grouping one result candidate per customer

`GROUP BY 1` groups by the first selected expression, `customer_id`. Every joined order for the same customer becomes part of one aggregate group.

The query also selects `name` without listing it in `GROUP BY`. In MySQL, this is valid when `customer_id` functionally determines `name` because the customer ID is unique. Other SQL modes or database systems may require grouping by both columns or applying an aggregate to the name.

Customers with no orders form no group because the query begins from `Orders` and uses inner joins.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "name"], "rows": [[1, "Winston"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston", "country": "USA"}, {"customer_id": 2, "name": "Jonathan", "country": "Peru"}, {"customer_id": 3, "name": "Moustafa", "country": "Egypt"}], "Product": [{"product_id": 10, "description": "LC Phone", "price": 300}, {"product_id": 20, "description": "LC T-Shirt", "price": 10}, {"product_id": 30, "description": "LC Book", "price": 45}, {"product_id": 40, "description": "LC Keychain", "price": 2}], "Orders": [{"order_id": 1, "customer_id": 1, "product_id": 10, "order_date": "2020-06-10", "quantity": 1}, {"order_id": 2, "customer_id": 1, "product_id": 20, "order_date": "2020-07-01", "quantity": 1}, {"order_id": 3, "customer_id": 1, "product_id": 30, "order_date": "2020-07-08", "quantity": 2}, {"order_id": 4, "customer_id": 2, "product_id": 10, "order_date": "2020-06-15", "quantity": 2}, {"order_id": 5, "customer_id": 2, "product_id": 40, "order_date": "2020-07-01", "quantity": 10}, {"order_id": 6, "customer_id": 3, "product_id": 20, "order_date": "2020-06-24", "quantity": 2}, {"order_id": 7, "customer_id": 3, "product_id": 30, "order_date": "2020-06-25", "quantity": 2}, {"order_id": 9, "customer_id": 3, "product_id": 30, "order_date": "2020-05-08", "quantity": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "name"], "rows": [[1, "Winston"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Half-open June-to-August range:** Filter `orde:** - **Half-open June-to-August range:** Filter `order_date` from June 1 inclusive to August 1 exclusive, then conditionally aggregate June and July. This is more index-friendly and excludes irrelevant 2020 months early.
- **Two monthly subqueries:** Aggregate June and July separately and inner join qualifying customer IDs. It makes the dual requirement explicit but scans or structures orders twice unless optimized.
- **Grouping by customer and month:** Produce monthly totals first, then require two qualifying month rows. This is flexible for more months but needs a second aggregation or pivot.
- **Exactly one hundred:** Greater-than-or-equal correctly includes the customer.
- **High spending in only one month:** The `AND` condition excludes the customer.
- **No July orders:** The July conditional sum is zero for a group with other 2020 orders, so the customer fails.
- **Orders only outside 2020:** They are removed before grouping, leaving no result row.
- **Several orders for one product:** Each quantity-price amount contributes independently.
- **No matching product or customer:** Inner joins discard the orphaned order.
- **Functional dependency of name:** MySQL can infer name from unique customer ID; stricter SQL may require both in `GROUP BY`.
- **Unrestricted order:** No output sort is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C+P+O)$. Let $C$ be the number of customers, $P$ the number of products, and $O$ the number of orders. A typical plan scans or indexes the relevant orders, joins dimension rows through key lookups or hashes, and groups by customer.
- **Auxiliary Space Complexity:** $O(C + P + O)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
