# Guided Example: Customer Who Visited but Did Not Make Any Transactions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Visits": [{"visit_id": 1, "customer_id": 23}, {"visit_id": 2, "customer_id": 9}, {"visit_id": 4, "customer_id": 30}, {"visit_id": 5, "customer_id": 54}, {"visit_id": 6, "customer_id": 96}, {"visit_id": 7, "customer_id": 54}, {"visit_id": 8, "customer_id": 54}], "Transactions": [{"transaction_id": 2, "visit_id": 5, "amount": 310}, {"transaction_id": 3, "visit_id": 5, "amount": 300}, {"transaction_id": 9, "visit_id": 5, "amount": 200}, {"transaction_id": 12, "visit_id": 1, "amount": 910}, {"transaction_id": 13, "visit_id": 2, "amount": 970}]}}`
- **Required output:** `{"columns": ["customer_id", "count_no_trans"], "rows": [[30, 1], [54, 2], [96, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Visits`

The objective is to compute `{"columns": ["customer_id", "count_no_trans"], "rows": [[30, 1], [54, 2], [96, 1]]}` from `{"tables": {"Visits": [{"visit_id": 1, "customer_id": 23}, {"visit_id": 2, "customer_id": 9}, {"visit_id": 4, "customer_id": 30}, {"visit_id": 5, "customer_id": 54}, {"visit_id": 6, "customer_id": 96}, {"visit_id": 7, "customer_id": 54}, {"visit_id": 8, "customer_id": 54}], "Transactions": [{"transaction_id": 2, "visit_id": 5, "amount": 310}, {"transaction_id": 3, "visit_id": 5, "amount": 300}, {"transaction_id": 9, "visit_id": 5, "amount": 200}, {"transaction_id": 12, "visit_id": 1, "amount": 910}, {"transaction_id": 13, "visit_id": 2, "amount": 970}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The result counts visits, not customers or transactions

The goal is to find visits for which no transaction row exists, then count those qualifying visits separately for each customer. A customer who visited three times without transacting must contribute three, not one. A visit with several transactions must contribute zero, not a negative value or one result row per transaction.

The query starts from `Visits` because that table contains the events being classified and counted:

`SELECT customer_id, COUNT(1) AS count_no_trans FROM Visits`

Each surviving row represents one visit. Grouping those rows by customer and counting them therefore produces the requested number of no-transaction visits.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Visits": [{"visit_id": 1, "customer_id": 23}, {"visit_id": 2, "customer_id": 9}, {"visit_id": 4, "customer_id": 30}, {"visit_id": 5, "customer_id": 54}, {"visit_id": 6, "customer_id": 96}, {"visit_id": 7, "customer_id": 54}, {"visit_id": 8, "customer_id": 54}], "Transactions": [{"transaction_id": 2, "visit_id": 5, "amount": 310}, {"transaction_id": 3, "visit_id": 5, "amount": 300}, {"transaction_id": 9, "visit_id": 5, "amount": 200}, {"transaction_id": 12, "visit_id": 1, "amount": 910}, {"transaction_id": 13, "visit_id": 2, "amount": 970}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Identifying visits that did have transactions

The subquery

`SELECT visit_id FROM Transactions`

returns the visit identifiers appearing in the transaction table. It does not need `transaction_id` or `amount`, because the question is only whether at least one transaction exists for a visit.

A visit may have multiple transaction rows. That causes the subquery to return the same `visit_id` more than once, but membership testing is unaffected: an identifier is either present or absent. The solution does not join these duplicates to `Visits`, so they cannot multiply the visit rows that will later be counted.

The outer predicate is

`WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)`.

For each row of `Visits`, this asks whether its `visit_id` is absent from the collection of transaction visit identifiers. If absent, no transaction was made during that visit and the row survives. If present one or more times, that visit had at least one transaction and is filtered out.

This is an anti-membership operation: it keeps left-side rows with no matching key on the right side. It is the SQL equivalent of taking the set of all visits and subtracting visits represented in `Transactions`, while still preserving every individual visit row from `Visits`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The subquery

`SELECT visit_id FROM Transactions`

returns t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why filtering happens before grouping

The `WHERE` clause is evaluated on visit rows before the aggregation. This ordering is exactly what the question requires:

1. classify each visit as having or not having any transaction;
2. discard visits that have transactions;
3. group the remaining visits by customer;
4. count the remaining rows in each group.

Grouping first would lose the visit-level distinction or require conditional aggregation. For example, a customer may have both transacting and non-transacting visits. The customer should remain in the result, but only the latter visits should be counted. Filtering the visit rows first handles that mixed history naturally.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "count_no_trans"], "rows": [[30, 1], [54, 2], [96, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Visits": [{"visit_id": 1, "customer_id": 23}, {"visit_id": 2, "customer_id": 9}, {"visit_id": 4, "customer_id": 30}, {"visit_id": 5, "customer_id": 54}, {"visit_id": 6, "customer_id": 96}, {"visit_id": 7, "customer_id": 54}, {"visit_id": 8, "customer_id": 54}], "Transactions": [{"transaction_id": 2, "visit_id": 5, "amount": 310}, {"transaction_id": 3, "visit_id": 5, "amount": 300}, {"transaction_id": 9, "visit_id": 5, "amount": 200}, {"transaction_id": 12, "visit_id": 1, "amount": 910}, {"transaction_id": 13, "visit_id": 2, "amount": 970}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "count_no_trans"], "rows": [[30, 1], [54, 2], [96, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`NOT EXISTS` anti-join:** A correlated `NOT EX:** - **`NOT EXISTS` anti-join:** A correlated `NOT EXISTS` predicate expresses the same absence test and handles nullable values more safely. It is often the preferred production form, but the checked-in solution specifically uses `NOT IN`.
- **`LEFT JOIN` with `IS NULL`:** Left-joining transactions and keeping rows with a null right-side key is another standard anti-join. It must filter before counting so transaction duplicates do not inflate results.
- **Conditional aggregation after a join:** This can work, but multiple transactions per visit require deduplication or visit-level aggregation first. The direct anti-membership filter is simpler.
- **Using `COUNT(transaction_id)`:** After filtering for visits with no transactions, there are no transaction rows to count. The requested quantity is surviving visit rows, so `COUNT(1)` is appropriate.
- **Multiple transactions during one visit:** The visit identifier’s repeated presence in the subquery still excludes that visit only once. No transaction row reaches the outer aggregation.
- **Customer with mixed visit types:** Transaction-bearing visits are removed, while no-transaction visits remain and are counted for that same customer.
- **Customer with no qualifying visits:** No row survives for that customer, so no output group is produced, as required.
- **Several qualifying visits for one customer:** Each unique `Visits` row contributes one, and grouping sums them into a single output row.
- **No transaction rows at all:** The subquery is empty, so every visit survives and the output counts all visits per customer.
- **Every visit has a transaction:** No outer row survives, and the result is empty.
- **Nullable transaction visit identifiers:** A null inside a `NOT IN` subquery can make the predicate unknown. The source contract’s concrete identifiers are required; otherwise use `NOT EXISTS` or explicitly filter nulls.
- **`GROUP BY 1` readability:** It is valid MySQL positional shorthand, but `GROUP BY customer_id` is clearer when select-list columns may later be reordered.
- **Output order:** Because any order is accepted, omitting `ORDER BY` avoids unnecessary sorting and makes no correctness promise about row order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((V+T)$. Let $V$ be the number of rows in `Visits` and $T$ the number of rows in `Transactions`.
- **Auxiliary Space Complexity:** $O(V+T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
