# Guided Example: Customers With Strictly Increasing Purchases

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_date": "2019-07-01", "price": 1100}, {"order_id": 2, "customer_id": 1, "order_date": "2019-11-01", "price": 1200}, {"order_id": 3, "customer_id": 1, "order_date": "2020-05-26", "price": 3000}, {"order_id": 4, "customer_id": 1, "order_date": "2021-08-31", "price": 3100}, {"order_id": 5, "customer_id": 1, "order_date": "2022-12-07", "price": 4700}, {"order_id": 6, "customer_id": 2, "order_date": "2015-01-01", "price": 700}, {"order_id": 7, "customer_id": 2, "order_date": "2017-11-07", "price": 1000}, {"order_id": 8, "customer_id": 3, "order_date": "2017-01-01", "price": 900}, {"order_id": 9, "customer_id": 3, "order_date": "2018-11-07", "price": 900}]}}`
- **Required output:** `{"columns": ["customer_id"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["customer_id"], "rows": [[1]]}` from `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_date": "2019-07-01", "price": 1100}, {"order_id": 2, "customer_id": 1, "order_date": "2019-11-01", "price": 1200}, {"order_id": 3, "customer_id": 1, "order_date": "2020-05-26", "price": 3000}, {"order_id": 4, "customer_id": 1, "order_date": "2021-08-31", "price": 3100}, {"order_id": 5, "customer_id": 1, "order_date": "2022-12-07", "price": 4700}, {"order_id": 6, "customer_id": 2, "order_date": "2015-01-01", "price": 700}, {"order_id": 7, "customer_id": 2, "order_date": "2017-11-07", "price": 1000}, {"order_id": 8, "customer_id": 3, "order_date": "2017-01-01", "price": 900}, {"order_id": 9, "customer_id": 3, "order_date": "2018-11-07", "price": 900}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First aggregate orders into one row per customer-year

The inner query groups by `customer_id` and `YEAR(order_date)`. `SUM(price) AS total` turns all orders from the same customer in the same calendar year into the required annual purchase total.

After grouping, each customer has one row for every year in which they ordered. Missing years have no row, so the later condition must reject gaps rather than silently ignoring them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_date": "2019-07-01", "price": 1100}, {"order_id": 2, "customer_id": 1, "order_date": "2019-11-01", "price": 1200}, {"order_id": 3, "customer_id": 1, "order_date": "2020-05-26", "price": 3000}, {"order_id": 4, "customer_id": 1, "order_date": "2021-08-31", "price": 3100}, {"order_id": 5, "customer_id": 1, "order_date": "2022-12-07", "price": 4700}, {"order_id": 6, "customer_id": 2, "order_date": "2015-01-01", "price": 700}, {"order_id": 7, "customer_id": 2, "order_date": "2017-11-07", "price": 1000}, {"order_id": 8, "customer_id": 3, "order_date": "2017-01-01", "price": 900}, {"order_id": 9, "customer_id": 3, "order_date": "2018-11-07", "price": 900}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank annual totals from smallest to largest

Within each customer partition,

`RANK() OVER (PARTITION BY customer_id ORDER BY SUM(price))`

assigns rank 1 to the smallest annual total, rank 2 to the next strictly larger total, and so on. Equal totals receive the same rank, with later ranks potentially skipped.

For totals to be strictly increasing as years increase with no missing year, chronological year order and total-rank order must move together one step at a time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Within each customer partition,

`RANK() OVER (PARTITION BY ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The constant-difference transformation

The query computes

`rk = YEAR(order_date) - rank`.

Suppose a customer's considered years are consecutive:

$$
Y,\ Y+1,\ldots,Y+t.
$$

If totals are strictly increasing, their ascending ranks are

$$
1,\ 2,\ldots,t+1.
$$

Each difference is the same constant $Y-1$. Therefore a valid customer has exactly one distinct `rk` value.

The outer query groups these derived rows by customer and applies

`HAVING COUNT(DISTINCT rk) = 1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_date": "2019-07-01", "price": 1100}, {"order_id": 2, "customer_id": 1, "order_date": "2019-11-01", "price": 1200}, {"order_id": 3, "customer_id": 1, "order_date": "2020-05-26", "price": 3000}, {"order_id": 4, "customer_id": 1, "order_date": "2021-08-31", "price": 3100}, {"order_id": 5, "customer_id": 1, "order_date": "2022-12-07", "price": 4700}, {"order_id": 6, "customer_id": 2, "order_date": "2015-01-01", "price": 700}, {"order_id": 7, "customer_id": 2, "order_date": "2017-11-07", "price": 1000}, {"order_id": 8, "customer_id": 3, "order_date": "2017-01-01", "price": 900}, {"order_id": 9, "customer_id": 3, "order_date": "2018-11-07", "price": 900}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` adjacent comparison:** Aggregate annual :** - **`LAG` adjacent comparison:** Aggregate annual totals, compare each year and total with the previous row, then reject any gap or non-increase. This matches the manifest wording and is often easier to read.
- **Recursive calendar expansion:** Generate every year between first and last and left join totals, filling gaps with zero. It models the statement literally but is much heavier.
- **Equal totals:** `RANK` ties them and the constant-difference test rejects the customer.
- **Missing intermediate year:** Consecutive total ranks cannot keep pace with the larger year jump, so the customer fails.
- **One active year:** It qualifies vacuously.
- **Multiple orders in one year:** `SUM(price)` combines them before ranking.
- **Order ID uniqueness:** It prevents duplicate row identity ambiguity but is not otherwise used by the query.
- **Any result order:** The outer query has no `ORDER BY`, which is allowed.
- **Positive prices:** A missing year's zero necessarily breaks increase after any positive prior annual total.
- **Rank versus row number:** `RANK` tie behavior is essential for rejecting equal totals; arbitrary row numbering could mask them.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of order rows and $y$ the number of grouped customer-year rows. Grouping orders is typically $O(r)$ with hashing or $O(r\log r)$ with sorting. The window function must order annual groups within customer partitions, giving an overall plan commonly bounded by $O(r\log r)$.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
