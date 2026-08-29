# Guided Example: Market Analysis I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 1, "join_date": "2018-01-01", "favorite_brand": "Lenovo"}, {"user_id": 2, "join_date": "2018-02-09", "favorite_brand": "Samsung"}, {"user_id": 3, "join_date": "2018-01-19", "favorite_brand": "LG"}, {"user_id": 4, "join_date": "2018-05-21", "favorite_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "buyer_id": 1, "seller_id": 2}, {"order_id": 2, "order_date": "2018-08-02", "item_id": 2, "buyer_id": 1, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "buyer_id": 2, "seller_id": 3}, {"order_id": 4, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 4, "seller_id": 2}, {"order_id": 5, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 3, "seller_id": 4}, {"order_id": 6, "order_date": "2019-08-05", "item_id": 2, "buyer_id": 2, "seller_id": 4}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}]}}`
- **Required output:** `{"columns": ["buyer_id", "join_date", "orders_in_2019"], "rows": [[1, "2018-01-01", 1], [2, "2018-02-09", 2], [3, "2018-01-19", 0], [4, "2018-05-21", 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["buyer_id", "join_date", "orders_in_2019"], "rows": [[1, "2018-01-01", 1], [2, "2018-02-09", 2], [3, "2018-01-19", 0], [4, "2018-05-21", 0]]}` from `{"tables": {"Users": [{"user_id": 1, "join_date": "2018-01-01", "favorite_brand": "Lenovo"}, {"user_id": 2, "join_date": "2018-02-09", "favorite_brand": "Samsung"}, {"user_id": 3, "join_date": "2018-01-19", "favorite_brand": "LG"}, {"user_id": 4, "join_date": "2018-05-21", "favorite_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "buyer_id": 1, "seller_id": 2}, {"order_id": 2, "order_date": "2018-08-02", "item_id": 2, "buyer_id": 1, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "buyer_id": 2, "seller_id": 3}, {"order_id": 4, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 4, "seller_id": 2}, {"order_id": 5, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 3, "seller_id": 4}, {"order_id": 6, "order_date": "2019-08-05", "item_id": 2, "buyer_id": 2, "seller_id": 4}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from `Users` because every user must appear

The report requires one row for each user, including people who placed no qualifying order. `Users AS u` is therefore the preserved side of a `LEFT JOIN`.

An inner join would retain only users with at least one matching order and would silently omit the required zero-order rows. A left join keeps every user row. When no order matches, SQL supplies one joined row whose `Orders` columns are null.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 1, "join_date": "2018-01-01", "favorite_brand": "Lenovo"}, {"user_id": 2, "join_date": "2018-02-09", "favorite_brand": "Samsung"}, {"user_id": 3, "join_date": "2018-01-19", "favorite_brand": "LG"}, {"user_id": 4, "join_date": "2018-05-21", "favorite_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "buyer_id": 1, "seller_id": 2}, {"order_id": 2, "order_date": "2018-08-02", "item_id": 2, "buyer_id": 1, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "buyer_id": 2, "seller_id": 3}, {"order_id": 4, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 4, "seller_id": 2}, {"order_id": 5, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 3, "seller_id": 4}, {"order_id": 6, "order_date": "2019-08-05", "item_id": 2, "buyer_id": 2, "seller_id": 4}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match users in their role as buyers

The relationship is

`u.user_id = o.buyer_id`.

Using `seller_id` would count orders a user sold rather than orders the user made as a buyer. The output alias `buyer_id` reinforces the requested role even though its value originates from `Users.user_id`.

The `Items` table is not needed. The report does not ask for an item brand or any property beyond the existence of an order. Joining `Items` would add work without changing the count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep the 2019 filter inside the join condition

The second join predicate is

`YEAR(order_date) = 2019`.

Only 2019 orders are allowed to match a user. Crucially, this condition belongs in the `ON` clause. If it were moved to a normal `WHERE` clause without special null handling, a user with no matching order would have a null `order_date`, fail the filter, and disappear. That would effectively turn the outer join into an inner join for this purpose.

With the predicate in `ON`, a user who has only 2018 orders behaves exactly like a user with no orders: none of those rows matches, but the preserved user row remains available for aggregation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["buyer_id", "join_date", "orders_in_2019"], "rows": [[1, "2018-01-01", 1], [2, "2018-02-09", 2], [3, "2018-01-19", 0], [4, "2018-05-21", 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 1, "join_date": "2018-01-01", "favorite_brand": "Lenovo"}, {"user_id": 2, "join_date": "2018-02-09", "favorite_brand": "Samsung"}, {"user_id": 3, "join_date": "2018-01-19", "favorite_brand": "LG"}, {"user_id": 4, "join_date": "2018-05-21", "favorite_brand": "HP"}], "Orders": [{"order_id": 1, "order_date": "2019-08-01", "item_id": 4, "buyer_id": 1, "seller_id": 2}, {"order_id": 2, "order_date": "2018-08-02", "item_id": 2, "buyer_id": 1, "seller_id": 3}, {"order_id": 3, "order_date": "2019-08-03", "item_id": 3, "buyer_id": 2, "seller_id": 3}, {"order_id": 4, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 4, "seller_id": 2}, {"order_id": 5, "order_date": "2018-08-04", "item_id": 1, "buyer_id": 3, "seller_id": 4}, {"order_id": 6, "order_date": "2019-08-05", "item_id": 2, "buyer_id": 2, "seller_id": 4}], "Items": [{"item_id": 1, "item_brand": "Samsung"}, {"item_id": 2, "item_brand": "Lenovo"}, {"item_id": 3, "item_brand": "LG"}, {"item_id": 4, "item_brand": "HP"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["buyer_id", "join_date", "orders_in_2019"], "rows": [[1, "2018-01-01", 1], [2, "2018-02-09", 2], [3, "2018-01-19", 0], [4, "2018-05-21", 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use an inner join:** Users with zero 2019 purchases disappear, violating the one-row-per-user report.
- **Put the year condition in `WHERE`:** Null-extended rows fail the condition and are removed. Keeping it in `ON` preserves zero-order users.
- **Use `COUNT(*)`:** The outer join creates one placeholder row for an unmatched user, so `COUNT(*)` would incorrectly return one instead of zero.
- **Count `item_id`:** It is non-null for real orders under the foreign-key model and could count them, but the primary order key states the intended unit most clearly.
- **Join `Items`:** Item attributes are irrelevant to this report, so that join is unnecessary.
- **Use `seller_id`:** That counts sales rather than purchases and answers a different marketplace question.
- **A user has only non-2019 orders:** null matches, but the user remains and receives count zero.
- **A user has no orders at all:** The behavior is the same: one preserved row and zero non-null order IDs.
- **Multiple 2019 orders:** Each unique order ID contributes one to the aggregate.
- **Year boundaries:** `YEAR(order_date) = 2019` includes every date from January 1 through December 31 of 2019.
- **Any output order:** The solution intentionally omits `ORDER BY` because the contract does not require it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` denote the total number of relevant input rows. A database may scan, join, group, and sort or hash rows depending on its plan. Under a conservative sort-based aggregation and join bound, time is `O(r log r)` and intermediate storage is `O(r)`, matching the manifest.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
