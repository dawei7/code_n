# Guided Example: Seasonal Sales Analysis

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"sales": [{"sale_id": 1, "product_id": 1, "sale_date": "2023-01-15", "quantity": 5, "price": 10.0}, {"sale_id": 2, "product_id": 2, "sale_date": "2023-01-20", "quantity": 4, "price": 15.0}, {"sale_id": 3, "product_id": 3, "sale_date": "2023-03-10", "quantity": 3, "price": 18.0}, {"sale_id": 4, "product_id": 4, "sale_date": "2023-04-05", "quantity": 1, "price": 20.0}, {"sale_id": 5, "product_id": 1, "sale_date": "2023-05-20", "quantity": 2, "price": 10.0}, {"sale_id": 6, "product_id": 2, "sale_date": "2023-06-12", "quantity": 4, "price": 15.0}, {"sale_id": 7, "product_id": 5, "sale_date": "2023-06-15", "quantity": 5, "price": 12.0}, {"sale_id": 8, "product_id": 3, "sale_date": "2023-07-24", "quantity": 2, "price": 18.0}, {"sale_id": 9, "product_id": 4, "sale_date": "2023-08-01", "quantity": 5, "price": 20.0}, {"sale_id": 10, "product_id": 5, "sale_date": "2023-09-03", "quantity": 3, "price": 12.0}, {"sale_id": 11, "product_id": 1, "sale_date": "2023-09-25", "quantity": 6, "price": 10.0}, {"sale_id": 12, "product_id": 2, "sale_date": "2023-11-10", "quantity": 4, "price": 15.0}, {"sale_id": 13, "product_id": 3, "sale_date": "2023-12-05", "quantity": 6, "price": 18.0}, {"sale_id": 14, "product_id": 4, "sale_date": "2023-12-22", "quantity": 3, "price": 20.0}, {"sale_id": 15, "product_id": 5, "sale_date": "2024-02-14", "quantity": 2, "price": 12.0}], "products": [{"product_id": 1, "product_name": "Warm Jacket", "category": "Apparel"}, {"product_id": 2, "product_name": "Designer Jeans", "category": "Apparel"}, {"product_id": 3, "product_name": "Cutting Board", "category": "Kitchen"}, {"product_id": 4, "product_name": "Smart Speaker", "category": "Tech"}, {"product_id": 5, "product_name": "Yoga Mat", "category": "Fitness"}]}}`
- **Required output:** `{"columns": ["season", "category", "total_quantity", "total_revenue"], "rows": [["Fall", "Apparel", 10, 120.0], ["Spring", "Kitchen", 3, 54.0], ["Summer", "Tech", 5, 100.0], ["Winter", "Apparel", 9, 110.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `sales`

The objective is to compute `{"columns": ["season", "category", "total_quantity", "total_revenue"], "rows": [["Fall", "Apparel", 10, 120.0], ["Spring", "Kitchen", 3, 54.0], ["Summer", "Tech", 5, 100.0], ["Winter", "Apparel", 9, 110.0]]}` from `{"tables": {"sales": [{"sale_id": 1, "product_id": 1, "sale_date": "2023-01-15", "quantity": 5, "price": 10.0}, {"sale_id": 2, "product_id": 2, "sale_date": "2023-01-20", "quantity": 4, "price": 15.0}, {"sale_id": 3, "product_id": 3, "sale_date": "2023-03-10", "quantity": 3, "price": 18.0}, {"sale_id": 4, "product_id": 4, "sale_date": "2023-04-05", "quantity": 1, "price": 20.0}, {"sale_id": 5, "product_id": 1, "sale_date": "2023-05-20", "quantity": 2, "price": 10.0}, {"sale_id": 6, "product_id": 2, "sale_date": "2023-06-12", "quantity": 4, "price": 15.0}, {"sale_id": 7, "product_id": 5, "sale_date": "2023-06-15", "quantity": 5, "price": 12.0}, {"sale_id": 8, "product_id": 3, "sale_date": "2023-07-24", "quantity": 2, "price": 18.0}, {"sale_id": 9, "product_id": 4, "sale_date": "2023-08-01", "quantity": 5, "price": 20.0}, {"sale_id": 10, "product_id": 5, "sale_date": "2023-09-03", "quantity": 3, "price": 12.0}, {"sale_id": 11, "product_id": 1, "sale_date": "2023-09-25", "quantity": 6, "price": 10.0}, {"sale_id": 12, "product_id": 2, "sale_date": "2023-11-10", "quantity": 4, "price": 15.0}, {"sale_id": 13, "product_id": 3, "sale_date": "2023-12-05", "quantity": 6, "price": 18.0}, {"sale_id": 14, "product_id": 4, "sale_date": "2023-12-22", "quantity": 3, "price": 20.0}, {"sale_id": 15, "product_id": 5, "sale_date": "2024-02-14", "quantity": 2, "price": 12.0}], "products": [{"product_id": 1, "product_name": "Warm Jacket", "category": "Apparel"}, {"product_id": 2, "product_name": "Designer Jeans", "category": "Apparel"}, {"product_id": 3, "product_name": "Cutting Board", "category": "Kitchen"}, {"product_id": 4, "product_name": "Smart Speaker", "category": "Tech"}, {"product_id": 5, "product_name": "Yoga Mat", "category": "Fitness"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Classifying each sale into a season

`MONTH(sale_date)` extracts an integer from one through twelve. The `CASE` expression maps all twelve months:

- `12, 1, 2` to Winter;
- `3, 4, 5` to Spring;
- `6, 7, 8` to Summer;
- `9, 10, 11` to Fall.

December and January belonging to the same season does not require grouping by year; the requested output combines all sales for a named season across the available data. Since every valid date has one of these months, the `CASE` covers every joined sale and needs no `ELSE` branch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"sales": [{"sale_id": 1, "product_id": 1, "sale_date": "2023-01-15", "quantity": 5, "price": 10.0}, {"sale_id": 2, "product_id": 2, "sale_date": "2023-01-20", "quantity": 4, "price": 15.0}, {"sale_id": 3, "product_id": 3, "sale_date": "2023-03-10", "quantity": 3, "price": 18.0}, {"sale_id": 4, "product_id": 4, "sale_date": "2023-04-05", "quantity": 1, "price": 20.0}, {"sale_id": 5, "product_id": 1, "sale_date": "2023-05-20", "quantity": 2, "price": 10.0}, {"sale_id": 6, "product_id": 2, "sale_date": "2023-06-12", "quantity": 4, "price": 15.0}, {"sale_id": 7, "product_id": 5, "sale_date": "2023-06-15", "quantity": 5, "price": 12.0}, {"sale_id": 8, "product_id": 3, "sale_date": "2023-07-24", "quantity": 2, "price": 18.0}, {"sale_id": 9, "product_id": 4, "sale_date": "2023-08-01", "quantity": 5, "price": 20.0}, {"sale_id": 10, "product_id": 5, "sale_date": "2023-09-03", "quantity": 3, "price": 12.0}, {"sale_id": 11, "product_id": 1, "sale_date": "2023-09-25", "quantity": 6, "price": 10.0}, {"sale_id": 12, "product_id": 2, "sale_date": "2023-11-10", "quantity": 4, "price": 15.0}, {"sale_id": 13, "product_id": 3, "sale_date": "2023-12-05", "quantity": 6, "price": 18.0}, {"sale_id": 14, "product_id": 4, "sale_date": "2023-12-22", "quantity": 3, "price": 20.0}, {"sale_id": 15, "product_id": 5, "sale_date": "2024-02-14", "quantity": 2, "price": 12.0}], "products": [{"product_id": 1, "product_name": "Warm Jacket", "category": "Apparel"}, {"product_id": 2, "product_name": "Designer Jeans", "category": "Apparel"}, {"product_id": 3, "product_name": "Cutting Board", "category": "Kitchen"}, {"product_id": 4, "product_name": "Smart Speaker", "category": "Tech"}, {"product_id": 5, "product_name": "Yoga Mat", "category": "Fitness"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Attaching categories

`sales JOIN products USING (product_id)` matches each sale to its product row. `products.product_id` is unique, so one sale obtains exactly one category.

The product name is irrelevant to seasonal category totals. The query carries only the category plus sale quantity, sale price, and derived season.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregating quantity and revenue

`SeasonalSales` groups by the first two selected expressions, which are `season` and `category`.

For each group:

- `SUM(quantity)` gives the category’s total number of units sold in that season;
- `SUM(quantity * price)` gives total revenue, correctly calculating revenue at each sale row’s actual price before summing.

Computing `SUM(quantity) * price` after grouping would be invalid when the same category’s sale rows have different prices. Row-level multiplication preserves the correct contribution of every sale.

After this CTE, there is one row per season-category combination that appears in the data. The much larger sale relation has been compressed to the exact grain needed for comparison.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["season", "category", "total_quantity", "total_revenue"], "rows": [["Fall", "Apparel", 10, 120.0], ["Spring", "Kitchen", 3, 54.0], ["Summer", "Tech", 5, 100.0], ["Winter", "Apparel", 9, 110.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"sales": [{"sale_id": 1, "product_id": 1, "sale_date": "2023-01-15", "quantity": 5, "price": 10.0}, {"sale_id": 2, "product_id": 2, "sale_date": "2023-01-20", "quantity": 4, "price": 15.0}, {"sale_id": 3, "product_id": 3, "sale_date": "2023-03-10", "quantity": 3, "price": 18.0}, {"sale_id": 4, "product_id": 4, "sale_date": "2023-04-05", "quantity": 1, "price": 20.0}, {"sale_id": 5, "product_id": 1, "sale_date": "2023-05-20", "quantity": 2, "price": 10.0}, {"sale_id": 6, "product_id": 2, "sale_date": "2023-06-12", "quantity": 4, "price": 15.0}, {"sale_id": 7, "product_id": 5, "sale_date": "2023-06-15", "quantity": 5, "price": 12.0}, {"sale_id": 8, "product_id": 3, "sale_date": "2023-07-24", "quantity": 2, "price": 18.0}, {"sale_id": 9, "product_id": 4, "sale_date": "2023-08-01", "quantity": 5, "price": 20.0}, {"sale_id": 10, "product_id": 5, "sale_date": "2023-09-03", "quantity": 3, "price": 12.0}, {"sale_id": 11, "product_id": 1, "sale_date": "2023-09-25", "quantity": 6, "price": 10.0}, {"sale_id": 12, "product_id": 2, "sale_date": "2023-11-10", "quantity": 4, "price": 15.0}, {"sale_id": 13, "product_id": 3, "sale_date": "2023-12-05", "quantity": 6, "price": 18.0}, {"sale_id": 14, "product_id": 4, "sale_date": "2023-12-22", "quantity": 3, "price": 20.0}, {"sale_id": 15, "product_id": 5, "sale_date": "2024-02-14", "quantity": 2, "price": 12.0}], "products": [{"product_id": 1, "product_name": "Warm Jacket", "category": "Apparel"}, {"product_id": 2, "product_name": "Designer Jeans", "category": "Apparel"}, {"product_id": 3, "product_name": "Cutting Board", "category": "Kitchen"}, {"product_id": 4, "product_name": "Smart Speaker", "category": "Tech"}, {"product_id": 5, "product_name": "Yoga Mat", "category": "Fitness"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["season", "category", "total_quantity", "total_revenue"], "rows": [["Fall", "Apparel", 10, 120.0], ["Spring", "Kitchen", 3, 54.0], ["Summer", "Tech", 5, 100.0], ["Winter", "Apparel", 9, 110.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correct complete ranking:** Use `ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC, category ASC)` and keep row one. This fixes the exact source’s equal-quantity/equal-revenue defect.
- **Add category to the existing RANK:** Because each category appears once per season after aggregation, appending `category ASC` also makes rank one unique. `ROW_NUMBER` communicates the single-winner requirement more directly.
- **Correlated maximum subqueries:** One can compare each group against maximum quantities and revenues, but nested tie logic is harder to read and can repeat aggregation work.
- **Aggregate revenue incorrectly:** `SUM(quantity * price)` is essential when prices vary by sale. Multiplying an aggregate quantity by one arbitrary price would be wrong.
- **Quantity leader:** A category with strictly largest total quantity wins regardless of revenue.
- **Revenue tie-breaker:** Revenue matters only among categories tied on total quantity.
- **Complete tie:** The current source returns multiple categories; the required result should keep only the lexicographically smaller one.
- **One category in a season:** It receives rank one automatically.
- **Missing season:** No synthetic row is generated. Producing all four seasons would require a season dimension and an outer join, which the statement does not demand.
- **Sales across years:** Rows are grouped by season name without year, so all Winters are combined. That follows the selected grouping columns.
- **December mapping:** December is explicitly listed with January and February, preventing the common mistake of treating seasons as simple consecutive quarter numbers.
- **Decimal revenue:** MySQL preserves an appropriate decimal result for multiplication and summation, avoiding binary floating-point comparison in the SQL expression.
- **Final season order:** `ORDER BY season` is lexicographic, not Winter-Spring-Summer-Fall chronology. It matches “season ascending” as a string column.
- **Join integrity:** The unique product identifier ensures one category per joined sale. Missing product rows would be excluded by the inner join.
- **Unused product name:** Popularity is category-based, so product names correctly do not affect grouping or ties.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S log S + P log P + G log G)$. Physical SQL complexity depends on indexes, join strategy, whether CTEs are materialized, and whether grouping/window ordering uses hashes, in-memory sorting, or disk spills. The query specifies logical operations rather than a single mandatory execution plan.
- **Auxiliary Space Complexity:** $O(S + P + G)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
