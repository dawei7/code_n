# Guided Example: Account Balance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"account_id": 1, "day": "2021-11-07", "type": "Deposit", "amount": 2000}, {"account_id": 1, "day": "2021-11-09", "type": "Withdraw", "amount": 1000}, {"account_id": 1, "day": "2021-11-11", "type": "Deposit", "amount": 3000}, {"account_id": 2, "day": "2021-12-07", "type": "Deposit", "amount": 7000}, {"account_id": 2, "day": "2021-12-12", "type": "Withdraw", "amount": 7000}]}}`
- **Required output:** `{"columns": ["account_id", "day", "balance"], "rows": [[1, "2021-11-07", 2000], [1, "2021-11-09", 1000], [1, "2021-11-11", 4000], [2, "2021-12-07", 7000], [2, "2021-12-12", 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["account_id", "day", "balance"], "rows": [[1, "2021-11-07", 2000], [1, "2021-11-09", 1000], [1, "2021-11-11", 4000], [2, "2021-12-07", 7000], [2, "2021-12-12", 0]]}` from `{"tables": {"Transactions": [{"account_id": 1, "day": "2021-11-07", "type": "Deposit", "amount": 2000}, {"account_id": 1, "day": "2021-11-09", "type": "Withdraw", "amount": 1000}, {"account_id": 1, "day": "2021-11-11", "type": "Deposit", "amount": 3000}, {"account_id": 2, "day": "2021-12-07", "type": "Deposit", "amount": 7000}, {"account_id": 2, "day": "2021-12-12", "type": "Withdraw", "amount": 7000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert each transaction to a signed change

A deposit increases balance, while a withdrawal decreases it. The query transforms one row with

`IF(type = 'Deposit', amount, -amount)`.

Because `type` is restricted to Deposit or Withdraw, the true branch covers deposits and the false branch covers withdrawals.

The starting balance is zero, so the balance after a transaction is the cumulative sum of these signed changes up to that row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"account_id": 1, "day": "2021-11-07", "type": "Deposit", "amount": 2000}, {"account_id": 1, "day": "2021-11-09", "type": "Withdraw", "amount": 1000}, {"account_id": 1, "day": "2021-11-11", "type": "Deposit", "amount": 3000}, {"account_id": 2, "day": "2021-12-07", "type": "Deposit", "amount": 7000}, {"account_id": 2, "day": "2021-12-12", "type": "Withdraw", "amount": 7000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep accounts independent with partitioning

The window clause uses `PARTITION BY account_id`. Each account receives its own running-sum sequence beginning conceptually from zero.

Transactions from another account never enter the current account's balance, even when their dates interleave globally.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The window clause uses `PARTITION BY account_id`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Put transactions in chronological order

Within each account partition, `ORDER BY day` arranges changes from earliest to latest.

The window `SUM` at a row includes the current signed change and all preceding changes in that ordered partition. It therefore reports the balance immediately after that day's transaction.

The composite primary key `(account_id,day)` guarantees that one account cannot have two transactions on the same day. There are no within-account order ties, so the cumulative order is deterministic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["account_id", "day", "balance"], "rows": [[1, "2021-11-07", 2000], [1, "2021-11-09", 1000], [1, "2021-11-11", 4000], [2, "2021-12-07", 7000], [2, "2021-12-12", 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"account_id": 1, "day": "2021-11-07", "type": "Deposit", "amount": 2000}, {"account_id": 1, "day": "2021-11-09", "type": "Withdraw", "amount": 1000}, {"account_id": 1, "day": "2021-11-11", "type": "Deposit", "amount": 3000}, {"account_id": 2, "day": "2021-12-07", "type": "Deposit", "amount": 7000}, {"account_id": 2, "day": "2021-12-12", "type": "Withdraw", "amount": 7000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["account_id", "day", "balance"], "rows": [[1, "2021-11-07", 2000], [1, "2021-11-09", 1000], [1, "2021-11-11", 4000], [2, "2021-12-07", 7000], [2, "2021-12-12", 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit `ROWS` frame:** State `ROWS UNBOUNDED:** - **Explicit `ROWS` frame:** State `ROWS UNBOUNDED PRECEDING` to make cumulative-row semantics explicit.
- **Correlated subquery:** Sum all earlier transactions per row, but can become quadratic without optimization.
- **User variables:** Can simulate running totals in MySQL but are more fragile than window functions.
- **First transaction:** Its balance equals its signed amount because the initial balance is zero.
- **Withdrawal:** Contributes negative amount.
- **Deposit:** Contributes positive amount.
- **Withdraw entire balance:** Running sum may become exactly zero.
- **Several accounts:** Partitions reset accumulation independently.
- **Same day across different accounts:** Harmless because they are in separate partitions.
- **Same account and day:** Excluded by the composite primary key.
- **Final ordering:** `ORDER BY 1,2` uses selected column ordinals.
- **No mutation:** The query reads transactions and returns derived balances.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of transaction rows. A general execution plan sorts rows for partitioned day order and final output, costing $O(R\log R)$ time in the worst case. Window accumulation itself is linear after ordering.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
