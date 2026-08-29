# Guided Example: Product Sales Analysis IV

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sales": [{"sale_id": 1, "product_id": 1, "user_id": 101, "quantity": 10}, {"sale_id": 2, "product_id": 3, "user_id": 101, "quantity": 7}, {"sale_id": 3, "product_id": 1, "user_id": 102, "quantity": 9}, {"sale_id": 4, "product_id": 2, "user_id": 102, "quantity": 6}, {"sale_id": 5, "product_id": 3, "user_id": 102, "quantity": 10}, {"sale_id": 6, "product_id": 1, "user_id": 102, "quantity": 6}], "Product": [{"product_id": 1, "price": 10}, {"product_id": 2, "price": 25}, {"product_id": 3, "price": 15}]}}`
- **Required output:** `{"columns": ["user_id", "product_id"], "rows": [[101, 3], [102, 1], [102, 2], [102, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sales`

The objective is to compute `{"columns": ["user_id", "product_id"], "rows": [[101, 3], [102, 1], [102, 2], [102, 3]]}` from `{"tables": {"Sales": [{"sale_id": 1, "product_id": 1, "user_id": 101, "quantity": 10}, {"sale_id": 2, "product_id": 3, "user_id": 101, "quantity": 7}, {"sale_id": 3, "product_id": 1, "user_id": 102, "quantity": 9}, {"sale_id": 4, "product_id": 2, "user_id": 102, "quantity": 6}, {"sale_id": 5, "product_id": 3, "user_id": 102, "quantity": 10}, {"sale_id": 6, "product_id": 1, "user_id": 102, "quantity": 6}], "Product": [{"product_id": 1, "price": 10}, {"product_id": 2, "price": 25}, {"product_id": 3, "price": 15}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First total the money spent on each user-product combination

One row in `Sales` represents a purchase event, not necessarily a user's complete spending on that product. The same user can buy the same product in multiple rows. Therefore ranking individual sales would be incorrect; all purchases for one `(user_id, product_id)` pair must be combined first.

The money represented by one sale row is

`quantity * price`.

`quantity` comes from `Sales`, while `price` comes from `Product`. The query joins the tables with `JOIN Product USING (product_id)` so every sale row gains the price belonging to its product.

The foreign-key relationship guarantees that a sale's `product_id` refers to the product table. `Product.product_id` is unique, so one sale joins to exactly one price row rather than being duplicated by multiple matches.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sales": [{"sale_id": 1, "product_id": 1, "user_id": 101, "quantity": 10}, {"sale_id": 2, "product_id": 3, "user_id": 101, "quantity": 7}, {"sale_id": 3, "product_id": 1, "user_id": 102, "quantity": 9}, {"sale_id": 4, "product_id": 2, "user_id": 102, "quantity": 6}, {"sale_id": 5, "product_id": 3, "user_id": 102, "quantity": 10}, {"sale_id": 6, "product_id": 1, "user_id": 102, "quantity": 6}], "Product": [{"product_id": 1, "price": 10}, {"product_id": 2, "price": 25}, {"product_id": 3, "price": 15}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group at exactly the level that will be ranked

`GROUP BY 1, 2` groups by the first and second selected expressions, which are `user_id` and `product_id`. Inside each group,

`SUM(quantity * price)`

adds all spending by that user on that product.

For example, if user 102 buys nine units of product 1 and later six more units, and its price is 10, the grouped total is `(9 + 6) * 10 = 150`. Treating the two rows separately would produce 90 and 60 and could fail to recognize product 1 as a maximum.

The price is constant for a product because it comes from the unique Product row. Multiplying each quantity before summing and summing quantities before multiplying by that price are equivalent, but the expression in the query works directly on joined sale rows.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rank totals independently for every user

The window function uses

`RANK() OVER (PARTITION BY user_id ORDER BY SUM(quantity * price) DESC)`.

`PARTITION BY user_id` restarts the ranking for each user. Spending by one user never competes with spending by another.

The aggregate total is ordered descending, so the largest total receives rank one. SQL logically groups the rows before applying the window function, which is why the aggregate expression can be used as the ranking key: each row entering the window stage already represents one user-product total.

`RANK` assigns the same rank to equal ordering values. If a user spends the same maximum amount on several products, every one of those grouped rows receives `rk = 1`. That exactly implements the requirement to report all maximum ties.

Using `DENSE_RANK` would behave identically for the only rank the query later selects. The difference between gaps after ties is irrelevant because ranks greater than one are discarded.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "product_id"], "rows": [[101, 3], [102, 1], [102, 2], [102, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sales": [{"sale_id": 1, "product_id": 1, "user_id": 101, "quantity": 10}, {"sale_id": 2, "product_id": 3, "user_id": 101, "quantity": 7}, {"sale_id": 3, "product_id": 1, "user_id": 102, "quantity": 9}, {"sale_id": 4, "product_id": 2, "user_id": 102, "quantity": 6}, {"sale_id": 5, "product_id": 3, "user_id": 102, "quantity": 10}, {"sale_id": 6, "product_id": 1, "user_id": 102, "quantity": 6}], "Product": [{"product_id": 1, "price": 10}, {"product_id": 2, "price": 25}, {"product_id": 3, "price": 15}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "product_id"], "rows": [[101, 3], [102, 1], [102, 2], [102, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate in one CTE, then use `MAX` in another:** Compute spend per user-product, compute each user's maximum, and join on equal totals. This is correct and explicit but requires an additional aggregation or join stage.
- **`DENSE_RANK` instead of `RANK`:** Both retain every maximum tie under `rk = 1`. Their treatment of later ranks differs but is irrelevant here.
- **`ROW_NUMBER` instead of `RANK`:** This would keep only one arbitrarily ordered product from a maximum tie and violate the requirement to return all tied products.
- **Rank raw sale rows:** Multiple purchases of one product must be combined. Ranking before grouping can choose a large individual sale rather than the largest total spend.
- **Group only by user:** This loses the product-level totals needed to identify which product won.
- **Group only by product:** This combines different users and answers a global sales question rather than a per-user question.
- **Use quantity without price:** The most units purchased need not be the product on which the most money was spent.
- **Inner join behavior:** The foreign key guarantees every sale product exists. Without that guarantee, an inner join would silently omit unmatched sales.
- **Several purchases of the same product:** Grouping combines them before ranking, as required.
- **Several products tied for maximum:** `RANK` gives each rank one, and all are returned.
- **One purchased product for a user:** It is automatically that user's maximum and receives rank one.
- **Different users buying the same product:** Partitions are independent, so the product may win for one user and not another.
- **No required output order:** Omitting a final sort is correct. Consumers must not infer a stable order from CTE or window processing.
- **Ordinal `GROUP BY`:** It is valid for the current select list but less robust to column reordering than explicit names.
- **Helper rank column:** It controls filtering inside the CTE and is intentionally absent from the final result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((s + p) log s)$. Let `s` be the number of Sales rows, `p` the number of Product rows, and `g` the number of distinct user-product groups, with `g <= s`. The database must join the tables, aggregate sale rows into groups, and rank grouped rows within users. With general comparison-based sorting for grouping or window ordering, a conservative bound is `O((s + p) \log s)`, matching the variant manifest. Hash joins and hash aggregation or suitable indexes may reduce particular stages, but physical behavior depends on the MySQL execution plan.
- **Auxiliary Space Complexity:** $O(s + p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
