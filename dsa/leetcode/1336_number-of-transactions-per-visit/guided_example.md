# Guided Example: Number of Transactions per Visit

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Visits": [{"user_id": 1, "visit_date": "2020-01-01"}, {"user_id": 2, "visit_date": "2020-01-02"}, {"user_id": 12, "visit_date": "2020-01-01"}, {"user_id": 19, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-02"}, {"user_id": 2, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-04"}, {"user_id": 7, "visit_date": "2020-01-11"}, {"user_id": 9, "visit_date": "2020-01-25"}, {"user_id": 8, "visit_date": "2020-01-28"}], "Transactions": [{"user_id": 1, "transaction_date": "2020-01-02", "amount": 120}, {"user_id": 2, "transaction_date": "2020-01-03", "amount": 22}, {"user_id": 7, "transaction_date": "2020-01-11", "amount": 232}, {"user_id": 1, "transaction_date": "2020-01-04", "amount": 7}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 33}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 66}, {"user_id": 8, "transaction_date": "2020-01-28", "amount": 1}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 99}]}}`
- **Required output:** `{"columns": ["transactions_count", "visits_count"], "rows": [[0, 4], [1, 5], [2, 0], [3, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Visits`

The objective is to compute `{"columns": ["transactions_count", "visits_count"], "rows": [[0, 4], [1, 5], [2, 0], [3, 1]]}` from `{"tables": {"Visits": [{"user_id": 1, "visit_date": "2020-01-01"}, {"user_id": 2, "visit_date": "2020-01-02"}, {"user_id": 12, "visit_date": "2020-01-01"}, {"user_id": 19, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-02"}, {"user_id": 2, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-04"}, {"user_id": 7, "visit_date": "2020-01-11"}, {"user_id": 9, "visit_date": "2020-01-25"}, {"user_id": 8, "visit_date": "2020-01-28"}], "Transactions": [{"user_id": 1, "transaction_date": "2020-01-02", "amount": 120}, {"user_id": 2, "transaction_date": "2020-01-03", "amount": 22}, {"user_id": 7, "transaction_date": "2020-01-11", "amount": 232}, {"user_id": 1, "transaction_date": "2020-01-04", "amount": 7}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 33}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 66}, {"user_id": 8, "transaction_date": "2020-01-28", "amount": 1}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 99}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate the complete bucket axis

The recursive common table expression `S` begins with `SELECT 0 AS n`. Its recursive member selects `n + 1` while the current value is smaller than the maximum count belonging to any user and transaction date.

The scalar subquery finds that maximum in two stages. Its inner query groups `Transactions` by `user_id, transaction_date` and computes `COUNT(1) AS cnt` for each group. Each group corresponds to the transaction rows belonging to one bank visit. The outer `MAX(cnt)` then finds the largest number of transactions performed during any visit.

If the maximum is three, recursion produces the rows zero, one, two, and three. The stopping condition is checked against the current `n`, so the row equal to the maximum is created from the preceding row, and recursion stops afterward. This inclusive endpoint is necessary because the most active visit needs its own output bucket.

Using `UNION` rather than `UNION ALL` asks SQL to remove duplicates, although this particular recurrence generates each increasing integer only once. The deduplication is not needed for correctness, but it does not change the produced sequence.

If `Transactions` has no rows, `MAX(cnt)` is `NULL`. The anchor row zero still exists, while `n < NULL` is not true in SQL’s three-valued logic, so recursion adds nothing. The bucket sequence then correctly consists only of zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Visits": [{"user_id": 1, "visit_date": "2020-01-01"}, {"user_id": 2, "visit_date": "2020-01-02"}, {"user_id": 12, "visit_date": "2020-01-01"}, {"user_id": 19, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-02"}, {"user_id": 2, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-04"}, {"user_id": 7, "visit_date": "2020-01-11"}, {"user_id": 9, "visit_date": "2020-01-25"}, {"user_id": 8, "visit_date": "2020-01-28"}], "Transactions": [{"user_id": 1, "transaction_date": "2020-01-02", "amount": 120}, {"user_id": 2, "transaction_date": "2020-01-03", "amount": 22}, {"user_id": 7, "transaction_date": "2020-01-11", "amount": 232}, {"user_id": 1, "transaction_date": "2020-01-04", "amount": 7}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 33}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 66}, {"user_id": 8, "transaction_date": "2020-01-28", "amount": 1}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 99}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Attach a count to every visit

The second common table expression, `T`, starts from `Visits AS v`. Its derived transaction table groups transaction rows by user and date and computes one `cnt` per group. The notation `GROUP BY 1, 2` refers to the first and second selected expressions, namely `user_id` and `transaction_date`.

The join condition uses both pieces of the visit identity:

- `v.user_id = t.user_id` matches the visitor.
- `v.visit_date = t.transaction_date` matches the date of that particular visit.

Joining only on the user would incorrectly combine transactions from different visits made by the same person. Joining on the composite key keeps each transaction group attached to exactly the promised visit.

The join is a `LEFT JOIN` from `Visits`. Therefore, a visit remains present even when no grouped transaction row matches it. In that case, `t.cnt` is `NULL`, and `COALESCE(cnt, 0)` turns it into the required zero-transaction count. Because `Visits` has one row per composite primary key and the transaction derived table has at most one row per same key, `T` has exactly one row for every visit.

The transaction `amount` never enters the calculation. The problem asks how many transactions occurred, not how much money they moved. Duplicate transaction rows count separately because each row represents a transaction and `COUNT(1)` counts every row in its group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The second common table expression, `T`, starts from `Visits... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preserve empty histogram buckets

The final query starts from `S AS s` and left-joins `T AS t` using `s.n = t.cnt`. Starting from the generated sequence is essential. If no visit made exactly two transactions, bucket two still survives the left join with null columns from `T`.

The expression `COUNT(user_id)` counts only non-null matched visit identifiers. It does not use `COUNT(*)`, which would count the placeholder row produced by the left join and incorrectly report one visit for an empty bucket. Because `user_id` comes from real visit rows, the result is the number of visits whose transaction count equals `n`, or zero if none match.

`GROUP BY n` creates one result row per bucket. The selected aliases name the bucket `transactions_count` and its frequency `visits_count`. Finally, `ORDER BY n` returns the histogram from zero upward, as required.

The whole construction is exhaustive and exclusive. Every visit appears once in `T` with its exact count, so it joins exactly one bucket. Every required bucket appears once in `S`, even if no visit joins it. The final grouped counts therefore describe all visits without omission or double counting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["transactions_count", "visits_count"], "rows": [[0, 4], [1, 5], [2, 0], [3, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Visits": [{"user_id": 1, "visit_date": "2020-01-01"}, {"user_id": 2, "visit_date": "2020-01-02"}, {"user_id": 12, "visit_date": "2020-01-01"}, {"user_id": 19, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-02"}, {"user_id": 2, "visit_date": "2020-01-03"}, {"user_id": 1, "visit_date": "2020-01-04"}, {"user_id": 7, "visit_date": "2020-01-11"}, {"user_id": 9, "visit_date": "2020-01-25"}, {"user_id": 8, "visit_date": "2020-01-28"}], "Transactions": [{"user_id": 1, "transaction_date": "2020-01-02", "amount": 120}, {"user_id": 2, "transaction_date": "2020-01-03", "amount": 22}, {"user_id": 7, "transaction_date": "2020-01-11", "amount": 232}, {"user_id": 1, "transaction_date": "2020-01-04", "amount": 7}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 33}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 66}, {"user_id": 8, "transaction_date": "2020-01-28", "amount": 1}, {"user_id": 9, "transaction_date": "2020-01-25", "amount": 99}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["transactions_count", "visits_count"], "rows": [[0, 4], [1, 5], [2, 0], [3, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Calendar or numbers table:** A permanent integ:** - **Calendar or numbers table:** A permanent integer table can replace the recursive `S` sequence. It avoids recursive-CTE limits but requires that the database already provide a sufficiently large range.
- **Window-based sequence generation:** Some SQL dialects can derive row numbers from an existing large relation. That approach is dialect-specific and must still guarantee a zero row when transaction data is empty.
- **Correlated count per visit:** A scalar subquery could count transactions for each visit, but repeatedly searching `Transactions` may be slower than grouping once and joining the result.
- **Starting from transaction groups:** An inner or left join rooted at grouped transactions would lose zero-transaction visits. The query correctly starts `T` from `Visits`.
- **Using `COUNT(*)` in the final query:** This would count the left-join placeholder for an empty bucket and return one instead of zero. Counting the nullable matched `user_id` avoids that error.
- **Same user on multiple dates:** Each `(user_id, visit_date)` pair is a separate visit. Both columns must participate in grouping and joining.
- **Duplicate transaction rows:** They are intentionally counted individually. The query does not use `DISTINCT` because duplicate rows still represent separate transactions under the table contract.
- **Unused amount column:** Transaction amounts do not affect bucket membership; only the number of transaction rows matters.
- **No visits in an intermediate bucket:** The recursive sequence preserves the bucket, and the final count is zero.
- **No transaction rows:** The maximum is null, recursion retains only zero, and all visits join the zero bucket.
- **Maximum endpoint:** The recursion must include the largest observed count, not stop one value before it. Testing `n < maximum` before producing `n + 1` creates the endpoint correctly.
- **Recursive depth limits:** A database may cap recursive common-table-expression iterations. If one visit can have a count beyond that configured cap, the session setting or sequence-generation strategy must accommodate it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $V$ be the number of rows in `Visits`, $T$ the number of rows in `Transactions`, $U$ the number of grouped visit keys that have transactions, and $K$ the maximum transaction count for one visit. The generated bucket sequence has $K + 1$ rows, and $K \le T$ whenever transactions exist.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
