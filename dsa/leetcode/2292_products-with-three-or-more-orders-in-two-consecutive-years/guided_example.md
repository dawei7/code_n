# Guided Example: Products With Three or More Orders in Two Consecutive Years

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_id": 1, "product_id": 1, "quantity": 7, "purchase_date": "2020-03-16"}, {"order_id": 2, "product_id": 1, "quantity": 4, "purchase_date": "2020-12-02"}, {"order_id": 3, "product_id": 1, "quantity": 7, "purchase_date": "2020-05-10"}, {"order_id": 4, "product_id": 1, "quantity": 6, "purchase_date": "2021-12-23"}, {"order_id": 5, "product_id": 1, "quantity": 5, "purchase_date": "2021-05-21"}, {"order_id": 6, "product_id": 1, "quantity": 6, "purchase_date": "2021-10-11"}, {"order_id": 7, "product_id": 2, "quantity": 6, "purchase_date": "2022-10-11"}]}}`
- **Required output:** `{"columns": ["product_id"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["product_id"], "rows": [[1]]}` from `{"tables": {"Orders": [{"order_id": 1, "product_id": 1, "quantity": 7, "purchase_date": "2020-03-16"}, {"order_id": 2, "product_id": 1, "quantity": 4, "purchase_date": "2020-12-02"}, {"order_id": 3, "product_id": 1, "quantity": 7, "purchase_date": "2020-05-10"}, {"order_id": 4, "product_id": 1, "quantity": 6, "purchase_date": "2021-12-23"}, {"order_id": 5, "product_id": 1, "quantity": 5, "purchase_date": "2021-05-21"}, {"order_id": 6, "product_id": 1, "quantity": 6, "purchase_date": "2021-10-11"}, {"order_id": 7, "product_id": 2, "quantity": 6, "purchase_date": "2022-10-11"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First reduce raw orders to one row per product and year

The condition concerns how many orders a product received in each calendar year. Individual purchase dates within a year no longer matter after their year is extracted.

The common table expression `P` groups `Orders` by `product_id` and `YEAR(purchase_date)`. Each resulting row represents one product-year combination.

`COUNT(1) >= 3 AS mark` counts order rows in that group and produces a MySQL Boolean value: one when the product has at least three orders that year, zero otherwise.

The query counts orders, not units. `quantity` is intentionally unused because a single order for quantity ten is still one order, while three order rows are three orders.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_id": 1, "product_id": 1, "quantity": 7, "purchase_date": "2020-03-16"}, {"order_id": 2, "product_id": 1, "quantity": 4, "purchase_date": "2020-12-02"}, {"order_id": 3, "product_id": 1, "quantity": 7, "purchase_date": "2020-05-10"}, {"order_id": 4, "product_id": 1, "quantity": 6, "purchase_date": "2021-12-23"}, {"order_id": 5, "product_id": 1, "quantity": 5, "purchase_date": "2021-05-21"}, {"order_id": 6, "product_id": 1, "quantity": 6, "purchase_date": "2021-10-11"}, {"order_id": 7, "product_id": 2, "quantity": 6, "purchase_date": "2022-10-11"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why calendar-year extraction is required

`YEAR(purchase_date)` maps every date to its calendar year. Consecutive years mean numerical year values differing by one, regardless of the months or days of the purchases.

Grouping by the full date would split orders too finely. Grouping only by product would lose the information needed to find two distinct adjacent years.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `YEAR(purchase_date)` maps every date to its calendar year.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep both qualifying and nonqualifying groups in the CTE

The exact CTE creates a row for every observed product-year and stores qualification in `mark`. It does not discard low-count groups with `HAVING`.

The outer `WHERE p1.mark AND p2.mark` later requires both joined years to qualify. In MySQL, nonzero Boolean values are true and zero values are false.

This two-phase layout separates “calculate yearly status” from “find adjacent qualifying statuses.”

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_id": 1, "product_id": 1, "quantity": 7, "purchase_date": "2020-03-16"}, {"order_id": 2, "product_id": 1, "quantity": 4, "purchase_date": "2020-12-02"}, {"order_id": 3, "product_id": 1, "quantity": 7, "purchase_date": "2020-05-10"}, {"order_id": 4, "product_id": 1, "quantity": 6, "purchase_date": "2021-12-23"}, {"order_id": 5, "product_id": 1, "quantity": 5, "purchase_date": "2021-05-21"}, {"order_id": 6, "product_id": 1, "quantity": 6, "purchase_date": "2021-10-11"}, {"order_id": 7, "product_id": 2, "quantity": 6, "purchase_date": "2022-10-11"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Filter with** `HAVING COUNT(*) >= 3`: The CTE :** - **Filter with** `HAVING COUNT(*) >= 3`: The CTE could retain only qualifying product-years, eliminating `mark` and the outer Boolean filter; the exact query keeps a mark column instead.
- **Window function over yearly groups:** `LAG` can compare the preceding qualifying year, but gaps and count filtering must be handled carefully.
- **Correlated subquery:** It can test for an adjacent qualifying year but may repeat aggregate work without suitable optimization.
- **Use** `SUM(quantity)`: That answers how many units were ordered, not how many orders occurred, and is incorrect here.
- **Exactly three orders:** `COUNT(1) >= 3` includes the boundary.
- **More than three orders:** The Boolean mark remains true; exact count is not needed later.
- **Three qualifying consecutive years:** Two join pairs are produced and `DISTINCT` returns one product row.
- **Gap between qualifying years:** Years differing by two or more do not join.
- **Only one qualifying year:** No two-year pair exists.
- **Low-count intervening year:** It prevents either adjacent pair from passing both marks.
- **Several products:** Product equality in the join prevents years from different products being paired.
- **Unique order IDs:** Each table row is one distinct order, supporting `COUNT(1)`.
- **Any output order:** Omitting `ORDER BY` is intentional.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r\log r)$. Let `r` be the number of order rows and `g` the number of distinct product-year groups. The physical cost depends on MySQL's execution plan and indexes.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
