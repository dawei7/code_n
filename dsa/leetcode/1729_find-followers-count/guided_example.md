# Guided Example: Find Followers Count

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Followers": [{"user_id": 0, "follower_id": 1}, {"user_id": 1, "follower_id": 0}, {"user_id": 2, "follower_id": 0}, {"user_id": 2, "follower_id": 1}]}}`
- **Required output:** `{"columns": ["user_id", "followers_count"], "rows": [[0, 1], [1, 1], [2, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Followers`

The objective is to compute `{"columns": ["user_id", "followers_count"], "rows": [[0, 1], [1, 1], [2, 2]]}` from `{"tables": {"Followers": [{"user_id": 0, "follower_id": 1}, {"user_id": 1, "follower_id": 0}, {"user_id": 2, "follower_id": 0}, {"user_id": 2, "follower_id": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each row represents one follower relationship

A row `(user_id, follower_id)` says that the follower follows that user. To find a user's follower count, count how many rows share that `user_id`.

The composite primary key guarantees that the same follower-user relationship cannot appear twice. Therefore a row count is also a distinct-follower count; no `DISTINCT` operation is required.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Followers": [{"user_id": 0, "follower_id": 1}, {"user_id": 1, "follower_id": 0}, {"user_id": 2, "follower_id": 0}, {"user_id": 2, "follower_id": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one group per followed user

`GROUP BY 1` groups by the first select-list expression. In this query, that expression is `user_id`.

Every row for the same followed user enters the same group, while rows for different users remain separate. Each nonempty group produces one output row.

Only users appearing in the `user_id` column are returned. A person who follows others but has no recorded follower relationship as a followed user does not form a group, which matches the table-driven request.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count every row in the group

`COUNT(1) AS followers_count` counts one non-null constant for every row. It therefore returns the number of follower relationships in the user group.

Under MySQL, `COUNT(1)` and `COUNT(*)` have the same relevant result here. Counting `follower_id` would also work under the primary-key schema because that column cannot be null within a key relationship, but counting a constant makes the intent to count rows explicit.

The alias `followers_count` supplies the required output column name.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "followers_count"], "rows": [[0, 1], [1, 1], [2, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Followers": [{"user_id": 0, "follower_id": 1}, {"user_id": 1, "follower_id": 0}, {"user_id": 2, "follower_id": 0}, {"user_id": 2, "follower_id": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "followers_count"], "rows": [[0, 1], [1, 1], [2, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`COUNT(*)`:** It is equivalent for counting group rows and is often the clearest conventional spelling.
- **`COUNT(follower_id)`:** It works when follower IDs are non-null, but row counting avoids relying on that detail.
- **`COUNT(DISTINCT follower_id)`:** It is redundant because the composite primary key already guarantees unique follower relationships.
- **Correlated subquery per user:** It repeats counting work and requires another source of user IDs.
- **One follower:** The group count is one.
- **Many followers:** Every unique relationship contributes once.
- **Mutual following:** Rows `(a,b)` and `(b,a)` belong to different user groups and each counts normally.
- **Self-follow outside unstated restrictions:** A row `(u,u)` would count as one relationship because the schema shown does not forbid it.
- **Zero-follower users:** They cannot appear without a separate users table and are not requested by this relation-only query.
- **Primary-key uniqueness:** It is what makes ordinary count equal distinct follower count.
- **Ascending order:** `ORDER BY 1` supplies it explicitly.
- **Ordinal maintenance:** Reordering projected columns could silently change both grouping and sorting targets.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let $R$ be the number of relationship rows and $U$ the number of distinct followed users. With hash aggregation, scanning rows and incrementing group counts takes expected $O(R)$ time and $O(U)$ group state, matching the manifest.
- **Auxiliary Space Complexity:** $O(U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
