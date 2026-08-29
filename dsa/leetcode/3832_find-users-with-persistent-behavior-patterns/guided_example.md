# Guided Example: Find Users with Persistent Behavior Patterns

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"activity": [{"user_id": 1, "action_date": "2024-01-01", "action": "login"}, {"user_id": 1, "action_date": "2024-01-02", "action": "login"}, {"user_id": 1, "action_date": "2024-01-03", "action": "login"}, {"user_id": 1, "action_date": "2024-01-04", "action": "login"}, {"user_id": 1, "action_date": "2024-01-05", "action": "login"}, {"user_id": 1, "action_date": "2024-01-06", "action": "logout"}, {"user_id": 2, "action_date": "2024-01-01", "action": "click"}, {"user_id": 2, "action_date": "2024-01-02", "action": "click"}, {"user_id": 2, "action_date": "2024-01-03", "action": "click"}, {"user_id": 2, "action_date": "2024-01-04", "action": "click"}, {"user_id": 3, "action_date": "2024-01-01", "action": "view"}, {"user_id": 3, "action_date": "2024-01-02", "action": "view"}, {"user_id": 3, "action_date": "2024-01-03", "action": "view"}, {"user_id": 3, "action_date": "2024-01-04", "action": "view"}, {"user_id": 3, "action_date": "2024-01-05", "action": "view"}, {"user_id": 3, "action_date": "2024-01-06", "action": "view"}, {"user_id": 3, "action_date": "2024-01-07", "action": "view"}]}}`
- **Required output:** `{"columns": ["user_id", "action", "streak_length", "start_date", "end_date"], "rows": [[3, "view", 7, "2024-01-01", "2024-01-07"], [1, "login", 5, "2024-01-01", "2024-01-05"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `activity`

The objective is to compute `{"columns": ["user_id", "action", "streak_length", "start_date", "end_date"], "rows": [[3, "view", 7, "2024-01-01", "2024-01-07"], [1, "login", 5, "2024-01-01", "2024-01-05"]]}` from `{"tables": {"activity": [{"user_id": 1, "action_date": "2024-01-01", "action": "login"}, {"user_id": 1, "action_date": "2024-01-02", "action": "login"}, {"user_id": 1, "action_date": "2024-01-03", "action": "login"}, {"user_id": 1, "action_date": "2024-01-04", "action": "login"}, {"user_id": 1, "action_date": "2024-01-05", "action": "login"}, {"user_id": 1, "action_date": "2024-01-06", "action": "logout"}, {"user_id": 2, "action_date": "2024-01-01", "action": "click"}, {"user_id": 2, "action_date": "2024-01-02", "action": "click"}, {"user_id": 2, "action_date": "2024-01-03", "action": "click"}, {"user_id": 2, "action_date": "2024-01-04", "action": "click"}, {"user_id": 3, "action_date": "2024-01-01", "action": "view"}, {"user_id": 3, "action_date": "2024-01-02", "action": "view"}, {"user_id": 3, "action_date": "2024-01-03", "action": "view"}, {"user_id": 3, "action_date": "2024-01-04", "action": "view"}, {"user_id": 3, "action_date": "2024-01-05", "action": "view"}, {"user_id": 3, "action_date": "2024-01-06", "action": "view"}, {"user_id": 3, "action_date": "2024-01-07", "action": "view"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First decide which user-days are eligible

The primary key is `(user_id, action_date, action)`. It prevents duplicate copies of the same action on one day, but it still allows one user to have several different actions on that date.

A streak day is valid only when the user performed exactly one action that day. The first common table expression, `daily_counts`, keeps every original row and attaches

`COUNT(*) OVER (PARTITION BY user_id, action_date) AS cnt`.

All rows for the same user and calendar date receive the same count. A date with one row receives 1. A date containing two distinct actions produces two rows, both marked 2.

`filtered_activity` retains only `cnt = 1`. After this filter:

- every remaining `(user_id, action_date)` occurs exactly once;
- its `action` is the user's sole action for that day;
- a multi-action day contributes no row at all.

Removing every row of an ineligible date is important. That date must not belong to a streak, and it must separate otherwise similar activity on the days around it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"activity": [{"user_id": 1, "action_date": "2024-01-01", "action": "login"}, {"user_id": 1, "action_date": "2024-01-02", "action": "login"}, {"user_id": 1, "action_date": "2024-01-03", "action": "login"}, {"user_id": 1, "action_date": "2024-01-04", "action": "login"}, {"user_id": 1, "action_date": "2024-01-05", "action": "login"}, {"user_id": 1, "action_date": "2024-01-06", "action": "logout"}, {"user_id": 2, "action_date": "2024-01-01", "action": "click"}, {"user_id": 2, "action_date": "2024-01-02", "action": "click"}, {"user_id": 2, "action_date": "2024-01-03", "action": "click"}, {"user_id": 2, "action_date": "2024-01-04", "action": "click"}, {"user_id": 3, "action_date": "2024-01-01", "action": "view"}, {"user_id": 3, "action_date": "2024-01-02", "action": "view"}, {"user_id": 3, "action_date": "2024-01-03", "action": "view"}, {"user_id": 3, "action_date": "2024-01-04", "action": "view"}, {"user_id": 3, "action_date": "2024-01-05", "action": "view"}, {"user_id": 3, "action_date": "2024-01-06", "action": "view"}, {"user_id": 3, "action_date": "2024-01-07", "action": "view"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert consecutive dates into an island key

For each `(user_id, action)` pair, `streak_groups` sorts eligible rows by `action_date` and assigns a one-based row number.

Suppose a consecutive run begins on date $d_1$. Its dates are

$$
d_1,\ d_1+1,\ d_1+2,\ldots
$$

and their row numbers within that user's action partition advance by exactly one as well. Subtracting the row number in days therefore gives the same shifted date for every row in the run:

$$
(d_1+r-1)-r=d_1-1.
$$

The source calculates this constant key as

`DATE_SUB(action_date, INTERVAL ROW_NUMBER() OVER (...) DAY) AS grp`.

When a calendar date is missing, the date advances by more than the row number and the key changes. When an ineligible multi-action date was removed, the surrounding eligible dates also have a gap and receive different keys.

The window is partitioned by both `user_id` and `action`. Different actions can never enter the same group even if their dates happen to produce equal shifted values.

Grouping later by `user_id, action, grp` therefore identifies exactly one maximal run of consecutive eligible days with the same action.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an action change breaks the run

Consider user activity `login` on January 1, `logout` on January 2, and `login` on January 3. The two login rows belong to the same `(user_id, action)` window, but their dates differ by two days while their row numbers differ by one. Their shifted `grp` dates differ, so they form separate login runs.

The logout row belongs to another action partition. Thus an intervening different action breaks the original-action island even though the island calculation does not explicitly call `LAG(action)`.

This relies on the single-action-day filter. Each eligible calendar day has one action, so any date occupied by another action appears as a missing date in the first action's partition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "action", "streak_length", "start_date", "end_date"], "rows": [[3, "view", 7, "2024-01-01", "2024-01-07"], [1, "login", 5, "2024-01-01", "2024-01-05"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"activity": [{"user_id": 1, "action_date": "2024-01-01", "action": "login"}, {"user_id": 1, "action_date": "2024-01-02", "action": "login"}, {"user_id": 1, "action_date": "2024-01-03", "action": "login"}, {"user_id": 1, "action_date": "2024-01-04", "action": "login"}, {"user_id": 1, "action_date": "2024-01-05", "action": "login"}, {"user_id": 1, "action_date": "2024-01-06", "action": "logout"}, {"user_id": 2, "action_date": "2024-01-01", "action": "click"}, {"user_id": 2, "action_date": "2024-01-02", "action": "click"}, {"user_id": 2, "action_date": "2024-01-03", "action": "click"}, {"user_id": 2, "action_date": "2024-01-04", "action": "click"}, {"user_id": 3, "action_date": "2024-01-01", "action": "view"}, {"user_id": 3, "action_date": "2024-01-02", "action": "view"}, {"user_id": 3, "action_date": "2024-01-03", "action": "view"}, {"user_id": 3, "action_date": "2024-01-04", "action": "view"}, {"user_id": 3, "action_date": "2024-01-05", "action": "view"}, {"user_id": 3, "action_date": "2024-01-06", "action": "view"}, {"user_id": 3, "action_date": "2024-01-07", "action": "view"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "action", "streak_length", "start_date", "end_date"], "rows": [[3, "view", 7, "2024-01-01", "2024-01-07"], [1, "login", 5, "2024-01-01", "2024-01-05"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **LAG plus cumulative break markers:** Compare each eligible row with its preceding user row, mark a new run when the action changes or `DATEDIFF` is not 1, and cumulatively sum markers into group IDs. This directly expresses all break conditions but needs careful handling after multi-action dates are removed.
- **Self-join date chains:** Joining each row to the next calendar day can identify local continuity, but assembling maximal streaks and selecting their endpoints is more cumbersome and may create large intermediates.
- **Multi-action date:** All rows for that user-date receive `cnt > 1` and are removed. The missing date separates runs on both sides.
- **Missing calendar date:** Adjacent records are not necessarily consecutive days; the shifted-date key changes across the gap.
- **Action change:** Separate action partitions plus the intervening date gap prevent two same-action stretches from merging.
- **Exactly five days:** The `>= 5` condition includes the boundary.
- **Several qualifying runs of different lengths:** Rank 1 selects the longest.
- **Several equally longest runs:** The exact query returns an arbitrary tied run because its ranking lacks a secondary order.
- **No qualifying user:** The final result is an empty table.
- **One row per day after filtering:** This makes `COUNT(*)` equal elapsed streak days rather than merely activity records.
- **Final ties across users:** Equal streak lengths are ordered by ascending `user_id` in the final result.
- **MySQL alias behavior:** The query uses `streak_length` in `HAVING`, which MySQL permits for a select-list aggregate alias.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of rows in `activity` and $U$ the number of returned users. The window count may require ordering or hashing rows by user and date. The streak row numbers require ordering by `user_id, action, action_date`. Grouping islands, ranking summaries, and final output ordering add further database operations.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
