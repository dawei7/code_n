# Guided Example: Find Golden Hour Customers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"restaurant_orders": [{"order_id": 1, "customer_id": 101, "order_timestamp": "2024-03-01 12:30:00", "order_amount": 25.5, "payment_method": "card", "order_rating": 5}, {"order_id": 2, "customer_id": 101, "order_timestamp": "2024-03-02 19:15:00", "order_amount": 32, "payment_method": "app", "order_rating": 4}, {"order_id": 3, "customer_id": 101, "order_timestamp": "2024-03-03 13:45:00", "order_amount": 28.75, "payment_method": "card", "order_rating": 5}, {"order_id": 4, "customer_id": 101, "order_timestamp": "2024-03-04 20:30:00", "order_amount": 41, "payment_method": "app", "order_rating": null}, {"order_id": 5, "customer_id": 102, "order_timestamp": "2024-03-01 11:30:00", "order_amount": 18.5, "payment_method": "cash", "order_rating": 4}, {"order_id": 6, "customer_id": 102, "order_timestamp": "2024-03-02 12:00:00", "order_amount": 22, "payment_method": "card", "order_rating": 3}, {"order_id": 7, "customer_id": 102, "order_timestamp": "2024-03-03 15:30:00", "order_amount": 19.75, "payment_method": "cash", "order_rating": null}, {"order_id": 8, "customer_id": 103, "order_timestamp": "2024-03-01 19:00:00", "order_amount": 55, "payment_method": "app", "order_rating": 5}, {"order_id": 9, "customer_id": 103, "order_timestamp": "2024-03-02 20:45:00", "order_amount": 48.5, "payment_method": "app", "order_rating": 4}, {"order_id": 10, "customer_id": 103, "order_timestamp": "2024-03-03 18:30:00", "order_amount": 62, "payment_method": "card", "order_rating": 5}, {"order_id": 11, "customer_id": 104, "order_timestamp": "2024-03-01 10:00:00", "order_amount": 15, "payment_method": "cash", "order_rating": 3}, {"order_id": 12, "customer_id": 104, "order_timestamp": "2024-03-02 09:30:00", "order_amount": 18, "payment_method": "cash", "order_rating": 2}, {"order_id": 13, "customer_id": 104, "order_timestamp": "2024-03-03 16:00:00", "order_amount": 20, "payment_method": "card", "order_rating": 3}, {"order_id": 14, "customer_id": 105, "order_timestamp": "2024-03-01 12:15:00", "order_amount": 30, "payment_method": "app", "order_rating": 4}, {"order_id": 15, "customer_id": 105, "order_timestamp": "2024-03-02 13:00:00", "order_amount": 35.5, "payment_method": "app", "order_rating": 5}, {"order_id": 16, "customer_id": 105, "order_timestamp": "2024-03-03 11:45:00", "order_amount": 28, "payment_method": "card", "order_rating": 4}]}}`
- **Required output:** `{"columns": ["customer_id", "total_orders", "peak_hour_percentage", "average_rating"], "rows": [[103, 3, 100, 4.67], [101, 4, 100, 4.67], [105, 3, 100, 4.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{restaurant}_{orders}$

The objective is to compute `{"columns": ["customer_id", "total_orders", "peak_hour_percentage", "average_rating"], "rows": [[103, 3, 100, 4.67], [101, 4, 100, 4.67], [105, 3, 100, 4.33]]}` from `{"tables": {"restaurant_orders": [{"order_id": 1, "customer_id": 101, "order_timestamp": "2024-03-01 12:30:00", "order_amount": 25.5, "payment_method": "card", "order_rating": 5}, {"order_id": 2, "customer_id": 101, "order_timestamp": "2024-03-02 19:15:00", "order_amount": 32, "payment_method": "app", "order_rating": 4}, {"order_id": 3, "customer_id": 101, "order_timestamp": "2024-03-03 13:45:00", "order_amount": 28.75, "payment_method": "card", "order_rating": 5}, {"order_id": 4, "customer_id": 101, "order_timestamp": "2024-03-04 20:30:00", "order_amount": 41, "payment_method": "app", "order_rating": null}, {"order_id": 5, "customer_id": 102, "order_timestamp": "2024-03-01 11:30:00", "order_amount": 18.5, "payment_method": "cash", "order_rating": 4}, {"order_id": 6, "customer_id": 102, "order_timestamp": "2024-03-02 12:00:00", "order_amount": 22, "payment_method": "card", "order_rating": 3}, {"order_id": 7, "customer_id": 102, "order_timestamp": "2024-03-03 15:30:00", "order_amount": 19.75, "payment_method": "cash", "order_rating": null}, {"order_id": 8, "customer_id": 103, "order_timestamp": "2024-03-01 19:00:00", "order_amount": 55, "payment_method": "app", "order_rating": 5}, {"order_id": 9, "customer_id": 103, "order_timestamp": "2024-03-02 20:45:00", "order_amount": 48.5, "payment_method": "app", "order_rating": 4}, {"order_id": 10, "customer_id": 103, "order_timestamp": "2024-03-03 18:30:00", "order_amount": 62, "payment_method": "card", "order_rating": 5}, {"order_id": 11, "customer_id": 104, "order_timestamp": "2024-03-01 10:00:00", "order_amount": 15, "payment_method": "cash", "order_rating": 3}, {"order_id": 12, "customer_id": 104, "order_timestamp": "2024-03-02 09:30:00", "order_amount": 18, "payment_method": "cash", "order_rating": 2}, {"order_id": 13, "customer_id": 104, "order_timestamp": "2024-03-03 16:00:00", "order_amount": 20, "payment_method": "card", "order_rating": 3}, {"order_id": 14, "customer_id": 105, "order_timestamp": "2024-03-01 12:15:00", "order_amount": 30, "payment_method": "app", "order_rating": 4}, {"order_id": 15, "customer_id": 105, "order_timestamp": "2024-03-02 13:00:00", "order_amount": 35.5, "payment_method": "app", "order_rating": 5}, {"order_id": 16, "customer_id": 105, "order_timestamp": "2024-03-03 11:45:00", "order_amount": 28, "payment_method": "card", "order_rating": 4}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One group per customer

`GROUP BY customer_id` collects all orders made by the same customer. Every selected expression that is not the grouping key is an aggregate over that customer's rows.

`COUNT(1) total_orders` counts every order row, regardless of whether `order_rating` is null. This is the correct denominator for both the peak-hour ratio and rating-completion ratio.

The alias `total_orders` is reused in the MySQL `HAVING` clause.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"restaurant_orders": [{"order_id": 1, "customer_id": 101, "order_timestamp": "2024-03-01 12:30:00", "order_amount": 25.5, "payment_method": "card", "order_rating": 5}, {"order_id": 2, "customer_id": 101, "order_timestamp": "2024-03-02 19:15:00", "order_amount": 32, "payment_method": "app", "order_rating": 4}, {"order_id": 3, "customer_id": 101, "order_timestamp": "2024-03-03 13:45:00", "order_amount": 28.75, "payment_method": "card", "order_rating": 5}, {"order_id": 4, "customer_id": 101, "order_timestamp": "2024-03-04 20:30:00", "order_amount": 41, "payment_method": "app", "order_rating": null}, {"order_id": 5, "customer_id": 102, "order_timestamp": "2024-03-01 11:30:00", "order_amount": 18.5, "payment_method": "cash", "order_rating": 4}, {"order_id": 6, "customer_id": 102, "order_timestamp": "2024-03-02 12:00:00", "order_amount": 22, "payment_method": "card", "order_rating": 3}, {"order_id": 7, "customer_id": 102, "order_timestamp": "2024-03-03 15:30:00", "order_amount": 19.75, "payment_method": "cash", "order_rating": null}, {"order_id": 8, "customer_id": 103, "order_timestamp": "2024-03-01 19:00:00", "order_amount": 55, "payment_method": "app", "order_rating": 5}, {"order_id": 9, "customer_id": 103, "order_timestamp": "2024-03-02 20:45:00", "order_amount": 48.5, "payment_method": "app", "order_rating": 4}, {"order_id": 10, "customer_id": 103, "order_timestamp": "2024-03-03 18:30:00", "order_amount": 62, "payment_method": "card", "order_rating": 5}, {"order_id": 11, "customer_id": 104, "order_timestamp": "2024-03-01 10:00:00", "order_amount": 15, "payment_method": "cash", "order_rating": 3}, {"order_id": 12, "customer_id": 104, "order_timestamp": "2024-03-02 09:30:00", "order_amount": 18, "payment_method": "cash", "order_rating": 2}, {"order_id": 13, "customer_id": 104, "order_timestamp": "2024-03-03 16:00:00", "order_amount": 20, "payment_method": "card", "order_rating": 3}, {"order_id": 14, "customer_id": 105, "order_timestamp": "2024-03-01 12:15:00", "order_amount": 30, "payment_method": "app", "order_rating": 4}, {"order_id": 15, "customer_id": 105, "order_timestamp": "2024-03-02 13:00:00", "order_amount": 35.5, "payment_method": "app", "order_rating": 5}, {"order_id": 16, "customer_id": 105, "order_timestamp": "2024-03-03 11:45:00", "order_amount": 28, "payment_method": "card", "order_rating": 4}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognizing peak-hour orders

`TIME(order_timestamp)` extracts only the time-of-day portion of each timestamp.

The query tests two inclusive intervals:

- `'11:00:00'` through `'14:00:00'`;
- `'18:00:00'` through `'21:00:00'`.

MySQL `BETWEEN` includes both endpoints. An order at exactly 14:00:00 or 21:00:00 is counted as peak, while one second later is not.

Each comparison produces Boolean zero or one. The `OR` is one when either interval contains the time. Summing that expression therefore counts peak-hour orders.

The displayed percentage is:

`ROUND(SUM(peak_condition) / COUNT(1) * 100)`.

Because `ROUND` has no second argument, it rounds to a whole percentage point.

For four peak orders among four total rows, the expression produces 100. For two among three, it displays 67 after rounding $66.666\ldots$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Average rating over rated orders only

`AVG(order_rating)` ignores null values in MySQL. It divides the sum of available ratings by the number of non-null ratings, not by `total_orders`.

The output expression:

`ROUND(AVG(order_rating), 2) average_rating`

rounds that rated-order average to two decimal places.

For ratings $5,4,5,\text{NULL}$, the average is:

$$
\frac{5+4+5}{3}=4.666\ldots,
$$

which displays as 4.67.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "total_orders", "peak_hour_percentage", "average_rating"], "rows": [[103, 3, 100, 4.67], [101, 4, 100, 4.67], [105, 3, 100, 4.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"restaurant_orders": [{"order_id": 1, "customer_id": 101, "order_timestamp": "2024-03-01 12:30:00", "order_amount": 25.5, "payment_method": "card", "order_rating": 5}, {"order_id": 2, "customer_id": 101, "order_timestamp": "2024-03-02 19:15:00", "order_amount": 32, "payment_method": "app", "order_rating": 4}, {"order_id": 3, "customer_id": 101, "order_timestamp": "2024-03-03 13:45:00", "order_amount": 28.75, "payment_method": "card", "order_rating": 5}, {"order_id": 4, "customer_id": 101, "order_timestamp": "2024-03-04 20:30:00", "order_amount": 41, "payment_method": "app", "order_rating": null}, {"order_id": 5, "customer_id": 102, "order_timestamp": "2024-03-01 11:30:00", "order_amount": 18.5, "payment_method": "cash", "order_rating": 4}, {"order_id": 6, "customer_id": 102, "order_timestamp": "2024-03-02 12:00:00", "order_amount": 22, "payment_method": "card", "order_rating": 3}, {"order_id": 7, "customer_id": 102, "order_timestamp": "2024-03-03 15:30:00", "order_amount": 19.75, "payment_method": "cash", "order_rating": null}, {"order_id": 8, "customer_id": 103, "order_timestamp": "2024-03-01 19:00:00", "order_amount": 55, "payment_method": "app", "order_rating": 5}, {"order_id": 9, "customer_id": 103, "order_timestamp": "2024-03-02 20:45:00", "order_amount": 48.5, "payment_method": "app", "order_rating": 4}, {"order_id": 10, "customer_id": 103, "order_timestamp": "2024-03-03 18:30:00", "order_amount": 62, "payment_method": "card", "order_rating": 5}, {"order_id": 11, "customer_id": 104, "order_timestamp": "2024-03-01 10:00:00", "order_amount": 15, "payment_method": "cash", "order_rating": 3}, {"order_id": 12, "customer_id": 104, "order_timestamp": "2024-03-02 09:30:00", "order_amount": 18, "payment_method": "cash", "order_rating": 2}, {"order_id": 13, "customer_id": 104, "order_timestamp": "2024-03-03 16:00:00", "order_amount": 20, "payment_method": "card", "order_rating": 3}, {"order_id": 14, "customer_id": 105, "order_timestamp": "2024-03-01 12:15:00", "order_amount": 30, "payment_method": "app", "order_rating": 4}, {"order_id": 15, "customer_id": 105, "order_timestamp": "2024-03-02 13:00:00", "order_amount": 35.5, "payment_method": "app", "order_rating": 5}, {"order_id": 16, "customer_id": 105, "order_timestamp": "2024-03-03 11:45:00", "order_amount": 28, "payment_method": "card", "order_rating": 4}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "total_orders", "peak_hour_percentage", "average_rating"], "rows": [[103, 3, 100, 4.67], [101, 4, 100, 4.67], [105, 3, 100, 4.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation with `CASE`:** `SUM(CASE WHEN peak_condition THEN 1 ELSE 0 END)` is more portable across SQL dialects. MySQL permits summing Boolean expressions directly.
- **Filter exact metrics:** To match the local contract strictly, compare the unrounded peak ratio and raw `AVG(order_rating)` in `HAVING`, then round only for output.
- **Use `COUNT(order_rating)`:** This counts rated rows because `COUNT(column)` ignores nulls and can replace `SUM(order_rating IS NOT NULL)`.
- **Inclusive interval endpoints:** `BETWEEN` counts orders exactly at 11:00, 14:00, 18:00, and 21:00.
- **Unrated orders:** They count toward total orders and peak percentage but are excluded automatically from `AVG(order_rating)`.
- **No rated orders:** `AVG` is null and the rating-completion ratio is zero, so the customer cannot pass all conditions.
- **Exactly half rated:** The `>= 0.5` comparison includes a customer with exactly 50% rated orders.
- **Exactly three orders:** The `>= 3` condition includes the threshold boundary.
- **Rounded peak false positive:** An exact percentage below 60 can round to 60 and pass the checked-in alias filter.
- **Ordering ties:** Equal rounded averages are ordered by descending `customer_id`, not by raw average or peak percentage.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let $R$ be the number of order rows and $C$ the number of distinct customers.
- **Auxiliary Space Complexity:** $O(R + C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
