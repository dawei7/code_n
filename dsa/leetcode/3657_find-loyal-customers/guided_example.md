# Guided Example: Find Loyal Customers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"customer_transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2024-01-05", "amount": 150, "transaction_type": "purchase"}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2024-01-15", "amount": 200, "transaction_type": "purchase"}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2024-02-10", "amount": 180, "transaction_type": "purchase"}, {"transaction_id": 4, "customer_id": 101, "transaction_date": "2024-02-20", "amount": 250, "transaction_type": "purchase"}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2024-01-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2024-01-12", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 7, "customer_id": 102, "transaction_date": "2024-01-15", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 8, "customer_id": 102, "transaction_date": "2024-01-18", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 9, "customer_id": 102, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 10, "customer_id": 103, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 11, "customer_id": 103, "transaction_date": "2024-01-02", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 12, "customer_id": 103, "transaction_date": "2024-01-03", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 13, "customer_id": 104, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 14, "customer_id": 104, "transaction_date": "2024-02-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 15, "customer_id": 104, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 16, "customer_id": 104, "transaction_date": "2024-03-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 17, "customer_id": 104, "transaction_date": "2024-03-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 18, "customer_id": 104, "transaction_date": "2024-03-15", "amount": 100, "transaction_type": "refund"}]}}`
- **Required output:** `{"columns": ["customer_id"], "rows": [[101], [104]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{customer}_{transactions}$

The objective is to compute `{"columns": ["customer_id"], "rows": [[101], [104]]}` from `{"tables": {"customer_transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2024-01-05", "amount": 150, "transaction_type": "purchase"}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2024-01-15", "amount": 200, "transaction_type": "purchase"}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2024-02-10", "amount": 180, "transaction_type": "purchase"}, {"transaction_id": 4, "customer_id": 101, "transaction_date": "2024-02-20", "amount": 250, "transaction_type": "purchase"}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2024-01-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2024-01-12", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 7, "customer_id": 102, "transaction_date": "2024-01-15", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 8, "customer_id": 102, "transaction_date": "2024-01-18", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 9, "customer_id": 102, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 10, "customer_id": 103, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 11, "customer_id": 103, "transaction_date": "2024-01-02", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 12, "customer_id": 103, "transaction_date": "2024-01-03", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 13, "customer_id": 104, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 14, "customer_id": 104, "transaction_date": "2024-02-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 15, "customer_id": 104, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 16, "customer_id": 104, "transaction_date": "2024-03-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 17, "customer_id": 104, "transaction_date": "2024-03-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 18, "customer_id": 104, "transaction_date": "2024-03-15", "amount": 100, "transaction_type": "refund"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce all loyalty criteria to one customer-level group

Every condition describes a customer across all of their transaction rows:

- A count of purchase transactions.
- A count or proportion of refund transactions.
- The span from the earliest transaction date to the latest.

These are aggregate properties, so the query groups rows by `customer_id` and evaluates one completed group per customer. No transaction amount is involved in the loyalty definition, and the unique `transaction_id` is only row identity; neither needs to appear in the result or filters.

The source writes

`GROUP BY 1`.

In MySQL, ordinal one refers to the first selected expression, `customer_id`. This is equivalent to `GROUP BY customer_id`. The explicit column name would be easier to maintain, but the positional form has the intended behavior here.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"customer_transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2024-01-05", "amount": 150, "transaction_type": "purchase"}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2024-01-15", "amount": 200, "transaction_type": "purchase"}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2024-02-10", "amount": 180, "transaction_type": "purchase"}, {"transaction_id": 4, "customer_id": 101, "transaction_date": "2024-02-20", "amount": 250, "transaction_type": "purchase"}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2024-01-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2024-01-12", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 7, "customer_id": 102, "transaction_date": "2024-01-15", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 8, "customer_id": 102, "transaction_date": "2024-01-18", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 9, "customer_id": 102, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 10, "customer_id": 103, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 11, "customer_id": 103, "transaction_date": "2024-01-02", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 12, "customer_id": 103, "transaction_date": "2024-01-03", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 13, "customer_id": 104, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 14, "customer_id": 104, "transaction_date": "2024-02-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 15, "customer_id": 104, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 16, "customer_id": 104, "transaction_date": "2024-03-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 17, "customer_id": 104, "transaction_date": "2024-03-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 18, "customer_id": 104, "transaction_date": "2024-03-15", "amount": 100, "transaction_type": "refund"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count refunds with a MySQL Boolean sum

The expression

`transaction_type = 'refund'`

evaluates to one for a refund row and zero for a purchase row in MySQL numeric context. Therefore

`SUM(transaction_type = 'refund')`

is the number of refunds in a customer’s group.

`COUNT(1)` counts every transaction row, regardless of type. Since the schema guarantees that `transaction_type` is either `'purchase'` or `'refund'`, the total count is

`T = P + R`,

where `P` is purchases and `R` is refunds.

MySQL’s `/` operator performs division rather than integer truncation in this expression, so

`SUM(transaction_type = 'refund') / COUNT(1)`

is the refund fraction `R / T`. The condition uses strict inequality:

`R / T < 0.2`.

A customer at exactly twenty percent does not qualify.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `COUNT(1) >= 3` still enforces three purchases

The statement asks for at least three purchases, but the source’s first condition is

`COUNT(1) >= 3`,

which counts purchases and refunds together. Viewed in isolation, that would not be the requested test. However, it appears in conjunction with the strict refund-rate condition, and together the two conditions are equivalent to the intended purchase minimum plus refund-rate requirement.

Assume the source conditions hold. Then `T >= 3` and

`R / T < 0.2`.

The purchase count is `P = T - R`, so

`P > 0.8T`.

Since `T >= 3`, this gives `P > 2.4`. Purchase counts are integers, so `P >= 3`.

Conversely, if a customer has at least three purchases and satisfies the refund-rate condition, then `T = P + R >= 3`, so the source’s total-count condition also holds.

Thus no customer with fewer than three purchases can pass the complete `HAVING` clause under the guaranteed two transaction types. The query is semantically correct, although writing

`SUM(transaction_type = 'purchase') >= 3`

would express the requirement more directly and remain correct even if new transaction types were later introduced.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id"], "rows": [[101], [104]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"customer_transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2024-01-05", "amount": 150, "transaction_type": "purchase"}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2024-01-15", "amount": 200, "transaction_type": "purchase"}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2024-02-10", "amount": 180, "transaction_type": "purchase"}, {"transaction_id": 4, "customer_id": 101, "transaction_date": "2024-02-20", "amount": 250, "transaction_type": "purchase"}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2024-01-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2024-01-12", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 7, "customer_id": 102, "transaction_date": "2024-01-15", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 8, "customer_id": 102, "transaction_date": "2024-01-18", "amount": 100, "transaction_type": "refund"}, {"transaction_id": 9, "customer_id": 102, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 10, "customer_id": 103, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 11, "customer_id": 103, "transaction_date": "2024-01-02", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 12, "customer_id": 103, "transaction_date": "2024-01-03", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 13, "customer_id": 104, "transaction_date": "2024-01-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 14, "customer_id": 104, "transaction_date": "2024-02-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 15, "customer_id": 104, "transaction_date": "2024-02-15", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 16, "customer_id": 104, "transaction_date": "2024-03-01", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 17, "customer_id": 104, "transaction_date": "2024-03-10", "amount": 100, "transaction_type": "purchase"}, {"transaction_id": 18, "customer_id": 104, "transaction_date": "2024-03-15", "amount": 100, "transaction_type": "refund"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id"], "rows": [[101], [104]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count purchases explicitly:** `SUM(transaction_type = 'purchase') >= 3` states the requirement directly and is more robust if transaction types ever expand. Under the current two-type guarantee and refund filter, it is equivalent to the source’s conjunction.
- **Conditional `CASE` expressions:** `SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END)` is more portable than MySQL Boolean arithmetic.
- **Correlated subqueries:** Separately querying counts and dates for every customer can repeatedly scan the table. One grouped aggregation computes all metrics together.
- **Filter refunds in `WHERE`:** Removing refund rows before grouping would force every observed refund rate to zero and corrupt total counts and date endpoints.
- **Exactly three total transactions:** To pass a refund rate below twenty percent, all three must be purchases; one refund would make the rate one-third.
- **Exactly twenty-percent refunds:** The customer is excluded because the rule and source both use strict `< 0.2`.
- **No refunds:** The refund sum is zero and the rate is zero, so the rate condition passes.
- **Fewer than three purchases:** Such a customer cannot satisfy both `COUNT(1) >= 3` and a refund rate below twenty percent under the two-type schema.
- **Transactions on one date:** `DATEDIFF` is zero regardless of transaction count, so the activity criterion fails.
- **Exactly 30 days apart:** The customer passes the activity condition because the query uses `>= 30`.
- **Refund extends the activity span:** It counts as activity because endpoints are taken over all transaction rows.
- **Repeated transaction dates:** They are counted as separate transactions but do not independently increase the min-to-max date span.
- **Transaction amount:** Purchase and refund amounts do not affect any criterion and are correctly ignored.
- **Ordinal column references:** `GROUP BY 1` and `ORDER BY 1` are valid MySQL shorthand but less self-documenting than naming `customer_id`.
- **Potential nulls:** The reference presents valid transaction types and dates. If nulls were allowed, Boolean sums, `MIN`, and `MAX` would need an explicit null policy.
- **Ascending result order:** `ORDER BY 1` defaults to ascending; adding `DESC` would contradict the requirement.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C)$. Let `N` be the number of transaction rows and `C` the number of distinct customers.
- **Auxiliary Space Complexity:** $O(N + C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
