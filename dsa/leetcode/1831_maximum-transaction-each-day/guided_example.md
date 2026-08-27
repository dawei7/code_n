# Guided Example: Maximum Transaction Each Day

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"transaction_id": 8, "day": "2021-04-03 15:57:28", "amount": 57}, {"transaction_id": 9, "day": "2021-04-28 08:47:25", "amount": 21}, {"transaction_id": 1, "day": "2021-04-29 13:28:30", "amount": 58}, {"transaction_id": 5, "day": "2021-04-28 16:39:59", "amount": 40}, {"transaction_id": 6, "day": "2021-04-29 23:39:28", "amount": 58}]}}`
- **Required output:** `{"columns": ["transaction_id"], "rows": [[1], [5], [6], [8]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["transaction_id"], "rows": [[1], [5], [6], [8]]}` from `{"tables": {"Transactions": [{"transaction_id": 8, "day": "2021-04-03 15:57:28", "amount": 57}, {"transaction_id": 9, "day": "2021-04-28 08:47:25", "amount": 21}, {"transaction_id": 1, "day": "2021-04-29 13:28:30", "amount": 58}, {"transaction_id": 5, "day": "2021-04-28 16:39:59", "amount": 40}, {"transaction_id": 6, "day": "2021-04-29 23:39:28", "amount": 58}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Rank transactions inside day groups.** The query uses a window function to compare each transaction with other rows assigned to the same group. The common table expression `T` selects the transaction identifier and computes

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"transaction_id": 8, "day": "2021-04-03 15:57:28", "amount": 57}, {"transaction_id": 9, "day": "2021-04-28 08:47:25", "amount": 21}, {"transaction_id": 1, "day": "2021-04-29 13:28:30", "amount": 58}, {"transaction_id": 5, "day": "2021-04-28 16:39:59", "amount": 40}, {"transaction_id": 6, "day": "2021-04-29 23:39:28", "amount": 58}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`RANK() OVER (PARTITION BY DAY(day) ORDER BY amount DESC)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `RANK() OVER (PARTITION BY DAY(day) ORDER BY amount DESC)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Within each partition, ordering amounts in descending order places the greatest amount first. `RANK` assigns rank one to that first amount. If several transactions tie for the maximum, they all receive rank one, because `RANK` gives equal ordering values the same rank. This is exactly the tie-preserving behavior the result needs; `ROW_NUMBER` would arbitrarily keep only one tied transaction.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["transaction_id"], "rows": [[1], [5], [6], [8]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"transaction_id": 8, "day": "2021-04-03 15:57:28", "amount": 57}, {"transaction_id": 9, "day": "2021-04-28 08:47:25", "amount": 21}, {"transaction_id": 1, "day": "2021-04-29 13:28:30", "amount": 58}, {"transaction_id": 5, "day": "2021-04-28 16:39:59", "amount": 40}, {"transaction_id": 6, "day": "2021-04-29 23:39:28", "amount": 58}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["transaction_id"], "rows": [[1], [5], [6], [8]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Full-date window partition:** `PARTITION BY DA:** - **Full-date window partition:** `PARTITION BY DATE(day)` preserves year, month, and day while ignoring time. It is the direct correction needed for the stated calendar-date contract.
- **Aggregate and join:** Compute each full date’s maximum amount, then join it back to `Transactions` on date and amount. This naturally retains all ties but requires an additional relational stage.
- **Correlated `NOT EXISTS`:** Keep a transaction when no row on the same full date has a greater amount. It also avoids `MAX()` for the follow-up, though indexing strongly affects performance.
- **Self anti-join:** Left join each row to a same-date row with a larger amount and retain rows with no match. This answers the follow-up without `MAX()` but needs careful date comparison and can create many intermediate pairs.
- **`DENSE_RANK`:** Filtering dense rank one gives the same winners as `RANK` because both preserve maximum ties.
- **`ROW_NUMBER`:** This is unsuitable when maximum amounts tie because only one tied row receives row number one.
- **Several maxima on one date:** `RANK` assigns one to all of them, so all identifiers survive.
- **Only one transaction on a date:** It is automatically the maximum and receives rank one.
- **Same day-of-month in different months:** The exact `DAY(day)` expression incorrectly merges these calendar dates and may discard valid winners.
- **Same day-of-month in different years:** The same defect occurs because the year is also discarded.
- **Different times on the same calendar date:** They should be grouped together; both `DAY(day)` and `DATE(day)` do that, but only `DATE(day)` also separates other months and years.
- **Output order:** `ORDER BY 1` refers to `transaction_id` in this one-column projection and sorts ascending by default, though spelling out the column name is more explicit for readers.
- **Null timestamps:** The local schema does not state a null rule. If nulls were possible, their partition behavior would require a separate contract decision rather than an assumption.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r\log r)$. Let `r` be the number of rows in `Transactions`. A database typically sorts rows by partition key and descending amount to evaluate this window specification. The usual upper bound is `O(r log r)` time, followed by linear filtering and output sorting. Because the final `ORDER BY transaction_id` may require another sort of up to `r` surviving rows, the overall asymptotic bound remains `O(r log r)`.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
