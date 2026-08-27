# Guided Example: Total Sales Amount by Year

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Product": [{"product_id": 1, "product_name": "LC Phone"}, {"product_id": 2, "product_name": "LC T-Shirt"}, {"product_id": 3, "product_name": "LC Keychain"}], "Sales": [{"product_id": 1, "period_start": "2019-01-25", "period_end": "2019-02-28", "average_daily_sales": 100}, {"product_id": 2, "period_start": "2018-12-01", "period_end": "2020-01-01", "average_daily_sales": 10}, {"product_id": 3, "period_start": "2019-12-01", "period_end": "2020-01-31", "average_daily_sales": 1}]}}`
- **Required output:** `{"columns": ["product_id", "product_name", "report_year", "total_amount"], "rows": [[1, "LC Phone", "2019", 3500], [2, "LC T-Shirt", "2018", 310], [2, "LC T-Shirt", "2019", 3650], [2, "LC T-Shirt", "2020", 10], [3, "LC Keychain", "2019", 31], [3, "LC Keychain", "2020", 31]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Product`

The objective is to compute `{"columns": ["product_id", "product_name", "report_year", "total_amount"], "rows": [[1, "LC Phone", "2019", 3500], [2, "LC T-Shirt", "2018", 310], [2, "LC T-Shirt", "2019", 3650], [2, "LC T-Shirt", "2020", 10], [3, "LC Keychain", "2019", 31], [3, "LC Keychain", "2020", 31]]}` from `{"tables": {"Product": [{"product_id": 1, "product_name": "LC Phone"}, {"product_id": 2, "product_name": "LC T-Shirt"}, {"product_id": 3, "product_name": "LC Keychain"}], "Sales": [{"product_id": 1, "period_start": "2019-01-25", "period_end": "2019-02-28", "average_daily_sales": 100}, {"product_id": 2, "period_start": "2018-12-01", "period_end": "2020-01-01", "average_daily_sales": 10}, {"product_id": 3, "period_start": "2019-12-01", "period_end": "2020-01-31", "average_daily_sales": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Expand one sales interval into the years it overlaps

Each `Sales` row describes one closed date interval and one average amount per day. The requested report needs a separate row for every calendar year touched by that interval. The exact query creates a tiny derived table `y` containing the only possible report years:

- 2018 with 365 days.
- 2019 with 365 days.
- 2020 with 366 days.

The 2020 value is different because 2020 is a leap year. Hard-coding these three rows is appropriate because the Reference explicitly bounds all dates to 2018 through 2020.

The first inner join matches a sales row with a year when

`YEAR(s.period_start) <= y.YEAR AND YEAR(s.period_end) >= y.YEAR`.

These inequalities say the sales interval begins no later than that year and ends no earlier than it. Equivalently, the interval overlaps that calendar year. A sale entirely within 2019 produces one joined row; a sale from late 2018 through early 2020 produces three.

An inner join is correct because a nonoverlapping year must not appear. Every valid sales interval overlaps at least one of the three allowed years.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Product": [{"product_id": 1, "product_name": "LC Phone"}, {"product_id": 2, "product_name": "LC T-Shirt"}, {"product_id": 3, "product_name": "LC Keychain"}], "Sales": [{"product_id": 1, "period_start": "2019-01-25", "period_end": "2019-02-28", "average_daily_sales": 100}, {"product_id": 2, "period_start": "2018-12-01", "period_end": "2020-01-01", "average_daily_sales": 10}, {"product_id": 3, "period_start": "2019-12-01", "period_end": "2020-01-31", "average_daily_sales": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert overlap endpoints into day-of-year positions

For each product-year overlap, the query needs the first and last included ordinal day inside that year.

The overlap's last day is:

- The year's final day when `YEAR(s.period_end) > y.YEAR`, because the sale continues beyond this report year.
- Otherwise `DAYOFYEAR(s.period_end)`, because the sale ends inside this report year.

The expression is

`IF(YEAR(s.period_end) > y.YEAR, y.days_of_year, DAYOFYEAR(s.period_end))`.

The overlap's first day is:

- Day one when `YEAR(s.period_start) < y.YEAR`, because the sale began in an earlier year and is already active on January 1.
- Otherwise `DAYOFYEAR(s.period_start)`, because the sale begins within this report year.

That expression is

`IF(YEAR(s.period_start) < y.YEAR, 1, DAYOFYEAR(s.period_start))`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each product-year overlap, the query needs the first and... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the formula adds one

Both `period_start` and `period_end` are inclusive. If ordinal start is $a$ and ordinal end is $b$, the number of included days is

$$
b-a+1.
$$

Without the final one, a one-day interval would incorrectly have zero days. The query multiplies this inclusive day count by `s.average_daily_sales` to obtain `total_amount`.

For the phone interval from 2019-01-25 through 2019-02-28, both endpoints lie in 2019. Their ordinal positions are 25 and 59, so the count is $59-25+1=35$. Multiplying by 100 produces 3500.

For the T-shirt interval from 2018-12-01 through 2020-01-01:

- The 2018 overlap begins at December 1 and ends at ordinal 365, giving 31 days.
- The 2019 overlap begins at day one and ends at day 365, giving 365 days.
- The 2020 overlap begins at day one and ends at January 1, also day one, giving one day.

The explicit `days_of_year` value makes the 2020 full-year boundary leap-year aware.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "product_name", "report_year", "total_amount"], "rows": [[1, "LC Phone", "2019", 3500], [2, "LC T-Shirt", "2018", 310], [2, "LC T-Shirt", "2019", 3650], [2, "LC T-Shirt", "2020", 10], [3, "LC Keychain", "2019", 31], [3, "LC Keychain", "2020", 31]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Product": [{"product_id": 1, "product_name": "LC Phone"}, {"product_id": 2, "product_name": "LC T-Shirt"}, {"product_id": 3, "product_name": "LC Keychain"}], "Sales": [{"product_id": 1, "period_start": "2019-01-25", "period_end": "2019-02-28", "average_daily_sales": 100}, {"product_id": 2, "period_start": "2018-12-01", "period_end": "2020-01-01", "average_daily_sales": 10}, {"product_id": 3, "period_start": "2019-12-01", "period_end": "2020-01-31", "average_daily_sales": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "product_name", "report_year", "total_amount"], "rows": [[1, "LC Phone", "2019", 3500], [2, "LC T-Shirt", "2018", 310], [2, "LC T-Shirt", "2019", 3650], [2, "LC T-Shirt", "2020", 10], [3, "LC Keychain", "2019", 31], [3, "LC Keychain", "2020", 31]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive calendar expansion:** Generate every:** - **Recursive calendar expansion:** Generate every overlapping year from the dates instead of hard-coding three rows. It generalizes beyond 2020 but is unnecessary for the fixed domain.
- **Intersection with `GREATEST` and `LEAST`:** Construct year-start and year-end dates, clamp interval endpoints, and use `DATEDIFF + 1`. This is more general and can make date semantics explicit.
- **Daily calendar table:** Join every active date and group by year. It is flexible but expands one row per day and performs far more work.
- **Interval inside one year:** Both ordinal endpoints come directly from `DAYOFYEAR`.
- **Interval spans a full report year:** The start becomes one and the end becomes `days_of_year`.
- **One-day interval:** The final `+ 1` produces one day rather than zero.
- **Leap year 2020:** Its last ordinal is 366; hard-coding 365 would undercount a full-year overlap.
- **Boundary on January 1:** `DAYOFYEAR` returns one, and inclusive arithmetic handles it correctly.
- **Boundary on December 31:** The ordinal equals that year's day count.
- **Product without sales:** It is absent because `Sales` drives the query, matching the contract.
- **Missing product lookup outside the intended relationship:** The product inner join would discard that sales row; valid data is expected to reference an existing product.
- **Fixed year domain:** A date outside 2018–2020 would not be fully represented because `y` contains only those years; the stated constraints make this safe.
- **Required ordering:** The final `ORDER BY` is essential because joins and `UNION ALL` do not promise result order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P + S + R)$. Let $P$ be the product count, $S$ the sales-row count, and $R$ the number of product-year rows produced. The report-year table has constant size three. Under hash or indexed joins, reading the source tables and generating overlaps costs $O(P+S+R)$ logical work, matching the manifest.
- **Auxiliary Space Complexity:** $O(P+S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
