# Guided Example: Monthly Transactions II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"id": 101, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2019-05-18"}, {"id": 102, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2019-05-19"}, {"id": 103, "country": "US", "state": "approved", "amount": 3000, "trans_date": "2019-06-10"}, {"id": 104, "country": "US", "state": "declined", "amount": 4000, "trans_date": "2019-06-13"}, {"id": 105, "country": "US", "state": "approved", "amount": 5000, "trans_date": "2019-06-15"}], "Chargebacks": [{"trans_id": 102, "trans_date": "2019-05-29"}, {"trans_id": 101, "trans_date": "2019-06-30"}, {"trans_id": 105, "trans_date": "2019-09-18"}]}}`
- **Required output:** `{"columns": ["month", "country", "approved_count", "approved_amount", "chargeback_count", "chargeback_amount"], "rows": [["2019-05", "US", 1, 1000, 1, 2000], ["2019-06", "US", 2, 8000, 1, 1000], ["2019-09", "US", 0, 0, 1, 5000]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["month", "country", "approved_count", "approved_amount", "chargeback_count", "chargeback_amount"], "rows": [["2019-05", "US", 1, 1000, 1, 2000], ["2019-06", "US", 2, 8000, 1, 1000], ["2019-09", "US", 0, 0, 1, 5000]]}` from `{"tables": {"Transactions": [{"id": 101, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2019-05-18"}, {"id": 102, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2019-05-19"}, {"id": 103, "country": "US", "state": "approved", "amount": 3000, "trans_date": "2019-06-10"}, {"id": 104, "country": "US", "state": "declined", "amount": 4000, "trans_date": "2019-06-13"}, {"id": 105, "country": "US", "state": "approved", "amount": 5000, "trans_date": "2019-06-15"}], "Chargebacks": [{"trans_id": 102, "trans_date": "2019-05-29"}, {"trans_id": 101, "trans_date": "2019-06-30"}, {"trans_id": 105, "trans_date": "2019-09-18"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve original transaction rows

The first branch of CTE `T` is `SELECT * FROM Transactions`. In the documented column order, each row contributes `id`, `country`, its original `state`, `amount`, and the transaction `trans_date`.

Approved rows will later contribute to approved metrics. Declined rows contribute zero to all four requested aggregates, but keeping them temporarily is harmless because the final `HAVING` removes groups with no approved or chargeback amount.

Relying on `SELECT *` also relies on the table’s column order matching the second branch. Listing columns explicitly would make the union contract more robust.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"id": 101, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2019-05-18"}, {"id": 102, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2019-05-19"}, {"id": 103, "country": "US", "state": "approved", "amount": 3000, "trans_date": "2019-06-10"}, {"id": 104, "country": "US", "state": "declined", "amount": 4000, "trans_date": "2019-06-13"}, {"id": 105, "country": "US", "state": "approved", "amount": 5000, "trans_date": "2019-06-15"}], "Chargebacks": [{"trans_id": 102, "trans_date": "2019-05-29"}, {"trans_id": 101, "trans_date": "2019-06-30"}, {"trans_id": 105, "trans_date": "2019-09-18"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one pseudo-transaction per chargeback

The second branch joins `Transactions AS t` to `Chargebacks AS c` on `t.id = c.trans_id`. The transaction row supplies country and amount; the chargeback row supplies its own event date.

It selects:

`id, country, 'chargeback', amount, c.trans_date`.

The literal state `'chargeback'` distinguishes this event from original approved and declined rows. The foreign-key relationship guarantees that the referenced transaction information exists.

This correctly attributes a June chargeback for a May transaction to June while retaining the original amount and country.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the exact union choice

The two branches use `UNION`, which performs duplicate elimination, rather than `UNION ALL`. Original transaction states are limited to `'approved'` and `'declined'`, so an original row cannot be identical to a synthetic `'chargeback'` row.

Duplicate elimination could matter among chargeback rows if identical entries for the same transaction and date were allowed. The exact query would combine them into one pseudo-row. Correctness therefore relies on the source semantics treating such duplicate chargeback facts as absent or irrelevant. The editorial’s `UNION ALL` approach preserves every event and is generally safer when duplicate events are meaningful.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["month", "country", "approved_count", "approved_amount", "chargeback_count", "chargeback_amount"], "rows": [["2019-05", "US", 1, 1000, 1, 2000], ["2019-06", "US", 2, 8000, 1, 1000], ["2019-09", "US", 0, 0, 1, 5000]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"id": 101, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2019-05-18"}, {"id": 102, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2019-05-19"}, {"id": 103, "country": "US", "state": "approved", "amount": 3000, "trans_date": "2019-06-10"}, {"id": 104, "country": "US", "state": "declined", "amount": 4000, "trans_date": "2019-06-13"}, {"id": 105, "country": "US", "state": "approved", "amount": 5000, "trans_date": "2019-06-15"}], "Chargebacks": [{"trans_id": 102, "trans_date": "2019-05-29"}, {"trans_id": 101, "trans_date": "2019-06-30"}, {"trans_id": 105, "trans_date": "2019-09-18"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["month", "country", "approved_count", "approved_amount", "chargeback_count", "chargeback_amount"], "rows": [["2019-05", "US", 1, 1000, 1, 2000], ["2019-06", "US", 2, 8000, 1, 1000], ["2019-09", "US", 0, 0, 1, 5000]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`UNION ALL` two preaggregated streams:** Aggregate approved transactions and chargebacks separately, union their metrics, then sum by month and country. This preserves duplicate events and can reduce intermediate rows.
- **Full outer join of aggregates:** Combine the two month-country aggregate tables while keeping groups present on only one side. MySQL requires emulating a full outer join.
- **Chargeback month differs from transaction month:** The synthetic row deliberately uses `c.trans_date`, so the metrics appear in the chargeback month.
- **Chargeback of a declined transaction:** It still counts because the chargeback branch does not require original approval.
- **Declined-only month-country group:** All requested metrics are zero and `HAVING` removes it.
- **Only chargebacks in a reported month:** Approved metrics are zero, while chargeback metrics keep the row.
- **Zero amount:** The exact amount-based `HAVING` assumes positive relevant amounts. Count-based conditions are safer if zero-amount events are valid.
- **Duplicate chargeback facts:** `UNION` removes identical synthetic rows. Use `UNION ALL` when each duplicate row represents a distinct event.
- **Column-order dependence:** `SELECT *` must align with the five expressions in the second branch. Explicit columns are safer for schema evolution.
- **Any output order:** No `ORDER BY` is needed because the contract accepts arbitrary row order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t+c)$. Let $t$ be the number of transactions, $c$ the number of chargebacks, and $g$ the number of output groups.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
