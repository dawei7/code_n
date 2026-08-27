# Guided Example: Product Sales Analysis I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}], "Product": [{"product_id": 100, "product_name": "Nokia"}, {"product_id": 200, "product_name": "Apple"}, {"product_id": 300, "product_name": "Samsung"}]}}`
- **Required output:** `{"columns": ["product_name", "year", "price"], "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sales`

The objective is to compute `{"columns": ["product_name", "year", "price"], "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]]}` from `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}], "Product": [{"product_id": 100, "product_name": "Nokia"}, {"product_id": 200, "product_name": "Apple"}, {"product_id": 300, "product_name": "Samsung"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify which table owns each requested column

The output needs `product_name`, `year`, and `price` for every row in `Sales`.

`year` and `price` are already stored in `Sales`. The readable `product_name` is stored in `Product`. Both tables share `product_id`:

- `Sales.product_id` is a foreign key referencing `Product.product_id`.
- `Product.product_id` is a primary key, so at most one product row matches any product identifier.

This is a direct relational join problem. Each sale row must be paired with its one referenced product row so the result can combine sales facts with the product name.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}], "Product": [{"product_id": 100, "product_name": "Nokia"}, {"product_id": 200, "product_name": "Apple"}, {"product_id": 300, "product_name": "Samsung"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use an inner join on the common key

The query's source is:



In MySQL, bare `JOIN` means `INNER JOIN`. Only row pairs whose `product_id` values are equal survive.

`USING (product_id)` is concise syntax for an equality join when both tables use the same column name. It corresponds to:



and exposes the join key as one merged output column rather than two separately named copies.

The foreign-key contract guarantees that every `Sales` row references an existing product. Therefore, no sale is lost through the inner join.

The primary-key contract on `Product.product_id` guarantees exactly one matching product row for a referenced identifier. Therefore, the join does not multiply one sale into several result rows.

Together, those constraints establish a one-to-one relationship from each sale row to its joined result row, even though one product can appear in many different sales.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query's source is:



In MySQL, bare `JOIN` means `INNER... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Project only the required attributes

The select list is:



`product_name` exists only in `Product`, while `year` and `price` exist only in `Sales`, so these unqualified names are unambiguous.

Other columns are intentionally omitted:

- `sale_id` identifies the source sale but is not requested.
- `product_id` performs the join but is not requested in the output.
- `quantity` does not affect the requested per-unit price and year.

Projection does not merge equal rows. If two distinct sales happen to have the same product name, year, and price, SQL returns two identical-looking result rows because there is no `DISTINCT`. That is correct: the requirement asks for one result for each `sale_id`, even though `sale_id` itself is not displayed.

Adding `DISTINCT` would be a semantic bug because it could collapse separate sales into one row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_name", "year", "price"], "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sales": [{"sale_id": 1, "product_id": 100, "year": 2008, "quantity": 10, "price": 5000}, {"sale_id": 2, "product_id": 100, "year": 2009, "quantity": 12, "price": 5000}, {"sale_id": 7, "product_id": 200, "year": 2011, "quantity": 15, "price": 9000}], "Product": [{"product_id": 100, "product_name": "Nokia"}, {"product_id": 200, "product_name": "Apple"}, {"product_id": 300, "product_name": "Samsung"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_name", "year", "price"], "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit ON syntax:** `JOIN Product ON Sales.p:** - **Explicit ON syntax:** `JOIN Product ON Sales.product_id = Product.product_id` is semantically equivalent and can be clearer when key names differ or table aliases are used.
- **Correlated scalar subquery:** Looking up the product name separately for each sale can produce the same result, but it is less direct and may lead to repeated index probes.
- **Left join:** It is unnecessary because every sale has a valid product foreign key. Starting from products with a left join could also introduce catalog rows with no sale.
- **DISTINCT:** Do not add it. Separate sale rows may project to identical visible values and must remain separate.
- **Product with many sales:** The product name appears once for each matching sale, preserving the required per-sale grain.
- **Product with no sales:** It contributes no row because the output is driven by `Sales`.
- **Same product and year across sales:** Each sale remains a separate joined row, even when all selected values are identical.
- **Composite Sales primary key:** Uniqueness of `(sale_id, year)` identifies sale records but is not needed as a join key; `product_id` is the relational link to `Product`.
- **Per-unit price:** The query selects `price` directly and does not multiply it by `quantity`.
- **Any result order:** Omitting `ORDER BY` is correct and avoids implying an unsupported ordering contract.
- **USING column behavior:** `USING (product_id)` requires the same key name in both tables and merges that key in the joined namespace.
- **Null key concerns:** The foreign-key description supplies referenced product identifiers. Under the stated schema, every sale has its corresponding product.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P)$. Let `R` be the number of rows in `Sales` and `P` the number of rows in `Product`.
- **Auxiliary Space Complexity:** $O(P+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
