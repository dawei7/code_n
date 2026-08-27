# Guided Example: Rearrange Products Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 0, "store1": 95, "store2": 100, "store3": 105}, {"product_id": 1, "store1": 70, "store2": null, "store3": 80}]}}`
- **Required output:** `{"columns": ["product_id", "store", "price"], "rows": [[0, "store1", 95], [1, "store1", 70], [0, "store2", 100], [0, "store3", 105], [1, "store3", 80]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "store", "price"], "rows": [[0, "store1", 95], [1, "store1", 70], [0, "store2", 100], [0, "store3", 105], [1, "store3", 80]]}` from `{"tables": {"Products": [{"product_id": 0, "store1": 95, "store2": 100, "store3": 105}, {"product_id": 1, "store1": 70, "store2": null, "store3": 80}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert a wide row into several narrow rows

The input uses a wide representation: one product row has separate `store1`, `store2`, and `store3` price columns. The requested output uses a long representation: every available product-store combination gets its own row with columns `product_id`, `store`, and `price`.

Each source row can therefore generate zero to three output rows:

- `(product_id, 'store1', store1)` when `store1` is not null;
- `(product_id, 'store2', store2)` when `store2` is not null;
- `(product_id, 'store3', store3)` when `store3` is not null.

The protected SQL expresses these three fixed transformations as three `SELECT` branches.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 0, "store1": 95, "store2": 100, "store3": 105}, {"product_id": 1, "store1": 70, "store2": null, "store3": 80}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: One branch per store column

The first branch selects the source `product_id`, the string literal `'store1'` under alias `store`, and the value of column `store1` under alias `price`. Its `WHERE store1 IS NOT NULL` filter removes products unavailable in that store.

The second and third branches repeat the same structure for `store2` and `store3`. The literal store label is essential: after the three price columns are stacked into one `price` column, that label records which original column supplied the value.

All branches return the same number of columns in the same semantic order. SQL set operators combine columns by position, so this structural agreement is required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first branch selects the source `product_id`, the string... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why null checks belong in each branch

A null price means the product is unavailable at that store and must not produce an output row. Filtering independently lets one product appear for its available stores while disappearing only from the unavailable branch.

For product 1 in the example, `store1 = 70` passes the first filter, `store2 = null` fails the second, and `store3 = 80` passes the third. The output consequently includes `(1, 'store1', 70)` and `(1, 'store3', 80)` but no store2 row.

The predicate must use `IS NOT NULL`. SQL null represents unknown or missing information and does not compare normally; expressions such as `store1 != NULL` evaluate to unknown rather than true and would not implement the intended test.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "store", "price"], "rows": [[0, "store1", 95], [1, "store1", 70], [0, "store2", 100], [0, "store3", 105], [1, "store3", 80]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 0, "store1": 95, "store2": 100, "store3": 105}, {"product_id": 1, "store1": 70, "store2": null, "store3": 80}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "store", "price"], "rows": [[0, "store1", 95], [1, "store1", 70], [0, "store2", 100], [0, "store3", 105], [1, "store3", 80]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`UNION ALL`:** The source primary key and dist:** - **`UNION ALL`:** The source primary key and distinct store literals guarantee no duplicate triples, so this avoids unnecessary distinct elimination while returning the same rows.
- **Native `UNPIVOT`:** Engines that support it can express wide-to-long conversion directly, but MySQL compatibility and null behavior must be checked.
- **JSON or dynamic SQL unpivoting:** Useful for a dynamic number of store columns, but unnecessary for the fixed three-column schema.
- **Application-side transformation:** It moves simple relational work out of the database and transfers a wider result than needed.
- **Omit null filters:** This would emit forbidden rows for stores where a product is unavailable.
- **Compare with `NULL` using equality:** `= NULL` and `!= NULL` do not behave as ordinary Boolean comparisons; `IS NOT NULL` is required.
- **Same price in multiple stores:** Both rows must remain because their `store` labels differ.
- **All three prices present:** One source row expands into exactly three output rows.
- **Only one price present:** Only that store's branch emits a row for the product.
- **All prices null:** The product emits no rows, exactly as the availability rule requires.
- **Unique product IDs:** The primary key prevents duplicate source rows for one product.
- **Any result order:** Without `ORDER BY`, row order is intentionally unspecified and accepted.
- **Fixed store schema:** The three explicit branches must be updated if the table later gains another store column.
- **Output-sensitive storage:** Distinct processing can retain up to $K$ triples even though the source scans are linear.
- **Source table unchanged:** The query only projects and filters data; it performs no updates.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K)$. Let $R$ be the number of product rows and $K$ the number of non-null store-price cells in the output, where $0\leq K\leq3R$. The query has three full-table branches. Because three is a fixed constant, their total scan work is $O(R)$.
- **Auxiliary Space Complexity:** $O(K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
