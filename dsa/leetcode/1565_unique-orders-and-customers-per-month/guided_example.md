# Guided Example: Unique Orders and Customers Per Month

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_id": 1, "order_date": "2020-09-15", "customer_id": 1, "invoice": 30}, {"order_id": 2, "order_date": "2020-09-17", "customer_id": 2, "invoice": 90}, {"order_id": 3, "order_date": "2020-10-06", "customer_id": 3, "invoice": 20}, {"order_id": 4, "order_date": "2020-10-20", "customer_id": 3, "invoice": 21}, {"order_id": 5, "order_date": "2020-11-10", "customer_id": 1, "invoice": 10}, {"order_id": 6, "order_date": "2020-11-21", "customer_id": 2, "invoice": 15}, {"order_id": 7, "order_date": "2020-12-01", "customer_id": 4, "invoice": 55}, {"order_id": 8, "order_date": "2020-12-03", "customer_id": 4, "invoice": 77}, {"order_id": 9, "order_date": "2021-01-07", "customer_id": 3, "invoice": 31}, {"order_id": 10, "order_date": "2021-01-15", "customer_id": 2, "invoice": 20}]}}`
- **Required output:** `{"columns": ["month", "order_count", "customer_count"], "rows": [["2020-09", 2, 2], ["2020-10", 1, 1], ["2020-12", 2, 1], ["2021-01", 1, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["month", "order_count", "customer_count"], "rows": [["2020-09", 2, 2], ["2020-10", 1, 1], ["2020-12", 2, 1], ["2021-01", 1, 1]]}` from `{"tables": {"Orders": [{"order_id": 1, "order_date": "2020-09-15", "customer_id": 1, "invoice": 30}, {"order_id": 2, "order_date": "2020-09-17", "customer_id": 2, "invoice": 90}, {"order_id": 3, "order_date": "2020-10-06", "customer_id": 3, "invoice": 20}, {"order_id": 4, "order_date": "2020-10-20", "customer_id": 3, "invoice": 21}, {"order_id": 5, "order_date": "2020-11-10", "customer_id": 1, "invoice": 10}, {"order_id": 6, "order_date": "2020-11-21", "customer_id": 2, "invoice": 15}, {"order_id": 7, "order_date": "2020-12-01", "customer_id": 4, "invoice": 55}, {"order_id": 8, "order_date": "2020-12-03", "customer_id": 4, "invoice": 77}, {"order_id": 9, "order_date": "2021-01-07", "customer_id": 3, "invoice": 31}, {"order_id": 10, "order_date": "2021-01-15", "customer_id": 2, "invoice": 20}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter qualifying orders before grouping

Only orders whose `invoice` is strictly greater than twenty contribute to either requested count.

The `WHERE invoice > 20` clause removes all nonqualifying rows before monthly groups are formed. An invoice equal to twenty is excluded because the condition is strict, not greater-than-or-equal.

Filtering first has an important consequence: a month containing orders but no invoice above twenty produces no group and therefore no output row. This matches the example's omission of November.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_id": 1, "order_date": "2020-09-15", "customer_id": 1, "invoice": 30}, {"order_id": 2, "order_date": "2020-09-17", "customer_id": 2, "invoice": 90}, {"order_id": 3, "order_date": "2020-10-06", "customer_id": 3, "invoice": 20}, {"order_id": 4, "order_date": "2020-10-20", "customer_id": 3, "invoice": 21}, {"order_id": 5, "order_date": "2020-11-10", "customer_id": 1, "invoice": 10}, {"order_id": 6, "order_date": "2020-11-21", "customer_id": 2, "invoice": 15}, {"order_id": 7, "order_date": "2020-12-01", "customer_id": 4, "invoice": 55}, {"order_id": 8, "order_date": "2020-12-03", "customer_id": 4, "invoice": 77}, {"order_id": 9, "order_date": "2021-01-07", "customer_id": 3, "invoice": 31}, {"order_id": 10, "order_date": "2021-01-15", "customer_id": 2, "invoice": 20}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert each date into a year-month key

`DATE_FORMAT(order_date, '%Y-%m')` produces a fixed-width string such as `2020-09`.

Every date in the same calendar month and year receives the same key. Dates in the same month number but different years remain separate because the year is included.

The formatted expression is aliased as `month` and is the first selected column.

Using a two-digit month is important for stable representation. January is `01` rather than `1`, and the output always follows the required `YYYY-MM` format.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Group by the computed month

`GROUP BY 1` refers positionally to the first selected expression, the formatted month.

After the qualifying filter, all remaining rows sharing that key form one group. No separate ordering is required because the contract permits any output order.

Positional grouping is concise, although it depends on the select-list order. Spelling out the date-format expression or its alias would communicate the same relational operation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "order_count", "customer_count"], "rows": [["2020-09", 2, 2], ["2020-10", 1, 1], ["2020-12", 2, 1], ["2021-01", 1, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_id": 1, "order_date": "2020-09-15", "customer_id": 1, "invoice": 30}, {"order_id": 2, "order_date": "2020-09-17", "customer_id": 2, "invoice": 90}, {"order_id": 3, "order_date": "2020-10-06", "customer_id": 3, "invoice": 20}, {"order_id": 4, "order_date": "2020-10-20", "customer_id": 3, "invoice": 21}, {"order_id": 5, "order_date": "2020-11-10", "customer_id": 1, "invoice": 10}, {"order_id": 6, "order_date": "2020-11-21", "customer_id": 2, "invoice": 15}, {"order_id": 7, "order_date": "2020-12-01", "customer_id": 4, "invoice": 55}, {"order_id": 8, "order_date": "2020-12-03", "customer_id": 4, "invoice": 77}, {"order_id": 9, "order_date": "2021-01-07", "customer_id": 3, "invoice": 31}, {"order_id": 10, "order_date": "2021-01-15", "customer_id": 2, "invoice": 20}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "order_count", "customer_count"], "rows": [["2020-09", 2, 2], ["2020-10", 1, 1], ["2020-12", 2, 1], ["2021-01", 1, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation without WHERE:** Group all months and count qualifying rows with conditions, then remove zero-count groups. It is more verbose here.
- **COUNT star:** After filtering, `COUNT(*)` is equivalent to counting non-null unique order identifiers.
- **COUNT DISTINCT order id:** It is correct but redundant because order identifiers are already unique.
- **Count customer rows directly:** It is wrong when one customer has multiple qualifying orders in a month.
- **Invoice exactly twenty:** It is excluded by the strict greater-than condition.
- **Month with no qualifying invoice:** It does not appear in the result.
- **Several orders by one customer:** All count as orders, but the customer counts once that month.
- **Same customer across months:** The customer counts once independently in each month.
- **Same month across years:** Including the year keeps the groups separate.
- **Any output order:** No outer sorting clause is necessary.
- **Positional GROUP BY:** It relies on `month` remaining the first selected expression.
- **Date formatting:** Fixed-width `YYYY-MM` matches the required output type and value.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of order rows and $Q$ the number that pass the invoice filter.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
