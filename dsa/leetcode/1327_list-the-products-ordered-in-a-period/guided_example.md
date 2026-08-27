# Guided Example: List the Products Ordered in a Period

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Products": [{"product_id": 1, "product_name": "Leetcode Solutions", "product_category": "Book"}, {"product_id": 2, "product_name": "Jewels of Stringology", "product_category": "Book"}, {"product_id": 3, "product_name": "HP", "product_category": "Laptop"}, {"product_id": 4, "product_name": "Lenovo", "product_category": "Laptop"}, {"product_id": 5, "product_name": "Leetcode Kit", "product_category": "T-shirt"}], "Orders": [{"product_id": 1, "order_date": "2020-02-05", "unit": 60}, {"product_id": 1, "order_date": "2020-02-10", "unit": 70}, {"product_id": 2, "order_date": "2020-01-18", "unit": 30}, {"product_id": 2, "order_date": "2020-02-11", "unit": 80}, {"product_id": 3, "order_date": "2020-02-17", "unit": 2}, {"product_id": 3, "order_date": "2020-02-24", "unit": 3}, {"product_id": 4, "order_date": "2020-03-01", "unit": 20}, {"product_id": 4, "order_date": "2020-03-04", "unit": 30}, {"product_id": 4, "order_date": "2020-03-04", "unit": 60}, {"product_id": 5, "order_date": "2020-02-25", "unit": 50}, {"product_id": 5, "order_date": "2020-02-27", "unit": 50}, {"product_id": 5, "order_date": "2020-03-01", "unit": 50}]}}`
- **Required output:** `{"columns": ["product_name", "unit"], "rows": [["Leetcode Kit", 100], ["Leetcode Solutions", 130]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Products`

The objective is to compute `{"columns": ["product_name", "unit"], "rows": [["Leetcode Kit", 100], ["Leetcode Solutions", 130]]}` from `{"tables": {"Products": [{"product_id": 1, "product_name": "Leetcode Solutions", "product_category": "Book"}, {"product_id": 2, "product_name": "Jewels of Stringology", "product_category": "Book"}, {"product_id": 3, "product_name": "HP", "product_category": "Laptop"}, {"product_id": 4, "product_name": "Lenovo", "product_category": "Laptop"}, {"product_id": 5, "product_name": "Leetcode Kit", "product_category": "T-shirt"}], "Orders": [{"product_id": 1, "order_date": "2020-02-05", "unit": 60}, {"product_id": 1, "order_date": "2020-02-10", "unit": 70}, {"product_id": 2, "order_date": "2020-01-18", "unit": 30}, {"product_id": 2, "order_date": "2020-02-11", "unit": 80}, {"product_id": 3, "order_date": "2020-02-17", "unit": 2}, {"product_id": 3, "order_date": "2020-02-24", "unit": 3}, {"product_id": 4, "order_date": "2020-03-01", "unit": 20}, {"product_id": 4, "order_date": "2020-03-04", "unit": 30}, {"product_id": 4, "order_date": "2020-03-04", "unit": 60}, {"product_id": 5, "order_date": "2020-02-25", "unit": 50}, {"product_id": 5, "order_date": "2020-02-27", "unit": 50}, {"product_id": 5, "order_date": "2020-03-01", "unit": 50}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Joining orders to names

`Orders AS o JOIN Products AS p ON o.product_id = p.product_id` is an inner join.

Each order's foreign-key identifier matches the unique primary-key row in `Products`, attaching exactly one `product_name`. Products with no February order do not need to appear, so the inner join is appropriate.

Duplicate rows are allowed in `Orders`. They represent separate input rows and each contributes its `unit` value to the total. The query does not use `DISTINCT`, so it does not incorrectly discard them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Products": [{"product_id": 1, "product_name": "Leetcode Solutions", "product_category": "Book"}, {"product_id": 2, "product_name": "Jewels of Stringology", "product_category": "Book"}, {"product_id": 3, "product_name": "HP", "product_category": "Laptop"}, {"product_id": 4, "product_name": "Lenovo", "product_category": "Laptop"}, {"product_id": 5, "product_name": "Leetcode Kit", "product_category": "T-shirt"}], "Orders": [{"product_id": 1, "order_date": "2020-02-05", "unit": 60}, {"product_id": 1, "order_date": "2020-02-10", "unit": 70}, {"product_id": 2, "order_date": "2020-01-18", "unit": 30}, {"product_id": 2, "order_date": "2020-02-11", "unit": 80}, {"product_id": 3, "order_date": "2020-02-17", "unit": 2}, {"product_id": 3, "order_date": "2020-02-24", "unit": 3}, {"product_id": 4, "order_date": "2020-03-01", "unit": 20}, {"product_id": 4, "order_date": "2020-03-04", "unit": 30}, {"product_id": 4, "order_date": "2020-03-04", "unit": 60}, {"product_id": 5, "order_date": "2020-02-25", "unit": 50}, {"product_id": 5, "order_date": "2020-02-27", "unit": 50}, {"product_id": 5, "order_date": "2020-03-01", "unit": 50}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filtering February 2020 before aggregation

`WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'` keeps exactly dates whose year and month are February 2020.

Filtering occurs before `GROUP BY`, so January and March units never enter the product sums. This is critical: aggregating all dates first and filtering later would compute lifetime totals rather than the requested period.

Formatting includes the year, preventing February from another year from entering the result.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'` keeps e... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Grouping by product identity

`GROUP BY o.product_id` creates one group for every product with at least one surviving February order.

The selected `product_name` is functionally determined by `product_id` because `Products.product_id` is a primary key and the join attaches one product row. MySQL can therefore associate the unique name with the group.

In SQL modes or database systems requiring every nonaggregated selected column to appear explicitly, grouping by both `o.product_id` and `p.product_name` would be more portable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_name", "unit"], "rows": [["Leetcode Kit", 100], ["Leetcode Solutions", 130]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Products": [{"product_id": 1, "product_name": "Leetcode Solutions", "product_category": "Book"}, {"product_id": 2, "product_name": "Jewels of Stringology", "product_category": "Book"}, {"product_id": 3, "product_name": "HP", "product_category": "Laptop"}, {"product_id": 4, "product_name": "Lenovo", "product_category": "Laptop"}, {"product_id": 5, "product_name": "Leetcode Kit", "product_category": "T-shirt"}], "Orders": [{"product_id": 1, "order_date": "2020-02-05", "unit": 60}, {"product_id": 1, "order_date": "2020-02-10", "unit": 70}, {"product_id": 2, "order_date": "2020-01-18", "unit": 30}, {"product_id": 2, "order_date": "2020-02-11", "unit": 80}, {"product_id": 3, "order_date": "2020-02-17", "unit": 2}, {"product_id": 3, "order_date": "2020-02-24", "unit": 3}, {"product_id": 4, "order_date": "2020-03-01", "unit": 20}, {"product_id": 4, "order_date": "2020-03-04", "unit": 30}, {"product_id": 4, "order_date": "2020-03-04", "unit": 60}, {"product_id": 5, "order_date": "2020-02-25", "unit": 50}, {"product_id": 5, "order_date": "2020-02-27", "unit": 50}, {"product_id": 5, "order_date": "2020-03-01", "unit": 50}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_name", "unit"], "rows": [["Leetcode Kit", 100], ["Leetcode Solutions", 130]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Half-open date range:** It expresses the same :** - **Half-open date range:** It expresses the same month and can use an ordinary date index more effectively.
- **Conditional aggregation:** Group all orders and sum a `CASE` only for February, but extra logic is needed to exclude zero-total or absent-period products.
- **Correlated subquery per product:** It is valid but may repeatedly scan `Orders` without good indexing.
- **Exactly 100 units:** The inclusive `>=` condition retains the product.
- **Duplicate order rows:** Every row contributes because duplicates are explicitly allowed.
- **No February orders:** The product has no group and does not appear.
- **Orders in February of another year:** The `%Y-%m` comparison excludes them.
- **Several orders on one date:** All their units are summed; no daily deduplication is required.
- **Functional dependency:** Grouping by product ID identifies one name under the primary-key join, but explicit name grouping is more portable.
- **Aggregate alias in `HAVING`:** MySQL permits `unit` there; other dialects may require repeating `SUM(o.unit)`.
- **Any-order output:** No final sort is necessary, so consumers must not assume incidental order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p+o+k\log k)$. Let $p$ be the number of product rows, $o$ the number of order rows, and $k$ the number of product groups surviving the month filter.
- **Auxiliary Space Complexity:** $O(p+k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
