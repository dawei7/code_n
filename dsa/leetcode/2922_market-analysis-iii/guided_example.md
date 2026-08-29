# Guided Example: Market Analysis III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"seller_id": 1, "join_date": "2019-01-01", "favorite_brand": "Lenovo"}, {"seller_id": 2, "join_date": "2019-02-09", "favorite_brand": "Samsung"}, {"seller_id": 3, "join_date": "2019-01-19", "favorite_brand": "LG"}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "seller_id": 2}, {"order_id": 2, "order_date": "2019-08-02", "item_id": 2, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "seller_id": 3}, {"order_id": 4, "order_date": "2019-08-04", "item_id": 1, "seller_id": 2}, {"order_id": 5, "order_date": "2019-08-04", "item_id": 4, "seller_id": 2}]}}`
- **Required output:** `{"columns": ["seller_id", "num_items"], "rows": [[2, 1], [3, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["seller_id", "num_items"], "rows": [[2, 1], [3, 1]]}` from `{"tables": {"Users": [{"seller_id": 1, "join_date": "2019-01-01", "favorite_brand": "Lenovo"}, {"seller_id": 2, "join_date": "2019-02-09", "favorite_brand": "Samsung"}, {"seller_id": 3, "join_date": "2019-01-19", "favorite_brand": "LG"}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "seller_id": 2}, {"order_id": 2, "order_date": "2019-08-02", "item_id": 2, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "seller_id": 3}, {"order_id": 4, "order_date": "2019-08-04", "item_id": 1, "seller_id": 2}, {"order_id": 5, "order_date": "2019-08-04", "item_id": 4, "seller_id": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Join each order to both required descriptions

`Orders` contains `seller_id` and `item_id` but not either brand. The query joins:

- `Orders JOIN Users USING (seller_id)` to obtain `favorite_brand`;
- `JOIN Items USING (item_id)` to obtain `item_brand`.

These are inner joins. Under the declared foreign-key relationships, every order's seller and item have matching reference rows, so no legitimate order is lost.

The `USING` syntax also exposes one shared column for each join key instead of duplicate qualified copies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"seller_id": 1, "join_date": "2019-01-01", "favorite_brand": "Lenovo"}, {"seller_id": 2, "join_date": "2019-02-09", "favorite_brand": "Samsung"}, {"seller_id": 3, "join_date": "2019-01-19", "favorite_brand": "LG"}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "seller_id": 2}, {"order_id": 2, "order_date": "2019-08-02", "item_id": 2, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "seller_id": 3}, {"order_id": 4, "order_date": "2019-08-04", "item_id": 1, "seller_id": 2}, {"order_id": 5, "order_date": "2019-08-04", "item_id": 4, "seller_id": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Discard favorite-brand sales

The predicate

`WHERE item_brand != favorite_brand`

keeps only orders whose sold item's brand differs from the seller's favorite. Applying this before grouping ensures favorite-brand orders contribute nothing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count unique items, not order rows

The CTE groups by `seller_id` and calculates

`COUNT(DISTINCT item_id) AS num_items`.

`DISTINCT` is essential. If a seller has several orders for the same non-favorite item identifier, that item must contribute one, not the number of sales. Different item identifiers count separately even if their brands are equal, because the requested uniqueness is about items.

After this aggregation, `T` contains one row per seller who has at least one qualifying non-favorite item, paired with that seller's distinct count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["seller_id", "num_items"], "rows": [[2, 1], [3, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"seller_id": 1, "join_date": "2019-01-01", "favorite_brand": "Lenovo"}, {"seller_id": 2, "join_date": "2019-02-09", "favorite_brand": "Samsung"}, {"seller_id": 3, "join_date": "2019-01-19", "favorite_brand": "LG"}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "seller_id": 2}, {"order_id": 2, "order_date": "2019-08-02", "item_id": 2, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "seller_id": 3}, {"order_id": 4, "order_date": "2019-08-04", "item_id": 1, "seller_id": 2}, {"order_id": 5, "order_date": "2019-08-04", "item_id": 4, "seller_id": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["seller_id", "num_items"], "rows": [[2, 1], [3, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count every order:** `COUNT(*)` overcounts an item sold multiple times. The exact query correctly uses `COUNT(DISTINCT item_id)`.
- **Count distinct brands:** That would merge different items of the same non-favorite brand and answer a different question.
- **Use `LIMIT 1`:** It loses sellers tied for the maximum and violates the contract.
- **Favorite-brand orders only:** Such a seller is absent from `T` because the filter occurs before grouping.
- **Repeated non-favorite sale:** Multiple orders with the same `item_id` contribute one.
- **Several non-favorite items of one brand:** Each distinct item identifier contributes separately.
- **Inner joins:** They rely on the declared foreign keys. With orphaned external data, unmatched orders would disappear.
- **`NULL` brands:** SQL's `!=` yields unknown when either side is `NULL`, so that row would be filtered. The schema does not describe nullable brands.
- **Output order:** `ORDER BY 1` means ascending `seller_id` because it is the first selected expression.
- **Empty CTE:** The exact source returns no rows because comparing a number with `NULL` is not true.
- **Seller with mixed sales:** Favorite-brand orders are removed, while distinct non-favorite item identifiers remain; the count is not based on the seller's total order volume.
- **Tie comparison after aggregation:** The maximum must be taken over per-seller counts, not over raw orders. The CTE establishes the correct level before the scalar maximum.
- **Date columns:** `join_date` and `order_date` do not affect this question and are correctly unused.
- **Why ties survive:** The scalar subquery returns one maximum count, and ordinary equality retains every seller whose already-aggregated count has that value; it does not arbitrarily select one group.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U+I+O)$. SQL performance depends on indexes and the optimizer. Using $U$, $I$, and $O$ for the sizes of `Users`, `Items`, and `Orders`, the logical work joins the tables, filters orders, groups qualifying rows, performs distinct aggregation, finds a maximum, and sorts $W$ winners.
- **Auxiliary Space Complexity:** $O(U + I + O)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
