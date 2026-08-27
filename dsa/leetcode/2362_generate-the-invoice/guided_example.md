# Guided Example: Generate the Invoice

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "price": 100}, {"product_id": 2, "price": 200}], "Purchases": [{"invoice_id": 1, "product_id": 1, "quantity": 2}, {"invoice_id": 3, "product_id": 2, "quantity": 1}, {"invoice_id": 2, "product_id": 2, "quantity": 3}, {"invoice_id": 2, "product_id": 1, "quantity": 4}, {"invoice_id": 4, "product_id": 1, "quantity": 10}]}}`
- **Required output:** `{"columns": ["product_id", "quantity", "price"], "rows": [[1, 4, 400], [2, 3, 600]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "quantity", "price"], "rows": [[1, 4, 400], [2, 3, 600]]}` from `{"tables": {"Products": [{"product_id": 1, "price": 100}, {"product_id": 2, "price": 200}], "Purchases": [{"invoice_id": 1, "product_id": 1, "quantity": 2}, {"invoice_id": 3, "product_id": 2, "quantity": 1}, {"invoice_id": 2, "product_id": 2, "quantity": 3}, {"invoice_id": 2, "product_id": 1, "quantity": 4}, {"invoice_id": 4, "product_id": 1, "quantity": 10}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate invoice selection from line-item output

The requested result is not one summary row. It is every purchased product line belonging to the winning invoice, with each line's extended price. Before those lines can be returned, the query must determine which invoice has the largest *total* value. The solution uses two common table expressions to separate these stages:

- `P` enriches every purchase line with its product's unit price.
- `T` aggregates those enriched lines, orders invoice totals according to the rules, and keeps the single winning invoice.

The final query joins the winner back to `P` to recover all of its detail rows.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "price": 100}, {"product_id": 2, "price": 200}], "Purchases": [{"invoice_id": 1, "product_id": 1, "quantity": 2}, {"invoice_id": 3, "product_id": 2, "quantity": 1}, {"invoice_id": 2, "product_id": 2, "quantity": 3}, {"invoice_id": 2, "product_id": 1, "quantity": 4}, {"invoice_id": 4, "product_id": 1, "quantity": 10}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enrich each purchase with its unit price

`Purchases` contains `invoice_id`, `product_id`, and `quantity`, but the unit `price` lives in `Products`. The first CTE performs:



An inner join is appropriate because each purchase line refers to a product whose price is required. `USING (product_id)` matches equal identifiers and exposes one shared `product_id` column rather than two separately qualified copies.

After this join, every logical row in `P` has the invoice, product, quantity, and unit price needed for both total calculation and final output. The name `P` is local to the SQL query; it should not be confused with a complexity variable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `Purchases` contains `invoice_id`, `product_id`, and `quanti... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute one total per invoice

For one purchase row, `price * quantity` is the total price of that product line. Summing this product over all rows sharing an invoice gives that invoice's full amount:



Grouping only by `invoice_id` is correct because the goal at this stage is one total per invoice, not one total per product. The source table's primary key `(invoice_id, product_id)` guarantees at most one line for a particular product within an invoice, though the sum would remain correct even if lines were repeated.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "quantity", "price"], "rows": [[1, 4, 400], [2, 3, 600]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "price": 100}, {"product_id": 2, "price": 200}], "Purchases": [{"invoice_id": 1, "product_id": 1, "quantity": 2}, {"invoice_id": 3, "product_id": 2, "quantity": 1}, {"invoice_id": 2, "product_id": 2, "quantity": 3}, {"invoice_id": 2, "product_id": 1, "quantity": 4}, {"invoice_id": 4, "product_id": 1, "quantity": 10}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "quantity", "price"], "rows": [[1, 4, 400], [2, 3, 600]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window functions:** Compute invoice totals wit:** - **Window functions:** Compute invoice totals with a window sum and rank invoices, then filter the winning rank. This can be correct but may repeat totals on every detail row and requires careful tie ordering.
- **Correlated subqueries:** Recomputing totals while filtering individual lines is usually harder to read and may repeat aggregation work.
- **`MAX(amount)` alone:** It identifies the highest total but does not select the smallest `invoice_id` among ties without additional logic.
- **Tie between invoices:** `ORDER BY amount DESC, invoice_id` guarantees that the smallest identifier wins.
- **One invoice only:** Its aggregate row is first automatically, and all its detail lines are returned.
- **One product line in the winner:** The invoice total and returned line price are the same `quantity * price` value.
- **Products absent from purchases:** The inner join contributes no rows for them, which is correct because they belong to no invoice.
- **Output ordering:** The final rows are intentionally unordered because any order is accepted.
- **Unit versus extended price:** The source `Products.price` is per unit; the returned `price` is multiplied by `quantity` for that invoice line.
- **Positional ordering references:** `2` means `amount` and `1` means `invoice_id` within CTE `T`; they are not numeric constants used to rank every row equally.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N_P+N_R)$. Let $N_P$ be the number of rows in `Products` and $N_R$ the number of rows in `Purchases`. The variant manifest states $O((N_P+N_R)\log(N_P+N_R))$ time and $O(N_P+N_R)$ space.
- **Auxiliary Space Complexity:** $O(P+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
