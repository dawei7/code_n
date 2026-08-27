# Guided Example: Page Recommendations II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}`
- **Required output:** `{"columns": ["user_id", "page_id", "friends_likes"], "rows": [[1, 77, 2], [1, 23, 1], [1, 24, 1], [1, 56, 1], [1, 33, 1], [2, 24, 1], [2, 56, 1], [2, 11, 1], [2, 88, 1], [3, 88, 1], [3, 23, 1], [4, 88, 1], [4, 77, 1], [4, 23, 1], [5, 77, 1], [5, 23, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friendship`

The objective is to compute `{"columns": ["user_id", "page_id", "friends_likes"], "rows": [[1, 77, 2], [1, 23, 1], [1, 24, 1], [1, 56, 1], [1, 33, 1], [2, 24, 1], [2, 56, 1], [2, 11, 1], [2, 88, 1], [3, 88, 1], [3, 23, 1], [4, 88, 1], [4, 77, 1], [4, 23, 1], [5, 77, 1], [5, 23, 1]]}` from `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Treat friendship as bidirectional.** Each stored row names two friends, but either user may need recommendations based on the other. CTE `S` creates a directed view of the relationship. The first query keeps `user1_id -> user2_id`, and the second reverses every row to `user2_id -> user1_id`. `UNION` removes duplicate directed pairs if the input happens to represent the same friendship in both directions. Afterward, `S.user1_id` is consistently the recommendation recipient and `S.user2_id` is one of that user's friends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Expand each friend into pages they like.** `S AS s LEFT JOIN Likes AS l ON s.user2_id = l.user_id` associates a directed user-friend pair with every liked page belonging to that friend. For an ordinary matched row, `l.page_id` is a candidate page for `s.user1_id`. If several friends like the same page, the join produces one row for each friend-page match, which is exactly the multiplicity needed for `friends_likes`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Expand each friend into pages they like.** `S AS s LEFT JO... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Remove pages already liked by the recipient.** The correlated `NOT EXISTS` subquery searches `Likes AS l2` for a row where `l2.user_id` equals the recipient and `l2.page_id` equals the candidate page. If such a row exists, the candidate is excluded. If none exists, the candidate has not been liked by the recipient and remains recommendable. Using `NOT EXISTS` avoids adding recipient-like columns to the outer grouping.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "page_id", "friends_likes"], "rows": [[1, 77, 2], [1, 23, 1], [1, 24, 1], [1, 56, 1], [1, 33, 1], [2, 24, 1], [2, 56, 1], [2, 11, 1], [2, 88, 1], [3, 88, 1], [3, 23, 1], [4, 88, 1], [4, 77, 1], [4, 23, 1], [5, 77, 1], [5, 23, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "page_id", "friends_likes"], "rows": [[1, 77, 2], [1, 23, 1], [1, 24, 1], [1, 56, 1], [1, 33, 1], [2, 24, 1], [2, 56, 1], [2, 11, 1], [2, 88, 1], [3, 88, 1], [3, 23, 1], [4, 88, 1], [4, 77, 1], [4, 23, 1], [5, 77, 1], [5, 23, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Inner join to `Likes`:** This is the appropria:** - **Inner join to `Likes`:** This is the appropriate general solution because a friend with no likes contributes no candidate. It prevents the exact source's possible null-page recommendation.
- **Add `l.page_id IS NOT NULL`:** Keeping the left join but filtering null candidate pages also restores correctness, though an inner join communicates the requirement more directly.
- **`UNION ALL` instead of `UNION`:** It is faster only if the input guarantees each undirected friendship is stored exactly once and never in both directions. Otherwise duplicate directed relationships inflate `friends_likes`.
- **Self anti-join:** Left join recipient likes on user and page, then require the recipient match to be null. This is equivalent to `NOT EXISTS` when written carefully.
- **Several friends like one page:** Grouping produces one recommendation and `COUNT(1)` reports every supporting friend.
- **Recipient already likes the page:** The correlated subquery finds the primary-key row and excludes the entire candidate before grouping.
- **Friend with no liked pages:** Under the exact `LEFT JOIN` this can create a null group, which is a correctness defect under the unrestricted schema; inner joining avoids it.
- **User with no friends:** The user has no row in `S` and therefore no recommendations, as intended.
- **No explicit ordering:** Any output order is valid. Adding `ORDER BY` would affect presentation and cost, not recommendation membership.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((F+L+C)\log C)$. Let $F$ be the number of friendship rows, $L$ the number of likes, and $C$ the number of friend-like candidate rows created by the join. Building the symmetric relation processes $O(F)$ rows and `UNION` may sort or hash up to $2F$ rows. With useful indexes or hashes, the joins and anti-lookups process the relations plus candidates, while grouping $C$ rows can cost $O(C)$ expected with hashing or $O(C\log C)$ with sorting.
- **Auxiliary Space Complexity:** $O(F+L+C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
