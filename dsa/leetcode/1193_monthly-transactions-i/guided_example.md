# Guided Example: Monthly Transactions I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"id": 121, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2018-12-18"}, {"id": 122, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2018-12-19"}, {"id": 123, "country": "US", "state": "approved", "amount": 2000, "trans_date": "2019-01-01"}, {"id": 124, "country": "DE", "state": "approved", "amount": 2000, "trans_date": "2019-01-07"}]}}`
- **Required output:** `{"columns": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "rows": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "DE", 1, 1, 2000, 2000], ["2019-01", "US", 1, 1, 2000, 2000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "rows": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "DE", 1, 1, 2000, 2000], ["2019-01", "US", 1, 1, 2000, 2000]]}` from `{"tables": {"Transactions": [{"id": 121, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2018-12-18"}, {"id": 122, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2018-12-19"}, {"id": 123, "country": "US", "state": "approved", "amount": 2000, "trans_date": "2019-01-01"}, {"id": 124, "country": "DE", "state": "approved", "amount": 2000, "trans_date": "2019-01-07"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize each date to a month key

`DATE_FORMAT(trans_date, '%Y-%m')` converts a full date such as `2018-12-18` into the year-month string `2018-12`. Including the four-digit year is essential. Grouping only by a month number would incorrectly combine January transactions from different years.

The expression is aliased as `month`, which gives the first required output column and is also the first grouping expression.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"id": 121, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2018-12-18"}, {"id": 122, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2018-12-19"}, {"id": 123, "country": "US", "state": "approved", "amount": 2000, "trans_date": "2019-01-01"}, {"id": 124, "country": "DE", "state": "approved", "amount": 2000, "trans_date": "2019-01-07"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one group per month and country

The query ends with `GROUP BY 1, 2`. MySQL ordinal grouping means “group by the first and second expressions in the `SELECT` list.” Those expressions are the formatted month and `country`. Every transaction with the same formatted year-month and country is therefore aggregated into one row.

Using ordinals is concise but depends on select-list order. Writing the expressions explicitly would be more verbose and less sensitive to reordering.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count every transaction

`COUNT(1) AS trans_count` contributes one for every row in the group. Unlike counting a nullable column, counting the constant one cannot skip a row because the expression is never `NULL`. The result is the group’s total transaction count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "rows": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "DE", 1, 1, 2000, 2000], ["2019-01", "US", 1, 1, 2000, 2000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"id": 121, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2018-12-18"}, {"id": 122, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2018-12-19"}, {"id": 123, "country": "US", "state": "approved", "amount": 2000, "trans_date": "2019-01-01"}, {"id": 124, "country": "DE", "state": "approved", "amount": 2000, "trans_date": "2019-01-07"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "rows": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "DE", 1, 1, 2000, 2000], ["2019-01", "US", 1, 1, 2000, 2000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Portable `CASE` expressions:** Replace MySQL Boolean sums and `IF` with standard conditional `CASE` expressions. The logic and grouping remain the same.
- **Filter to approved rows in `WHERE`:** This would destroy the all-transaction count and total, so it cannot produce every requested aggregate in the same grouped query.
- **Separate approved and total subqueries:** Aggregate twice and join the results by month and country. It works but repeats grouping work and complicates groups with no approved rows.
- **No approved transactions in a group:** Every Boolean contribution and conditional amount contribution is zero, so both approved aggregates return zero.
- **All transactions approved:** Approved count equals total count, and approved amount equals total amount.
- **Same month number in different years:** `%Y-%m` keeps the years separate.
- **Same month in different countries:** Including `country` in the grouping key prevents cross-country combination.
- **Any output order:** Omitting `ORDER BY` is valid and avoids imposing unnecessary sorting for presentation.
- **Ordinal grouping:** `GROUP BY 1, 2` refers to formatted month and country. Changing the select-list order without updating these ordinals could silently alter grouping semantics.
- **MySQL-specific truth values:** `SUM(state = 'approved')` depends on MySQL converting true and false to one and zero. Other SQL dialects may require explicit conversion.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(g)$. Let $n$ be the number of rows in `Transactions` and $g$ be the number of distinct month-country groups.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
