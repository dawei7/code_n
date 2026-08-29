# Guided Example: The Users That Are Eligible for Discount

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}`
- **Required output:** `{"columns": ["user_id"], "rows": [[3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["user_id"], "rows": [[3]]}` from `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Eligibility is proven by one qualifying purchase row

A user needs at least one purchase satisfying all three predicates:

- `amount >= minAmount`;
- `time_stamp >= startDate`; and
- `time_stamp <= endDate`.

The SQL procedure filters purchase rows directly. It does not aggregate amounts across purchases because the rule applies to one purchase with at least the threshold amount, not to a user's total spending.

The exact predicate is

`amount >= minAmount AND time_stamp BETWEEN startDate AND endDate`.

In MySQL, `BETWEEN` is inclusive at both endpoints, so it expresses the two time comparisons together.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the date-to-datetime boundary exactly

The procedure parameters `startDate` and `endDate` have type `DATE`, while `time_stamp` is `DATETIME`. When MySQL compares them, a date is treated as the start of that day at `00:00:00`.

That behavior is explicitly required by the problem. If `endDate` is `2022-03-20`, the upper endpoint is `2022-03-20 00:00:00`. A purchase at exactly midnight is included, but a purchase later that same calendar day is after the stated endpoint and is excluded.

This differs from many business reports where an ending date informally means the entire day. The solution must follow this problem's start-of-day instruction and must not rewrite the condition as “before the next day.”

Likewise, a purchase before midnight at the start date is outside, while one exactly at `startDate 00:00:00` is included.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Apply amount and time conditions to the same row

SQL evaluates the conjunction for each row. A user does not qualify by combining one purchase that meets the amount with another purchase that meets the date interval. One row must satisfy both.

This explains the example: user `1` has a sufficiently large amount but its timestamp is outside the interval. User `2` is inside the time interval but below `minAmount`. Only user `3` has one row meeting both predicates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id"], "rows": [[3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id"], "rows": [[3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Group by user:** Filter rows and use `GROUP BY user_id` instead of `DISTINCT`. It can produce the same IDs, but `DISTINCT` states the intent directly because no aggregate is needed.
- **Use `EXISTS` over a users table:** This would be useful if a separate user table were required, but the only needed IDs already occur in qualifying purchase rows.
- **Aggregate each user's total amount:** That changes the contract. One purchase must individually meet `minAmount`.
- **Use an end-exclusive next-day boundary:** Common reporting logic such as `time_stamp < endDate + INTERVAL 1 DAY` would include the whole end date, contradicting the explicit midnight interpretation here.
- **Purchase exactly at `startDate 00:00:00`:** It is included by `BETWEEN`.
- **Purchase exactly at `endDate 00:00:00`:** It is also included.
- **Purchase later on the ending date:** It is excluded because the `DATE` parameter represents midnight.
- **Amount exactly equal to `minAmount`:** `>=` includes it.
- **Several qualifying purchases:** `DISTINCT` returns the user once.
- **No qualifying rows:** The procedure returns an empty result table.
- **One row meets amount and another meets time:** The user remains ineligible because `AND` applies both requirements to each individual row.
- **Required ordering:** `ORDER BY user_id` is necessary even after `DISTINCT`.
- **Null data:** The declared schema does not state nullability here; if a compared value were null, the predicate would not be true under SQL three-valued logic.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of purchase rows. Without an index tailored to the filter, the database scans `r` rows, taking `O(r)` predicate-evaluation time.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
