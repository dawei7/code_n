# Guided Example: Immediate Food Delivery I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 5, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-11"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-26"}, {"delivery_id": 5, "customer_id": 4, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}]}}`
- **Required output:** `{"columns": ["immediate_percentage"], "rows": [[33.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Delivery`

The objective is to compute `{"columns": ["immediate_percentage"], "rows": [[33.33]]}` from `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 5, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-11"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-26"}, {"delivery_id": 5, "customer_id": 4, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the definition into a row-level Boolean

An order is immediate exactly when

`order_date = customer_pref_delivery_date`.

In MySQL, a true comparison used in numeric context evaluates to one and a false comparison evaluates to zero. Therefore, the expression itself is an indicator variable for an immediate order.

No grouping by customer is needed. This version asks for the percentage among all orders in the table, so every delivery row has equal weight.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 5, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-11"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-26"}, {"delivery_id": 5, "customer_id": 4, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sum the indicators to count immediate orders

`SUM(order_date = customer_pref_delivery_date)` adds one for each immediate row and zero for each scheduled row. Its result is exactly the number of immediate orders.

This is equivalent to a longer conditional aggregate such as `SUM(CASE WHEN ... THEN 1 ELSE 0 END)`, but the MySQL Boolean expression is more compact.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count the complete denominator

`COUNT(1)` counts every row in `Delivery`. The literal one is non-null for every row, so this is equivalent to `COUNT(*)` here.

The denominator must count orders, not distinct customers. A customer who placed several orders contributes each one separately because the question is the percentage of immediate orders in the whole table.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["immediate_percentage"], "rows": [[33.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 5, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-11"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-26"}, {"delivery_id": 5, "customer_id": 4, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["immediate_percentage"], "rows": [[33.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use a `CASE` expression:** `SUM(CASE WHEN condition THEN 1 ELSE 0 END)` is more portable across SQL dialects and computes the same numerator.
- **Use `AVG` of the Boolean:** `AVG(order_date = customer_pref_delivery_date) * 100` directly averages the zero-one indicators and is equivalent on non-null dates.
- **Count distinct customers:** That changes the denominator and answers a different question.
- **Group by customer:** This would produce per-customer percentages rather than the required global value.
- **All orders immediate:** The sum equals the count, so the result is `100.00`.
- **No orders immediate:** The sum is zero, so the result is `0.00` for a nonempty table.
- **Preferred date after order date:** The equality is false, so the order is scheduled.
- **Dates exactly equal:** The indicator is one; no time-of-day issue exists because both columns are dates.
- **Round only the fraction first:** Premature rounding can distort the percentage. The exact query rounds after multiplying by 100.
- **Empty table:** The exact expression yields null because of division by zero; it does not define a fallback.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of delivery rows. The database scans each row once to evaluate the equality, update the sum, and update the count. Logical time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
