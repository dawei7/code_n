# Guided Example: Calculate Product Final Price

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "category": "Electronics", "price": 1000}, {"product_id": 2, "category": "Clothing", "price": 50}, {"product_id": 3, "category": "Electronics", "price": 1200}, {"product_id": 4, "category": "Home", "price": 500}], "Discounts": [{"category": "Electronics", "discount": 10}, {"category": "Clothing", "discount": 20}]}}`
- **Required output:** `{"columns": ["product_id", "final_price", "category"], "rows": [[1, 900, "Electronics"], [2, 40, "Clothing"], [3, 1080, "Electronics"], [4, 500, "Home"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_id", "final_price", "category"], "rows": [[1, 900, "Electronics"], [2, 40, "Clothing"], [3, 1080, "Electronics"], [4, 500, "Home"]]}` from `{"tables": {"Products": [{"product_id": 1, "category": "Electronics", "price": 1000}, {"product_id": 2, "category": "Clothing", "price": 50}, {"product_id": 3, "category": "Electronics", "price": 1200}, {"product_id": 4, "category": "Home", "price": 500}], "Discounts": [{"category": "Electronics", "discount": 10}, {"category": "Clothing", "discount": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Start from every product, not from every discount.** The output must contain one row for each row of `Products`, including products whose category has no entry in `Discounts`. That requirement determines the join direction. The query writes `Products LEFT JOIN Discounts USING (category)`, so every product survives. When a category exists in both tables, the matching discount is attached. When no match exists, the joined `discount` value is SQL `NULL` rather than the product row disappearing.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "category": "Electronics", "price": 1000}, {"product_id": 2, "category": "Clothing", "price": 50}, {"product_id": 3, "category": "Electronics", "price": 1200}, {"product_id": 4, "category": "Home", "price": 500}], "Discounts": [{"category": "Electronics", "discount": 10}, {"category": "Clothing", "discount": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

An inner join would be wrong for the same reason: it would silently remove an undiscounted product such as the example's `Home` item. A right join would preserve discounts that have no products, which are irrelevant output rows. The left join exactly matches the “all products, optional discount” relationship.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An inner join would be wrong for the same reason: it would s... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why one join match cannot duplicate a product.** `Discounts.category` is the table's primary key, so at most one discount row has a given category. Each product therefore joins to zero or one discount row. Even if many products share a category, each product gets the same single category discount and still produces exactly one result row. This schema guarantee is what makes the plain join sufficient; no grouping or deduplication is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "final_price", "category"], "rows": [[1, 900, "Electronics"], [2, 40, "Clothing"], [3, 1080, "Electronics"], [4, 500, "Home"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "category": "Electronics", "price": 1000}, {"product_id": 2, "category": "Clothing", "price": 50}, {"product_id": 3, "category": "Electronics", "price": 1200}, {"product_id": 4, "category": "Home", "price": 500}], "Discounts": [{"category": "Electronics", "discount": 10}, {"category": "Clothing", "discount": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "final_price", "category"], "rows": [[1, 900, "Electronics"], [2, 40, "Clothing"], [3, 1080, "Electronics"], [4, 500, "Home"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Inner join:** This incorrectly drops products :** - **Inner join:** This incorrectly drops products whose categories have no discount, directly violating the unchanged-price requirement.
- **Correlated scalar subquery:** Looking up the discount separately for every product can express the same logic, but it is less direct and may lead to repeated lookups unless the optimizer rewrites it.
- **`CASE WHEN discount IS NULL`:** A `CASE` expression can substitute zero or return `price` explicitly. `COALESCE` is shorter and communicates the missing-value fallback precisely.
- **Subtracting the discount amount:** `price - price * discount / 100` is algebraically equivalent for matched rows, but it still needs a `NULL` fallback. The multiplier form handles matched and unmatched rows uniformly.
- **No matching discount:** The left join produces `NULL`, `COALESCE` converts it to zero, and the formula returns the original price.
- **Zero-percent discount:** The joined row exists, but the formula also returns the original price. No special branch is needed.
- **One-hundred-percent discount:** `100 - discount` becomes zero, so `final_price` is zero as expected.
- **Many products in one category:** Primary-key uniqueness in `Discounts` lets all of them reuse one discount without multiplying rows.
- **Discount category with no product:** Starting from `Products` means such a discount generates no output, which is correct because the result is about products.
- **Fractional decimal result:** The exact query does not round. Adding `ROUND` or converting to an integer would impose behavior absent from the contract.
- **`ORDER BY 1` maintainability:** It is valid and exact here, but reordering select columns could silently change the sort key. `ORDER BY product_id ASC` is clearer in evolving production SQL.
- **`NULL` product category:** The documented schema does not state such rows are possible. Under ordinary SQL equality semantics, `NULL` would not match another `NULL` category and would therefore receive zero discount through `COALESCE`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((P + D) log(P + D))$. Let $P$ be the number of rows in `Products` and $D$ the number in `Discounts`. Logical query complexity depends on the execution plan and available indexes. A typical plan can index or hash the primary-key categories and match all products in $O(P+D)$ expected work, then sort the $P$ output rows by `product_id` in $O(P\log P)$ time. This gives the safe overall characterization $O(P+D+P\log P)$, commonly summarized by the manifest as $O((P+D)\log(P+D))$.
- **Auxiliary Space Complexity:** $O(P + D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
