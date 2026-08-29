# Guided Example: Leetcodify Similar Friends

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}]}}`
- **Required output:** `{"columns": ["user1_id", "user2_id"], "rows": [[1, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Listens`

The objective is to compute `{"columns": ["user1_id", "user2_id"], "rows": [[1, 2]]}` from `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Begin with actual friendship pairs.** The output must preserve `user1_id < user2_id` exactly as stored. The query starts from `Friendship AS f`, so every candidate is already a real friend pair in canonical order. Unlike recommendation queries, no reversed copy is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Attach listen histories for both endpoints.** The first join connects `user1_id` to `l1.user_id`; the second connects `user2_id` to `l2.user_id`. Conceptually this forms combinations of listen rows for the two friends. The `WHERE` clause retains combinations with the same `song_id` and the same `day`, which represent one song both users heard on one date.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Although both joins are written `LEFT JOIN`, the equality predicates in `WHERE` reject rows where either listen side is null. They therefore behave like inner joins for result membership. Writing explicit inner joins would communicate this more directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user1_id", "user2_id"], "rows": [[1, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Listens": [{"user_id": 1, "song_id": 10, "day": "2021-03-15"}, {"user_id": 1, "song_id": 11, "day": "2021-03-15"}, {"user_id": 1, "song_id": 12, "day": "2021-03-15"}, {"user_id": 2, "song_id": 10, "day": "2021-03-15"}, {"user_id": 2, "song_id": 11, "day": "2021-03-15"}, {"user_id": 2, "song_id": 12, "day": "2021-03-15"}, {"user_id": 3, "song_id": 10, "day": "2021-03-15"}, {"user_id": 3, "song_id": 11, "day": "2021-03-15"}, {"user_id": 3, "song_id": 12, "day": "2021-03-15"}, {"user_id": 4, "song_id": 10, "day": "2021-03-15"}, {"user_id": 4, "song_id": 11, "day": "2021-03-15"}, {"user_id": 4, "song_id": 13, "day": "2021-03-15"}, {"user_id": 5, "song_id": 10, "day": "2021-03-16"}, {"user_id": 5, "song_id": 11, "day": "2021-03-16"}, {"user_id": 5, "song_id": 12, "day": "2021-03-16"}], "Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user1_id", "user2_id"], "rows": [[1, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Pre-deduplicate `Listens`:** A distinct user/song/day CTE prevents duplicate join multiplication and preserves semantics.
- **Use explicit inner joins:** Produces the same qualifying rows and makes the effective null-rejecting behavior clearer.
- **Start from all listener pairs:** Then friendship must be joined afterward; beginning with `Friendship` naturally preserves canonical pair order.
- **Duplicate listen records:** `COUNT(DISTINCT song_id)` ensures one song counts once.
- **Three songs on different days:** Grouping by day keeps them separate and rejects the pair.
- **Qualifies on multiple days:** Final `DISTINCT` returns one friendship row.
- **Nonfriends with matching songs:** They never enter because `Friendship` is the driving table.
- **Already canonical ordering:** The query returns stored columns and never reverses them.
- **Any output order:** Absence of `ORDER BY` is valid.
- **Exactly three distinct matches:** The inclusive `>= 3` threshold accepts the pair.
- **Friend with no listen rows:** Null-extended join rows fail equality predicates, so the pair produces no qualifying group.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L^2 + F)$. Let $L$ be listen-row count and $F$ friendship count. A broad plan may create up to quadratic combinations of listen rows while matching friend endpoints, giving the manifest's $O(L^2+F)$ time summary. Suitable indexes on user, day, and song can reduce actual matching substantially.
- **Auxiliary Space Complexity:** $O(L^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
