# Guided Example: Sales Analysis I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 2, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 4, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}`
- **Required output:** `{"columns": ["seller_id"], "rows": [[1], [3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Product`

The objective is to compute `{"columns": ["seller_id"], "rows": [[1], [3]]}` from `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 2, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 4, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Aggregate the recorded sale price by seller

The best seller is defined by the sum of `Sales.price` across that seller's rows.

The reference clarifies that `price` is already the total recorded price for a sale. It must be added directly. Multiplying it by `quantity` would count quantity twice and produce incorrect totals.

The query groups:



Every represented seller gets one group containing all of that seller's sale rows.

`Product` is not needed. Product name and catalog unit price do not change the stored sale-price total, and all required columns are already in `Sales`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 2, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 4, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute one total for the current seller

The outer aggregate is:



Every stored row contributes its price. The schema permits repeated `Sales` rows, and repeated rows represent repeated stored sales for aggregation purposes. They must all contribute; neither `DISTINCT` nor deduplication belongs here.

Because the condition uses an aggregate after groups are formed, it appears in `HAVING` rather than `WHERE`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Produce the comparison set of all seller totals

The subquery is:



It returns one total-price value per seller. Seller identifiers are not needed inside this subquery because the outer group only needs to compare its total with the complete collection.

For totals 2800, 800, and 2800, the subquery yields those three numbers.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["seller_id"], "rows": [[1], [3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 2, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 4, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["seller_id"], "rows": [[1], [3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **CTE plus MAX:** Compute seller totals once, then keep rows whose total equals `MAX(total_price)`. This is often the clearest explicit form.
- **RANK window function:** Rank grouped totals descending and keep rank one. `RANK` or `DENSE_RANK` preserves ties; `ROW_NUMBER` would not.
- **ORDER BY with LIMIT:** Plain `LIMIT 1` loses tied sellers and is incorrect unless tie-aware syntax is available.
- **Product join:** It is unnecessary because the measure is `Sales.price`.
- **Multiply by quantity:** Do not do this; price already represents the entire sale.
- **Repeated sale rows:** Every stored row contributes separately to the sum.
- **Several rows for one seller:** Aggregation combines every recorded sale before comparison, so no individual high-priced row can win unless that seller's complete total is globally maximal.
- **One seller:** That seller is automatically the maximum and is returned.
- **Several tied sellers:** `>= ALL` returns every one.
- **Negative prices:** Even if allowed, maximum comparison still works; the schema's intended sale prices are ordinary values.
- **Empty Sales:** No outer group exists, so the result is empty.
- **GROUP BY positional form:** The exact query names `seller_id` directly, avoiding dependence on select position.
- **Any order:** No final sorting is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of `Sales` rows and `G` the number of represented sellers.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
