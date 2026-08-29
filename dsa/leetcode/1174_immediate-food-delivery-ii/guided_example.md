# Guided Example: Immediate Food Delivery II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-12"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-24"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-09", "customer_pref_delivery_date": "2019-08-09"}]}}`
- **Required output:** `{"columns": ["immediate_percentage"], "rows": [[50.0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Delivery`

The objective is to compute `{"columns": ["immediate_percentage"], "rows": [[50.0]]}` from `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-12"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-24"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-09", "customer_pref_delivery_date": "2019-08-09"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First restrict the population to one order per customer

This version asks about first orders, not every delivery row. For each `customer_id`, the first order is the one with the smallest `order_date`.

The grouped subquery computes

`SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY 1`.

`GROUP BY 1` groups by the first selected expression, `customer_id`. The result contains each customer and that customer's earliest order date.

The statement guarantees that every customer has precisely one first order. Therefore, the pair `(customer_id, minimum_date)` identifies exactly one delivery row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-12"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-24"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-09", "customer_pref_delivery_date": "2019-08-09"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter with a composite row-value match

The outer `WHERE` condition tests

`(customer_id, order_date) IN (...)`.

A delivery survives only when both its customer identifier and date match one earliest-date pair from the subquery. Matching only `order_date` would be wrong because different customers can share dates. Matching both fields selects each customer's own first order.

The uniqueness guarantee matters. If one customer could place two orders on the same earliest date, both rows would match and that customer would receive double weight. The problem explicitly excludes that ambiguity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Average the immediate indicators

For every surviving first-order row, the Boolean expression

`order_date = customer_pref_delivery_date`

is one for an immediate order and zero for a scheduled order in MySQL numeric context.

`AVG(...)` sums those indicators and divides by their count. Because there is exactly one surviving row per customer, the average is the fraction of customers whose first order is immediate.

Multiplying by 100 converts the fraction to a percentage, and `ROUND(..., 2)` supplies the required two-decimal rounding. The output alias is `immediate_percentage`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["immediate_percentage"], "rows": [[50.0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Delivery": [{"delivery_id": 1, "customer_id": 1, "order_date": "2019-08-01", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 2, "customer_id": 2, "order_date": "2019-08-02", "customer_pref_delivery_date": "2019-08-02"}, {"delivery_id": 3, "customer_id": 1, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-12"}, {"delivery_id": 4, "customer_id": 3, "order_date": "2019-08-24", "customer_pref_delivery_date": "2019-08-24"}, {"delivery_id": 5, "customer_id": 3, "order_date": "2019-08-21", "customer_pref_delivery_date": "2019-08-22"}, {"delivery_id": 6, "customer_id": 2, "order_date": "2019-08-11", "customer_pref_delivery_date": "2019-08-13"}, {"delivery_id": 7, "customer_id": 4, "order_date": "2019-08-09", "customer_pref_delivery_date": "2019-08-09"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["immediate_percentage"], "rows": [[50.0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Window function with `ROW_NUMBER`:** Partition by customer, order by date, keep row one, and average its indicator. This is explicit and also relies on or resolves tie rules.
- **Correlated minimum subquery:** Compare each row's date to a per-customer minimum. It can be concise but may repeat work without an index.
- **Average all deliveries:** Customers with later orders would be included and the result would answer version I, not version II.
- **Match only minimum date:** Different customers can share dates, so the customer identifier must be part of the comparison.
- **Two earliest orders on the same day:** The query would include both, but the contract guarantees precisely one first order per customer.
- **One customer:** The percentage is either `100.00` or `0.00` according to that first order.
- **Later immediate order after a scheduled first order:** It does not count; only the earliest order is evaluated.
- **Scheduled first order:** Its Boolean contributes zero.
- **Immediate first order:** Its Boolean contributes one.
- **No ordering requirement:** The aggregate returns one row, so final row order is irrelevant.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of delivery rows and `c` the number of customers. A hash-based grouped minimum can scan `n` rows in `O(n)` expected time while storing one date per customer. Filtering and averaging scan or probe the rows with linear total logical work, matching the manifest's `O(n)` time.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
