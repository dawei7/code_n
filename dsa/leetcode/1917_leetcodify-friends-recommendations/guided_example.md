# Guided Example: Leetcodify Friends Recommendations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}]}}`
- **Required output:** `{"columns": ["user_id", "recommended_id"], "rows": [[1, 3], [2, 3], [3, 1], [3, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Listens`

The objective is to compute `{"columns": ["user_id", "recommended_id"], "rows": [[1, 3], [2, 3], [3, 1], [3, 2]]}` from `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Make existing friendship directional.** Recommendations must contain both directions, but existing friendships must block both directions. CTE `T` keeps every stored `user1_id -> user2_id` pair and unions its reversal. A correlated lookup can then test an ordered candidate pair directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Pair listen rows sharing one song and day.** The comma-separated `Listens AS l1, Listens AS l2` is a self cross join constrained by the `WHERE` clause. Requiring equal `day` and `song_id` retains pairs of users who listened to the same song on the same date. `l1.user_id != l2.user_id` excludes pairing a user with themselves.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Pair listen rows sharing one song and day.** The comma-sep... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Because the join is directional, a match between users one and three generates both `1 -> 3` and `3 -> 1`. This naturally supplies the unidirectional output requirement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "recommended_id"], "rows": [[1, 3], [2, 3], [3, 1], [3, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "recommended_id"], "rows": [[1, 3], [2, 3], [3, 1], [3, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pre-deduplicate listens:** Selecting distinct :** - **Pre-deduplicate listens:** Selecting distinct user, song, and day before the self join can greatly reduce duplicate multiplication while preserving results.
- **Join through friendship first:** That solves the similar-friends problem, not recommendations; here existing friends must be excluded.
- **Count without `DISTINCT`:** Incorrect when `Listens` contains duplicate rows.
- **Three songs across different days:** Separate groups never combine, so the pair does not qualify.
- **Qualifies on several days:** Outer `DISTINCT` returns each direction once.
- **Directional output:** The self join emits both user orders. Returning only smaller-first pairs would violate the contract.
- **Self recommendation:** Explicit user inequality prevents it.
- **No friendship rows:** `T` is empty, so every qualifying distinct-user pair is eligible.
- **Any output order:** Absence of `ORDER BY` is intentional.
- **Exactly two common songs:** The group exists but fails `HAVING`; only three or more distinct song IDs qualify.
- **Same songs but shifted dates:** Equality is row-by-row on `day`, so matching song sets on different dates provide no evidence.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L^2 + F)$. Let $L$ be the number of listen rows and $F$ the number of friendships. Symmetrizing friendship costs $O(F)$ plus constant-factor duplicate elimination. A broad self-join can consider $O(L^2)$ row pairs before equality filters, matching the manifest's $O(L^2+F)$ time summary.
- **Auxiliary Space Complexity:** $O(L^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
