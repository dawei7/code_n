# Guided Example: Customers with Maximum Number of Transactions on Consecutive Days

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}]}}`
- **Required output:** `{"columns": ["customer_id"], "rows": [[101], [105]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["customer_id"], "rows": [[101], [105]]}` from `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn consecutive dates into equal group keys

For each customer, sort transactions by `transaction_date` and assign row numbers one, two, three, and so on.

On a run of consecutive days, both the date and row number advance by one each row. Subtracting the row number in days from the date therefore remains constant throughout the run.

For example, dates May 1, May 2, and May 3 with row numbers one, two, and three all map to April 30. A gap breaks this equality.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First CTE computes the islands key

CTE `s` selects `customer_id` and:

`DATE_SUB(transaction_date, INTERVAL ROW_NUMBER() ... DAY)`.

The window partitions by customer, so row numbering restarts independently for every customer. Ordering by date makes the offset technique meaningful.

The aliased output column is also called `transaction_date`, but it is no longer the original date. It is the derived group identifier for a consecutive island.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why unique customer-date rows matter

The schema guarantees each customer has at most one transaction on a date. Therefore advancing to the next row corresponds to advancing to a distinct later date.

If duplicate dates existed, row number would increase while date did not, splitting or distorting islands. The uniqueness guarantee prevents that issue.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id"], "rows": [[101], [105]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id"], "rows": [[101], [105]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **LAG plus running group number:** Detect date gaps explicitly, cumulatively label islands, then group; more verbose but equally valid.
- **Recursive date walking:** Unnecessary and often slower than window-based islands and gaps.
- **Single transaction:** Forms a streak of length one.
- **Several customers tied:** All maximum streak rows pass the equality filter.
- **Multiple streaks for one customer:** They receive different offset keys and are counted separately.
- **Duplicate qualifying customer:** Exact query may output it twice if two of its streaks tie the global maximum.
- **Unique customer-date guarantee:** Essential to the simple row-number offset.
- **Large gap:** Changes the derived key and starts a new island.
- **Amount values:** Do not affect streak membership or length.
- **Output order:** Ascending customer ID is explicit, but uniqueness is not.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the transaction count. The window function generally requires ordering rows by customer and date, costing $O(n\log n)$ without a supporting order. Grouping derived keys and finding the maximum are typically $O(n)$ expected with hashing or $O(n\log n)$ with sorting.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
