# Guided Example: Find Category Recommendation Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 201, "quantity": 3}, {"user_id": 1, "product_id": 301, "quantity": 1}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 2}, {"user_id": 2, "product_id": 103, "quantity": 1}, {"user_id": 2, "product_id": 201, "quantity": 5}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 301, "quantity": 4}, {"user_id": 3, "product_id": 401, "quantity": 2}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 201, "quantity": 3}, {"user_id": 4, "product_id": 301, "quantity": 1}, {"user_id": 4, "product_id": 401, "quantity": 2}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 103, "quantity": 1}, {"user_id": 5, "product_id": 201, "quantity": 2}, {"user_id": 5, "product_id": 202, "quantity": 3}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Books", "price": 35}, {"product_id": 201, "category": "Clothing", "price": 45}, {"product_id": 202, "category": "Clothing", "price": 60}, {"product_id": 301, "category": "Sports", "price": 75}, {"product_id": 401, "category": "Kitchen", "price": 50}]}}`
- **Required output:** `{"columns": ["category1", "category2", "customer_count"], "rows": [["Books", "Clothing", 3], ["Books", "Electronics", 3], ["Clothing", "Electronics", 3], ["Electronics", "Sports", 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `ProductPurchases`

The objective is to compute `{"columns": ["category1", "category2", "customer_count"], "rows": [["Books", "Clothing", 3], ["Books", "Electronics", 3], ["Clothing", "Electronics", 3], ["Electronics", "Sports", 3]]}` from `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 201, "quantity": 3}, {"user_id": 1, "product_id": 301, "quantity": 1}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 2}, {"user_id": 2, "product_id": 103, "quantity": 1}, {"user_id": 2, "product_id": 201, "quantity": 5}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 301, "quantity": 4}, {"user_id": 3, "product_id": 401, "quantity": 2}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 201, "quantity": 3}, {"user_id": 4, "product_id": 301, "quantity": 1}, {"user_id": 4, "product_id": 401, "quantity": 2}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 103, "quantity": 1}, {"user_id": 5, "product_id": 201, "quantity": 2}, {"user_id": 5, "product_id": 202, "quantity": 3}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Books", "price": 35}, {"product_id": 201, "category": "Clothing", "price": 45}, {"product_id": 202, "category": "Clothing", "price": 60}, {"product_id": 301, "category": "Sports", "price": 75}, {"product_id": 401, "category": "Kitchen", "price": 50}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Stage 1: translate products into category memberships

`ProductPurchases JOIN ProductInfo USING (product_id)` matches every purchased product with its category. `USING (product_id)` is appropriate because both tables use the same join-column name, and `ProductInfo.product_id` uniquely identifies one product description.

Only `user_id` and `category` are selected. The purchased `quantity` does not affect whether the customer bought from a category: buying one unit or many units creates the same membership. The product `price` is also irrelevant to the requested count.

The crucial word is `DISTINCT`:

`SELECT DISTINCT user_id, category`

Suppose one customer bought two different book products, or has multiple qualifying product rows that map to Books. After the join, Books could appear more than once for that user. `DISTINCT` collapses those rows into one `(user, Books)` membership. This ensures later work counts a customer’s presence in a category, not the number of products or purchases.

After this CTE, it is helpful to imagine each customer owning a set of categories. For example, a customer associated with Books, Clothing, and Electronics contributes exactly those three set members.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 201, "quantity": 3}, {"user_id": 1, "product_id": 301, "quantity": 1}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 2}, {"user_id": 2, "product_id": 103, "quantity": 1}, {"user_id": 2, "product_id": 201, "quantity": 5}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 301, "quantity": 4}, {"user_id": 3, "product_id": 401, "quantity": 2}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 201, "quantity": 3}, {"user_id": 4, "product_id": 301, "quantity": 1}, {"user_id": 4, "product_id": 401, "quantity": 2}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 103, "quantity": 1}, {"user_id": 5, "product_id": 201, "quantity": 2}, {"user_id": 5, "product_id": 202, "quantity": 3}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Books", "price": 35}, {"product_id": 201, "category": "Clothing", "price": 45}, {"product_id": 202, "category": "Clothing", "price": 60}, {"product_id": 301, "category": "Sports", "price": 75}, {"product_id": 401, "category": "Kitchen", "price": 50}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Stage 2: create each unordered pair once per customer

`pair_per_user` joins `user_category` to itself. Aliases `a` and `b` represent two category memberships belonging to the same customer. The first join condition,

`a.user_id = b.user_id`,

prevents categories belonging to different customers from being paired.

The second condition,

`a.category < b.category`,

does three jobs at once:

- it prevents pairing a category with itself;
- it chooses one canonical orientation for an unordered pair;
- it prevents both `(Books, Clothing)` and `(Clothing, Books)` from appearing.

The comparison follows the database’s string collation, which is also the natural mechanism used by the final lexicographic ordering. The smaller category becomes `category1` and the larger becomes `category2`.

If one user has `c` distinct categories, this self-join emits exactly

$$
\binom{c}{2} = \frac{c(c-1)}{2}
$$

rows for that user. Because `user_category` was deduplicated first, each particular `(user_id, category1, category2)` combination occurs once.

For a user with Books, Clothing, and Electronics, the generated rows are Books-Clothing, Books-Electronics, and Clothing-Electronics. No reverse pairs and no same-category pairs are generated.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pair_per_user` joins `user_category` to itself.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Stage 3: count shared customers

The outer query groups rows by `category1` and `category2`. Every row in one group represents a customer who belongs to both categories, so

`COUNT(DISTINCT user_id) AS customer_count`

gives the number of unique shared customers.

Given the preceding `DISTINCT` and strict pair construction, each user already contributes at most one row to a particular pair. Thus plain `COUNT(*)` would be equivalent for this exact query. Keeping `COUNT(DISTINCT user_id)` makes the intended business meaning explicit and protects the count if the earlier CTE is later changed in a way that reintroduces duplicates.

`GROUP BY 1, 2` is positional shorthand for grouping by the first and second selected expressions, namely `category1` and `category2`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["category1", "category2", "customer_count"], "rows": [["Books", "Clothing", 3], ["Books", "Electronics", 3], ["Clothing", "Electronics", 3], ["Electronics", "Sports", 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"ProductPurchases": [{"user_id": 1, "product_id": 101, "quantity": 2}, {"user_id": 1, "product_id": 102, "quantity": 1}, {"user_id": 1, "product_id": 201, "quantity": 3}, {"user_id": 1, "product_id": 301, "quantity": 1}, {"user_id": 2, "product_id": 101, "quantity": 1}, {"user_id": 2, "product_id": 102, "quantity": 2}, {"user_id": 2, "product_id": 103, "quantity": 1}, {"user_id": 2, "product_id": 201, "quantity": 5}, {"user_id": 3, "product_id": 101, "quantity": 2}, {"user_id": 3, "product_id": 103, "quantity": 1}, {"user_id": 3, "product_id": 301, "quantity": 4}, {"user_id": 3, "product_id": 401, "quantity": 2}, {"user_id": 4, "product_id": 101, "quantity": 1}, {"user_id": 4, "product_id": 201, "quantity": 3}, {"user_id": 4, "product_id": 301, "quantity": 1}, {"user_id": 4, "product_id": 401, "quantity": 2}, {"user_id": 5, "product_id": 102, "quantity": 2}, {"user_id": 5, "product_id": 103, "quantity": 1}, {"user_id": 5, "product_id": 201, "quantity": 2}, {"user_id": 5, "product_id": 202, "quantity": 3}], "ProductInfo": [{"product_id": 101, "category": "Electronics", "price": 100}, {"product_id": 102, "category": "Books", "price": 20}, {"product_id": 103, "category": "Books", "price": 35}, {"product_id": 201, "category": "Clothing", "price": 45}, {"product_id": 202, "category": "Clothing", "price": 60}, {"product_id": 301, "category": "Sports", "price": 75}, {"product_id": 401, "category": "Kitchen", "price": 50}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["category1", "category2", "customer_count"], "rows": [["Books", "Clothing", 3], ["Books", "Electronics", 3], ["Clothing", "Electronics", 3], ["Electronics", "Sports", 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated existence checks:** One could enume:** - **Correlated existence checks:** One could enumerate category pairs and test how many users have purchases in both categories, but repeated scans or correlated subqueries tend to do much more work than building memberships and grouping once.
- **Conditional aggregation:** Pivoting categories into columns can count co-occurrence for a small fixed category set, but categories here are data values rather than a fixed schema, so a self-join is the general solution.
- **Skip the membership deduplication:** Joining raw purchase rows to themselves would multiply combinations when a customer owns several products in one category. Even `COUNT(DISTINCT user_id)` could recover the final count, but the intermediate join could become dramatically larger.
- **Use `COUNT(*)`:** It is correct after the exact `DISTINCT user_id, category` CTE because one user-pair row is unique. `COUNT(DISTINCT user_id)` communicates the contract more defensively.
- **Canonical pair orientation:** The strict condition `a.category < b.category` is essential. Using inequality alone would generate both orientations; using `<=` would also generate same-category pairs.
- **Exactly three customers:** Such a pair passes because `HAVING` uses `>= 3`.
- **A customer in only one category:** That user creates no row in `pair_per_user`, which is correct because one category cannot form a pair.
- **Several products in one category:** `DISTINCT` reduces them to one membership, so they do not inflate `customer_count`.
- **Quantities and prices:** Neither changes whether a customer has purchased from a category, so excluding them is intentional.
- **No reportable pairs:** After `HAVING`, the query returns an empty result table, which is the correct representation.
- **String collation:** Both `<` and the ascending order use the database collation. If a system requires a specific case-sensitive or locale-specific lexical definition, the query would need an explicit collation; the supplied category data and MySQL environment define the intended behavior here.
- **Positional clauses:** `GROUP BY 1, 2` and `ORDER BY 3 DESC, 1, 2` are concise but depend on select-column order. Naming the expressions explicitly would be more resilient to later reordering without changing the algorithm.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P log P + J log J + I log I)$. SQL complexity depends on indexes, join algorithms, collation, whether common table expressions are materialized, and whether `DISTINCT`, grouping, and ordering use hashing or sorting. The query text specifies the relational operations but does not force one physical execution plan.
- **Auxiliary Space Complexity:** $O(U + J + I)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
