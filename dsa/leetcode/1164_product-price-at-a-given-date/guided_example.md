# Guided Example: Product Price at a Given Date

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "new_price": 20, "change_date": "2019-08-14"}, {"product_id": 2, "new_price": 50, "change_date": "2019-08-14"}, {"product_id": 1, "new_price": 30, "change_date": "2019-08-15"}, {"product_id": 1, "new_price": 35, "change_date": "2019-08-16"}, {"product_id": 2, "new_price": 65, "change_date": "2019-08-17"}, {"product_id": 3, "new_price": 20, "change_date": "2019-08-18"}]}}`
- **Required output:** `{"columns": ["product_id", "price"], "rows": [[1, 35], [2, 50], [3, 10]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "price"], "rows": [[1, 35], [2, 50], [3, 10]]}` from `{"tables": {"Products": [{"product_id": 1, "new_price": 20, "change_date": "2019-08-14"}, {"product_id": 2, "new_price": 50, "change_date": "2019-08-14"}, {"product_id": 1, "new_price": 30, "change_date": "2019-08-15"}, {"product_id": 1, "new_price": 35, "change_date": "2019-08-16"}, {"product_id": 2, "new_price": 65, "change_date": "2019-08-17"}, {"product_id": 3, "new_price": 20, "change_date": "2019-08-18"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every product must appear, even without an earlier change

The `Products` table is a history of price changes rather than a separate product catalog. A product may have only rows dated after `2019-08-16`, but it still needs an output row with the initial price ten.

The first common table expression,

`T AS (SELECT DISTINCT product_id FROM Products)`,

extracts the complete product population from all history rows, regardless of date. `DISTINCT` gives exactly one row per product identifier.

Starting the final query from `T` ensures future-only products are not lost when the solution searches for changes on or before the report date.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "new_price": 20, "change_date": "2019-08-14"}, {"product_id": 2, "new_price": 50, "change_date": "2019-08-14"}, {"product_id": 1, "new_price": 30, "change_date": "2019-08-15"}, {"product_id": 1, "new_price": 35, "change_date": "2019-08-16"}, {"product_id": 2, "new_price": 65, "change_date": "2019-08-17"}, {"product_id": 3, "new_price": 20, "change_date": "2019-08-18"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the latest applicable date for each product

A price change remains effective until a later change replaces it. Therefore, the price on `2019-08-16` comes from the greatest `change_date` that is no later than that date.

The grouped subquery filters to

`change_date <= '2019-08-16'`

and computes `MAX(change_date)` per `product_id`. This yields one key pair for every product that has an applicable change:

`(product_id, latest_applicable_date)`.

A change on the report date itself is included because the comparison is `<=`. Changes after that date are excluded and cannot affect the historical price.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Retrieve the price attached to that date

The second CTE `P` filters `Products` with a row-value membership test:

`(product_id, change_date) IN (...)`.

Only a row whose product and date together match one of the grouped latest-date pairs survives. It projects `new_price AS price`.

The composite primary key `(product_id, change_date)` guarantees at most one price-change row for that product on that date. Therefore, each product contributes at most one row to `P`, and the selected `new_price` is unambiguous.

It would not be sufficient to compare `change_date` with one global maximum date. Different products can have their most recent applicable changes on different days, so the maximum must be grouped by product.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "price"], "rows": [[1, 35], [2, 50], [3, 10]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "new_price": 20, "change_date": "2019-08-14"}, {"product_id": 2, "new_price": 50, "change_date": "2019-08-14"}, {"product_id": 1, "new_price": 30, "change_date": "2019-08-15"}, {"product_id": 1, "new_price": 35, "change_date": "2019-08-16"}, {"product_id": 2, "new_price": 65, "change_date": "2019-08-17"}, {"product_id": 3, "new_price": 20, "change_date": "2019-08-18"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "price"], "rows": [[1, 35], [2, 50], [3, 10]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use a window function:** Ranking each product's rows by date descending after filtering and keeping rank one also finds the latest applicable price. A separate all-product base is still needed for future-only products.
- **Use correlated subqueries:** For each product, a subquery can order applicable changes descending and take one. This can be concise but may repeat lookup work without suitable indexes.
- **Use `UNION ALL` for changed and unchanged products:** One branch can return latest prices and another initial tens. The left-join formulation expresses the two cases in one final projection.
- **Start only from filtered rows:** Products with no change by the report date disappear instead of receiving price ten.
- **Use a global maximum date:** Products have independent histories, so their latest applicable dates must be grouped separately.
- **Change exactly on `2019-08-16`:** It is included and becomes effective that day.
- **Only future changes:** The product appears through `T` and receives the initial price ten.
- **Earlier and future changes:** The latest earlier row is selected; the future row is ignored.
- **Several earlier changes:** `MAX(change_date)` selects only the most recent effective one.
- **Composite primary key:** It guarantees one price for a product-date pair, preventing ambiguity in `P`.
- **Any result order:** The query intentionally omits sorting because the contract allows it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of rows in `Products`. Distinct product extraction, date filtering, grouped maximum calculation, and the joins may be implemented with sorting or hashing. Under the manifest's conservative sort-based view, time is `O(r log r)` and intermediate storage is `O(r)`.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
