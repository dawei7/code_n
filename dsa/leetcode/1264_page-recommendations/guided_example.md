# Guided Example: Page Recommendations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}`
- **Required output:** `{"columns": ["recommended_page"], "rows": [[23], [24], [56], [33], [77]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friendship`

The objective is to compute `{"columns": ["recommended_page"], "rows": [[23], [24], [56], [33], [77]]}` from `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The recommendation rule has three separate jobs

A page belongs in the result only if at least one friend of user `1` likes it, user `1` does not already like it, and it appears only once even when several friends like it. The query mirrors these three jobs: construct the friend set, join those friends to their likes, and filter plus deduplicate the resulting pages.

The challenge in the first job is that friendship is undirected in meaning but stored in two directed-looking columns. User `1` may appear as `user1_id` or as `user2_id`. Looking at only one column would silently miss valid friends.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Constructing a one-column friend relation

The common table expression named `T` normalizes both orientations:

`SELECT user1_id AS user_id FROM Friendship WHERE user2_id = 1`

selects the opposite endpoint when user `1` is stored on the right. The second branch

`SELECT user2_id AS user_id FROM Friendship WHERE user1_id = 1`

selects the opposite endpoint when user `1` is stored on the left. Both branches name their result `user_id`, so the rest of the query can treat them as one ordinary table of friends without remembering how each friendship row was oriented.

The branches are combined with `UNION` rather than `UNION ALL`. `UNION` removes duplicate friend identifiers. The composite primary key prevents the exact same ordered pair from appearing twice, but the normalized result could still conceptually receive the same person from multiple orientations if both ordered representations were present. Deduplicating here ensures each friend is joined to `Likes` once. Correctness would still be protected later by the outer `DISTINCT`, but the early normalization can avoid redundant join rows.

For the example, rows containing user `1` produce friend identifiers `2`, `3`, `4`, and `6`. Friendship rows such as `(2, 3)` do not involve user `1` and appear in neither branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The common table expression named `T` normalizes both orient... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Finding pages liked by those friends

The main query joins `T` with `Likes` using `JOIN Likes USING (user_id)`. The `USING` clause means that the equally named `user_id` columns must match. Consequently, every joined row represents a page liked by a known friend of user `1`.

This is an inner join, which is appropriate. A friend with no like rows contributes no recommendable page and need not appear in an intermediate result. Likewise, likes from users outside `T` cannot join and are ignored.

After the join, the query needs only `page_id`. It aliases that column as `recommended_page` to satisfy the required output schema.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["recommended_page"], "rows": [[23], [24], [56], [33], [77]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friendship": [{"user1_id": 1, "user2_id": 2}, {"user1_id": 1, "user2_id": 3}, {"user1_id": 1, "user2_id": 4}, {"user1_id": 2, "user2_id": 3}, {"user1_id": 2, "user2_id": 4}, {"user1_id": 2, "user2_id": 5}, {"user1_id": 6, "user2_id": 1}], "Likes": [{"user_id": 1, "page_id": 88}, {"user_id": 2, "page_id": 23}, {"user_id": 3, "page_id": 24}, {"user_id": 4, "page_id": 56}, {"user_id": 5, "page_id": 11}, {"user_id": 6, "page_id": 33}, {"user_id": 2, "page_id": 77}, {"user_id": 3, "page_id": 77}, {"user_id": 6, "page_id": 88}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["recommended_page"], "rows": [[23], [24], [56], [33], [77]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated `EXISTS` and `NOT EXISTS`:** Existe:** - **Correlated `EXISTS` and `NOT EXISTS`:** Existence predicates can express “some friend likes this page” and “user one does not.” They avoid the `NULL` semantics of `NOT IN` and may optimize well, but the current schema already makes `page_id` non-null.
- **`LEFT JOIN` anti-join:** Candidate pages can be left-joined to user `1`'s likes and filtered with `IS NULL`. This is a common equivalent anti-join formulation but requires careful aliases because `Likes` appears twice.
- **`UNION ALL` instead of `UNION`:** It could preserve duplicate friend rows and rely on final `DISTINCT` for correct output. That may create unnecessary join work and makes the normalized friend relation less clean.
- **Friend stored in either column:** The two CTE branches are both necessary; omitting either one misses friendships in the opposite orientation.
- **Several friends like one page:** `DISTINCT` returns that page exactly once.
- **Friend likes a page user one likes:** The `NOT IN` filter removes it regardless of how many friends like it.
- **Friend with no likes:** The inner join produces no row for that friend, which is correct.
- **User one has no friends:** `T` is empty, so the join and result are empty.
- **User one has no likes:** The anti-subquery is empty, so every distinct page liked by a friend is eligible.
- **No ordering requirement:** Without `ORDER BY`, MySQL may return valid recommendations in any physical order.
- **Primary-key nullability:** The safety of `NOT IN` depends on `page_id` being non-null, which follows from its participation in the declared primary key.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $F$ be the number of `Friendship` rows, $L$ the number of `Likes` rows, and $R=F+L$. In the standard relational-algorithm model, the two filtered friendship scans take $O(F)$ without relying on indexes. Building the normalized friend set and joining it with likes can be performed with hashing in expected $O(F+L)$ time. The anti-membership set for user `1`'s likes and final duplicate elimination can likewise be implemented in expected linear time in their input sizes. This yields expected $O(R)$ time, plus the unavoidable cost of writing the result.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
