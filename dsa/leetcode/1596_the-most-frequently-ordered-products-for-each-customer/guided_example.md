# Guided Example: The Most Frequently Ordered Products for Each Customer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "name": "Alice"}, {"customer_id": 2, "name": "Bob"}, {"customer_id": 3, "name": "Tom"}, {"customer_id": 4, "name": "Jerry"}, {"customer_id": 5, "name": "John"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 3}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}`
- **Required output:** `{"columns": ["customer_id", "product_id", "product_name"], "rows": [[1, 2, "mouse"], [2, 1, "keyboard"], [2, 2, "mouse"], [2, 3, "screen"], [3, 3, "screen"], [4, 1, "keyboard"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["customer_id", "product_id", "product_name"], "rows": [[1, 2, "mouse"], [2, 1, "keyboard"], [2, 2, "mouse"], [2, 3, "screen"], [3, 3, "screen"], [4, 1, "keyboard"]]}` from `{"tables": {"Customers": [{"customer_id": 1, "name": "Alice"}, {"customer_id": 2, "name": "Bob"}, {"customer_id": 3, "name": "Tom"}, {"customer_id": 4, "name": "Jerry"}, {"customer_id": 5, "name": "John"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 3}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count orders at the customer-product level

The requested frequency is the number of order rows for one product made by one customer. The first stage must therefore reduce `Orders` to one grouped row for every distinct pair:

`GROUP BY customer_id, product_id`.

The checked-in query writes this positionally as `GROUP BY 1, 2`. Within the common table expression’s select list, expression one is `customer_id` and expression two is `product_id`.

After grouping, `COUNT(1)` for a row is that customer’s order frequency for that product. An order on a different date remains a separate row and contributes again. The statement guarantees the same customer does not order the same product more than once on one day, but the query does not need the date because frequency is over all order records, not distinct days.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "name": "Alice"}, {"customer_id": 2, "name": "Bob"}, {"customer_id": 3, "name": "Tom"}, {"customer_id": 4, "name": "Jerry"}, {"customer_id": 5, "name": "John"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 3}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank frequencies separately for each customer

The window expression is:

`RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(1) DESC) AS rk`.

`PARTITION BY customer_id` restarts the ranking for each customer. Without this partition, products would be ranked globally and customers with fewer total orders could disappear even when one product is their personal most frequent.

Within one customer partition, `ORDER BY COUNT(1) DESC` places larger product frequencies first. The most frequently ordered product or products receive rank one.

`RANK` is deliberately tie-preserving. If three products were each ordered twice and no product was ordered more often, all three grouped rows have the same ordering value and all receive `rk = 1`. This matches the plural “product(s)” requirement.

The gaps that `RANK` may leave after ties do not matter because the outer query keeps only rank one. `DENSE_RANK` would produce the same selected rows for this particular filter, while `ROW_NUMBER` would be wrong because it would arbitrarily choose only one tied product.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The window expression is:

`RANK() OVER (PARTITION BY custom... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the common table expression contains

The CTE `T` contains:

- the customer identifier;
- the product identifier;
- that product’s frequency rank within the customer.

It does not expose `COUNT(1)` as a separate column because the final result does not request the count. The aggregate is still valid inside the window ordering after the `GROUP BY` establishes one row per customer-product pair.

Customers with no orders never appear in `T`. This is correct: the output should include only each `customer_id` who ordered at least once. The `Customers` table is not referenced because no customer name is requested and `Orders.customer_id` already identifies every qualifying customer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "product_id", "product_name"], "rows": [[1, 2, "mouse"], [2, 1, "keyboard"], [2, 2, "mouse"], [2, 3, "screen"], [3, 3, "screen"], [4, 1, "keyboard"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "name": "Alice"}, {"customer_id": 2, "name": "Bob"}, {"customer_id": 3, "name": "Tom"}, {"customer_id": 4, "name": "Jerry"}, {"customer_id": 5, "name": "John"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "product_id": 1}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "product_id": 2}, {"order_id": 3, "order_date": "2020-08-29", "customer_id": 3, "product_id": 3}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "product_id": 1}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "product_id": 2}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "product_id": 1}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "product_id": 3}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "product_id": 2}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "product_id": 3}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "product_id": 2}], "Products": [{"product_id": 1, "product_name": "keyboard", "price": 120}, {"product_id": 2, "product_name": "mouse", "price": 80}, {"product_id": 3, "product_name": "screen", "price": 600}, {"product_id": 4, "product_name": "hard disk", "price": 450}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "product_id", "product_name"], "rows": [[1, 2, "mouse"], [2, 1, "keyboard"], [2, 2, "mouse"], [2, 3, "screen"], [3, 3, "screen"], [4, 1, "keyboard"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`DENSE_RANK` instead of `RANK`:** It selects t:** - **`DENSE_RANK` instead of `RANK`:** It selects the same rank-one ties here because only the first rank is filtered. Later rank numbering would differ but is not returned.
- **`ROW_NUMBER`:** This is incorrect for ties because it assigns a unique sequence number and would retain only one equally frequent product.
- **Correlated maximum-count subquery:** One can compare each grouped count with the maximum for that customer, but it is usually more verbose and may repeat aggregation work.
- **Join `Customers` first:** This is unnecessary because customer names are not returned and customers without orders must be excluded. Starting from `Orders` naturally limits the population.
- **One ordered product:** Its grouped row is automatically rank one and is returned.
- **Several tied maxima:** Every tied row receives `rk = 1` and survives.
- **Customer with no orders:** No row enters the CTE, so the customer is correctly absent.
- **Repeated orders on different days:** Every order row contributes to `COUNT(1)`, as required.
- **Same-day guarantee:** It prevents duplicate customer-product orders within one day, but no distinct-date expression is needed because the task counts orders themselves.
- **Unique product key:** It ensures the name join attaches one product row without duplicating output.
- **Missing product reference:** The source assumes order product identifiers correspond to `Products` rows. An unmatched identifier would be removed by the inner join.
- **`GROUP BY 1, 2` readability:** It is valid positional shorthand, but naming `customer_id, product_id` explicitly is safer if the select list is later reordered.
- **Any output order:** Omitting a final `ORDER BY` is correct and avoids promising an order the statement does not require.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r\log r)$. Let $R$ be the number of order rows and $G$ the number of distinct customer-product groups.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
