# Guided Example: Friday Purchases II 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}`
- **Required output:** `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [2, "2023-11-10", 0], [3, "2023-11-17", 0], [4, "2023-11-24", 21692]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [2, "2023-11-10", 0], [3, "2023-11-17", 0], [4, "2023-11-24", 21692]]}` from `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from a calendar so missing purchases still have rows

Version II must return every Friday of November 2023, assigning zero when no purchase occurred. A query driven only by `Purchases` cannot produce a date absent from that table. The exact solution therefore constructs all November dates first.

Recursive CTE `T` begins with `'2023-11-01'`. Its recursive branch adds one day:

`purchase_date + INTERVAL 1 DAY`

while the current date is before `'2023-11-30'`. The generated relation contains one row for each of the 30 calendar dates from November 1 through November 30 inclusive.

The query uses `UNION` rather than `UNION ALL`. Dates are inherently unique in this increasing sequence, so duplicate removal changes no membership, though `UNION ALL` would express the fact more cheaply.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Preserve calendar dates with a left join

`T LEFT JOIN Purchases USING (purchase_date)` matches every purchase to its date while retaining a calendar row even when no match exists.

For a date with purchases, the join produces one row per purchase. For a date without purchases, it produces one row whose purchase-side columns, including `amount_spend`, are `NULL`.

An inner join would discard exactly the missing dates that this version must show, so join direction is central to correctness.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `T LEFT JOIN Purchases USING (purchase_date)` matches every ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Keep only Fridays after building the calendar

`WHERE DAYOFWEEK(purchase_date) = 6` filters the calendar to MySQL Fridays. Because `USING` exposes one coalesced join column and every retained row has a CTE date, the function remains defined even when there is no purchase.

The four generated dates are November 3, 10, 17, and 24. Filtering after the left join is safe because the condition refers to the preserved date, not a nullable purchase-side field. A condition on `amount_spend` in `WHERE` could accidentally turn the left join into an inner join, but this query avoids that.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [2, "2023-11-10", 0], [3, "2023-11-17", 0], [4, "2023-11-24", 21692]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-07", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-30", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-14", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-03", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-16", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-12", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-24", "amount_spend": 12000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["week_of_month", "purchase_date", "total_amount"], "rows": [[1, "2023-11-03", 5117], [2, "2023-11-10", 0], [3, "2023-11-17", 0], [4, "2023-11-24", 21692]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Drive from `Purchases`:** This cannot emit Fri:** - **Drive from `Purchases`:** This cannot emit Fridays with no rows and would solve version I instead.
- **Hard-code four `UNION ALL` dates:** It works for this fixed month but is less systematic than generating the calendar.
- **Use a permanent calendar table:** In production analytics this is often preferable and avoids recursive generation.
- **Use an inner join:** It drops zero-purchase Fridays and violates the core requirement.
- **Place a purchase-side filter in `WHERE`:** It can null-reject unmatched rows and unintentionally undo the left join.
- **Omit `COALESCE`:** Empty Friday groups would display `NULL` rather than zero.
- **Multiple purchases on one date:** The left join creates multiple rows and `SUM` combines all amounts.
- **MySQL weekday numbering:** Friday is six because Sunday is one.
- **Recursive termination:** The strict “less than November 30” condition generates November 30 once and stops before December.
- **Output order:** `ORDER BY 1` gives weeks one through four.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $D=30$ be the generated day count and $R$ the purchase-row count. Calendar generation is $O(D)$. Joining can be expected $O(D+R)$ with hashing or indexed date lookup, while a sort/merge or grouping plan may cost $O((D+R)\log(D+R))$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
