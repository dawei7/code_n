# Guided Example: Dynamic Pivoting of a Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "store": "Shop", "price": 110}, {"product_id": 1, "store": "LC_Store", "price": 100}, {"product_id": 2, "store": "Nozama", "price": 200}, {"product_id": 2, "store": "Souq", "price": 190}, {"product_id": 3, "store": "Shop", "price": 1000}, {"product_id": 3, "store": "Souq", "price": 1900}]}}`
- **Required output:** `{"columns": ["product_id", "LC_Store", "Nozama", "Shop", "Souq"], "rows": [[1, 100, null, 110, null], [2, null, 200, null, 190], [3, null, null, 1000, 1900]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "LC_Store", "Nozama", "Shop", "Souq"], "rows": [[1, 100, null, 110, null], [2, null, 200, null, 190], [3, null, null, 1000, 1900]]}` from `{"tables": {"Products": [{"product_id": 1, "store": "Shop", "price": 110}, {"product_id": 1, "store": "LC_Store", "price": 100}, {"product_id": 2, "store": "Nozama", "price": 200}, {"product_id": 2, "store": "Souq", "price": 190}, {"product_id": 3, "store": "Shop", "price": 1000}, {"product_id": 3, "store": "Souq", "price": 1900}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why this pivot must be dynamic

The input stores one product-store price per row, but the output needs one product per row and one column per store. Store names can change between test cases, so a fixed query cannot name all output columns in advance.

The procedure first discovers the current stores and builds a SQL query as text. It then prepares and executes that text. This is dynamic SQL: table data determines the query's selected columns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "store": "Shop", "price": 110}, {"product_id": 1, "store": "LC_Store", "price": 100}, {"product_id": 2, "store": "Nozama", "price": 200}, {"product_id": 2, "store": "Souq", "price": 190}, {"product_id": 3, "store": "Shop", "price": 1000}, {"product_id": 3, "store": "Souq", "price": 1900}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build one conditional aggregate per store

For store name `S`, the generated fragment has the logical form:

`MAX(CASE WHEN store = 'S' THEN price ELSE NULL END) AS S`.

Within all rows for one product, the `CASE` returns that product's price on the row for store `S` and `NULL` on other-store rows. The primary key `(product_id, store)` guarantees at most one matching price row.

`MAX` ignores nulls and returns the one price when present. If the product is not sold in `S`, every case result is null and the aggregate returns null, exactly as required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Discover, deduplicate, and order store expressions

The first `SELECT` reads `Products` and feeds store values into `STRING_AGG`. `DISTINCT` creates only one expression per store even though many products may be sold there.

`ORDER BY store` inside the aggregation arranges fragments lexicographically by store name. Since those fragments become output columns in that order, the dynamic table satisfies the required lexicographical column ordering.

The resulting comma-separated expression list is assigned to session variable `@sql`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "LC_Store", "Nozama", "Shop", "Souq"], "rows": [[1, 100, null, 110, null], [2, null, 200, null, 190], [3, null, null, 1000, 1900]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "store": "Shop", "price": 110}, {"product_id": 1, "store": "LC_Store", "price": 100}, {"product_id": 2, "store": "Nozama", "price": 200}, {"product_id": 2, "store": "Souq", "price": 190}, {"product_id": 3, "store": "Shop", "price": 1000}, {"product_id": 3, "store": "Souq", "price": 1900}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "LC_Store", "Nozama", "Shop", "Souq"], "rows": [[1, 100, null, 110, null], [2, null, 200, null, 190], [3, null, null, 1000, 1900]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Static conditional aggregation:** It works only when store names are known ahead of time; this problem changes them by test case.
- **Return rows without pivoting:** That preserves the source shape and fails the required one-column-per-store output.
- **Self-join once per known store:** It is also static and becomes unwieldy as store sets change.
- **Missing product-store pair:** All case values are null, so the pivot cell is null.
- **One store:** The generated query has one dynamic price column.
- **Many products in one store:** `DISTINCT` generates the store column once.
- **Primary-key guarantee:** It ensures at most one non-null price per product-store aggregate.
- **Lexicographical columns:** Ordering belongs inside dynamic expression aggregation; output row ordering is irrelevant.
- **Generated-string length:** Raising `group_concat_max_len` prevents silent truncation of the statement.
- **Prepared-resource cleanup:** `DEALLOCATE PREPARE` releases the statement after execution.
- **Any row order:** No final `ORDER BY product_id` is necessary.
- **Null behavior:** `MAX` ignores nulls but returns null when all values in the group are null.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let `r` be the number of product-store rows and `s` the number of distinct stores, with `s <= 30`. Discovering stores scans `O(r)` data and orders at most thirty store names. Executing the grouped conditional-aggregation query scans `O(r)` rows and evaluates `s` bounded expressions per row.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
