# Guided Example: Friends With No Mutual Friends

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friends": [{"user_id1": 1, "user_id2": 2}, {"user_id1": 2, "user_id2": 3}, {"user_id1": 2, "user_id2": 4}, {"user_id1": 1, "user_id2": 5}, {"user_id1": 6, "user_id2": 7}, {"user_id1": 3, "user_id2": 4}, {"user_id1": 2, "user_id2": 5}, {"user_id1": 8, "user_id2": 9}]}}`
- **Required output:** `{"columns": ["user_id1", "user_id2"], "rows": [[6, 7], [8, 9]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friends`

The objective is to compute `{"columns": ["user_id1", "user_id2"], "rows": [[6, 7], [8, 9]]}` from `{"tables": {"Friends": [{"user_id1": 1, "user_id2": 2}, {"user_id1": 2, "user_id2": 3}, {"user_id1": 2, "user_id2": 4}, {"user_id1": 1, "user_id2": 5}, {"user_id1": 6, "user_id2": 7}, {"user_id1": 3, "user_id2": 4}, {"user_id1": 2, "user_id2": 5}, {"user_id1": 8, "user_id2": 9}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn undirected friendships into directed adjacency rows.** Each `Friends` row stores a pair once, but either user must be searchable as the starting user. CTE `T` contains the original orientation and the reversed orientation through `UNION ALL`:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friends": [{"user_id1": 1, "user_id2": 2}, {"user_id1": 2, "user_id2": 3}, {"user_id1": 2, "user_id2": 4}, {"user_id1": 1, "user_id2": 5}, {"user_id1": 6, "user_id2": 7}, {"user_id1": 3, "user_id2": 4}, {"user_id1": 2, "user_id2": 5}, {"user_id1": 8, "user_id2": 9}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`(user_id1,user_id2)` and `(user_id2,user_id1)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Thus every row in `T` can be read as “the first user has the second user as a neighbor.”

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id1", "user_id2"], "rows": [[6, 7], [8, 9]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friends": [{"user_id1": 1, "user_id2": 2}, {"user_id1": 2, "user_id2": 3}, {"user_id1": 2, "user_id2": 4}, {"user_id1": 1, "user_id2": 5}, {"user_id1": 6, "user_id2": 7}, {"user_id1": 3, "user_id2": 4}, {"user_id1": 2, "user_id2": 5}, {"user_id1": 8, "user_id2": 9}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id1", "user_id2"], "rows": [[6, 7], [8, 9]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`NOT EXISTS` correlated anti-join:** It avoids tuple `NOT IN` null semantics and can stop at the first mutual friend, often giving the optimizer a clearer anti-join.
- **Store normalized undirected edges:** Normalization helps uniqueness but still requires checking adjacency from both endpoints; the bidirectional CTE makes that explicit.
- **One mutual friend:** A single shared neighbor is enough to exclude the friendship.
- **Several mutual friends:** The subquery may emit the endpoint pair repeatedly, but membership remains true and the outer friendship is excluded once.
- **No mutual friend:** The pair never appears in the subquery and survives.
- **Direct friendship only:** The endpoints are not treated as their own mutual neighbor.
- **Self-pairs in subquery:** They are harmless because valid friendships connect two users.
- **Duplicate friendship rows:** The composite primary key prevents them.
- **NULL identifiers:** Primary-key non-null guarantees are important for `NOT IN` correctness.
- **Output orientation:** The query preserves the orientation stored in `Friends` and sorts those columns as requested.
- **Why `UNION ALL` does not create false mutual friends:** The two orientations represent genuine adjacency. A common-neighbor match still requires identical neighbor identifiers, so merely duplicating direction does not invent a third connection.
- **High-degree user:** A popular mutual friend creates many endpoint combinations in the self-join, explaining why runtime depends on degree distribution rather than only the number of original friendship rows.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m d + m log m)$. Let $M$ be the number of friendship rows and $d_z$ the degree of user $z$. CTE `T` has $2M$ rows. The common-neighbor self-join emits
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
