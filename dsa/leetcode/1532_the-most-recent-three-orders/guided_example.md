# Guided Example: The Most Recent Three Orders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "cost": 30}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "cost": 40}, {"order_id": 3, "order_date": "2020-07-31", "customer_id": 3, "cost": 70}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "cost": 100}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "cost": 1010}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "cost": 102}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "cost": 111}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "cost": 99}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "cost": 32}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "cost": 2}]}}`
- **Required output:** `{"columns": ["customer_name", "customer_id", "order_id", "order_date"], "rows": [["Annabelle", 3, 7, "2020-08-01"], ["Annabelle", 3, 3, "2020-07-31"], ["Jonathan", 2, 9, "2020-08-07"], ["Jonathan", 2, 6, "2020-08-01"], ["Jonathan", 2, 2, "2020-07-30"], ["Marwan", 4, 4, "2020-07-29"], ["Winston", 1, 8, "2020-08-03"], ["Winston", 1, 1, "2020-07-31"], ["Winston", 1, 10, "2020-07-15"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["customer_name", "customer_id", "order_id", "order_date"], "rows": [["Annabelle", 3, 7, "2020-08-01"], ["Annabelle", 3, 3, "2020-07-31"], ["Jonathan", 2, 9, "2020-08-07"], ["Jonathan", 2, 6, "2020-08-01"], ["Jonathan", 2, 2, "2020-07-30"], ["Marwan", 4, 4, "2020-07-29"], ["Winston", 1, 8, "2020-08-03"], ["Winston", 1, 1, "2020-07-31"], ["Winston", 1, 10, "2020-07-15"]]}` from `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "cost": 30}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "cost": 40}, {"order_id": 3, "order_date": "2020-07-31", "customer_id": 3, "cost": 70}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "cost": 100}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "cost": 1010}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "cost": 102}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "cost": 111}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "cost": 99}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "cost": 32}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "cost": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rank orders independently for each customer

The requested limit is not three rows for the whole table. It is at most three rows for every customer who has placed an order. That makes this a grouped top-$k$ query: orders must first be separated by `customer_id`, then ranked from newest to oldest inside each customer's group.

The common table expression named `T` performs exactly that preparation. It joins `Orders` with `Customers` through `JOIN Customers USING (customer_id)`, so each order row gains the corresponding customer name. Because this is an inner join, a customer with no order does not create a result row. That matches a report whose rows represent actual orders.

The query selects every joined column temporarily because the outer query will need the customer's name and identifier as well as the order's identifier and date. The `cost` column survives inside `T` but is intentionally not projected by the final `SELECT`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "cost": 30}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "cost": 40}, {"order_id": 3, "order_date": "2020-07-31", "customer_id": 3, "cost": 70}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "cost": 100}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "cost": 1010}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "cost": 102}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "cost": 111}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "cost": 99}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "cost": 32}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "cost": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why ROW_NUMBER is the right window function

`ROW_NUMBER() OVER (...)` assigns consecutive integers one, two, three, and so on to rows without collapsing them. Its `PARTITION BY customer_id` clause restarts the numbering whenever the customer changes. Therefore, every customer has a private ranking sequence rather than competing with every other customer.

Within a partition, `ORDER BY order_date DESC` places the most recent date first. Rank one is the newest order, rank two is the next newest, and rank three is the third newest.

The statement guarantees that a customer has at most one order on any date. Consequently, two orders belonging to the same customer cannot tie on `order_date`. No additional order-id tiebreaker is required to make the top three deterministic.

`ROW_NUMBER` is preferable to `RANK` for expressing a fixed row count. If date ties were possible, `RANK` could assign the same rank to multiple rows and `rk <= 3` might return more than three orders. The no-duplicate-date guarantee prevents ambiguity here, but `ROW_NUMBER` still states the intended row limit directly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Filter only after ranking

The outer query applies `WHERE rk <= 3`. Filtering must happen after the window value has been computed. If rows were limited globally before partitioned ranking, orders of one customer could consume positions needed by another customer.

A customer with at least three orders contributes exactly the rows ranked one through three. A customer with one or two orders contributes all available rows, because all their ranks are at most three. This handles the “less than three” rule without a separate count or conditional branch.

For Winston in the example, the dates sort as August 3, July 31, July 15, and June 10. Their ranks are one through four in that order. The filter retains the first three and removes only June 10. Annabelle has ranks one and two, so neither row is removed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_name", "customer_id", "order_id", "order_date"], "rows": [["Annabelle", 3, 7, "2020-08-01"], ["Annabelle", 3, 3, "2020-07-31"], ["Jonathan", 2, 9, "2020-08-07"], ["Jonathan", 2, 6, "2020-08-01"], ["Jonathan", 2, 2, "2020-07-30"], ["Marwan", 4, 4, "2020-07-29"], ["Winston", 1, 8, "2020-08-03"], ["Winston", 1, 1, "2020-07-31"], ["Winston", 1, 10, "2020-07-15"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "name": "Winston"}, {"customer_id": 2, "name": "Jonathan"}, {"customer_id": 3, "name": "Annabelle"}, {"customer_id": 4, "name": "Marwan"}, {"customer_id": 5, "name": "Khaled"}], "Orders": [{"order_id": 1, "order_date": "2020-07-31", "customer_id": 1, "cost": 30}, {"order_id": 2, "order_date": "2020-07-30", "customer_id": 2, "cost": 40}, {"order_id": 3, "order_date": "2020-07-31", "customer_id": 3, "cost": 70}, {"order_id": 4, "order_date": "2020-07-29", "customer_id": 4, "cost": 100}, {"order_id": 5, "order_date": "2020-06-10", "customer_id": 1, "cost": 1010}, {"order_id": 6, "order_date": "2020-08-01", "customer_id": 2, "cost": 102}, {"order_id": 7, "order_date": "2020-08-01", "customer_id": 3, "cost": 111}, {"order_id": 8, "order_date": "2020-08-03", "customer_id": 1, "cost": 99}, {"order_id": 9, "order_date": "2020-08-07", "customer_id": 2, "cost": 32}, {"order_id": 10, "order_date": "2020-07-15", "customer_id": 1, "cost": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_name", "customer_id", "order_id", "order_date"], "rows": [["Annabelle", 3, 7, "2020-08-01"], ["Annabelle", 3, 3, "2020-07-31"], ["Jonathan", 2, 9, "2020-08-07"], ["Jonathan", 2, 6, "2020-08-01"], ["Jonathan", 2, 2, "2020-07-30"], ["Marwan", 4, 4, "2020-07-29"], ["Winston", 1, 8, "2020-08-03"], ["Winston", 1, 1, "2020-07-31"], ["Winston", 1, 10, "2020-07-15"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correlated count:** Count, for each order, how many newer orders the same customer has and retain counts below three. It can be correct but is often more expensive and harder to read than a window rank.
- **RANK or DENSE_RANK:** These can return more than three rows when ranking values tie; `ROW_NUMBER` expresses a row limit directly.
- **Global LIMIT 3:** It returns only three orders overall and is therefore wrong for a per-customer requirement.
- **Customers with no orders:** The inner join omits them because there is no order row to report.
- **One or two orders:** Their ranks all satisfy `rk <= 3`, so every order is returned.
- **Exactly three orders:** All three survive without special handling.
- **More than three orders:** Only ranks one, two, and three survive.
- **Duplicate customer names:** The secondary ascending `customer_id` key gives the required deterministic grouping.
- **Same-day orders:** The contract excludes two orders by one customer on the same date, so date alone totally orders each partition.
- **Unused cost:** It participates in the intermediate wildcard row but is omitted from the final projection.
- **Positional ordering:** `ORDER BY 1, 2, 4 DESC` is concise but depends on select-column order; spelling out column names would be more robust to projection changes.
- **General most recent n:** Replace the literal three in the rank filter with the desired positive limit; the partitioning and ranking logic remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m\log m + c)$. Let $M$ be the number of order rows, $C$ the number of customer rows, and $R$ the number of returned rows. Here $R \le 3C$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
