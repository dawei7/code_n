# Guided Example: Dynamic Unpivoting of a Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "LC_Store": 100, "Nozama": null, "Shop": 110, "Souq": null}, {"product_id": 2, "LC_Store": null, "Nozama": 200, "Shop": null, "Souq": 190}, {"product_id": 3, "LC_Store": null, "Nozama": null, "Shop": 1000, "Souq": 1900}]}}`
- **Required output:** `{"columns": ["product_id", "store", "price"], "rows": [[1, "LC_Store", 100], [1, "Shop", 110], [2, "Nozama", 200], [2, "Souq", 190], [3, "Shop", 1000], [3, "Souq", 1900]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "store", "price"], "rows": [[1, "LC_Store", 100], [1, "Shop", 110], [2, "Nozama", 200], [2, "Souq", 190], [3, "Shop", 1000], [3, "Souq", 1900]]}` from `{"tables": {"Products": [{"product_id": 1, "LC_Store": 100, "Nozama": null, "Shop": 110, "Souq": null}, {"product_id": 2, "LC_Store": null, "Nozama": 200, "Shop": null, "Souq": 190}, {"product_id": 3, "LC_Store": null, "Nozama": null, "Shop": 1000, "Souq": 1900}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why column discovery is necessary

The source table has one row per product and one price column per store. Store column names change between test cases, so a static query cannot write one branch for each store in advance.

The procedure queries database metadata to discover every current store column, generates a `SELECT` for each, joins those branches with `UNION`, then prepares and executes the resulting SQL.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "LC_Store": 100, "Nozama": null, "Shop": 110, "Souq": null}, {"product_id": 2, "LC_Store": null, "Nozama": 200, "Shop": null, "Souq": 190}, {"product_id": 3, "LC_Store": null, "Nozama": null, "Shop": 1000, "Souq": 1900}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read store columns from `information_schema`

The CTE `t` selects `column_name` from `information_schema.columns` with three filters:

- `table_schema = DATABASE()` restricts metadata to the active database;
- `table_name = 'Products'` restricts it to the source table;
- `column_name != 'product_id'` excludes the identifier column.

Every remaining column is a store-price column by the supplied schema. There is at least one, so the generated query is nonempty.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The CTE `t` selects `column_name` from `information_schema.c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Generate one long-form projection per store

For a discovered column named `S`, the generated branch has this logical form:

`SELECT product_id, 'S' store, S price FROM Products WHERE S IS NOT NULL`.

It transforms each non-null cell of column `S` into a row:

- the existing product ID;
- the literal store name `S`;
- that cell's price.

The `WHERE` clause omits null cells, which represent products not sold in that store.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "store", "price"], "rows": [[1, "LC_Store", 100], [1, "Shop", 110], [2, "Nozama", 200], [2, "Souq", 190], [3, "Shop", 1000], [3, "Souq", 1900]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "LC_Store": 100, "Nozama": null, "Shop": 110, "Souq": null}, {"product_id": 2, "LC_Store": null, "Nozama": 200, "Shop": null, "Souq": 190}, {"product_id": 3, "LC_Store": null, "Nozama": null, "Shop": 1000, "Souq": 1900}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "store", "price"], "rows": [[1, "LC_Store", 100], [1, "Shop", 110], [2, "Nozama", 200], [2, "Souq", 190], [3, "Shop", 1000], [3, "Souq", 1900]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Static `UNION ALL` branches:** Simpler when st:** - **Static `UNION ALL` branches:** Simpler when store columns are fixed, but invalid when names change dynamically.
- **Application-side unpivoting:** It moves transformation outside SQL and does not implement the requested stored procedure.
- **Use `UNION ALL` dynamically:** It would be sufficient and may avoid deduplication because generated triples are inherently distinct; the exact solution uses `UNION`.
- **Null price:** The branch predicate omits that product-store combination entirely.
- **Zero price:** Zero is not null and is correctly emitted.
- **One store column:** The generated statement contains one select and no meaningful separator.
- **Maximum thirty stores:** Increasing `group_concat_max_len` protects the longer generated text.
- **Product unavailable everywhere:** Its row emits no long-form result.
- **Any result order:** Neither metadata ordering nor a final `ORDER BY` is required.
- **Active database filter:** It avoids accidentally discovering a same-named table in another schema.
- **Exclude `product_id`:** Treating it as a store would create invalid rows; the metadata predicate prevents that.
- **Prepared-resource cleanup:** The statement is explicitly deallocated after execution.
- **Generated identifier safety:** Store names come from actual metadata column identifiers and are inserted unquoted into the dynamic statement. The source relies on the supplied schema using names valid in that position.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let `r` be the number of product rows and `s` the number of store columns, with `1 <= s <= 30`. Metadata discovery processes `O(s)` columns. The generated union contains `s` branches, each scanning `r` rows, for `O(rs)` logical row work.
- **Auxiliary Space Complexity:** $O(rs)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
