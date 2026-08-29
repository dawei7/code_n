# Guided Example: Product Sales Analysis III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}]}}`
- **Required output:** `{"columns": ["product_id", "first_year", "quantity", "price"], "rows": [[100, 2008, 10, 5000], [200, 2011, 15, 9000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sales`

The objective is to compute `{"columns": ["product_id", "first_year", "quantity", "price"], "rows": [[100, 2008, 10, 5000], [200, 2011, 15, 9000]]}` from `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate finding the first year from returning its sales

For each product, the query must first discover its minimum `year`. It must then return every original sale row for that product in that year.

These are deliberately two steps. Aggregating to `MIN(year)` alone loses `quantity` and `price` because those values belong to individual sale rows. Joining or filtering the original table by the per-product minimum restores the full first-year rows.

The phrase "all sales entries" matters. A product can have multiple sales in its earliest year. The query must retain every one rather than choose an arbitrary row or combine their quantities.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute one earliest-year key per product

The inner query is:



`GROUP BY product_id` creates one group from all sale rows for each product.

Within each group, `MIN(year)` returns the smallest year value. The subquery therefore produces one pair:



for every product appearing in `Sales`.

The alias `AS year` makes the second column's role compatible with the outer tuple comparison. The alias is not the final output name; the outer query later renames the original sale year to `first_year`.

No `quantity` or `price` appears in this grouped result. Selecting either without aggregation would not identify which source row it came from, especially when several rows share the earliest year.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Filter original rows with a composite membership test

The outer condition is:



`(product_id, year)` is a row-value expression. A sale row passes when its two-column pair equals one of the product-and-minimum-year pairs returned by the subquery.

Matching both columns is essential:

- Matching only `year` could retain a later sale for one product merely because that year is the first year of another product.
- Matching only `product_id` would retain every year for that product.

The composite pair expresses exactly the desired relation: this sale's year equals the minimum year for this same product.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "first_year", "quantity", "price"], "rows": [[100, 2008, 10, 5000], [200, 2011, 15, 9000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "first_year", "quantity", "price"], "rows": [[100, 2008, 10, 5000], [200, 2011, 15, 9000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Join with the aggregate subquery:** Compute `(product_id, MIN(year))` and inner-join it to `Sales` on both product and year. This is semantically equivalent and often makes the two-step logic explicit.
- **Window function:** Compute `MIN(year) OVER (PARTITION BY product_id)` for each row, then filter where `year` equals that window value. This preserves all ties but may require a derived table because window aliases are not normally available directly in `WHERE`.
- **Correlated subquery:** Filter with `year = (SELECT MIN(year) ... WHERE product_id = outer.product_id)`. Optimizers may decorrelate it, but the grouped key set is often clearer.
- **ROW_NUMBER:** Using `ROW_NUMBER() = 1` would keep only one row when several sales share the first year. A minimum-year filter or `DENSE_RANK() = 1` is required to preserve all ties.
- **One sale for a product:** Its year is automatically the minimum and the row is returned.
- **Several first-year sales:** Every row with the minimum year is returned independently.
- **Later sale with identical quantity and price:** It is rejected because the composite key includes year.
- **Same earliest year across products:** Matching also includes product identifier, so groups cannot interfere.
- **No Product table:** This problem requires only `Sales`; product metadata is irrelevant.
- **No DISTINCT:** Identical-looking projected rows may represent different sales and must not be collapsed.
- **Alias first_year:** Only the output column name changes; filtering still uses the source `year`.
- **Any order:** Omitting `ORDER BY` matches the contract.
- **Composite row IN support:** MySQL supports row-value membership for the two-column comparison used by the exact query.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(G)$. Let `R` be the number of rows in `Sales` and `G` the number of distinct products.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
