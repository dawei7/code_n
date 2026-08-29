# Guided Example: Find Zombie Sessions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"app_events": [{"event_id": 1, "user_id": 201, "event_timestamp": "2024-03-01 10:00:00", "event_type": "app_open", "session_id": "S001", "event_value": null}, {"event_id": 2, "user_id": 201, "event_timestamp": "2024-03-01 10:05:00", "event_type": "scroll", "session_id": "S001", "event_value": 500}, {"event_id": 3, "user_id": 201, "event_timestamp": "2024-03-01 10:10:00", "event_type": "scroll", "session_id": "S001", "event_value": 750}, {"event_id": 4, "user_id": 201, "event_timestamp": "2024-03-01 10:15:00", "event_type": "scroll", "session_id": "S001", "event_value": 600}, {"event_id": 5, "user_id": 201, "event_timestamp": "2024-03-01 10:20:00", "event_type": "scroll", "session_id": "S001", "event_value": 800}, {"event_id": 6, "user_id": 201, "event_timestamp": "2024-03-01 10:25:00", "event_type": "scroll", "session_id": "S001", "event_value": 550}, {"event_id": 7, "user_id": 201, "event_timestamp": "2024-03-01 10:30:00", "event_type": "scroll", "session_id": "S001", "event_value": 900}, {"event_id": 8, "user_id": 201, "event_timestamp": "2024-03-01 10:35:00", "event_type": "app_close", "session_id": "S001", "event_value": null}, {"event_id": 9, "user_id": 202, "event_timestamp": "2024-03-01 11:00:00", "event_type": "app_open", "session_id": "S002", "event_value": null}, {"event_id": 10, "user_id": 202, "event_timestamp": "2024-03-01 11:02:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 11, "user_id": 202, "event_timestamp": "2024-03-01 11:05:00", "event_type": "scroll", "session_id": "S002", "event_value": 400}, {"event_id": 12, "user_id": 202, "event_timestamp": "2024-03-01 11:08:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 13, "user_id": 202, "event_timestamp": "2024-03-01 11:10:00", "event_type": "scroll", "session_id": "S002", "event_value": 350}, {"event_id": 14, "user_id": 202, "event_timestamp": "2024-03-01 11:15:00", "event_type": "purchase", "session_id": "S002", "event_value": 50}, {"event_id": 15, "user_id": 202, "event_timestamp": "2024-03-01 11:20:00", "event_type": "app_close", "session_id": "S002", "event_value": null}, {"event_id": 16, "user_id": 203, "event_timestamp": "2024-03-01 12:00:00", "event_type": "app_open", "session_id": "S003", "event_value": null}, {"event_id": 17, "user_id": 203, "event_timestamp": "2024-03-01 12:10:00", "event_type": "scroll", "session_id": "S003", "event_value": 1000}, {"event_id": 18, "user_id": 203, "event_timestamp": "2024-03-01 12:20:00", "event_type": "scroll", "session_id": "S003", "event_value": 1200}, {"event_id": 19, "user_id": 203, "event_timestamp": "2024-03-01 12:25:00", "event_type": "click", "session_id": "S003", "event_value": null}, {"event_id": 20, "user_id": 203, "event_timestamp": "2024-03-01 12:30:00", "event_type": "scroll", "session_id": "S003", "event_value": 800}, {"event_id": 21, "user_id": 203, "event_timestamp": "2024-03-01 12:40:00", "event_type": "scroll", "session_id": "S003", "event_value": 900}, {"event_id": 22, "user_id": 203, "event_timestamp": "2024-03-01 12:50:00", "event_type": "scroll", "session_id": "S003", "event_value": 1100}, {"event_id": 23, "user_id": 203, "event_timestamp": "2024-03-01 13:00:00", "event_type": "app_close", "session_id": "S003", "event_value": null}, {"event_id": 24, "user_id": 204, "event_timestamp": "2024-03-01 14:00:00", "event_type": "app_open", "session_id": "S004", "event_value": null}, {"event_id": 25, "user_id": 204, "event_timestamp": "2024-03-01 14:05:00", "event_type": "scroll", "session_id": "S004", "event_value": 600}, {"event_id": 26, "user_id": 204, "event_timestamp": "2024-03-01 14:08:00", "event_type": "scroll", "session_id": "S004", "event_value": 700}, {"event_id": 27, "user_id": 204, "event_timestamp": "2024-03-01 14:10:00", "event_type": "click", "session_id": "S004", "event_value": null}, {"event_id": 28, "user_id": 204, "event_timestamp": "2024-03-01 14:12:00", "event_type": "app_close", "session_id": "S004", "event_value": null}]}}`
- **Required output:** `{"columns": ["session_id", "user_id", "session_duration_minutes", "scroll_count"], "rows": [["S001", 201, 35, 6]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{app}_{events}$

The objective is to compute `{"columns": ["session_id", "user_id", "session_duration_minutes", "scroll_count"], "rows": [["S001", 201, 35, 6]]}` from `{"tables": {"app_events": [{"event_id": 1, "user_id": 201, "event_timestamp": "2024-03-01 10:00:00", "event_type": "app_open", "session_id": "S001", "event_value": null}, {"event_id": 2, "user_id": 201, "event_timestamp": "2024-03-01 10:05:00", "event_type": "scroll", "session_id": "S001", "event_value": 500}, {"event_id": 3, "user_id": 201, "event_timestamp": "2024-03-01 10:10:00", "event_type": "scroll", "session_id": "S001", "event_value": 750}, {"event_id": 4, "user_id": 201, "event_timestamp": "2024-03-01 10:15:00", "event_type": "scroll", "session_id": "S001", "event_value": 600}, {"event_id": 5, "user_id": 201, "event_timestamp": "2024-03-01 10:20:00", "event_type": "scroll", "session_id": "S001", "event_value": 800}, {"event_id": 6, "user_id": 201, "event_timestamp": "2024-03-01 10:25:00", "event_type": "scroll", "session_id": "S001", "event_value": 550}, {"event_id": 7, "user_id": 201, "event_timestamp": "2024-03-01 10:30:00", "event_type": "scroll", "session_id": "S001", "event_value": 900}, {"event_id": 8, "user_id": 201, "event_timestamp": "2024-03-01 10:35:00", "event_type": "app_close", "session_id": "S001", "event_value": null}, {"event_id": 9, "user_id": 202, "event_timestamp": "2024-03-01 11:00:00", "event_type": "app_open", "session_id": "S002", "event_value": null}, {"event_id": 10, "user_id": 202, "event_timestamp": "2024-03-01 11:02:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 11, "user_id": 202, "event_timestamp": "2024-03-01 11:05:00", "event_type": "scroll", "session_id": "S002", "event_value": 400}, {"event_id": 12, "user_id": 202, "event_timestamp": "2024-03-01 11:08:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 13, "user_id": 202, "event_timestamp": "2024-03-01 11:10:00", "event_type": "scroll", "session_id": "S002", "event_value": 350}, {"event_id": 14, "user_id": 202, "event_timestamp": "2024-03-01 11:15:00", "event_type": "purchase", "session_id": "S002", "event_value": 50}, {"event_id": 15, "user_id": 202, "event_timestamp": "2024-03-01 11:20:00", "event_type": "app_close", "session_id": "S002", "event_value": null}, {"event_id": 16, "user_id": 203, "event_timestamp": "2024-03-01 12:00:00", "event_type": "app_open", "session_id": "S003", "event_value": null}, {"event_id": 17, "user_id": 203, "event_timestamp": "2024-03-01 12:10:00", "event_type": "scroll", "session_id": "S003", "event_value": 1000}, {"event_id": 18, "user_id": 203, "event_timestamp": "2024-03-01 12:20:00", "event_type": "scroll", "session_id": "S003", "event_value": 1200}, {"event_id": 19, "user_id": 203, "event_timestamp": "2024-03-01 12:25:00", "event_type": "click", "session_id": "S003", "event_value": null}, {"event_id": 20, "user_id": 203, "event_timestamp": "2024-03-01 12:30:00", "event_type": "scroll", "session_id": "S003", "event_value": 800}, {"event_id": 21, "user_id": 203, "event_timestamp": "2024-03-01 12:40:00", "event_type": "scroll", "session_id": "S003", "event_value": 900}, {"event_id": 22, "user_id": 203, "event_timestamp": "2024-03-01 12:50:00", "event_type": "scroll", "session_id": "S003", "event_value": 1100}, {"event_id": 23, "user_id": 203, "event_timestamp": "2024-03-01 13:00:00", "event_type": "app_close", "session_id": "S003", "event_value": null}, {"event_id": 24, "user_id": 204, "event_timestamp": "2024-03-01 14:00:00", "event_type": "app_open", "session_id": "S004", "event_value": null}, {"event_id": 25, "user_id": 204, "event_timestamp": "2024-03-01 14:05:00", "event_type": "scroll", "session_id": "S004", "event_value": 600}, {"event_id": 26, "user_id": 204, "event_timestamp": "2024-03-01 14:08:00", "event_type": "scroll", "session_id": "S004", "event_value": 700}, {"event_id": 27, "user_id": 204, "event_timestamp": "2024-03-01 14:10:00", "event_type": "click", "session_id": "S004", "event_value": null}, {"event_id": 28, "user_id": 204, "event_timestamp": "2024-03-01 14:12:00", "event_type": "app_close", "session_id": "S004", "event_value": null}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Aggregate all behavior at the session level

Every zombie criterion describes a complete session rather than one event:

- Duration depends on the earliest and latest timestamps.
- Scroll and click requirements depend on event counts.
- Purchase absence depends on whether any purchase row exists.

The source groups all rows by `session_id`. One output group then contains every event used to calculate that session’s metrics.

It also selects `user_id` without including it in `GROUP BY`. This relies on the stated data model that a session belongs to one user, making `user_id` functionally dependent on `session_id`. In MySQL, that dependency allows the selected value when the schema or mode recognizes it. Listing both columns in `GROUP BY` would make the assumption explicit and more portable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"app_events": [{"event_id": 1, "user_id": 201, "event_timestamp": "2024-03-01 10:00:00", "event_type": "app_open", "session_id": "S001", "event_value": null}, {"event_id": 2, "user_id": 201, "event_timestamp": "2024-03-01 10:05:00", "event_type": "scroll", "session_id": "S001", "event_value": 500}, {"event_id": 3, "user_id": 201, "event_timestamp": "2024-03-01 10:10:00", "event_type": "scroll", "session_id": "S001", "event_value": 750}, {"event_id": 4, "user_id": 201, "event_timestamp": "2024-03-01 10:15:00", "event_type": "scroll", "session_id": "S001", "event_value": 600}, {"event_id": 5, "user_id": 201, "event_timestamp": "2024-03-01 10:20:00", "event_type": "scroll", "session_id": "S001", "event_value": 800}, {"event_id": 6, "user_id": 201, "event_timestamp": "2024-03-01 10:25:00", "event_type": "scroll", "session_id": "S001", "event_value": 550}, {"event_id": 7, "user_id": 201, "event_timestamp": "2024-03-01 10:30:00", "event_type": "scroll", "session_id": "S001", "event_value": 900}, {"event_id": 8, "user_id": 201, "event_timestamp": "2024-03-01 10:35:00", "event_type": "app_close", "session_id": "S001", "event_value": null}, {"event_id": 9, "user_id": 202, "event_timestamp": "2024-03-01 11:00:00", "event_type": "app_open", "session_id": "S002", "event_value": null}, {"event_id": 10, "user_id": 202, "event_timestamp": "2024-03-01 11:02:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 11, "user_id": 202, "event_timestamp": "2024-03-01 11:05:00", "event_type": "scroll", "session_id": "S002", "event_value": 400}, {"event_id": 12, "user_id": 202, "event_timestamp": "2024-03-01 11:08:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 13, "user_id": 202, "event_timestamp": "2024-03-01 11:10:00", "event_type": "scroll", "session_id": "S002", "event_value": 350}, {"event_id": 14, "user_id": 202, "event_timestamp": "2024-03-01 11:15:00", "event_type": "purchase", "session_id": "S002", "event_value": 50}, {"event_id": 15, "user_id": 202, "event_timestamp": "2024-03-01 11:20:00", "event_type": "app_close", "session_id": "S002", "event_value": null}, {"event_id": 16, "user_id": 203, "event_timestamp": "2024-03-01 12:00:00", "event_type": "app_open", "session_id": "S003", "event_value": null}, {"event_id": 17, "user_id": 203, "event_timestamp": "2024-03-01 12:10:00", "event_type": "scroll", "session_id": "S003", "event_value": 1000}, {"event_id": 18, "user_id": 203, "event_timestamp": "2024-03-01 12:20:00", "event_type": "scroll", "session_id": "S003", "event_value": 1200}, {"event_id": 19, "user_id": 203, "event_timestamp": "2024-03-01 12:25:00", "event_type": "click", "session_id": "S003", "event_value": null}, {"event_id": 20, "user_id": 203, "event_timestamp": "2024-03-01 12:30:00", "event_type": "scroll", "session_id": "S003", "event_value": 800}, {"event_id": 21, "user_id": 203, "event_timestamp": "2024-03-01 12:40:00", "event_type": "scroll", "session_id": "S003", "event_value": 900}, {"event_id": 22, "user_id": 203, "event_timestamp": "2024-03-01 12:50:00", "event_type": "scroll", "session_id": "S003", "event_value": 1100}, {"event_id": 23, "user_id": 203, "event_timestamp": "2024-03-01 13:00:00", "event_type": "app_close", "session_id": "S003", "event_value": null}, {"event_id": 24, "user_id": 204, "event_timestamp": "2024-03-01 14:00:00", "event_type": "app_open", "session_id": "S004", "event_value": null}, {"event_id": 25, "user_id": 204, "event_timestamp": "2024-03-01 14:05:00", "event_type": "scroll", "session_id": "S004", "event_value": 600}, {"event_id": 26, "user_id": 204, "event_timestamp": "2024-03-01 14:08:00", "event_type": "scroll", "session_id": "S004", "event_value": 700}, {"event_id": 27, "user_id": 204, "event_timestamp": "2024-03-01 14:10:00", "event_type": "click", "session_id": "S004", "event_value": null}, {"event_id": 28, "user_id": 204, "event_timestamp": "2024-03-01 14:12:00", "event_type": "app_close", "session_id": "S004", "event_value": null}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Calculate duration from the timestamp endpoints

`MIN(event_timestamp)` is the first event and `MAX(event_timestamp)` is the last.

The source computes

`TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp))`

and exposes it as `session_duration_minutes`.

MySQL `TIMESTAMPDIFF(MINUTE, ...)` returns the number of complete minute boundaries, truncating any leftover seconds. A duration of 35 minutes and 40 seconds is displayed as 35.

This is an appropriate integer output column for the example, but its use in filtering needs careful boundary handling.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count event types with MySQL Boolean sums

In MySQL numeric context, a true comparison is one and a false comparison is zero.

Therefore:

- `SUM(event_type = 'scroll')` counts scroll events.
- `SUM(event_type = 'click')` counts click events.
- `SUM(event_type = 'purchase')` counts purchases.

The selected `scroll_count` is the first expression above.

The source requires at least five scrolls, no purchases, and

`click_count / scroll_count < 0.2`.

Because qualifying groups must have at least five scrolls, the intended denominator is positive. MySQL may evaluate the division expression for a zero-scroll group before the separate `HAVING` condition; division by zero yields `NULL` rather than a qualifying true comparison, but using `NULLIF(scroll_count, 0)` would express the safety explicitly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["session_id", "user_id", "session_duration_minutes", "scroll_count"], "rows": [["S001", 201, 35, 6]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"app_events": [{"event_id": 1, "user_id": 201, "event_timestamp": "2024-03-01 10:00:00", "event_type": "app_open", "session_id": "S001", "event_value": null}, {"event_id": 2, "user_id": 201, "event_timestamp": "2024-03-01 10:05:00", "event_type": "scroll", "session_id": "S001", "event_value": 500}, {"event_id": 3, "user_id": 201, "event_timestamp": "2024-03-01 10:10:00", "event_type": "scroll", "session_id": "S001", "event_value": 750}, {"event_id": 4, "user_id": 201, "event_timestamp": "2024-03-01 10:15:00", "event_type": "scroll", "session_id": "S001", "event_value": 600}, {"event_id": 5, "user_id": 201, "event_timestamp": "2024-03-01 10:20:00", "event_type": "scroll", "session_id": "S001", "event_value": 800}, {"event_id": 6, "user_id": 201, "event_timestamp": "2024-03-01 10:25:00", "event_type": "scroll", "session_id": "S001", "event_value": 550}, {"event_id": 7, "user_id": 201, "event_timestamp": "2024-03-01 10:30:00", "event_type": "scroll", "session_id": "S001", "event_value": 900}, {"event_id": 8, "user_id": 201, "event_timestamp": "2024-03-01 10:35:00", "event_type": "app_close", "session_id": "S001", "event_value": null}, {"event_id": 9, "user_id": 202, "event_timestamp": "2024-03-01 11:00:00", "event_type": "app_open", "session_id": "S002", "event_value": null}, {"event_id": 10, "user_id": 202, "event_timestamp": "2024-03-01 11:02:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 11, "user_id": 202, "event_timestamp": "2024-03-01 11:05:00", "event_type": "scroll", "session_id": "S002", "event_value": 400}, {"event_id": 12, "user_id": 202, "event_timestamp": "2024-03-01 11:08:00", "event_type": "click", "session_id": "S002", "event_value": null}, {"event_id": 13, "user_id": 202, "event_timestamp": "2024-03-01 11:10:00", "event_type": "scroll", "session_id": "S002", "event_value": 350}, {"event_id": 14, "user_id": 202, "event_timestamp": "2024-03-01 11:15:00", "event_type": "purchase", "session_id": "S002", "event_value": 50}, {"event_id": 15, "user_id": 202, "event_timestamp": "2024-03-01 11:20:00", "event_type": "app_close", "session_id": "S002", "event_value": null}, {"event_id": 16, "user_id": 203, "event_timestamp": "2024-03-01 12:00:00", "event_type": "app_open", "session_id": "S003", "event_value": null}, {"event_id": 17, "user_id": 203, "event_timestamp": "2024-03-01 12:10:00", "event_type": "scroll", "session_id": "S003", "event_value": 1000}, {"event_id": 18, "user_id": 203, "event_timestamp": "2024-03-01 12:20:00", "event_type": "scroll", "session_id": "S003", "event_value": 1200}, {"event_id": 19, "user_id": 203, "event_timestamp": "2024-03-01 12:25:00", "event_type": "click", "session_id": "S003", "event_value": null}, {"event_id": 20, "user_id": 203, "event_timestamp": "2024-03-01 12:30:00", "event_type": "scroll", "session_id": "S003", "event_value": 800}, {"event_id": 21, "user_id": 203, "event_timestamp": "2024-03-01 12:40:00", "event_type": "scroll", "session_id": "S003", "event_value": 900}, {"event_id": 22, "user_id": 203, "event_timestamp": "2024-03-01 12:50:00", "event_type": "scroll", "session_id": "S003", "event_value": 1100}, {"event_id": 23, "user_id": 203, "event_timestamp": "2024-03-01 13:00:00", "event_type": "app_close", "session_id": "S003", "event_value": null}, {"event_id": 24, "user_id": 204, "event_timestamp": "2024-03-01 14:00:00", "event_type": "app_open", "session_id": "S004", "event_value": null}, {"event_id": 25, "user_id": 204, "event_timestamp": "2024-03-01 14:05:00", "event_type": "scroll", "session_id": "S004", "event_value": 600}, {"event_id": 26, "user_id": 204, "event_timestamp": "2024-03-01 14:08:00", "event_type": "scroll", "session_id": "S004", "event_value": 700}, {"event_id": 27, "user_id": 204, "event_timestamp": "2024-03-01 14:10:00", "event_type": "click", "session_id": "S004", "event_value": null}, {"event_id": 28, "user_id": 204, "event_timestamp": "2024-03-01 14:12:00", "event_type": "app_close", "session_id": "S004", "event_value": null}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["session_id", "user_id", "session_duration_minutes", "scroll_count"], "rows": [["S001", 201, 35, 6]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Seconds-based duration filter:** Compare `TIMESTAMPDIFF(SECOND, MIN(...), MAX(...)) > 1800` to enforce “more than 30 minutes” exactly.
- **Use `> 30` on the minute alias:** It rejects exact 30 minutes but also incorrectly rejects durations from 30:01 through 30:59 because `TIMESTAMPDIFF(MINUTE)` truncates.
- **Integer ratio comparison:** `5 * click_count < scroll_count` expresses a strict rate below one fifth without division.
- **Conditional `CASE` counts:** `SUM(CASE WHEN event_type='scroll' THEN 1 ELSE 0 END)` is more portable than MySQL Boolean arithmetic.
- **Filter event types in `WHERE`:** This would remove rows before aggregation and corrupt counts, duration endpoints, or purchase detection.
- **Exactly five scrolls:** This passes the minimum because the source uses `>= 5`.
- **Ratio exactly 0.20:** It fails because the comparison is strict.
- **No scrolls:** The group fails the five-scroll condition; explicit `NULLIF` can make division safety clearer.
- **No clicks:** The ratio is zero when scroll count is positive and passes.
- **One purchase:** `SUM(...)=0` fails, regardless of amount.
- **Exact 30-minute session:** The source incorrectly admits it because of `>= 30`.
- **Refund or other event values:** `event_value` is irrelevant to all criteria.
- **Several users sharing one session ID:** This would violate the session model and make selected `user_id` ambiguous; grouping both columns would separate them.
- **Ordering ties:** Equal scroll counts are resolved by ascending `session_id`.
- **Potential null timestamps/types:** The reference presents valid event rows. A nullable production schema would need an explicit policy.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let `N` be the number of event rows and `S` the number of distinct sessions.
- **Auxiliary Space Complexity:** $O(N + S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
