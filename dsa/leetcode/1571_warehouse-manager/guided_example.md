# Guided Example: Warehouse Manager

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Warehouse": [{"name": "LCHouse1", "product_id": 1, "units": 1}, {"name": "LCHouse1", "product_id": 2, "units": 10}, {"name": "LCHouse1", "product_id": 3, "units": 5}, {"name": "LCHouse2", "product_id": 1, "units": 2}, {"name": "LCHouse2", "product_id": 2, "units": 2}, {"name": "LCHouse3", "product_id": 4, "units": 1}], "Products": [{"product_id": 1, "product_name": "LC-TV", "Width": 5, "Length": 50, "Height": 40}, {"product_id": 2, "product_name": "LC-KeyChain", "Width": 5, "Length": 5, "Height": 5}, {"product_id": 3, "product_name": "LC-Phone", "Width": 2, "Length": 10, "Height": 10}, {"product_id": 4, "product_name": "LC-T-Shirt", "Width": 4, "Length": 10, "Height": 20}]}}`
- **Required output:** `{"columns": ["warehouse_name", "volume"], "rows": [["LCHouse1", 12250], ["LCHouse2", 20250], ["LCHouse3", 800]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Warehouse`

The objective is to compute `{"columns": ["warehouse_name", "volume"], "rows": [["LCHouse1", 12250], ["LCHouse2", 20250], ["LCHouse3", 800]]}` from `{"tables": {"Warehouse": [{"name": "LCHouse1", "product_id": 1, "units": 1}, {"name": "LCHouse1", "product_id": 2, "units": 10}, {"name": "LCHouse1", "product_id": 3, "units": 5}, {"name": "LCHouse2", "product_id": 1, "units": 2}, {"name": "LCHouse2", "product_id": 2, "units": 2}, {"name": "LCHouse3", "product_id": 4, "units": 1}], "Products": [{"product_id": 1, "product_name": "LC-TV", "Width": 5, "Length": 50, "Height": 40}, {"product_id": 2, "product_name": "LC-KeyChain", "Width": 5, "Length": 5, "Height": 5}, {"product_id": 3, "product_name": "LC-Phone", "Width": 2, "Length": 10, "Height": 10}, {"product_id": 4, "product_name": "LC-T-Shirt", "Width": 4, "Length": 10, "Height": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute volume at inventory-row granularity

One unit of a product occupies:

`width * length * height`

cubic feet. A warehouse inventory row stores `units` copies, so that row's complete occupied volume is:

`width * length * height * units`.

The query computes this expression after joining each inventory row to the dimensions of its product.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Warehouse": [{"name": "LCHouse1", "product_id": 1, "units": 1}, {"name": "LCHouse1", "product_id": 2, "units": 10}, {"name": "LCHouse1", "product_id": 3, "units": 5}, {"name": "LCHouse2", "product_id": 1, "units": 2}, {"name": "LCHouse2", "product_id": 2, "units": 2}, {"name": "LCHouse3", "product_id": 4, "units": 1}], "Products": [{"product_id": 1, "product_name": "LC-TV", "Width": 5, "Length": 50, "Height": 40}, {"product_id": 2, "product_name": "LC-KeyChain", "Width": 5, "Length": 5, "Height": 5}, {"product_id": 3, "product_name": "LC-Phone", "Width": 2, "Length": 10, "Height": 10}, {"product_id": 4, "product_name": "LC-T-Shirt", "Width": 4, "Length": 10, "Height": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Join inventory to product dimensions

`Warehouse` knows warehouse name, product identifier, and unit count. `Products` knows the three dimensions.

`JOIN Products USING (product_id)` matches rows with the same product identifier and exposes both the unit count and dimensions in one joined row.

Because `product_id` is unique in `Products`, one warehouse inventory row matches at most one dimensions row. The join therefore does not multiply inventory facts.

`USING` also represents the shared product identifier as one join-key column, though the final result does not need to project it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why multiplication occurs inside SUM

A warehouse can store several products with different dimensions and quantities. Total volume is additive across inventory rows.

`SUM(width * length * height * units)` first computes each row's occupied volume, then adds those values within the warehouse group.

Multiplying a sum of units by one arbitrary product volume would be wrong because products do not share dimensions. Row-level multiplication must precede cross-product aggregation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["warehouse_name", "volume"], "rows": [["LCHouse1", 12250], ["LCHouse2", 20250], ["LCHouse3", 800]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Warehouse": [{"name": "LCHouse1", "product_id": 1, "units": 1}, {"name": "LCHouse1", "product_id": 2, "units": 10}, {"name": "LCHouse1", "product_id": 3, "units": 5}, {"name": "LCHouse2", "product_id": 1, "units": 2}, {"name": "LCHouse2", "product_id": 2, "units": 2}, {"name": "LCHouse3", "product_id": 4, "units": 1}], "Products": [{"product_id": 1, "product_name": "LC-TV", "Width": 5, "Length": 50, "Height": 40}, {"product_id": 2, "product_name": "LC-KeyChain", "Width": 5, "Length": 5, "Height": 5}, {"product_id": 3, "product_name": "LC-Phone", "Width": 2, "Length": 10, "Height": 10}, {"product_id": 4, "product_name": "LC-T-Shirt", "Width": 4, "Length": 10, "Height": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["warehouse_name", "volume"], "rows": [["LCHouse1", 12250], ["LCHouse2", 20250], ["LCHouse3", 800]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precompute unit volume in a subquery:** Join `Warehouse` to `product_id, width*length*height` and then multiply by units. It is relationally equivalent.
- **Left join:** It preserves unmatched inventory rows but would require deciding how null dimensions should affect volume.
- **Aggregate units before joining:** Group by warehouse and product first, then join dimensions; it is useful only if multiple rows per pair are possible.
- **Sum units alone:** It is wrong because products occupy different volume per unit.
- **Multiply after SUM:** It is wrong unless every grouped row has identical dimensions.
- **One product in a warehouse:** Its row contribution is the warehouse total.
- **Several products:** Each row's independently computed contribution is added.
- **Several warehouses carrying one product:** The same dimensions join to each inventory row, while grouping keeps names separate.
- **No ORDER BY:** It is valid because result ordering is unrestricted.
- **Composite primary key:** It prevents duplicate warehouse-product inventory rows.
- **Unique product key:** It prevents a join from duplicating one inventory row.
- **Product name:** It is irrelevant to physical volume and intentionally not selected.
- **Positional GROUP BY:** `GROUP BY 1` depends on warehouse name remaining the first selected expression.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W \log W)$. Let $W$ be the number of warehouse inventory rows and $P$ the number of product rows.
- **Auxiliary Space Complexity:** $O(W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
