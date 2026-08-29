# Guided Example: Find Emotionally Consistent Users

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"reactions": [{"user_id": 1, "content_id": 101, "reaction": "like"}, {"user_id": 1, "content_id": 102, "reaction": "like"}, {"user_id": 1, "content_id": 103, "reaction": "like"}, {"user_id": 1, "content_id": 104, "reaction": "wow"}, {"user_id": 1, "content_id": 105, "reaction": "like"}, {"user_id": 2, "content_id": 201, "reaction": "like"}, {"user_id": 2, "content_id": 202, "reaction": "wow"}, {"user_id": 2, "content_id": 203, "reaction": "sad"}, {"user_id": 2, "content_id": 204, "reaction": "like"}, {"user_id": 2, "content_id": 205, "reaction": "wow"}, {"user_id": 3, "content_id": 301, "reaction": "love"}, {"user_id": 3, "content_id": 302, "reaction": "love"}, {"user_id": 3, "content_id": 303, "reaction": "love"}, {"user_id": 3, "content_id": 304, "reaction": "love"}, {"user_id": 3, "content_id": 305, "reaction": "love"}]}}`
- **Required output:** `{"columns": ["user_id", "dominant_reaction", "reaction_ratio"], "rows": [[3, "love", 1.0], [1, "like", 0.8]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `reactions`

The objective is to compute `{"columns": ["user_id", "dominant_reaction", "reaction_ratio"], "rows": [[3, "love", 1.0], [1, "like", 0.8]]}` from `{"tables": {"reactions": [{"user_id": 1, "content_id": 101, "reaction": "like"}, {"user_id": 1, "content_id": 102, "reaction": "like"}, {"user_id": 1, "content_id": 103, "reaction": "like"}, {"user_id": 1, "content_id": 104, "reaction": "wow"}, {"user_id": 1, "content_id": 105, "reaction": "like"}, {"user_id": 2, "content_id": 201, "reaction": "like"}, {"user_id": 2, "content_id": 202, "reaction": "wow"}, {"user_id": 2, "content_id": 203, "reaction": "sad"}, {"user_id": 2, "content_id": 204, "reaction": "like"}, {"user_id": 2, "content_id": 205, "reaction": "wow"}, {"user_id": 3, "content_id": 301, "reaction": "love"}, {"user_id": 3, "content_id": 302, "reaction": "love"}, {"user_id": 3, "content_id": 303, "reaction": "love"}, {"user_id": 3, "content_id": 304, "reaction": "love"}, {"user_id": 3, "content_id": 305, "reaction": "love"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn many reaction rows into one count per user and reaction type

The input contains one row for every distinct user-and-content pair. A user can therefore have many rows, and the same reaction word can appear on several of them. The final answer does not care which content item received each reaction; it needs only two quantities for every user:

1. the user's total number of reaction rows, and
2. the largest number of those rows that share one reaction type.

The first common table expression, `t`, performs the useful compression. It groups by `user_id` and `reaction` and computes `COUNT(1)`. A row such as `(7, 'like', 8)` in `t` means that user 7 used `like` on eight different content items. Call the number of rows in the original table $R$, the number of users $U$, and the number of distinct user-and-reaction pairs $D$. The original $R$ rows become only $D$ grouped rows, where $D \le R$.

This first aggregation is important because the next step must compare reaction types within each user. Doing that from `t` is simpler than repeatedly recounting the original table. For one user, if the rows of `t` have counts $c_1,c_2,\ldots,c_k$, then `SUM(cnt)` is that user's total number of reactions:

$$
R_u = c_1+c_2+\cdots+c_k.
$$

Similarly, `MAX(cnt)` is the count of the user's most frequent reaction:

$$
M_u = \max(c_1,c_2,\ldots,c_k).
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"reactions": [{"user_id": 1, "content_id": 101, "reaction": "like"}, {"user_id": 1, "content_id": 102, "reaction": "like"}, {"user_id": 1, "content_id": 103, "reaction": "like"}, {"user_id": 1, "content_id": 104, "reaction": "wow"}, {"user_id": 1, "content_id": 105, "reaction": "like"}, {"user_id": 2, "content_id": 201, "reaction": "like"}, {"user_id": 2, "content_id": 202, "reaction": "wow"}, {"user_id": 2, "content_id": 203, "reaction": "sad"}, {"user_id": 2, "content_id": 204, "reaction": "like"}, {"user_id": 2, "content_id": 205, "reaction": "wow"}, {"user_id": 3, "content_id": 301, "reaction": "love"}, {"user_id": 3, "content_id": 302, "reaction": "love"}, {"user_id": 3, "content_id": 303, "reaction": "love"}, {"user_id": 3, "content_id": 304, "reaction": "love"}, {"user_id": 3, "content_id": 305, "reaction": "love"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build one summary row per user

The second common table expression, `s`, groups the rows of `t` by `user_id`. It retains `MAX(cnt)` as `mx_cnt` and calculates `ROUND(MAX(cnt) / SUM(cnt), 2)` as `reaction_ratio`. It also applies two conditions in its `HAVING` clause:

- `SUM(cnt) >= 5` requires at least five reaction rows for the user.
- `reaction_ratio >= 0.60` requires the computed, two-decimal ratio to be at least 0.60.

Using `HAVING` is appropriate because these conditions depend on aggregate values that do not exist until all grouped rows for a user have been combined. A `WHERE` condition at this stage could filter individual rows, but it could not directly decide whether a user's total is at least five or whether their largest category reaches the threshold.

For the first example's user 1, `t` contains counts 4 for `like` and 1 for `wow`. The row constructed in `s` has `mx_cnt = 4`, total 5, and `reaction_ratio = 0.80`. User 2 has grouped counts 2, 2, and 1, so the largest ratio is 0.40 and no row for that user survives. User 3 has only one grouped count, 5, giving a ratio of 1.00.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Recover the name belonging to the maximum count

The summary row in `s` contains the maximum count but not the corresponding reaction string. The final query joins `s` back to `t` with `JOIN t USING (user_id)`. This temporarily pairs each qualifying user's summary with all of that user's reaction-type counts. The condition `WHERE cnt = mx_cnt` keeps the row whose count equals the recorded maximum, thereby recovering `reaction` and exposing it under the alias `dominant_reaction`.

Under the intended 60% condition, the dominant type is unique. Two different reaction types cannot each account for at least 60% of the same total because their combined share would be at least 120%. The source's rounded test also only admits displayed ratios of at least 0.60; every exact share that rounds that high is still greater than one half. Consequently, two categories cannot tie at `mx_cnt` for a row that this query admits, so the join produces one result row per admitted user rather than duplicate winners.

The last clause, `ORDER BY 3 DESC, 1`, refers to result columns by position. Column 3 is `reaction_ratio`, so larger ratios appear first. Column 1 is `user_id`, so users with the same displayed ratio appear in ascending identifier order. The selected columns are exactly the requested three: the user, the dominant reaction, and its two-decimal ratio.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "dominant_reaction", "reaction_ratio"], "rows": [[3, "love", 1.0], [1, "like", 0.8]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"reactions": [{"user_id": 1, "content_id": 101, "reaction": "like"}, {"user_id": 1, "content_id": 102, "reaction": "like"}, {"user_id": 1, "content_id": 103, "reaction": "like"}, {"user_id": 1, "content_id": 104, "reaction": "wow"}, {"user_id": 1, "content_id": 105, "reaction": "like"}, {"user_id": 2, "content_id": 201, "reaction": "like"}, {"user_id": 2, "content_id": 202, "reaction": "wow"}, {"user_id": 2, "content_id": 203, "reaction": "sad"}, {"user_id": 2, "content_id": 204, "reaction": "like"}, {"user_id": 2, "content_id": 205, "reaction": "wow"}, {"user_id": 3, "content_id": 301, "reaction": "love"}, {"user_id": 3, "content_id": 302, "reaction": "love"}, {"user_id": 3, "content_id": 303, "reaction": "love"}, {"user_id": 3, "content_id": 304, "reaction": "love"}, {"user_id": 3, "content_id": 305, "reaction": "love"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "dominant_reaction", "reaction_ratio"], "rows": [[3, "love", 1.0], [1, "like", 0.8]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional window functions:** Windowed `COUNT(*)` values can attach each user's total and each user/type count to grouped data, after which a rank chooses the dominant type. This can be expressive, but it usually carries more repeated values and still needs careful handling of the threshold, uniqueness, and final ordering.
- **Rank every reaction type:** `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY cnt DESC)` can select the largest type directly instead of joining `s` back to `t`. It removes the recovery join, although the current join is safe because every admitted user has a unique maximum.
- **Test exact counts before formatting:** The essential repair is to use `MAX(cnt) * 5 >= SUM(cnt) * 3`, or an equivalent unrounded comparison, and apply `ROUND` only to the output expression. This prevents shares from roughly 59.5% through just under 60% from entering the result.
- **Exactly five reactions:** A user with five rows is eligible for consideration. Three matching reactions give exactly 60% and qualify; two give 40% and do not.
- **Fewer than five reactions:** Even a user whose reactions are all the same type must be excluded when the total is below five, because consistency alone does not satisfy the minimum-activity rule.
- **One reaction type:** If an eligible user has only one reaction type, `t` has one row for that user, `MAX(cnt)` equals `SUM(cnt)`, and the displayed ratio is 1.00.
- **Equal displayed ratios:** Different exact shares can round to the same two-decimal number. The query correctly breaks such output ties by ascending `user_id` because it orders by the displayed `reaction_ratio` and then the identifier.
- **No qualifying users:** Both `s` and the final result can be empty; SQL naturally returns an empty result table without requiring a special sentinel row.
- **Primary-key implication:** Because `(user_id, content_id)` is unique, `COUNT(1)` truly counts different content items for a user. No `COUNT(DISTINCT content_id)` is needed under the stated schema.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R+U)$. Let $R$ be the number of rows in `reactions`, $D$ the number of distinct `(user_id, reaction)` pairs, and $U$ the number of distinct users. The first grouping reads all $R$ rows and materializes $D$ counts. The second grouping reads those $D$ rows and materializes at most $U$ summaries. The join then processes the grouped data for the qualifying users, and the final ordering sorts at most $U$ result rows.
- **Auxiliary Space Complexity:** $O(R + U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
