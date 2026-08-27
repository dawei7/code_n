# Guided Example: All the Pairs With the Maximum Number of Common Followers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Relations": [{"user_id": 1, "follower_id": 3}, {"user_id": 2, "follower_id": 3}, {"user_id": 7, "follower_id": 3}, {"user_id": 1, "follower_id": 4}, {"user_id": 2, "follower_id": 4}, {"user_id": 7, "follower_id": 4}, {"user_id": 1, "follower_id": 5}, {"user_id": 2, "follower_id": 6}, {"user_id": 7, "follower_id": 5}]}}`
- **Required output:** `{"columns": ["user1_id", "user2_id"], "rows": [[1, 7]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Relations`

The objective is to compute `{"columns": ["user1_id", "user2_id"], "rows": [[1, 7]]}` from `{"tables": {"Relations": [{"user_id": 1, "follower_id": 3}, {"user_id": 2, "follower_id": 3}, {"user_id": 7, "follower_id": 3}, {"user_id": 1, "follower_id": 4}, {"user_id": 2, "follower_id": 4}, {"user_id": 7, "follower_id": 4}, {"user_id": 1, "follower_id": 5}, {"user_id": 2, "follower_id": 6}, {"user_id": 7, "follower_id": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each shared follower into evidence for a user pair

`Relations` stores one row per user-follower relationship. The query joins the table to itself on equal `follower_id`. A joined row means that the same follower follows both `r1.user_id` and `r2.user_id`.

The additional condition `r1.user_id < r2.user_id` has two purposes. It prevents pairing a user with itself, and it chooses one canonical orientation for each unordered pair. Without it, a shared follower would generate both $(x,y)$ and $(y,x)$.

Because `(user_id, follower_id)` is a primary key, a follower contributes at most one joined row to a fixed user pair. Therefore `COUNT(1)` after grouping is exactly the number of distinct common followers; an explicit `COUNT(DISTINCT follower_id)` is unnecessary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Relations": [{"user_id": 1, "follower_id": 3}, {"user_id": 2, "follower_id": 3}, {"user_id": 7, "follower_id": 3}, {"user_id": 1, "follower_id": 4}, {"user_id": 2, "follower_id": 4}, {"user_id": 7, "follower_id": 4}, {"user_id": 1, "follower_id": 5}, {"user_id": 2, "follower_id": 6}, {"user_id": 7, "follower_id": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count common followers per pair

The join output is grouped by `r1.user_id, r2.user_id`. Every group represents one user pair that shares at least one follower, and its count is that pair's common-follower total.

For the sample, follower three generates evidence for pairs $(1,2)$, $(1,7)$, and $(2,7)$. Follower four generates the same three. Follower five adds evidence for $(1,7)$ only, making its grouped count the largest.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The join output is grouped by `r1.user_id, r2.user_id`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rank grouped counts and keep every maximum

Within the CTE, `RANK() OVER (ORDER BY COUNT(1) DESC)` orders pair groups from the greatest count to the least. Every pair tied for the greatest count receives rank one. `RANK` rather than `ROW_NUMBER` is essential because the problem asks for all maximum pairs, not an arbitrary single winner.

The outer query selects the two IDs from rank-one rows. The ordering is already canonical from the join predicate. No `ORDER BY` is needed because any output order is accepted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user1_id", "user2_id"], "rows": [[1, 7]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Relations": [{"user_id": 1, "follower_id": 3}, {"user_id": 2, "follower_id": 3}, {"user_id": 7, "follower_id": 3}, {"user_id": 1, "follower_id": 4}, {"user_id": 2, "follower_id": 4}, {"user_id": 7, "follower_id": 4}, {"user_id": 1, "follower_id": 5}, {"user_id": 2, "follower_id": 6}, {"user_id": 7, "follower_id": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user1_id", "user2_id"], "rows": [[1, 7]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dense rank:** `DENSE_RANK` would also assign o:** - **Dense rank:** `DENSE_RANK` would also assign one to all maximum groups. Differences in later rank gaps do not matter when filtering only rank one.
- **Maximum subquery:** Compute counts in one CTE, compute their maximum in another, and join or filter for equality. It is more verbose but expresses the same logic.
- **Row number:** `ROW_NUMBER` is incorrect because it selects only one row among tied maximum pairs.
- **Missing order predicate:** Without `r1.user_id < r2.user_id`, self-pairs and reversed duplicates appear.
- **One shared follower:** Such a pair forms a group; it wins if no pair has a larger count.
- **Tied maxima:** Every tied group receives `rk = 1` and is returned.
- **Unique maximum:** Exactly one grouped pair receives rank one, so the outer query returns one row.
- **Primary-key guarantee:** It prevents one follower from being counted twice for the same user.
- **Followers as users:** A `follower_id` need not have rows as a followed user; only their role as a shared follower matters.
- **High-degree follower:** One follower following $d$ users generates $d(d-1)/2$ canonical pair witnesses.
- **Any output order:** The outer query deliberately omits ordering.
- **Positive-group scope:** The self-join cannot materialize pairs with zero common followers; a separate user universe would be required for that different interpretation.
- **Why `COUNT(1)` is sufficient:** The relation key makes each joined witness a distinct common follower for that canonical user pair, so counting joined rows equals counting common followers.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R+J\log J)$. Let $R$ be the number of relation rows and $J$ the number of joined shared-follower witness rows.
- **Auxiliary Space Complexity:** $O(J)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
