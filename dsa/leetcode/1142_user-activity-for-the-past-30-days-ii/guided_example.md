# Guided Example: User Activity for the Past 30 Days II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "scroll_down"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}`
- **Required output:** `{"columns": ["average_sessions_per_user"], "rows": [[1.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activity`

The objective is to compute `{"columns": ["average_sessions_per_user"], "rows": [[1.33]]}` from `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "scroll_down"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the calculation into per-user counts and one overall average

The requested average is not the number of activity rows divided by the number of users. Each participating user first needs an individual count of distinct sessions with at least one activity in the reporting window. Only then are those per-user session counts averaged.

The common table expression `T` performs the first level. It groups filtered activity rows by `user_id` and produces one column:

`COUNT(DISTINCT session_id) AS sessions`.

The outer query performs the second level by applying `AVG(sessions)` to the rows of `T`. This two-stage structure matches the mathematical definition of an average across users. Trying to place `AVG(COUNT(...))` in one ordinary grouping level is not valid SQL aggregation and would blur the two different populations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "scroll_down"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter to exactly 30 inclusive dates

The target period ends on `2019-07-27` and includes that date. Its earliest date is `2019-06-28`. The CTE uses

`activity_date <= '2019-07-27'`

together with

`DATEDIFF('2019-07-27', activity_date) < 30`.

For dates from `2019-06-28` through `2019-07-27`, the difference ranges from 29 down to zero, so the rows are retained. `2019-06-27` has difference 30 and is excluded.

The upper bound is not redundant. A future date would create a negative date difference, and that value would satisfy `< 30`. Requiring the activity date to be no later than the reporting date prevents future rows from entering the window.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The target period ends on `2019-07-27` and includes that dat... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count a session once for its user

A session qualifies when it has at least one activity in the period. It may have several qualifying rows because the user can open it, scroll, send messages, and end it, possibly with duplicate rows in the table. `COUNT(DISTINCT session_id)` collapses all of those rows to one session inside the user's group.

The grouping is by `user_id` because the final population consists of users. The contract guarantees that each session belongs to exactly one user, so the same session identifier cannot legitimately contribute to multiple owners. Even so, the distinct count occurs within each user group, making the intended ownership boundary explicit.

There is no `activity_type` condition because every activity type listed by the schema is valid evidence that a session was active. There is also no need for a session to start or end within the period. One qualifying activity of any type is enough for that session to count.

Only users with at least one qualifying activity produce a group in `T`. This is exactly the population described by the problem: the average is across users whose sessions have activity in the window. Users with no qualifying row are absent rather than treated as having zero sessions. Including inactive users with zeros would require another user table and would change the requested denominator.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["average_sessions_per_user"], "rows": [[1.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "scroll_down"}, {"user_id": 3, "session_id": 5, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["average_sessions_per_user"], "rows": [[1.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Average raw activity counts:** This overweight:** - **Average raw activity counts:** This overweights sessions that generate many events and does not compute sessions per user.
- **Count sessions without `DISTINCT`:** A session with several activity rows would be counted repeatedly. Distinct session identifiers implement the phrase “at least one activity.”
- **Average globally distinct sessions divided by users:** Because sessions belong to one user, that quotient can match some datasets, but the grouped CTE directly preserves the required per-user definition and safely exposes each user's count.
- **Include inactive users as zeros:** The input contains activity rows rather than a complete user roster, and the requested average concerns users with qualifying activity. Adding zero-session users would change the denominator.
- **Filter by `activity_type`:** Every listed activity type qualifies, so any restriction to openings, endings, scrolling, or messages would omit valid sessions.
- **Only a `DATEDIFF < 30` condition:** Future activity dates produce negative differences and would be incorrectly accepted. The upper bound closes that hole.
- **A session spans the window boundary:** It counts if at least one of its activity rows lies inside the period, regardless of when it began or ended.
- **Duplicate rows:** `COUNT(DISTINCT session_id)` prevents them from inflating a user's session total.
- **No qualifying rows:** The CTE is empty, `AVG` is null, and `COALESCE` returns the required zero.
- **Exactly one active user:** The average equals that user's distinct-session count, rounded to two decimals by the same expression.
- **Boundary dates:** `2019-06-28` and `2019-07-27` are accepted; the immediately adjacent outside dates are rejected.
- **Rounding:** The query rounds the final average rather than truncating it, preserving standard MySQL rounding behavior to two decimal places.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let `R` be the number of rows in `Activity`. Filtering examines candidate activity rows. Grouping by user and deduplicating session identifiers can be implemented through sorting, giving the repository's conservative `O(R log R)` time bound. The final average visits at most one CTE row per participating user and is no larger than the grouping work.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
