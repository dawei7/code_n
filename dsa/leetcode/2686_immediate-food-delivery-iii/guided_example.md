# Guided Example: Immediate Food Delivery III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 8, "customer_id": 1, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 9, "customer_id": 5, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-08"}, {"delivery_id": 10, "customer_id": 2, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-18"}]}}`
- **Required output:** `{"columns": ["order_date", "immediate_percentage"], "rows": [["2019-08-01", 66.67], ["2019-08-02", 66.67], ["2019-08-03", 100.0], ["2019-08-04", 0.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Delivery`

The objective is to compute `{"columns": ["order_date", "immediate_percentage"], "rows": [["2019-08-01", 66.67], ["2019-08-02", 66.67], ["2019-08-03", 100.0], ["2019-08-04", 0.0]]}` from `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 8, "customer_id": 1, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 9, "customer_id": 5, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-08"}, {"delivery_id": 10, "customer_id": 2, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-18"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each order into a zero-or-one indicator

An order is immediate exactly when `customer_pref_delivery_date = order_date`.

For aggregation, it is useful to translate that Boolean fact into a number:

- immediate order becomes 1;
- scheduled order becomes 0.

The MySQL expression `IF(customer_pref_delivery_date = order_date, 1, 0)` performs this translation for every row.

Once rows are indicators, counting immediate orders is just summing them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 8, "customer_id": 1, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 9, "customer_id": 5, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-08"}, {"delivery_id": 10, "customer_id": 2, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-18"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group by the date being reported

The requested result has one row for each unique `order_date`. The clause `GROUP BY order_date` partitions all deliveries according to that column.

Every aggregate in the `SELECT` list is evaluated separately within one date's group:

- `SUM(IF(...))` is the number of immediate orders on that date;
- `COUNT(*)` is the total number of orders on that date.

No customer grouping is involved. The same customer may order on several dates, and each row contributes to its own order-date group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The requested result has one row for each unique `order_date... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute a percentage rather than a fraction

For a group with $I$ immediate orders and $T$ total orders, the desired value is:

$$
100\cdot\frac{I}{T}.
$$

The query writes `100 * SUM(...) / COUNT(*)`.

Multiplying by 100 converts the proportion into percentage points. Without that factor, two immediate orders out of three would produce approximately 0.67 rather than 66.67.

Every emitted group has at least one row, so `COUNT(*)` is positive and division by zero cannot occur.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["order_date", "immediate_percentage"], "rows": [["2019-08-01", 66.67], ["2019-08-02", 66.67], ["2019-08-03", 100.0], ["2019-08-04", 0.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-01"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 8, "customer_id": 1, "order_date": "2019-08-03", "customer_pref_delivery_date": "2019-08-03"}, {"delivery_id": 9, "customer_id": 5, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-08"}, {"delivery_id": 10, "customer_id": 2, "order_date": "2019-08-04", "customer_pref_delivery_date": "2019-08-18"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["order_date", "immediate_percentage"], "rows": [["2019-08-01", 66.67], ["2019-08-02", 66.67], ["2019-08-03", 100.0], ["2019-08-04", 0.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Average the Boolean condition:** In MySQL, `10:** - **Average the Boolean condition:** In MySQL, `100 * AVG(condition)` can express the same indicator ratio, but the explicit sum and count are easier to derive.
- **Conditional `COUNT`:** Counting only immediate rows also works if null behavior is handled carefully.
- **Correlated subquery per date:** Correct but needlessly repeats work.
- **Group by customer:** Incorrect because the requested denominator is orders on each date.
- **All immediate:** The ratio is one and the percentage is 100.00.
- **All scheduled:** The numerator is zero and the percentage is 0.00.
- **One order on a date:** Its percentage is either 100.00 or 0.00.
- **Repeating customers:** Each delivery row still counts independently.
- **Rounding:** Apply it after division, not to intermediate counts.
- **Ascending dates:** The explicit `ORDER BY` makes output deterministic by date.
- **Nonempty groups:** `COUNT(*)` cannot be zero for a produced date.
- **SQL execution plans:** Indexes may improve physical performance without changing the query's logical result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of delivery rows and $D$ the number of distinct order dates. The database must scan $R$ rows. Grouping and final ordering are commonly bounded by $O(R\log R)$ time without assuming a favorable index or hash aggregation plan.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
