# Guided Example: User Activity for the Past 30 Days I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}`
- **Required output:** `{"columns": ["day", "active_users"], "rows": [["2019-07-20", 2], ["2019-07-21", 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activity`

The objective is to compute `{"columns": ["day", "active_users"], "rows": [["2019-07-20", 2], ["2019-07-21", 2]]}` from `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter to the exact inclusive 30-day window

The reporting date is `2019-07-27`, and that date is included. A 30-day inclusive period contains the reporting date itself plus the preceding 29 dates, so the earliest accepted date is `2019-06-28`.

The query expresses this with two conditions:

`activity_date <= '2019-07-27'`

and

`DATEDIFF('2019-07-27', activity_date) < 30`.

In MySQL, `DATEDIFF(later, earlier)` returns the number of date boundaries between its arguments. On `2019-07-27` the difference is zero; on `2019-06-28` it is 29. Both satisfy the strict less-than-30 test. On `2019-06-27` the difference is 30, so it is excluded.

The upper-bound comparison is still necessary. A date after `2019-07-27` would produce a negative `DATEDIFF` result, and a negative number is also less than 30. Without the explicit `activity_date <= '2019-07-27'` condition, future activities could incorrectly enter the result. Together, the predicates implement exactly the closed date interval from `2019-06-28` through `2019-07-27`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group activities by calendar day

After filtering, the requested output has one row per date that has qualifying activity. `GROUP BY 1` groups by the first expression in the select list, which is `activity_date AS day`. It is a positional shorthand for grouping by `activity_date`.

SQL grouping naturally omits dates for which no source row survives the filter. This matches the example's statement that days with zero active users do not need output rows. Generating a calendar table and left joining it would instead create zero-count days, which is outside the requested result shape.

The alias `day` gives the output column its required name. Since the result may be returned in any order, no `ORDER BY` clause is necessary. Omitting ordering also avoids promising a presentation order that the contract does not require.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After filtering, the requested output has one row per date t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count users, not activity rows

A user is active on a day when that user performs at least one activity on that date. One user can have many activity rows on the same date: a session might be opened, scrolled, used to send a message, and ended. The table may even contain duplicate rows. Counting raw rows would therefore measure activity events rather than active users.

`COUNT(DISTINCT user_id)` deduplicates all appearances of the same user inside each date group. Whether a user has one qualifying row, several activity types, several sessions, or duplicate copies of the same row, that user contributes exactly one to that day's count.

The query deliberately does not filter on `activity_type`. The statement says every listed activity type counts as valid activity. Once a row falls in the date window, its presence is enough to make its user active on that day. Adding a condition for only session-opening events, messages, or any other subset would undercount legitimate active users.

The `session_id` column is also irrelevant for this report. Sessions matter only as the source of activities; the measurement unit is a distinct user-date pair. The guarantee that each session belongs to exactly one user is consistent with the data model but requires no special join or grouping here.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["day", "active_users"], "rows": [["2019-07-20", 2], ["2019-07-21", 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activity": [{"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "scroll_down"}, {"user_id": 1, "session_id": 1, "activity_date": "2019-07-20", "activity_type": "end_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-20", "activity_type": "open_session"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 2, "session_id": 4, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "open_session"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "send_message"}, {"user_id": 3, "session_id": 2, "activity_date": "2019-07-21", "activity_type": "end_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "open_session"}, {"user_id": 4, "session_id": 3, "activity_date": "2019-06-25", "activity_type": "end_session"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["day", "active_users"], "rows": [["2019-07-20", 2], ["2019-07-21", 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count all rows per day:** `COUNT(*)` overcount:** - **Count all rows per day:** `COUNT(*)` overcounts users who perform multiple activities or whose rows are duplicated. The required unit is a distinct `user_id` within each day.
- **Count distinct sessions:** `COUNT(DISTINCT session_id)` answers a different question. One user may own multiple sessions yet should contribute only one active user for a date.
- **Use only the `DATEDIFF` predicate:** Future dates yield negative differences and would incorrectly satisfy `< 30`. The explicit upper date bound prevents that leak.
- **Use `DATEDIFF <= 30`:** That includes 31 calendar dates because differences zero through 30 are all accepted. The correct inclusive 30-day window uses differences zero through 29.
- **Use a half-open interval:** `activity_date >= '2019-06-28' AND activity_date < '2019-07-28'` is an equivalent clear formulation for date values. The exact solution instead combines an upper bound with `DATEDIFF`.
- **Duplicate activity rows:** Distinct user counting makes them harmless for the active-user total.
- **Several sessions for one user on one day:** The user still contributes one because deduplication is on `user_id`, not `session_id`.
- **Any listed activity type:** Opening, ending, scrolling, and messaging all count. No type-specific predicate should be added.
- **No qualifying activity at all:** No groups are formed, so the query returns an empty result table, which is consistent with omitting zero-activity days.
- **Boundary dates:** Activities on `2019-06-28` and `2019-07-27` are included; activities on `2019-06-27` and `2019-07-28` are excluded.
- **Output ordering:** The contract permits any order. If a consumer later requires chronological output, an `ORDER BY day` could be added, but it is unnecessary here.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let `R` be the number of rows in `Activity`. The database must inspect candidate rows to apply the date filter. Grouping by date and computing distinct user identifiers may be implemented with sorting or hashing. Under the repository's conservative sort-based bound, the time complexity is `O(R log R)`.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
