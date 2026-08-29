# Guided Example: Find Active Users

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Users": [{"user_id": 5, "item": "Smart Crock Pot", "created_at": "2021-09-18", "amount": 698882}, {"user_id": 6, "item": "Smart Lock", "created_at": "2021-09-14", "amount": 11487}, {"user_id": 6, "item": "Smart Thermostat", "created_at": "2021-09-10", "amount": 674762}, {"user_id": 8, "item": "Smart Light Strip", "created_at": "2021-09-29", "amount": 630773}, {"user_id": 4, "item": "Smart Cat Feeder", "created_at": "2021-09-02", "amount": 693545}, {"user_id": 4, "item": "Smart Bed", "created_at": "2021-09-13", "amount": 170249}]}}`
- **Required output:** `{"columns": ["user_id"], "rows": [[6]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Users`

The objective is to compute `{"columns": ["user_id"], "rows": [[6]]}` from `{"tables": {"Users": [{"user_id": 5, "item": "Smart Crock Pot", "created_at": "2021-09-18", "amount": 698882}, {"user_id": 6, "item": "Smart Lock", "created_at": "2021-09-14", "amount": 11487}, {"user_id": 6, "item": "Smart Thermostat", "created_at": "2021-09-10", "amount": 674762}, {"user_id": 8, "item": "Smart Light Strip", "created_at": "2021-09-29", "amount": 630773}, {"user_id": 4, "item": "Smart Cat Feeder", "created_at": "2021-09-02", "amount": 693545}, {"user_id": 4, "item": "Smart Bed", "created_at": "2021-09-13", "amount": 170249}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort each user's purchases chronologically

An active user needs at least one pair of purchases no more than seven days apart.

The window expression:

`LAG(created_at, 1) OVER (PARTITION BY user_id ORDER BY created_at)`

examines purchases separately for each user and orders that user's rows by timestamp. For every row except the first in its partition, it exposes the immediately preceding purchase time as `prev_created_at`.

Partitioning prevents a purchase from one user being compared with another user's purchase.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Users": [{"user_id": 5, "item": "Smart Crock Pot", "created_at": "2021-09-18", "amount": 698882}, {"user_id": 6, "item": "Smart Lock", "created_at": "2021-09-14", "amount": 11487}, {"user_id": 6, "item": "Smart Thermostat", "created_at": "2021-09-10", "amount": 674762}, {"user_id": 8, "item": "Smart Light Strip", "created_at": "2021-09-29", "amount": 630773}, {"user_id": 4, "item": "Smart Cat Feeder", "created_at": "2021-09-02", "amount": 693545}, {"user_id": 4, "item": "Smart Bed", "created_at": "2021-09-13", "amount": 170249}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why checking only adjacent purchases is sufficient

At first, “within seven days of any other purchase” sounds as though every pair must be tested.

Suppose some earlier purchase $A$ and later purchase $B$ are within seven days. Let $P$ be the purchase immediately before $B$ in chronological order. Because $P$ is no earlier than $A$:

$$
B-P\le B-A\le7\text{ days}.
$$

Therefore $B$ and its immediate predecessor also form a qualifying pair.

Conversely, any adjacent pair within seven days is plainly a pair of the user's purchases. So adjacent comparison detects existence exactly and avoids a quadratic self-join.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build a derived table because the lag value is computed

The inner query returns `user_id`, `created_at`, and the window result `prev_created_at` for every purchase row.

The surrounding derived table is named `t`. The next query level can then filter using the computed alias.

This layering is useful in MySQL because a window-function result is conceptually produced after the ordinary `WHERE` phase of the same query block and cannot simply be filtered there as though it were a base column.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id"], "rows": [[6]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Users": [{"user_id": 5, "item": "Smart Crock Pot", "created_at": "2021-09-18", "amount": 698882}, {"user_id": 6, "item": "Smart Lock", "created_at": "2021-09-14", "amount": 11487}, {"user_id": 6, "item": "Smart Thermostat", "created_at": "2021-09-10", "amount": 674762}, {"user_id": 8, "item": "Smart Light Strip", "created_at": "2021-09-29", "amount": 630773}, {"user_id": 4, "item": "Smart Cat Feeder", "created_at": "2021-09-02", "amount": 693545}, {"user_id": 4, "item": "Smart Bed", "created_at": "2021-09-13", "amount": 170249}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id"], "rows": [[6]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join every user's purchase pairs:** Correct but can create $O(R^2)$ candidate pairs for a prolific user.
- **Correlated existence subquery:** Expresses the condition directly but may repeat searches without an effective index.
- **Select directly from the lag-derived table:** Can eliminate the outer `IN` scan while preserving the same adjacent-gap reasoning.
- **User with one purchase:** Has no predecessor and is not active.
- **Gap exactly seven days:** Qualifies because the predicate is inclusive.
- **Gap greater than seven days:** Does not qualify.
- **Same timestamp:** Difference zero, so duplicate purchase rows make the user active.
- **Many qualifying pairs:** `DISTINCT` emits the user only once.
- **Different users with nearby dates:** Never compare because `PARTITION BY user_id` separates them.
- **First partition row:** Its null predecessor is naturally filtered out.
- **Datetime values:** MySQL `DATEDIFF` compares date portions in calendar days.
- **Any output order:** No final sorting is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of purchase rows. Partition ordering can require sorting the rows, giving $O(R\log R)$ time in the absence of a suitable index. Window evaluation, filtering, and deduplication are linear or sorting/hash-based within that bound.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
