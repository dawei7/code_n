# Guided Example: Loan Types

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Loans": [{"loan_id": 683, "user_id": 101, "loan_type": "Mortgage"}, {"loan_id": 218, "user_id": 101, "loan_type": "AutoLoan"}, {"loan_id": 802, "user_id": 101, "loan_type": "Inschool"}, {"loan_id": 593, "user_id": 102, "loan_type": "Mortgage"}, {"loan_id": 138, "user_id": 102, "loan_type": "Refinance"}, {"loan_id": 294, "user_id": 102, "loan_type": "Inschool"}, {"loan_id": 308, "user_id": 103, "loan_type": "Refinance"}, {"loan_id": 389, "user_id": 104, "loan_type": "Mortgage"}]}}`
- **Required output:** `{"columns": ["user_id"], "rows": [[102]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Loans`

The objective is to compute `{"columns": ["user_id"], "rows": [[102]]}` from `{"tables": {"Loans": [{"loan_id": 683, "user_id": 101, "loan_type": "Mortgage"}, {"loan_id": 218, "user_id": 101, "loan_type": "AutoLoan"}, {"loan_id": 802, "user_id": 101, "loan_type": "Inschool"}, {"loan_id": 593, "user_id": 102, "loan_type": "Mortgage"}, {"loan_id": 138, "user_id": 102, "loan_type": "Refinance"}, {"loan_id": 294, "user_id": 102, "loan_type": "Inschool"}, {"loan_id": 308, "user_id": 103, "loan_type": "Refinance"}, {"loan_id": 389, "user_id": 104, "loan_type": "Mortgage"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn two existence requirements into grouped counts

The output needs one row per user who has at least one `'Refinance'` loan and at least one `'Mortgage'` loan. Other loan types neither help nor disqualify the user.

The query groups all loan rows by `user_id`. Within each group, MySQL evaluates comparison expressions as numeric Boolean values:

- `loan_type = 'Refinance'` is one for a matching row and zero for another non-null type;
- `loan_type = 'Mortgage'` behaves similarly.

Summing each expression therefore counts rows of that target type.

The `HAVING` clause requires both sums to be greater than zero. This exactly means both loan categories exist at least once in the user’s group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Loans": [{"loan_id": 683, "user_id": 101, "loan_type": "Mortgage"}, {"loan_id": 218, "user_id": 101, "loan_type": "AutoLoan"}, {"loan_id": 802, "user_id": 101, "loan_type": "Inschool"}, {"loan_id": 593, "user_id": 102, "loan_type": "Mortgage"}, {"loan_id": 138, "user_id": 102, "loan_type": "Refinance"}, {"loan_id": 294, "user_id": 102, "loan_type": "Inschool"}, {"loan_id": 308, "user_id": 103, "loan_type": "Refinance"}, {"loan_id": 389, "user_id": 104, "loan_type": "Mortgage"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `HAVING` is the right stage

`WHERE` can filter individual loan rows but cannot by itself assert that one user has rows in two different categories. `HAVING` evaluates after all of a user’s rows have been collected and the two sums have been computed.

The logical flow is:

1. partition loan rows by user;
2. count refinance matches in each partition;
3. count mortgage matches in each partition;
4. retain partitions with both counts positive;
5. output the partition key once.

Because each group yields at most one output row, `user_id` values are automatically distinct. A separate `DISTINCT` is unnecessary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why unrelated loan types are harmless

An `'AutoLoan'` row contributes zero to both sums. It remains in the group but does not change either existence test. This is faithful to “at least one” requirements: extra categories do not invalidate a qualifying user.

Repeated loans of a target type contribute multiple ones, but the predicate only asks whether the sum is greater than zero. One and ten both satisfy it, so duplicates do not alter membership.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id"], "rows": [[102]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Loans": [{"loan_id": 683, "user_id": 101, "loan_type": "Mortgage"}, {"loan_id": 218, "user_id": 101, "loan_type": "AutoLoan"}, {"loan_id": 802, "user_id": 101, "loan_type": "Inschool"}, {"loan_id": 593, "user_id": 102, "loan_type": "Mortgage"}, {"loan_id": 138, "user_id": 102, "loan_type": "Refinance"}, {"loan_id": 294, "user_id": 102, "loan_type": "Inschool"}, {"loan_id": 308, "user_id": 103, "loan_type": "Refinance"}, {"loan_id": 389, "user_id": 104, "loan_type": "Mortgage"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id"], "rows": [[102]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`COUNT(DISTINCT loan_type) = 2` after filtering:** This is equivalent if a `WHERE loan_type IN (...)` filter is added, but the exact query uses two Boolean sums.
- **Self-join Loans:** Joining one Mortgage row to one Refinance row per user proves existence but can multiply duplicates and then require `DISTINCT`.
- **Two correlated `EXISTS` tests:** They are readable and can use indexes, but grouping scans all user evidence in one relation.
- **Only one required type:** One sum is zero, so the conjunction correctly rejects the user.
- **Many loans of both types:** Positive sums remain sufficient and the grouped output still contains one row.
- **Unrelated categories:** They contribute zero to both sums and do not disqualify anyone.
- **Null loan type:** It contributes to neither sum under MySQL’s three-valued logic.
- **Dialect portability:** Replace Boolean sums with `CASE` expressions outside MySQL.
- **Output order:** `ORDER BY 1` provides ascending distinct user IDs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let $R$ be the loan-row count and $U$ the number of users. A hash aggregation can scan rows and update two counters per user in expected $O(R)$ time with $O(U)$ group space. A sort-based implementation may take $O(R\log R)$ time.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
