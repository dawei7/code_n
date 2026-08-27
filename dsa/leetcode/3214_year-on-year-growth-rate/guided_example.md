# Guided Example: Year on Year Growth Rate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"user_transactions": [{"transaction_id": 1341, "product_id": 123424, "spend": 1500.6, "transaction_date": "2019-12-31 12:00:00"}, {"transaction_id": 1423, "product_id": 123424, "spend": 1000.2, "transaction_date": "2020-12-31 12:00:00"}, {"transaction_id": 1623, "product_id": 123424, "spend": 1246.44, "transaction_date": "2021-12-31 12:00:00"}, {"transaction_id": 1322, "product_id": 123424, "spend": 2145.32, "transaction_date": "2022-12-31 12:00:00"}]}}`
- **Required output:** `{"columns": ["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"], "rows": [[2019, 123424, 1500.6, null, null], [2020, 123424, 1000.2, 1500.6, -33.35], [2021, 123424, 1246.44, 1000.2, 24.62], [2022, 123424, 2145.32, 1246.44, 72.12]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{user}_{transactions}$

The objective is to compute `{"columns": ["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"], "rows": [[2019, 123424, 1500.6, null, null], [2020, 123424, 1000.2, 1500.6, -33.35], [2021, 123424, 1246.44, 1000.2, 24.62], [2022, 123424, 2145.32, 1246.44, 72.12]]}` from `{"tables": {"user_transactions": [{"transaction_id": 1341, "product_id": 123424, "spend": 1500.6, "transaction_date": "2019-12-31 12:00:00"}, {"transaction_id": 1423, "product_id": 123424, "spend": 1000.2, "transaction_date": "2020-12-31 12:00:00"}, {"transaction_id": 1623, "product_id": 123424, "spend": 1246.44, "transaction_date": "2021-12-31 12:00:00"}, {"transaction_id": 1322, "product_id": 123424, "spend": 2145.32, "transaction_date": "2022-12-31 12:00:00"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Aggregate transactions at the reporting grain first.** The required output has one row per product and calendar year, not one row per transaction. CTE `T` extracts `YEAR(transaction_date)` and groups by `product_id` and year. `SUM(spend)` produces `curr_year_spend` for that product-year.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"user_transactions": [{"transaction_id": 1341, "product_id": 123424, "spend": 1500.6, "transaction_date": "2019-12-31 12:00:00"}, {"transaction_id": 1423, "product_id": 123424, "spend": 1000.2, "transaction_date": "2020-12-31 12:00:00"}, {"transaction_id": 1623, "product_id": 123424, "spend": 1246.44, "transaction_date": "2021-12-31 12:00:00"}, {"transaction_id": 1322, "product_id": 123424, "spend": 2145.32, "transaction_date": "2022-12-31 12:00:00"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Doing this before previous-year matching is essential. Joining raw transactions from adjacent years could form every pair of transactions across the years and multiply spend totals. One annual row per side makes the later relationship one-to-one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Doing this before previous-year matching is essential.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Match the exact preceding calendar year.** CTE `S` takes each annual row `t1` and left joins another annual row `t2` when:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"], "rows": [[2019, 123424, 1500.6, null, null], [2020, 123424, 1000.2, 1500.6, -33.35], [2021, 123424, 1246.44, 1000.2, 24.62], [2022, 123424, 2145.32, 1246.44, 72.12]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"user_transactions": [{"transaction_id": 1341, "product_id": 123424, "spend": 1500.6, "transaction_date": "2019-12-31 12:00:00"}, {"transaction_id": 1423, "product_id": 123424, "spend": 1000.2, "transaction_date": "2020-12-31 12:00:00"}, {"transaction_id": 1623, "product_id": 123424, "spend": 1246.44, "transaction_date": "2021-12-31 12:00:00"}, {"transaction_id": 1322, "product_id": 123424, "spend": 2145.32, "transaction_date": "2022-12-31 12:00:00"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"], "rows": [[2019, 123424, 1500.6, null, null], [2020, 123424, 1000.2, 1500.6, -33.35], [2021, 123424, 1246.44, 1000.2, 24.62], [2022, 123424, 2145.32, 1246.44, 72.12]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window `LAG` with gap check:** Compute lagged :** - **Window `LAG` with gap check:** Compute lagged year and spend, then use the prior spend only when `previous_year = year - 1`. The explicit gap check makes it equivalent to the self-join.
- **Bare `LAG`:** Shorter, but incorrect for exact previous-calendar-year semantics when a product skips a year.
- **Correlated subquery:** Look up the same product at `year-1` for each annual row. It is readable but may execute less efficiently without suitable indexing.
- **First recorded year:** No exact prior row exists, so both `prev_year_spend` and `yoy_rate` are null.
- **Gap in years:** A 2021 row does not borrow 2019 merely because it is the previous available record.
- **Several transactions in one year:** `SUM` combines them before any growth calculation.
- **Several products:** Product equality in the join prevents one product's spend from becoming another's baseline.
- **Decreasing spend:** The numerator is negative and produces a negative percentage.
- **No change:** Equal totals produce zero percent.
- **Previous spend zero:** Division by zero yields null or an engine warning under MySQL settings; the exact source provides no special interpretation.
- **Null spend values:** `SUM` ignores null inputs under ordinary SQL semantics; all-null groups can produce null and propagate through the rate.
- **Rounding order:** Only the final ratio is rounded, preserving annual totals and intermediate precision.
- **Datetime extraction:** Transactions at any time within the same calendar year share the extracted year.
- **Positional ordering:** `ORDER BY 2,1` depends on select-column positions; explicit names would be safer during schema changes.
- **Manifest mismatch:** The exact implementation is annual aggregation plus exact-year self-join, not a partitioned lag.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t)$. Let $t$ be the number of transaction rows and $g$ the number of distinct product-year groups. Extracting years and aggregating can be $O(t)$ with hashing or $O(t\log t)$ with sort-based grouping. Joining the $g$ annual rows to themselves on indexed or hashed product/year keys can be $O(g)$ expected, while a sort-merge plan is $O(g\log g)$. Final ordering costs $O(g\log g)$.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
