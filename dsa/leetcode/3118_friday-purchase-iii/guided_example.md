# Guided Example: Friday Purchase III 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-03", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-10", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-17", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-24", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-24", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-22", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-21", "amount_spend": 12000}], "Users": [{"user_id": 11, "membership": "Premium"}, {"user_id": 15, "membership": "VIP"}, {"user_id": 17, "membership": "Standard"}, {"user_id": 12, "membership": "VIP"}, {"user_id": 8, "membership": "Premium"}, {"user_id": 1, "membership": "VIP"}, {"user_id": 10, "membership": "Standard"}, {"user_id": 13, "membership": "Premium"}]}}`
- **Required output:** `{"columns": ["week_of_month", "membership", "total_amount"], "rows": [[1, "Premium", 1126], [1, "VIP", 0], [2, "Premium", 0], [2, "VIP", 7473], [3, "Premium", 0], [3, "VIP", 0], [4, "Premium", 5117], [4, "VIP", 14933]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["week_of_month", "membership", "total_amount"], "rows": [[1, "Premium", 1126], [1, "VIP", 0], [2, "Premium", 0], [2, "VIP", 7473], [3, "Premium", 0], [3, "VIP", 0], [4, "Premium", 5117], [4, "VIP", 14933]]}` from `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-03", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-10", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-17", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-24", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-24", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-22", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-21", "amount_spend": 12000}], "Users": [{"user_id": 11, "membership": "Premium"}, {"user_id": 15, "membership": "VIP"}, {"user_id": 17, "membership": "Standard"}, {"user_id": 12, "membership": "VIP"}, {"user_id": 8, "membership": "Premium"}, {"user_id": 1, "membership": "VIP"}, {"user_id": 10, "membership": "Standard"}, {"user_id": 13, "membership": "Premium"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**The result must contain rows even when no purchase exists.** A query that starts from `Purchases` cannot produce a missing Premium/week or VIP/week combination. The exact SQL first constructs the complete required eight-row grid: four weeks crossed with two membership types. Purchase totals are then left-joined onto that grid.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-03", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-10", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-17", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-24", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-24", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-22", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-21", "amount_spend": 12000}], "Users": [{"user_id": 11, "membership": "Premium"}, {"user_id": 15, "membership": "VIP"}, {"user_id": 17, "membership": "Standard"}, {"user_id": 12, "membership": "VIP"}, {"user_id": 8, "membership": "Premium"}, {"user_id": 1, "membership": "VIP"}, {"user_id": 10, "membership": "Standard"}, {"user_id": 13, "membership": "Premium"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Generate week numbers one through four.** Recursive CTE `T` begins with:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Its recursive branch adds one while the existing value is less than four. The produced rows are exactly 1, 2, 3, and 4. `UNION` removes duplicates, though this simple increasing recursion would not create any.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["week_of_month", "membership", "total_amount"], "rows": [[1, "Premium", 1126], [1, "VIP", 0], [2, "Premium", 0], [2, "VIP", 7473], [3, "Premium", 0], [3, "VIP", 0], [4, "Premium", 5117], [4, "VIP", 14933]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"user_id": 11, "purchase_date": "2023-11-03", "amount_spend": 1126}, {"user_id": 15, "purchase_date": "2023-11-10", "amount_spend": 7473}, {"user_id": 17, "purchase_date": "2023-11-17", "amount_spend": 2414}, {"user_id": 12, "purchase_date": "2023-11-24", "amount_spend": 9692}, {"user_id": 8, "purchase_date": "2023-11-24", "amount_spend": 5117}, {"user_id": 1, "purchase_date": "2023-11-24", "amount_spend": 5241}, {"user_id": 10, "purchase_date": "2023-11-22", "amount_spend": 8266}, {"user_id": 13, "purchase_date": "2023-11-21", "amount_spend": 12000}], "Users": [{"user_id": 11, "membership": "Premium"}, {"user_id": 15, "membership": "VIP"}, {"user_id": 17, "membership": "Standard"}, {"user_id": 12, "membership": "VIP"}, {"user_id": 8, "membership": "Premium"}, {"user_id": 1, "membership": "VIP"}, {"user_id": 10, "membership": "Standard"}, {"user_id": 13, "membership": "Premium"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["week_of_month", "membership", "total_amount"], "rows": [[1, "Premium", 1126], [1, "VIP", 0], [2, "Premium", 0], [2, "VIP", 7473], [3, "Premium", 0], [3, "VIP", 0], [4, "Premium", 5117], [4, "VIP", 14933]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Literal dimension tables:** Replace recursive `T` with four `UNION ALL` rows. The domain is fixed, but recursion is reusable and clear.
- **Conditional aggregation:** Cross join weeks and memberships, then sum a case expression from purchases; it can express the same zero-preserving grid.
- **Start from purchases only:** Incorrect because missing combinations would have no row to convert to zero.
- **Friday mapping:** MySQL `DAYOFWEEK` uses 6 for Friday, not 5.
- **November date scope:** Guaranteed by the table contract, so the source need not repeat it.
- **Standard members:** Their facts do not match the Premium/VIP grid.
- **No purchases on a Friday:** Left join plus `COALESCE` returns zero.
- **Multiple purchases in one group:** `SUM` combines all of them.
- **Week boundaries:** `CEIL(day / 7)` maps the four relevant Fridays to 1–4.
- **November 29–30:** They are not Fridays in 2023 and are filtered out.
- **Cartesian join syntax:** `T JOIN M` without a condition produces the intended eight combinations in MySQL.
- **Membership ordering:** Premium sorts before VIP lexicographically.
- **Primary key uniqueness:** Individual purchase rows remain distinct before aggregation.
- **Null amount after left join:** `SUM` would be null for an empty group, so `COALESCE` is necessary.
- **Output columns:** Only week, membership, and total are selected.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u+p)$. The generated dimensions have fixed sizes four and two. Let $p$ be the purchase count and $u$ the user count. With an index or primary-key lookup on `Users.user_id`, enriching purchases is roughly $O(p)$ after user storage is available. Hash or indexed joining and aggregation are likewise linear in relevant rows under a typical plan.
- **Auxiliary Space Complexity:** $O(u + p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
