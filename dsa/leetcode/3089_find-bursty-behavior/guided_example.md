# Guided Example: Find Bursty Behavior

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Posts": [{"post_id": 1, "user_id": 1, "post_date": "2024-02-27"}, {"post_id": 2, "user_id": 5, "post_date": "2024-02-06"}, {"post_id": 3, "user_id": 3, "post_date": "2024-02-25"}, {"post_id": 4, "user_id": 3, "post_date": "2024-02-14"}, {"post_id": 5, "user_id": 3, "post_date": "2024-02-06"}, {"post_id": 6, "user_id": 2, "post_date": "2024-02-25"}]}}`
- **Required output:** `{"columns": ["user_id", "max_7day_posts", "avg_weekly_posts"], "rows": [[1, 1, 0.25], [2, 1, 0.25], [5, 1, 0.25]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Posts`

The objective is to compute `{"columns": ["user_id", "max_7day_posts", "avg_weekly_posts"], "rows": [[1, 1, 0.25], [2, 1, 0.25], [5, 1, 0.25]]}` from `{"tables": {"Posts": [{"post_id": 1, "user_id": 1, "post_date": "2024-02-27"}, {"post_id": 2, "user_id": 5, "post_date": "2024-02-06"}, {"post_id": 3, "user_id": 3, "post_date": "2024-02-25"}, {"post_id": 4, "user_id": 3, "post_date": "2024-02-14"}, {"post_id": 5, "user_id": 3, "post_date": "2024-02-06"}, {"post_id": 6, "user_id": 2, "post_date": "2024-02-25"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**What the query is trying to measure.** For each user, the reference task compares two quantities within February 2024:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Posts": [{"post_id": 1, "user_id": 1, "post_date": "2024-02-27"}, {"post_id": 2, "user_id": 5, "post_date": "2024-02-06"}, {"post_id": 3, "user_id": 3, "post_date": "2024-02-25"}, {"post_id": 4, "user_id": 3, "post_date": "2024-02-14"}, {"post_id": 5, "user_id": 3, "post_date": "2024-02-06"}, {"post_id": 6, "user_id": 2, "post_date": "2024-02-25"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the user's maximum number of posts in any inclusive seven-day period;
- the user's average weekly post count, defined as the February total divided by four.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - the user's maximum number of posts in any inclusive seven-... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

A user is bursty when the maximum seven-day count is at least twice that average. The exact SQL source organizes this work into two common table expressions, `P` and `T`, and a final grouped query.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "max_7day_posts", "avg_weekly_posts"], "rows": [[1, 1, 0.25], [2, 1, 0.25], [5, 1, 0.25]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Posts": [{"post_id": 1, "user_id": 1, "post_date": "2024-02-27"}, {"post_id": 2, "user_id": 5, "post_date": "2024-02-06"}, {"post_id": 3, "user_id": 3, "post_date": "2024-02-25"}, {"post_id": 4, "user_id": 3, "post_date": "2024-02-14"}, {"post_id": 5, "user_id": 3, "post_date": "2024-02-06"}, {"post_id": 6, "user_id": 2, "post_date": "2024-02-25"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "max_7day_posts", "avg_weekly_posts"], "rows": [[1, 1, 0.25], [2, 1, 0.25], [5, 1, 0.25]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correctly scoped self-join:** Add explicit rep:** - **Correctly scoped self-join:** Add explicit reporting-period conditions for the anchor and counted posts. This fixes the exact source's major date-scope defect.
- **Sliding window per user:** Sorting posts by `(user_id, post_date)` and maintaining two date pointers can find maximum seven-day counts without enumerating every matching pair.
- **Window-function formulation:** Some SQL dialects can combine ordered analytics with date-range frames, although support for interval-based frames varies.
- **Index support:** A composite index on `(user_id, post_date)` materially improves the same-user date-range join.
- **Windows anchored on empty dates:** They need not be generated because any nonempty optimum can move its left boundary to its earliest included post.
- **Inclusive seven days:** `BETWEEN anchor AND anchor + 6 days` contains seven calendar dates, not six.
- **Multiple posts on one date:** Every row is counted; the measure is posts, not distinct active days.
- **February 29:** The local note deliberately excludes it by defining the analysis as February 1 through February 28, despite 2024 being a leap year.
- **Posts outside February:** The exact `P` CTE includes them, which is the principal correctness defect.
- **Window crossing into March:** The exact join includes such `p2` rows because it has no upper reporting boundary.
- **Users without February posts:** They do not appear in `T`, so the inner join removes them even if `P` finds activity elsewhere.
- **Zero average:** A user present in `T` has at least one February post, so its average is positive.
- **Threshold equality:** `>=` correctly includes a maximum exactly twice the average.
- **Functional dependency in grouping:** `avg_weekly_posts` is selected without being explicitly grouped or aggregated. Since `T` has one row per user it is functionally determined, but strict SQL modes or other engines may demand an aggregate or an added group key.
- **Result order:** `ORDER BY 1` sorts by `user_id` ascending, matching the expected deterministic output.
- **Not the manifest algorithm:** The checked-in query is a self-join, not a true linear sliding-window implementation, so its complexity must be assessed from the SQL actually present.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let $P$ be the total number of rows in `Posts`, $U$ the number of users, and $M$ the number of matching self-join pairs. Constructing `P` requires work proportional to the join plan. Without a useful composite index, comparing same-user date candidates can approach $O(P^2)$ time in the worst case. With an index such as `(user_id, post_date)`, the engine can range-scan matching dates, giving a more output-sensitive cost near $O(P\log P+M)$.
- **Auxiliary Space Complexity:** $O(P+U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
