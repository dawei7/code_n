# Guided Example: Product's Worth Over Invoices

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Product": [{"product_id": 0, "name": "ham"}, {"product_id": 1, "name": "bacon"}], "Invoice": [{"invoice_id": 23, "product_id": 0, "rest": 2, "paid": 0, "canceled": 5, "refunded": 0}, {"invoice_id": 12, "product_id": 0, "rest": 0, "paid": 4, "canceled": 0, "refunded": 3}, {"invoice_id": 1, "product_id": 1, "rest": 1, "paid": 1, "canceled": 0, "refunded": 1}, {"invoice_id": 2, "product_id": 1, "rest": 1, "paid": 0, "canceled": 1, "refunded": 1}, {"invoice_id": 3, "product_id": 1, "rest": 0, "paid": 1, "canceled": 1, "refunded": 1}, {"invoice_id": 4, "product_id": 1, "rest": 1, "paid": 1, "canceled": 1, "refunded": 0}]}}`
- **Required output:** `{"columns": ["name", "rest", "paid", "canceled", "refunded"], "rows": [["bacon", 3, 3, 3, 3], ["ham", 2, 4, 5, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Product`

The objective is to compute `{"columns": ["name", "rest", "paid", "canceled", "refunded"], "rows": [["bacon", 3, 3, 3, 3], ["ham", 2, 4, 5, 3]]}` from `{"tables": {"Product": [{"product_id": 0, "name": "ham"}, {"product_id": 1, "name": "bacon"}], "Invoice": [{"invoice_id": 23, "product_id": 0, "rest": 2, "paid": 0, "canceled": 5, "refunded": 0}, {"invoice_id": 12, "product_id": 0, "rest": 0, "paid": 4, "canceled": 0, "refunded": 3}, {"invoice_id": 1, "product_id": 1, "rest": 1, "paid": 1, "canceled": 0, "refunded": 1}, {"invoice_id": 2, "product_id": 1, "rest": 1, "paid": 0, "canceled": 1, "refunded": 1}, {"invoice_id": 3, "product_id": 1, "rest": 0, "paid": 1, "canceled": 1, "refunded": 1}, {"invoice_id": 4, "product_id": 1, "rest": 1, "paid": 1, "canceled": 1, "refunded": 0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from products, not invoices

The result must include every product, even one that has no invoice. That requirement determines the join direction:

`Product LEFT JOIN Invoice USING (product_id)`.

Every row from `Product` survives a left join. Matching invoice rows are attached by equal `product_id`. If no invoice matches, SQL still produces one null-extended joined row for that product. Starting from `Invoice` or using an inner join would incorrectly omit invoice-free products.

`USING (product_id)` is concise join syntax for the equality between the two tables’ same-named `product_id` columns. It also presents the join key as one merged column to later clauses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Product": [{"product_id": 0, "name": "ham"}, {"product_id": 1, "name": "bacon"}], "Invoice": [{"invoice_id": 23, "product_id": 0, "rest": 2, "paid": 0, "canceled": 5, "refunded": 0}, {"invoice_id": 12, "product_id": 0, "rest": 0, "paid": 4, "canceled": 0, "refunded": 3}, {"invoice_id": 1, "product_id": 1, "rest": 1, "paid": 1, "canceled": 0, "refunded": 1}, {"invoice_id": 2, "product_id": 1, "rest": 1, "paid": 0, "canceled": 1, "refunded": 1}, {"invoice_id": 3, "product_id": 1, "rest": 0, "paid": 1, "canceled": 1, "refunded": 1}, {"invoice_id": 4, "product_id": 1, "rest": 1, "paid": 1, "canceled": 1, "refunded": 0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate each monetary category independently

The query groups joined rows by `product_id`. For a product with several invoices, all of its invoice rows enter one group. The four aggregates then compute:

- `SUM(rest)`: total amount still due;
- `SUM(paid)`: total amount paid;
- `SUM(canceled)`: total amount canceled;
- `SUM(refunded)`: total amount refunded.

Each category must be summed separately because the requested output preserves their meanings. Adding them together or subtracting one from another would answer a different accounting question.

The product name is selected directly. Since `Product.product_id` is unique, one grouped product ID determines exactly one name. MySQL can therefore return that functionally dependent `name` alongside the aggregates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query groups joined rows by `product_id`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `COALESCE` is required

For a product with no invoices, the left join supplies nulls for every invoice column. SQL’s `SUM` ignores null inputs, and when there is no non-null value to add, its result is `NULL` rather than numeric zero.

The contract expects totals of zero for such a product. `COALESCE(SUM(rest), 0)` returns the sum when it is non-null and substitutes zero otherwise. The source applies this separately to all four aggregate columns.

For products that do have invoices, `SUM` returns their normal totals and `COALESCE` leaves those values unchanged.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["name", "rest", "paid", "canceled", "refunded"], "rows": [["bacon", 3, 3, 3, 3], ["ham", 2, 4, 5, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Product": [{"product_id": 0, "name": "ham"}, {"product_id": 1, "name": "bacon"}], "Invoice": [{"invoice_id": 23, "product_id": 0, "rest": 2, "paid": 0, "canceled": 5, "refunded": 0}, {"invoice_id": 12, "product_id": 0, "rest": 0, "paid": 4, "canceled": 0, "refunded": 3}, {"invoice_id": 1, "product_id": 1, "rest": 1, "paid": 1, "canceled": 0, "refunded": 1}, {"invoice_id": 2, "product_id": 1, "rest": 1, "paid": 0, "canceled": 1, "refunded": 1}, {"invoice_id": 3, "product_id": 1, "rest": 0, "paid": 1, "canceled": 1, "refunded": 1}, {"invoice_id": 4, "product_id": 1, "rest": 1, "paid": 1, "canceled": 1, "refunded": 0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["name", "rest", "paid", "canceled", "refunded"], "rows": [["bacon", 3, 3, 3, 3], ["ham", 2, 4, 5, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated subqueries:** Four subqueries per p:** - **Correlated subqueries:** Four subqueries per product can compute the totals but may rescan invoices repeatedly unless the optimizer rewrites them.
- **Pre-aggregate invoices first:** Group `Invoice` by `product_id` in a derived table, then left join those totals to `Product`. This is equally valid and can make the one-row-per-product structure explicit.
- **Inner join:** It is incorrect because products without invoices would disappear.
- **Filter invoice rows in `WHERE`:** Conditions on nullable invoice columns after a left join can accidentally turn it into inner-join behavior; such filters belong in the join condition when preservation is required.
- **No invoices for a product:** The left join retains it, and `COALESCE` changes each null aggregate to zero.
- **Zero-valued invoices:** Their sums are numeric zero, not null, and `COALESCE` leaves them unchanged.
- **Several invoices per product:** Grouping combines all of them without duplicating the product row.
- **Invoice referencing a product:** The intended schema relationship makes the join meaningful; an orphan invoice would not create an output product because `Product` is the preserved side.
- **Unique product names:** Ordering has no ties, so no secondary key is necessary.
- **Functional dependency:** Selecting `name` while grouping by `product_id` is sound because one unique ID determines one product row; stricter SQL modes or other databases may prefer grouping by both fields.
- **Null amounts outside the stated model:** `SUM` ignores individual nulls. If every invoice value in one category were null, `COALESCE` would output zero, which may or may not match a different business rule.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(I + P \log P)$. Let `P` be the number of products and `I` the number of invoices. With an index or hash strategy on `product_id`, forming join associations and aggregating them can be $O(P+I)$ expected time. Producing the required name order costs $O(P\log P)$ when a separate sort is needed. This gives the manifest bound $O(I + P\log P)$, with the `P` scan absorbed.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
