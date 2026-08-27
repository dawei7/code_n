# Guided Example: Product's Price for Each Store

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 0, "store": "store1", "price": 95}, {"product_id": 0, "store": "store3", "price": 105}, {"product_id": 0, "store": "store2", "price": 100}, {"product_id": 1, "store": "store1", "price": 70}, {"product_id": 1, "store": "store3", "price": 80}]}}`
- **Required output:** `{"columns": ["product_id", "store1", "store2", "store3"], "rows": [[0, 95, 100, 105], [1, 70, null, 80]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "store1", "store2", "store3"], "rows": [[0, 95, 100, 105], [1, 70, null, 80]]}` from `{"tables": {"Products": [{"product_id": 0, "store": "store1", "price": 95}, {"product_id": 0, "store": "store3", "price": 105}, {"product_id": 0, "store": "store2", "price": 100}, {"product_id": 1, "store": "store1", "price": 70}, {"product_id": 1, "store": "store3", "price": 80}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Pivot store rows into store columns

`Products` is in long form: each row describes one product at one store. The requested result is wide form: one row per `product_id` with separate `store1`, `store2`, and `store3` price columns.

The exact SQL query uses conditional aggregation. It groups all rows of one product, conditionally exposes the price for each store, and aggregates that exposed value into its output column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 0, "store": "store1", "price": 95}, {"product_id": 0, "store": "store3", "price": 105}, {"product_id": 0, "store": "store2", "price": 100}, {"product_id": 1, "store": "store1", "price": 70}, {"product_id": 1, "store": "store3", "price": 80}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one conditional value per store

For store one, the expression is:

`IF(store = 'store1', price, NULL)`.

On the product's `store1` row, it returns that row's price. On rows for other stores, it returns null. The query repeats the same structure for `store2` and `store3`.

Using null rather than zero matters. Zero would assert a price of zero for nonmatching rows and could make a missing store look present. Null represents the absence of a matching store row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For store one, the expression is:

`IF(store = 'store1', pri... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why SUM acts as a pivot selector

Each conditional expression is wrapped in `SUM`. The primary key `(product_id, store)` guarantees at most one row for a particular product-store pair.

Within one product group, the conditional values for a store are therefore either:

- one real price plus nulls from other store rows, or
- only nulls when that product is unavailable at the store.

SQL aggregate `SUM` ignores null inputs. In the first case, the sum equals the single real price. In the second case, summing an all-null set returns null, exactly the desired missing-store output.

Because uniqueness guarantees only one price, `MAX` or `MIN` would behave equivalently. `SUM` is correct here as a selector, not because multiple store prices need addition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "store1", "store2", "store3"], "rows": [[0, 95, 100, 105], [1, 70, null, 80]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 0, "store": "store1", "price": 95}, {"product_id": 0, "store": "store3", "price": 105}, {"product_id": 0, "store": "store2", "price": 100}, {"product_id": 1, "store": "store1", "price": 70}, {"product_id": 1, "store": "store3", "price": 80}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "store1", "store2", "store3"], "rows": [[0, 95, 100, 105], [1, 70, null, 80]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **MAX with CASE:** `MAX(CASE WHEN store = 'store:** - **MAX with CASE:** `MAX(CASE WHEN store = 'store1' THEN price END)` is the conventional portable equivalent.
- **Self-join per store:** It can pivot columns but requires outer joins to preserve products missing a store.
- **Native PIVOT operator:** Some database systems support it, but MySQL conditional aggregation is broadly applicable.
- **Missing store:** All conditional inputs are null and `SUM` returns null.
- **All stores present:** Each output store column receives its unique price.
- **Only one store present:** The product row remains, with two null columns.
- **Primary-key uniqueness:** It makes sum equal selection rather than addition of multiple observations.
- **Price zero:** If allowed, it would remain distinguishable from null; the query does not substitute zero for missing.
- **Ordinal grouping:** `GROUP BY 1` depends on `product_id` remaining the first selected expression.
- **Any result order:** No ordering clause is required.
- **Different products at same store:** Product grouping keeps their prices separate.
- **Null aggregate semantics:** `SUM` ignores nulls but returns null when there is no non-null value.
- **Fixed enum domain:** Exactly three conditional columns cover every possible store.
- **No input mutation:** The query reads and reshapes rows without updating `Products`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of input rows and $P$ the number of distinct products. With hash aggregation, the database scans each row once, evaluates three constant-time conditions, and updates one product group, for expected $O(R)$ time.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
