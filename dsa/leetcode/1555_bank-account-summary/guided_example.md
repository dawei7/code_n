# Guided Example: Bank Account Summary

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 1, "user_name": "Moustafa", "credit": 100}, {"user_id": 2, "user_name": "Jonathan", "credit": 200}, {"user_id": 3, "user_name": "Winston", "credit": 10000}, {"user_id": 4, "user_name": "Luis", "credit": 800}], "Transactions": [{"trans_id": 1, "paid_by": 1, "paid_to": 3, "amount": 400, "transacted_on": "2020-08-01"}, {"trans_id": 2, "paid_by": 3, "paid_to": 2, "amount": 500, "transacted_on": "2020-08-02"}, {"trans_id": 3, "paid_by": 2, "paid_to": 1, "amount": 200, "transacted_on": "2020-08-03"}]}}`
- **Required output:** `{"columns": ["user_id", "user_name", "credit", "credit_limit_breached"], "rows": [[1, "Moustafa", -100, "Yes"], [2, "Jonathan", 500, "No"], [3, "Winston", 9900, "No"], [4, "Luis", 800, "No"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id", "user_name", "credit", "credit_limit_breached"], "rows": [[1, "Moustafa", -100, "Yes"], [2, "Jonathan", 500, "No"], [3, "Winston", 9900, "No"], [4, "Luis", 800, "No"]]}` from `{"tables": {"Users": [{"user_id": 1, "user_name": "Moustafa", "credit": 100}, {"user_id": 2, "user_name": "Jonathan", "credit": 200}, {"user_id": 3, "user_name": "Winston", "credit": 10000}, {"user_id": 4, "user_name": "Luis", "credit": 800}], "Transactions": [{"trans_id": 1, "paid_by": 1, "paid_to": 3, "amount": 400, "transacted_on": "2020-08-01"}, {"trans_id": 2, "paid_by": 3, "paid_to": 2, "amount": 500, "transacted_on": "2020-08-02"}, {"trans_id": 3, "paid_by": 2, "paid_to": 1, "amount": 200, "transacted_on": "2020-08-03"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert all balance effects into one signed ledger

Each user's current balance equals initial credit plus incoming transaction amounts minus outgoing transaction amounts.

The derived table `t` creates rows with a uniform schema `(user_id, credit)` for all three components:

- A payer receives `-amount` because sending money decreases balance.
- A recipient receives `amount` because receiving money increases balance.
- Every user receives one row containing their initial `credit`.

Once all effects have the same two columns, the final balance is simply their sum per user.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 1, "user_name": "Moustafa", "credit": 100}, {"user_id": 2, "user_name": "Jonathan", "credit": 200}, {"user_id": 3, "user_name": "Winston", "credit": 10000}, {"user_id": 4, "user_name": "Luis", "credit": 800}], "Transactions": [{"trans_id": 1, "paid_by": 1, "paid_to": 3, "amount": 400, "transacted_on": "2020-08-01"}, {"trans_id": 2, "paid_by": 3, "paid_to": 2, "amount": 500, "transacted_on": "2020-08-02"}, {"trans_id": 3, "paid_by": 2, "paid_to": 1, "amount": 200, "transacted_on": "2020-08-03"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why UNION ALL is essential

The query combines the three streams with `UNION ALL`, which preserves every row.

Ordinary `UNION` removes duplicate rows. Two legitimate transactions can have the same user and amount, and deduplicating them would lose a real balance effect. An initial-credit row could also numerically match a transaction effect. Those are separate facts and must all contribute.

`UNION ALL` expresses ledger addition rather than set union.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Guarantee that users without transactions remain

The third branch selects `user_id, credit` from every `Users` row. Therefore every user appears in `t` at least once even when they never paid or received money.

For such a user, the group sum contains only the initial credit and returns it unchanged. No outer join or missing-value replacement is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "user_name", "credit", "credit_limit_breached"], "rows": [[1, "Moustafa", -100, "Yes"], [2, "Jonathan", 500, "No"], [3, "Winston", 9900, "No"], [4, "Luis", 800, "No"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 1, "user_name": "Moustafa", "credit": 100}, {"user_id": 2, "user_name": "Jonathan", "credit": 200}, {"user_id": 3, "user_name": "Winston", "credit": 10000}, {"user_id": 4, "user_name": "Luis", "credit": 800}], "Transactions": [{"trans_id": 1, "paid_by": 1, "paid_to": 3, "amount": 400, "transacted_on": "2020-08-01"}, {"trans_id": 2, "paid_by": 3, "paid_to": 2, "amount": 500, "transacted_on": "2020-08-02"}, {"trans_id": 3, "paid_by": 2, "paid_to": 1, "amount": 200, "transacted_on": "2020-08-03"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "user_name", "credit", "credit_limit_breached"], "rows": [[1, "Moustafa", -100, "Yes"], [2, "Jonathan", 500, "No"], [3, "Winston", 9900, "No"], [4, "Luis", 800, "No"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Separate incoming and outgoing aggregates:** Aggregate each transaction side by user and left join both to users. It is correct but needs null handling and more join logic.
- **Conditional aggregation after joins:** Joining users to transactions in both roles can create multiplicative rows unless designed carefully.
- **UNION instead of UNION ALL:** It is incorrect because equal-looking ledger effects are distinct financial events.
- **User with no transactions:** The initial-credit branch guarantees one group row and preserves the balance.
- **Only outgoing transactions:** All effects beyond initial credit are negative.
- **Only incoming transactions:** All effects beyond initial credit are positive.
- **Balance exactly zero:** The breach label is `"No"` because the test is strictly less than zero.
- **Negative balance:** It produces `"Yes"` regardless of how many transactions caused it.
- **Self-transfer:** Positive and negative rows cancel for the same user.
- **Repeated equal amounts:** `UNION ALL` preserves every occurrence.
- **Transaction dates:** They do not affect an all-time current-balance summary and are intentionally ignored.
- **Any output order:** No sorting clause is required.
- **Functional dependency:** Selecting `user_name` while grouping by primary-key `user_id` relies on MySQL recognizing that dependency.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((U+T)$. Let $U$ be user count and $T$ transaction count. The unioned ledger has $U+2T$ rows.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
