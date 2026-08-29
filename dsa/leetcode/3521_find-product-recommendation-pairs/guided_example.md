# Guided Example: Find Product Recommendation Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 103, "quantity": 3}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 5}, {"user_id": 2, "product_id": 104, "quantity": 1}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 105, "quantity": 4}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 102, "quantity": 1}, {"user_id": 4, "product_id": 103, "quantity": 2}, {"user_id": 4, "product_id": 104, "quantity": 3}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 104, "quantity": 1}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Clothing", "price": 35}, {"product_id": 104, "category": "Kitchen", "price": 50}, {"product_id": 105, "category": "Sports", "price": 75}]}}`
- **Required output:** `{"columns": ["product1_id", "product2_id", "product1_category", "product2_category", "customer_count"], "rows": [[101, 102, "Electronics", "Books", 3], [101, 103, "Electronics", "Clothing", 3], [102, 104, "Books", "Kitchen", 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `ProductPurchases`

The objective is to compute `{"columns": ["product1_id", "product2_id", "product1_category", "product2_category", "customer_count"], "rows": [[101, 102, "Electronics", "Books", 3], [101, 103, "Electronics", "Clothing", 3], [102, 104, "Books", "Kitchen", 3]]}` from `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 103, "quantity": 3}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 5}, {"user_id": 2, "product_id": 104, "quantity": 1}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 105, "quantity": 4}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 102, "quantity": 1}, {"user_id": 4, "product_id": 103, "quantity": 2}, {"user_id": 4, "product_id": 104, "quantity": 3}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 104, "quantity": 1}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Clothing", "price": 35}, {"product_id": 104, "category": "Kitchen", "price": 50}, {"product_id": 105, "category": "Sports", "price": 75}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Interpret a purchase row as customer-product presence

`ProductPurchases` has a unique key on `(user_id, product_id)`. Therefore, a user has at most one row for a particular product. `quantity` tells how many units were purchased, but recommendation eligibility depends only on whether the customer purchased both products, not on units. The query correctly does not use `quantity`.

The central task is to turn each customer's purchased products into distinct unordered pairs, count how many users generated each pair, keep counts of at least three, and attach the two product categories.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 103, "quantity": 3}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 5}, {"user_id": 2, "product_id": 104, "quantity": 1}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 105, "quantity": 4}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 102, "quantity": 1}, {"user_id": 4, "product_id": 103, "quantity": 2}, {"user_id": 4, "product_id": 104, "quantity": 3}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 104, "quantity": 1}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Clothing", "price": 35}, {"product_id": 104, "category": "Kitchen", "price": 50}, {"product_id": 105, "category": "Sports", "price": 75}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Self-join purchases by the same user

The query gives `ProductPurchases` two aliases, `pp1` and `pp2`, and joins them on:

`pp2.user_id = pp1.user_id`.

This creates combinations of two products bought by the same customer. A user who bought `d` distinct products could otherwise produce ordered pairs in both directions and pairs of a product with itself.

The additional predicate:

`pp2.product_id > pp1.product_id`

solves both problems:

- strict inequality excludes self-pairs;
- greater-than fixes the canonical orientation `product1_id < product2_id`;
- each unordered pair for one user appears once rather than as both `(a,b)` and `(b,a)`.

Because `(user_id, product_id)` is unique, one user cannot produce duplicate joined rows for the same canonical pair. This property is central to the customer count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Attach each side's category independently

The joined purchase aliases contain product IDs but not categories. The query joins `ProductInfo` twice:

- `pi1.product_id = pp1.product_id` supplies `product1_category`;
- `pi2.product_id = pp2.product_id` supplies `product2_category`.

`product_id` is the primary key of `ProductInfo`, so each dimension join matches at most one row and does not multiply co-purchase rows. The selected categories therefore correspond to the correct side of the ordered pair.

`price` is not part of the requested output or eligibility rule, so it is intentionally unused.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product1_id", "product2_id", "product1_category", "product2_category", "customer_count"], "rows": [[101, 102, "Electronics", "Books", 3], [101, 103, "Electronics", "Clothing", 3], [102, 104, "Books", "Kitchen", 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 103, "quantity": 3}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 5}, {"user_id": 2, "product_id": 104, "quantity": 1}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 105, "quantity": 4}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 102, "quantity": 1}, {"user_id": 4, "product_id": 103, "quantity": 2}, {"user_id": 4, "product_id": 104, "quantity": 3}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 104, "quantity": 1}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Clothing", "price": 35}, {"product_id": 104, "category": "Kitchen", "price": 50}, {"product_id": 105, "category": "Sports", "price": 75}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product1_id", "product2_id", "product1_category", "product2_category", "customer_count"], "rows": [[101, 102, "Electronics", "Books", 3], [101, 103, "Electronics", "Clothing", 3], [102, 104, "Books", "Kitchen", 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Join with product IDs not equal:** `pp1.product_id <> pp2.product_id` would create both orientations. It would require a later normalization and could double counts if handled carelessly.
- **Use less-than instead of greater-than:** `pp1.product_id < pp2.product_id` is logically equivalent. The protected predicate expresses the same canonical orientation from the second alias.
- **Group by user first:** One can derive each user's product pairs in a CTE and aggregate afterward. The direct self-join already performs that relational expansion.
- **Count purchase quantities:** Summing `quantity` would answer a different question. Eligibility is based on distinct customers who bought both products.
- **COUNT(*) under declared keys:** It would equal the distinct-user count because each user-product row and each ProductInfo row is unique. `COUNT(DISTINCT ...)` makes the business requirement robust and explicit.
- **Filter with WHERE:** Aggregate thresholds belong in `HAVING`. `WHERE` filters source rows before customer counts exist.
- **Customer bought only one product:** That user creates no self-join row and contributes to no recommendation pair.
- **Customer bought exactly two products:** The user contributes exactly one canonical pair.
- **Exactly three customers:** The inclusive `>= 3` condition keeps the pair.
- **Multiple quantities in one row:** Quantity does not create repeated customer contributions.
- **Missing ProductInfo row:** The inner joins would omit any pair side lacking product information. The schema normally implies referenced products are represented; if not, left joins would be needed to retain unknown categories, but that is not the protected query.
- **Same category on both products:** Products remain a valid distinct pair; category equality does not affect grouping or eligibility.
- **Tied customer counts:** Ascending product IDs supply the required deterministic order.
- **ProductInfo price:** It is deliberately ignored because neither output nor filtering uses it.
- **Data violating the unique purchase key:** Duplicate user-product rows could multiply the self-join. `COUNT(DISTINCT user_id)` would still protect the aggregate count, although join work would grow.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P\log P + J\log J + I\log I)$. Let `P` be the number of `ProductPurchases` rows, `I` the number of `ProductInfo` rows, and:
- **Auxiliary Space Complexity:** $O(J + I)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
