# Guided Example: The Most Recent Orders for Each Product

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 1}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}`
- **Required output:** `{"columns": ["product_name", "product_id", "order_id", "order_date"], "rows": [["keyboard", 1, 6, "2020-08-01"], ["keyboard", 1, 7, "2020-08-01"], ["mouse", 2, 8, "2020-08-03"], ["screen", 3, 3, "2020-08-29"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["product_name", "product_id", "order_id", "order_date"], "rows": [["keyboard", 1, 6, "2020-08-01"], ["keyboard", 1, 7, "2020-08-01"], ["mouse", 2, 8, "2020-08-03"], ["screen", 3, 3, "2020-08-29"]]}` from `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 1}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank order dates separately for every product

The task asks for each product's latest date and every order placed on that date. This is not a single latest row per product: two customers may order the same product on the same latest date, and both orders must appear.

The common table expression `T` joins `Orders` with `Products` through `product_id`. Each order thereby gains its product name while products without orders create no row under the inner join.

The `Customers` table is not used because the requested output contains no customer name and the order row already has all information needed to identify the product and order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 1}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why RANK preserves all latest-date ties

The window expression partitions joined rows by `product_id`. Each product therefore receives an independent ranking.

Within each partition, `ORDER BY order_date DESC` places newest dates first. `RANK()` assigns rank one to every row tied at that newest date.

This tie behavior is essential. In the example, keyboard orders six and seven share August 1. Both receive `rk = 1` and both must be returned.

`ROW_NUMBER` would arbitrarily number those rows one and two, causing a filter for one to discard a required latest order. `DENSE_RANK` would behave the same as `RANK` for the rank-one filter, but `RANK` directly provides the needed semantics.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Filter after computing the window

The outer query applies `WHERE rk = 1`. Window ranks are computed over all order rows in each product partition before this filter.

For a product with several dates, only rows on its maximum date have rank one. For a product with one order, that row is automatically rank one. A never-ordered product has no joined row and therefore no rank, so it is absent as required.

Filtering before ranking would be logically backwards because the query would not yet know which date is latest within each complete product history.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_name", "product_id", "order_id", "order_date"], "rows": [["keyboard", 1, 6, "2020-08-01"], ["keyboard", 1, 7, "2020-08-01"], ["mouse", 2, 8, "2020-08-03"], ["screen", 3, 3, "2020-08-29"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 1}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_name", "product_id", "order_id", "order_date"], "rows": [["keyboard", 1, 6, "2020-08-01"], ["keyboard", 1, 7, "2020-08-01"], ["mouse", 2, 8, "2020-08-03"], ["screen", 3, 3, "2020-08-29"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **MAX-date subquery:** Group orders by product to find `MAX(order_date)`, then join back on both product and date. It also preserves every latest-date tie.
- **ROW_NUMBER:** It is wrong here because it keeps only one row when several orders share the latest date.
- **DENSE_RANK:** Filtering rank one is correct and equivalent to `RANK` for this task.
- **Correlated NOT EXISTS:** Keep an order when no later order exists for the same product; it is valid but may be less direct or efficient.
- **Product with one order:** That row receives rank one and is returned.
- **Several orders on latest date:** All receive rank one and survive.
- **Product never ordered:** The inner join creates no row, so it is omitted.
- **Duplicate product names:** Secondary `product_id` sorting produces the required deterministic order.
- **Customer table:** It is intentionally unused because no customer attribute is requested.
- **Same customer and product per day:** The contract forbids duplicates of that pair, but different customers may create latest-date ties.
- **Positional ORDER BY:** It is concise but depends on the select-list order.
- **Wildcard in T:** Extra columns are carried only temporarily and removed by the outer projection.
- **Rank versus row count:** Rank one identifies a date tier, not a fixed number of orders.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r \log r)$. Let $R$ be order count, $P$ product count, and $Q$ returned-row count.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
