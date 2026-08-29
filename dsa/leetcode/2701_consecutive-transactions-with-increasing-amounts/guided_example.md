# Guided Example: Consecutive Transactions with Increasing Amounts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 10, "customer_id": 105, "transaction_date": "2023-05-04", "amount": 300}, {"transaction_id": 11, "customer_id": 105, "transaction_date": "2023-05-12", "amount": 250}, {"transaction_id": 12, "customer_id": 105, "transaction_date": "2023-05-13", "amount": 260}, {"transaction_id": 13, "customer_id": 105, "transaction_date": "2023-05-14", "amount": 270}]}}`
- **Required output:** `{"columns": ["customer_id", "consecutive_start", "consecutive_end"], "rows": [[101, "2023-05-01", "2023-05-03"], [105, "2023-05-01", "2023-05-04"], [105, "2023-05-12", "2023-05-14"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["customer_id", "consecutive_start", "consecutive_end"], "rows": [[101, "2023-05-01", "2023-05-03"], [105, "2023-05-01", "2023-05-04"], [105, "2023-05-12", "2023-05-14"]]}` from `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 10, "customer_id": 105, "transaction_date": "2023-05-04", "amount": 300}, {"transaction_id": 11, "customer_id": 105, "transaction_date": "2023-05-12", "amount": 250}, {"transaction_id": 12, "customer_id": 105, "transaction_date": "2023-05-13", "amount": 260}, {"transaction_id": 13, "customer_id": 105, "transaction_date": "2023-05-14", "amount": 270}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A streak continues only through a qualifying predecessor

For a transaction on date $D$ to continue an existing streak, the same customer must have a transaction on exactly $D-1$ whose amount is strictly smaller.

The CTE self-joins current row `t1` to potential predecessor `t2` with three conditions:

- equal `customer_id`;
- `t1.amount > t2.amount`;
- `DATEDIFF(t1.transaction_date, t2.transaction_date) = 1`.

The schema guarantees one transaction per customer and date, so a current row has at most one such previous-day row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 10, "customer_id": 105, "transaction_date": "2023-05-04", "amount": 300}, {"transaction_id": 11, "customer_id": 105, "transaction_date": "2023-05-12", "amount": 250}, {"transaction_id": 12, "customer_id": 105, "transaction_date": "2023-05-13", "amount": 260}, {"transaction_id": 13, "customer_id": 105, "transaction_date": "2023-05-14", "amount": 270}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a left join so broken rows remain visible

An inner join would discard every row that begins a streak. The query instead uses `LEFT JOIN`.

When no qualifying predecessor exists, the `t2` columns are null. That happens for:

- a customer's first transaction;
- a gap of more than one day;
- a previous-day amount that is equal or greater;
- no transaction on the previous day.

Each of these conditions must begin a new candidate run.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark every new run

The `CASE` expression returns one when `t2.customer_id IS NULL` and zero otherwise.

Viewed in customer/date order, these values are boundary markers:

- one means “this row starts a new streak”;
- zero means “this row continues the preceding streak.”

Strictly increasing amounts are enforced by `t1.amount > t2.amount`. Equality is correctly treated as a break.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "consecutive_start", "consecutive_end"], "rows": [[101, "2023-05-01", "2023-05-03"], [105, "2023-05-01", "2023-05-04"], [105, "2023-05-12", "2023-05-14"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Transactions": [{"transaction_id": 1, "customer_id": 101, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 3, "customer_id": 101, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 4, "customer_id": 102, "transaction_date": "2023-05-01", "amount": 50}, {"transaction_id": 5, "customer_id": 102, "transaction_date": "2023-05-03", "amount": 100}, {"transaction_id": 6, "customer_id": 102, "transaction_date": "2023-05-04", "amount": 200}, {"transaction_id": 7, "customer_id": 105, "transaction_date": "2023-05-01", "amount": 100}, {"transaction_id": 8, "customer_id": 105, "transaction_date": "2023-05-02", "amount": 150}, {"transaction_id": 9, "customer_id": 105, "transaction_date": "2023-05-03", "amount": 200}, {"transaction_id": 10, "customer_id": 105, "transaction_date": "2023-05-04", "amount": 300}, {"transaction_id": 11, "customer_id": 105, "transaction_date": "2023-05-12", "amount": 250}, {"transaction_id": 12, "customer_id": 105, "transaction_date": "2023-05-13", "amount": 260}, {"transaction_id": 13, "customer_id": 105, "transaction_date": "2023-05-14", "amount": 270}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "consecutive_start", "consecutive_end"], "rows": [[101, "2023-05-01", "2023-05-03"], [105, "2023-05-01", "2023-05-04"], [105, "2023-05-12", "2023-05-14"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`LAG` previous date and amount:** Can mark breaks directly after ordering each customer, avoiding the self-join.
- **Date minus row-number islands alone:** Detects consecutive days but needs an additional break marker for non-increasing amounts.
- **One transaction:** Forms a one-row island and is filtered out.
- **Exactly three days:** Qualifies because `HAVING` is inclusive.
- **Equal amount on the next day:** Breaks the streak because increase must be strict.
- **Missing day:** Breaks the streak even if the later amount is larger.
- **Several periods for one customer:** Group identifiers keep them separate.
- **Customer transition:** The new customer's first row starts a fresh marker value.
- **Unique customer/date guarantee:** Prevents multiple predecessor matches from duplicating rows.
- **Final ordering:** The exact query lacks explicit start/end tie ordering within one customer.
- **Source table:** The query reads and groups it without mutation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of transactions. With effective lookup support for customer/date, the self-join, window ordering, and grouping are commonly implemented in $O(R\log R)$ time and $O(R)$ working space, matching the manifest.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
