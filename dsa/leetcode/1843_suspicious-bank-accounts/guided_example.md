# Guided Example: Suspicious Bank Accounts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Accounts": [{"account_id": 3, "max_income": 21000}, {"account_id": 4, "max_income": 10400}], "Transactions": [{"transaction_id": 2, "account_id": 3, "type": "Creditor", "amount": 107100, "day": "2021-06-02 11:38:14"}, {"transaction_id": 4, "account_id": 4, "type": "Creditor", "amount": 10400, "day": "2021-06-20 12:39:18"}, {"transaction_id": 11, "account_id": 4, "type": "Debtor", "amount": 58800, "day": "2021-07-23 12:41:55"}, {"transaction_id": 1, "account_id": 4, "type": "Creditor", "amount": 49300, "day": "2021-05-03 16:11:04"}, {"transaction_id": 15, "account_id": 3, "type": "Debtor", "amount": 75500, "day": "2021-05-23 14:40:20"}, {"transaction_id": 10, "account_id": 3, "type": "Creditor", "amount": 102100, "day": "2021-06-15 10:37:16"}, {"transaction_id": 14, "account_id": 4, "type": "Creditor", "amount": 56300, "day": "2021-07-21 12:12:25"}, {"transaction_id": 19, "account_id": 4, "type": "Debtor", "amount": 101100, "day": "2021-05-09 15:21:49"}, {"transaction_id": 8, "account_id": 3, "type": "Creditor", "amount": 64900, "day": "2021-07-26 15:09:56"}, {"transaction_id": 7, "account_id": 3, "type": "Creditor", "amount": 90900, "day": "2021-06-14 11:23:07"}]}}`
- **Required output:** `{"columns": ["account_id"], "rows": [[3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Accounts`

The objective is to compute `{"columns": ["account_id"], "rows": [[3]]}` from `{"tables": {"Accounts": [{"account_id": 3, "max_income": 21000}, {"account_id": 4, "max_income": 10400}], "Transactions": [{"transaction_id": 2, "account_id": 3, "type": "Creditor", "amount": 107100, "day": "2021-06-02 11:38:14"}, {"transaction_id": 4, "account_id": 4, "type": "Creditor", "amount": 10400, "day": "2021-06-20 12:39:18"}, {"transaction_id": 11, "account_id": 4, "type": "Debtor", "amount": 58800, "day": "2021-07-23 12:41:55"}, {"transaction_id": 1, "account_id": 4, "type": "Creditor", "amount": 49300, "day": "2021-05-03 16:11:04"}, {"transaction_id": 15, "account_id": 3, "type": "Debtor", "amount": 75500, "day": "2021-05-23 14:40:20"}, {"transaction_id": 10, "account_id": 3, "type": "Creditor", "amount": 102100, "day": "2021-06-15 10:37:16"}, {"transaction_id": 14, "account_id": 4, "type": "Creditor", "amount": 56300, "day": "2021-07-21 12:12:25"}, {"transaction_id": 19, "account_id": 4, "type": "Debtor", "amount": 101100, "day": "2021-05-09 15:21:49"}, {"transaction_id": 8, "account_id": 3, "type": "Creditor", "amount": 64900, "day": "2021-07-26 15:09:56"}, {"transaction_id": 7, "account_id": 3, "type": "Creditor", "amount": 90900, "day": "2021-06-14 11:23:07"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**First label every creditor transaction with its month’s total-income status.** The common table expression `S` reads `Transactions`, left joins the matching `Accounts` row to obtain `max_income`, and filters to `type = 'Creditor'`. Debtor withdrawals must not contribute to income, so removing them before the window sum is essential.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Accounts": [{"account_id": 3, "max_income": 21000}, {"account_id": 4, "max_income": 10400}], "Transactions": [{"transaction_id": 2, "account_id": 3, "type": "Creditor", "amount": 107100, "day": "2021-06-02 11:38:14"}, {"transaction_id": 4, "account_id": 4, "type": "Creditor", "amount": 10400, "day": "2021-06-20 12:39:18"}, {"transaction_id": 11, "account_id": 4, "type": "Debtor", "amount": 58800, "day": "2021-07-23 12:41:55"}, {"transaction_id": 1, "account_id": 4, "type": "Creditor", "amount": 49300, "day": "2021-05-03 16:11:04"}, {"transaction_id": 15, "account_id": 3, "type": "Debtor", "amount": 75500, "day": "2021-05-23 14:40:20"}, {"transaction_id": 10, "account_id": 3, "type": "Creditor", "amount": 102100, "day": "2021-06-15 10:37:16"}, {"transaction_id": 14, "account_id": 4, "type": "Creditor", "amount": 56300, "day": "2021-07-21 12:12:25"}, {"transaction_id": 19, "account_id": 4, "type": "Debtor", "amount": 101100, "day": "2021-05-09 15:21:49"}, {"transaction_id": 8, "account_id": 3, "type": "Creditor", "amount": 64900, "day": "2021-07-26 15:09:56"}, {"transaction_id": 7, "account_id": 3, "type": "Creditor", "amount": 90900, "day": "2021-06-14 11:23:07"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`DATE_FORMAT(day, '%Y-%m-01')` normalizes every timestamp to a string representing the first day of its month. Using year and month together preserves calendar order across different years and makes every transaction in the same account-month share one value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `DATE_FORMAT(day, '%Y-%m-01')` normalizes every timestamp to... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

`SUM(amount) OVER (PARTITION BY account_id, formatted_month)`

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["account_id"], "rows": [[3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Accounts": [{"account_id": 3, "max_income": 21000}, {"account_id": 4, "max_income": 10400}], "Transactions": [{"transaction_id": 2, "account_id": 3, "type": "Creditor", "amount": 107100, "day": "2021-06-02 11:38:14"}, {"transaction_id": 4, "account_id": 4, "type": "Creditor", "amount": 10400, "day": "2021-06-20 12:39:18"}, {"transaction_id": 11, "account_id": 4, "type": "Debtor", "amount": 58800, "day": "2021-07-23 12:41:55"}, {"transaction_id": 1, "account_id": 4, "type": "Creditor", "amount": 49300, "day": "2021-05-03 16:11:04"}, {"transaction_id": 15, "account_id": 3, "type": "Debtor", "amount": 75500, "day": "2021-05-23 14:40:20"}, {"transaction_id": 10, "account_id": 3, "type": "Creditor", "amount": 102100, "day": "2021-06-15 10:37:16"}, {"transaction_id": 14, "account_id": 4, "type": "Creditor", "amount": 56300, "day": "2021-07-21 12:12:25"}, {"transaction_id": 19, "account_id": 4, "type": "Debtor", "amount": 101100, "day": "2021-05-09 15:21:49"}, {"transaction_id": 8, "account_id": 3, "type": "Creditor", "amount": 64900, "day": "2021-07-26 15:09:56"}, {"transaction_id": 7, "account_id": 3, "type": "Creditor", "amount": 90900, "day": "2021-06-14 11:23:07"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["account_id"], "rows": [[3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Monthly aggregation CTE:** Group creditor tran:** - **Monthly aggregation CTE:** Group creditor transactions by account and year-month, sum income, and retain only over-limit months before self-joining. This removes transaction-level duplication.
- **`LAG` over qualifying months:** After monthly aggregation, compare each over-limit month with the preceding month using a window function. Care is needed because filtering out nonqualifying months before checking gaps must still verify calendar adjacency.
- **`PERIOD_DIFF` self-join:** Formatting as `YYYYMM` and comparing periods is another direct way to recognize consecutive months.
- **Exactly equal to `max_income`:** The strict greater-than comparison marks it false, as required.
- **Debtor-only month:** It has no income row in `S` and cannot form an over-limit pair.
- **High months separated by a normal month:** Their month difference is two, so they do not join as consecutive.
- **December followed by January:** First-of-month normalization and `TIMESTAMPDIFF` correctly treat them as one month apart.
- **Three or more consecutive high months:** At least two adjacent pairs exist, and `DISTINCT` returns the account once.
- **Multiple transactions per month:** The window sum is correct, but the CTE repeats the month and the self-join multiplies rows.
- **No matching account row:** A null threshold prevents `marked = 1`, assuming ordinary SQL null semantics.
- **Left join in the outer query:** The marked condition on `s2` eliminates unmatched rows, so an inner join would express the effective requirement more clearly.
- **Final ordering:** Any order is allowed; `ORDER BY s1.tx` is unnecessary and can conflict with strict handling of `SELECT DISTINCT`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of creditor transaction rows. Window partitioning normally requires sorting or equivalent grouping work, often `O(r log r)`, and stores `O(r)` rows. However, because `S` retains each transaction and the self-join pairs all rows from consecutive months, the exact query can generate `O(r^2)` intermediate rows in the worst case. Its worst-case time and intermediate-space behavior can therefore be quadratic, not the manifest’s `O(r log r)` and `O(r)`.
- **Auxiliary Space Complexity:** $O(r log r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
