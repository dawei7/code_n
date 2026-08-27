# Guided Example: The Number of Users That Are Eligible for Discount

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}`
- **Required output:** `{"columns": ["user_cnt"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["user_cnt"], "rows": [[1]]}` from `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter by the timestamp interval

`time_stamp BETWEEN startDate AND endDate` is equivalent to

`time_stamp >= startDate AND time_stamp <= endDate`.

Both endpoints are inclusive, matching the statement.

The parameters are DATE values, while `time_stamp` is DATETIME. Under the described contract, each date is interpreted at the start of its day. Thus an end date such as March 20 means March 20 at `00:00:00`, not the entire calendar day through `23:59:59`.

A purchase later during the end date does not qualify under that explicit interpretation. A purchase exactly at midnight does.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Apply the amount threshold to the same row

`amount >= minAmount` is joined with the time condition by `AND`.

The same purchase must satisfy both conditions. A user cannot combine one in-range low purchase with one out-of-range high purchase to become eligible.

Equality is accepted because the requirement says “at least” `minAmount`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `amount >= minAmount` is joined with the time condition by `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count users rather than purchases

`COUNT(DISTINCT user_id)` counts each qualifying user once no matter how many matching purchases they made.

Using ordinary `COUNT(*)` would count rows and overstate eligibility when one user has several purchases in the interval.

The primary key allows many rows per user at different timestamps, making `DISTINCT` necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_cnt"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"user_id": 1, "time_stamp": "2022-04-20 09:03:00", "amount": 4416}, {"user_id": 2, "time_stamp": "2022-03-19 19:24:02", "amount": 678}, {"user_id": 3, "time_stamp": "2022-03-18 12:03:09", "amount": 4523}, {"user_id": 3, "time_stamp": "2022-03-30 09:43:42", "amount": 626}], "Parameters": [{"startDate": "2022-03-08 00:00:00", "endDate": "2022-03-20 00:00:00", "minAmount": 1000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_cnt"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Group by user then count groups:** Select qual:** - **Group by user then count groups:** Select qualifying user IDs grouped by `user_id` in a subquery and count them. It is equivalent but more verbose.
- **Use `EXISTS` per user:** Starting from a separate Users table can express eligibility directly, but no Users table is part of this schema.
- **End-of-day interpretation:** Do not add one day or `23:59:59` here; the problem explicitly interprets `endDate` as start-of-day.
- **Purchase exactly at start:** Inclusive `BETWEEN` accepts it.
- **Purchase exactly at end midnight:** Inclusive `BETWEEN` accepts it.
- **Purchase later on end date:** It is after the specified endpoint and does not qualify.
- **Amount equal to threshold:** `>=` accepts it.
- **Multiple qualifying purchases:** `DISTINCT` counts their user once.
- **Different rows satisfy different halves:** The user does not qualify unless one row satisfies both predicates together.
- **No qualifying purchases:** `COUNT` returns zero.
- **One user, many timestamps:** Composite primary key permits them, and distinct counting handles duplication.
- **Function result type:** The count fits the declared integer under ordinary dataset size assumptions.
- **Source table unchanged:** The function is read-only.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $r$ be the number of purchase rows examined and $u$ the number of distinct qualifying users.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
