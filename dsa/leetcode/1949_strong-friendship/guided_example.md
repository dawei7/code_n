# Guided Example: Strong Friendship

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 1, "user2_id": 5}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 1, "user2_id": 7}, {"user1_id": 3, "user2_id": 7}, {"user1_id": 1, "user2_id": 6}, {"user1_id": 3, "user2_id": 6}, {"user1_id": 2, "user2_id": 6}]}}`
- **Required output:** `{"columns": ["user1_id", "user2_id", "common_friend"], "rows": [[1, 2, 4], [1, 3, 3]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friendship`

The objective is to compute `{"columns": ["user1_id", "user2_id", "common_friend"], "rows": [[1, 2, 4], [1, 3, 3]]}` from `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 1, "user2_id": 5}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 1, "user2_id": 7}, {"user1_id": 3, "user2_id": 7}, {"user1_id": 1, "user2_id": 6}, {"user1_id": 3, "user2_id": 6}, {"user1_id": 2, "user2_id": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Make the undirected graph explicit

Each `Friendship` row stores one undirected edge only in the canonical order `user1_id < user2_id`. To find neighbors uniformly from either endpoint, CTE `t` creates two directed rows per friendship: the original direction and the reversed direction through `UNION ALL`.

Because the primary key prevents duplicate original edges and the endpoints have strict order, these directed rows are distinct. In `t`, a row `(x, y)` can be read as “$y$ is a friend of $x$.”

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 1, "user2_id": 5}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 1, "user2_id": 7}, {"user1_id": 3, "user2_id": 7}, {"user1_id": 1, "user2_id": 6}, {"user1_id": 3, "user2_id": 6}, {"user1_id": 2, "user2_id": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Start from an existing friendship

Alias `t1` is the friendship being evaluated. This matters because the output asks which existing friendships are strong, not every arbitrary user pair with common neighbors.

Although `t` contains both orientations, the predicate `t1.user1_id < t1.user2_id` retains only the canonical orientation. The result therefore cannot contain both $(x,y)$ and $(y,x)$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join both endpoints to the same neighbor

`t2` is joined with `t1.user2_id = t2.user1_id`. For candidate pair $(x,y)$, each matching `t2` row exposes one friend `t2.user2_id` of $y$.

`t3` is joined with `t1.user1_id = t3.user1_id`, exposing friends `t3.user2_id` of $x$.

The WHERE equality `t3.user2_id = t2.user2_id` requires those exposed neighbor IDs to be the same. Each surviving joined row therefore represents one user $z$ who is a friend of both $x$ and $y$.

Grouping by the candidate endpoints and computing `COUNT(1)` gives the number of common friends. `HAVING COUNT(1) >= 3` retains exactly strong friendships and exposes the count under alias `common_friend`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user1_id", "user2_id", "common_friend"], "rows": [[1, 2, 4], [1, 3, 3]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 1, "user2_id": 5}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 1, "user2_id": 7}, {"user1_id": 3, "user2_id": 7}, {"user1_id": 1, "user2_id": 6}, {"user1_id": 3, "user2_id": 6}, {"user1_id": 2, "user2_id": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user1_id", "user2_id", "common_friend"], "rows": [[1, 2, 4], [1, 3, 3]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Normalize with a separate adjacency table:** Materialize both directions once and index by user. This can simplify repeated graph queries but is unnecessary for a single statement.
- **Correlated common-neighbor count:** Count intersection per friendship with subqueries. It is readable but may repeat neighbor scans.
- **Omit symmetrization:** Then friendships stored with a user in the second column would be missed when looking up that user's neighbors.
- **Use `UNION` instead of `UNION ALL`:** Duplicate elimination is unnecessary because the schema and endpoint order already make the two directed sets disjoint.
- **Exactly three common friends:** The inclusive `>= 3` threshold accepts the friendship.
- **Two common friends:** The group exists but fails HAVING.
- **No common friend:** No witness row reaches grouping, so the friendship is absent.
- **High-degree users:** They can create many join combinations; join-output size is the important workload measure.
- **Canonical endpoint order:** The final inequality removes the reversed copy and satisfies `user1_id < user2_id`.
- **Only actual friendships:** Driving the query from `t1` prevents reporting nonfriends who happen to share neighbors.
- **Candidate endpoints:** Neither endpoint is counted as a common friend because the directed adjacency CTE contains no self-edges.
- **Any output order:** No `ORDER BY` is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W)$. Let $E$ be the number of original friendships and let $W$ be the number of joined common-neighbor witness rows generated before grouping.
- **Auxiliary Space Complexity:** $O(E+W)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
