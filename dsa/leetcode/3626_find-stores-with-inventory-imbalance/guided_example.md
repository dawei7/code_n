# Guided Example: Find Stores with Inventory Imbalance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"stores": [{"store_id": 1, "store_name": "Downtown Tech", "location": "New York"}, {"store_id": 2, "store_name": "Suburb Mall", "location": "Chicago"}, {"store_id": 3, "store_name": "City Center", "location": "Los Angeles"}, {"store_id": 4, "store_name": "Corner Shop", "location": "Miami"}, {"store_id": 5, "store_name": "Plaza Store", "location": "Seattle"}], "inventory": [{"inventory_id": 1, "store_id": 1, "product_name": "Laptop", "quantity": 5, "price": 999.99}, {"inventory_id": 2, "store_id": 1, "product_name": "Mouse", "quantity": 50, "price": 19.99}, {"inventory_id": 3, "store_id": 1, "product_name": "Keyboard", "quantity": 25, "price": 79.99}, {"inventory_id": 4, "store_id": 1, "product_name": "Monitor", "quantity": 15, "price": 299.99}, {"inventory_id": 5, "store_id": 2, "product_name": "Phone", "quantity": 3, "price": 699.99}, {"inventory_id": 6, "store_id": 2, "product_name": "Charger", "quantity": 100, "price": 25.99}, {"inventory_id": 7, "store_id": 2, "product_name": "Case", "quantity": 75, "price": 15.99}, {"inventory_id": 8, "store_id": 2, "product_name": "Headphones", "quantity": 20, "price": 149.99}, {"inventory_id": 9, "store_id": 3, "product_name": "Tablet", "quantity": 2, "price": 499.99}, {"inventory_id": 10, "store_id": 3, "product_name": "Stylus", "quantity": 80, "price": 29.99}, {"inventory_id": 11, "store_id": 3, "product_name": "Cover", "quantity": 60, "price": 39.99}, {"inventory_id": 12, "store_id": 4, "product_name": "Watch", "quantity": 10, "price": 299.99}, {"inventory_id": 13, "store_id": 4, "product_name": "Band", "quantity": 25, "price": 49.99}, {"inventory_id": 14, "store_id": 5, "product_name": "Camera", "quantity": 8, "price": 599.99}, {"inventory_id": 15, "store_id": 5, "product_name": "Lens", "quantity": 12, "price": 199.99}]}}`
- **Required output:** `{"columns": ["store_id", "store_name", "location", "most_exp_product", "cheapest_product", "imbalance_ratio"], "rows": [[3, "City Center", "Los Angeles", "Tablet", "Stylus", 40], [2, "Suburb Mall", "Chicago", "Phone", "Case", 25], [1, "Downtown Tech", "New York", "Laptop", "Mouse", 10]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `stores`

The objective is to compute `{"columns": ["store_id", "store_name", "location", "most_exp_product", "cheapest_product", "imbalance_ratio"], "rows": [[3, "City Center", "Los Angeles", "Tablet", "Stylus", 40], [2, "Suburb Mall", "Chicago", "Phone", "Case", 25], [1, "Downtown Tech", "New York", "Laptop", "Mouse", 10]]}` from `{"tables": {"stores": [{"store_id": 1, "store_name": "Downtown Tech", "location": "New York"}, {"store_id": 2, "store_name": "Suburb Mall", "location": "Chicago"}, {"store_id": 3, "store_name": "City Center", "location": "Los Angeles"}, {"store_id": 4, "store_name": "Corner Shop", "location": "Miami"}, {"store_id": 5, "store_name": "Plaza Store", "location": "Seattle"}], "inventory": [{"inventory_id": 1, "store_id": 1, "product_name": "Laptop", "quantity": 5, "price": 999.99}, {"inventory_id": 2, "store_id": 1, "product_name": "Mouse", "quantity": 50, "price": 19.99}, {"inventory_id": 3, "store_id": 1, "product_name": "Keyboard", "quantity": 25, "price": 79.99}, {"inventory_id": 4, "store_id": 1, "product_name": "Monitor", "quantity": 15, "price": 299.99}, {"inventory_id": 5, "store_id": 2, "product_name": "Phone", "quantity": 3, "price": 699.99}, {"inventory_id": 6, "store_id": 2, "product_name": "Charger", "quantity": 100, "price": 25.99}, {"inventory_id": 7, "store_id": 2, "product_name": "Case", "quantity": 75, "price": 15.99}, {"inventory_id": 8, "store_id": 2, "product_name": "Headphones", "quantity": 20, "price": 149.99}, {"inventory_id": 9, "store_id": 3, "product_name": "Tablet", "quantity": 2, "price": 499.99}, {"inventory_id": 10, "store_id": 3, "product_name": "Stylus", "quantity": 80, "price": 29.99}, {"inventory_id": 11, "store_id": 3, "product_name": "Cover", "quantity": 60, "price": 39.99}, {"inventory_id": 12, "store_id": 4, "product_name": "Watch", "quantity": 10, "price": 299.99}, {"inventory_id": 13, "store_id": 4, "product_name": "Band", "quantity": 25, "price": 49.99}, {"inventory_id": 14, "store_id": 5, "product_name": "Camera", "quantity": 8, "price": 599.99}, {"inventory_id": 15, "store_id": 5, "product_name": "Lens", "quantity": 12, "price": 199.99}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: CTE `T`: ranking both extremes

Every inventory row retains `store_id`, `product_name`, and `quantity` and receives three window values.

`rk1` uses:

`ORDER BY price DESC, quantity DESC`.

The highest price comes first. If several products share that price, the larger quantity comes first.

`rk2` uses:

`ORDER BY price, quantity DESC`.

The lowest price comes first, again preferring larger quantity among equal prices.

`cnt = COUNT(1) OVER (PARTITION BY store_id)` counts inventory rows for the store.

Window functions are useful because they preserve individual product rows while also attaching per-store ranks and counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"stores": [{"store_id": 1, "store_name": "Downtown Tech", "location": "New York"}, {"store_id": 2, "store_name": "Suburb Mall", "location": "Chicago"}, {"store_id": 3, "store_name": "City Center", "location": "Los Angeles"}, {"store_id": 4, "store_name": "Corner Shop", "location": "Miami"}, {"store_id": 5, "store_name": "Plaza Store", "location": "Seattle"}], "inventory": [{"inventory_id": 1, "store_id": 1, "product_name": "Laptop", "quantity": 5, "price": 999.99}, {"inventory_id": 2, "store_id": 1, "product_name": "Mouse", "quantity": 50, "price": 19.99}, {"inventory_id": 3, "store_id": 1, "product_name": "Keyboard", "quantity": 25, "price": 79.99}, {"inventory_id": 4, "store_id": 1, "product_name": "Monitor", "quantity": 15, "price": 299.99}, {"inventory_id": 5, "store_id": 2, "product_name": "Phone", "quantity": 3, "price": 699.99}, {"inventory_id": 6, "store_id": 2, "product_name": "Charger", "quantity": 100, "price": 25.99}, {"inventory_id": 7, "store_id": 2, "product_name": "Case", "quantity": 75, "price": 15.99}, {"inventory_id": 8, "store_id": 2, "product_name": "Headphones", "quantity": 20, "price": 149.99}, {"inventory_id": 9, "store_id": 3, "product_name": "Tablet", "quantity": 2, "price": 499.99}, {"inventory_id": 10, "store_id": 3, "product_name": "Stylus", "quantity": 80, "price": 29.99}, {"inventory_id": 11, "store_id": 3, "product_name": "Cover", "quantity": 60, "price": 39.99}, {"inventory_id": 12, "store_id": 4, "product_name": "Watch", "quantity": 10, "price": 299.99}, {"inventory_id": 13, "store_id": 4, "product_name": "Band", "quantity": 25, "price": 49.99}, {"inventory_id": 14, "store_id": 5, "product_name": "Camera", "quantity": 8, "price": 599.99}, {"inventory_id": 15, "store_id": 5, "product_name": "Lens", "quantity": 12, "price": 199.99}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `RANK` matters

`RANK` assigns rank 1 to every row tied on the entire ordering tuple.

Different products with the same price but different quantities are not tied because quantity is the secondary key. The one with larger quantity gets rank 1.

If multiple rows have both the same extreme price and same quantity, all receive rank 1. Later joins can then produce several output combinations for one store. The statement does not specify a tie-breaking rule for equally priced products, so deterministic single-row behavior would require another key such as `product_name` or `inventory_id` and usually `ROW_NUMBER`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `RANK` assigns rank 1 to every row tied on the entire orderi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: CTEs `P1` and `P2`

`P1` keeps rows with `rk1=1` and `cnt>=3`. These are candidate most-expensive products for stores passing the size requirement as interpreted by the query.

`P2` keeps every `rk2=1` row, representing candidate cheapest products. It does not repeat the count filter because joining by store with `P1` already restricts the store.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["store_id", "store_name", "location", "most_exp_product", "cheapest_product", "imbalance_ratio"], "rows": [[3, "City Center", "Los Angeles", "Tablet", "Stylus", 40], [2, "Suburb Mall", "Chicago", "Phone", "Case", 25], [1, "Downtown Tech", "New York", "Laptop", "Mouse", 10]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"stores": [{"store_id": 1, "store_name": "Downtown Tech", "location": "New York"}, {"store_id": 2, "store_name": "Suburb Mall", "location": "Chicago"}, {"store_id": 3, "store_name": "City Center", "location": "Los Angeles"}, {"store_id": 4, "store_name": "Corner Shop", "location": "Miami"}, {"store_id": 5, "store_name": "Plaza Store", "location": "Seattle"}], "inventory": [{"inventory_id": 1, "store_id": 1, "product_name": "Laptop", "quantity": 5, "price": 999.99}, {"inventory_id": 2, "store_id": 1, "product_name": "Mouse", "quantity": 50, "price": 19.99}, {"inventory_id": 3, "store_id": 1, "product_name": "Keyboard", "quantity": 25, "price": 79.99}, {"inventory_id": 4, "store_id": 1, "product_name": "Monitor", "quantity": 15, "price": 299.99}, {"inventory_id": 5, "store_id": 2, "product_name": "Phone", "quantity": 3, "price": 699.99}, {"inventory_id": 6, "store_id": 2, "product_name": "Charger", "quantity": 100, "price": 25.99}, {"inventory_id": 7, "store_id": 2, "product_name": "Case", "quantity": 75, "price": 15.99}, {"inventory_id": 8, "store_id": 2, "product_name": "Headphones", "quantity": 20, "price": 149.99}, {"inventory_id": 9, "store_id": 3, "product_name": "Tablet", "quantity": 2, "price": 499.99}, {"inventory_id": 10, "store_id": 3, "product_name": "Stylus", "quantity": 80, "price": 29.99}, {"inventory_id": 11, "store_id": 3, "product_name": "Cover", "quantity": 60, "price": 39.99}, {"inventory_id": 12, "store_id": 4, "product_name": "Watch", "quantity": 10, "price": 299.99}, {"inventory_id": 13, "store_id": 4, "product_name": "Band", "quantity": 25, "price": 49.99}, {"inventory_id": 14, "store_id": 5, "product_name": "Camera", "quantity": 8, "price": 599.99}, {"inventory_id": 15, "store_id": 5, "product_name": "Lens", "quantity": 12, "price": 199.99}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["store_id", "store_name", "location", "most_exp_product", "cheapest_product", "imbalance_ratio"], "rows": [[3, "City Center", "Los Angeles", "Tablet", "Stylus", 40], [2, "Suburb Mall", "Chicago", "Phone", "Case", 25], [1, "Downtown Tech", "New York", "Laptop", "Mouse", 10]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`ROW_NUMBER` with deterministic tie-breaker:**:** - **`ROW_NUMBER` with deterministic tie-breaker:** Select exactly one extreme product using price, then product or inventory ID.
- **Aggregate extreme prices then join:** Compute `MAX(price)` and `MIN(price)` per store, but ties still need an explicit policy.
- **Count distinct products:** Use `COUNT(DISTINCT product_name)` to match “different products” without relying on row uniqueness.
- **Exactly two products:** The store is excluded by `cnt>=3`.
- **Exactly three unique rows:** It passes the count threshold.
- **Duplicate product rows:** The exact `COUNT(1)` may overstate the number of different products.
- **Equal highest-price quantities:** `RANK` can produce multiple `P1` rows and duplicate outputs.
- **Equal lowest-price quantities:** The same issue can occur in `P2`.
- **Most and cheapest quantities equal:** Strict `<` rejects the store.
- **Most-expensive quantity larger:** The store is not imbalanced and is excluded.
- **Zero most-expensive quantity:** Ratio division is undefined unless data guarantees positivity or query handling is added.
- **Rounded-ratio ties:** Store name determines order after rounding.
- **Duplicate store names:** Their remaining relative order is unspecified unless `store_id` is added as a final key.
- **Store with no inventory:** It never appears in `T` and cannot qualify.
- **Missing store metadata:** The inner join to `stores` removes the row.
- **Read-only behavior:** The query ranks and selects without modifying either table.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `R` be the number of inventory rows and `S` the number of stores. SQL physical cost depends on indexes and the optimizer.
- **Auxiliary Space Complexity:** $O(R + S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
