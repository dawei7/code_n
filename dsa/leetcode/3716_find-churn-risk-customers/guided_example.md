# Guided Example: Find Churn Risk Customers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"subscription_events": [{"event_id": 1, "user_id": 501, "event_date": "2024-01-01", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 2, "user_id": 501, "event_date": "2024-02-15", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 3, "user_id": 501, "event_date": "2024-03-20", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 4, "user_id": 502, "event_date": "2024-01-05", "event_type": "start", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 5, "user_id": 502, "event_date": "2024-02-10", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 6, "user_id": 502, "event_date": "2024-03-15", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 7, "user_id": 503, "event_date": "2024-01-10", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 8, "user_id": 503, "event_date": "2024-02-20", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 9, "user_id": 503, "event_date": "2024-03-25", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 10, "user_id": 504, "event_date": "2024-01-15", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 11, "user_id": 504, "event_date": "2024-03-01", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 12, "user_id": 504, "event_date": "2024-03-30", "event_type": "cancel", "plan_name": null, "monthly_amount": 0}, {"event_id": 13, "user_id": 505, "event_date": "2024-02-01", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 14, "user_id": 505, "event_date": "2024-02-28", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 15, "user_id": 506, "event_date": "2024-01-20", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 16, "user_id": 506, "event_date": "2024-03-10", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}]}}`
- **Required output:** `{"columns": ["user_id", "current_plan", "current_monthly_amount", "max_historical_amount", "days_as_subscriber"], "rows": [[501, "basic", 9.99, 29.99, 79], [502, "basic", 9.99, 29.99, 70]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: $\text{subscription}_{events}$

The objective is to compute `{"columns": ["user_id", "current_plan", "current_monthly_amount", "max_historical_amount", "days_as_subscriber"], "rows": [[501, "basic", 9.99, 29.99, 79], [502, "basic", 9.99, 29.99, 70]]}` from `{"tables": {"subscription_events": [{"event_id": 1, "user_id": 501, "event_date": "2024-01-01", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 2, "user_id": 501, "event_date": "2024-02-15", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 3, "user_id": 501, "event_date": "2024-03-20", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 4, "user_id": 502, "event_date": "2024-01-05", "event_type": "start", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 5, "user_id": 502, "event_date": "2024-02-10", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 6, "user_id": 502, "event_date": "2024-03-15", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 7, "user_id": 503, "event_date": "2024-01-10", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 8, "user_id": 503, "event_date": "2024-02-20", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 9, "user_id": 503, "event_date": "2024-03-25", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 10, "user_id": 504, "event_date": "2024-01-15", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 11, "user_id": 504, "event_date": "2024-03-01", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 12, "user_id": 504, "event_date": "2024-03-30", "event_type": "cancel", "plan_name": null, "monthly_amount": 0}, {"event_id": 13, "user_id": 505, "event_date": "2024-02-01", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 14, "user_id": 505, "event_date": "2024-02-28", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 15, "user_id": 506, "event_date": "2024-01-20", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 16, "user_id": 506, "event_date": "2024-03-10", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate “what happened over the whole history” from “what is true now”

Each output condition depends on one of two different views of a user's subscription events:

- Historical facts use all of the user's rows: the first and last event dates, the highest monthly amount ever recorded, and whether any downgrade occurred.
- Current facts must come from one specific row: the user's latest event, including its event type, plan name, and monthly amount.

Trying to obtain both views in one ordinary `GROUP BY user_id` query is unsafe. Aggregates such as `MIN`, `MAX`, and `SUM` summarize many rows, but `plan_name` and `event_type` must remain tied to the same latest row. Selecting an arbitrary plan beside aggregated values could describe a plan the user no longer has. The Optimal query therefore builds the two views independently and joins them only after each has the correct meaning.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"subscription_events": [{"event_id": 1, "user_id": 501, "event_date": "2024-01-01", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 2, "user_id": 501, "event_date": "2024-02-15", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 3, "user_id": 501, "event_date": "2024-03-20", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 4, "user_id": 502, "event_date": "2024-01-05", "event_type": "start", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 5, "user_id": 502, "event_date": "2024-02-10", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 6, "user_id": 502, "event_date": "2024-03-15", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 7, "user_id": 503, "event_date": "2024-01-10", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 8, "user_id": 503, "event_date": "2024-02-20", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 9, "user_id": 503, "event_date": "2024-03-25", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 10, "user_id": 504, "event_date": "2024-01-15", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 11, "user_id": 504, "event_date": "2024-03-01", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 12, "user_id": 504, "event_date": "2024-03-30", "event_type": "cancel", "plan_name": null, "monthly_amount": 0}, {"event_id": 13, "user_id": 505, "event_date": "2024-02-01", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 14, "user_id": 505, "event_date": "2024-02-28", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 15, "user_id": 506, "event_date": "2024-01-20", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 16, "user_id": 506, "event_date": "2024-03-10", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank each user's events to identify one deterministic latest row

The first common table expression, `user_with_last_event`, selects every event and adds:

`ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_date DESC, event_id DESC) AS rn`.

The window function restarts numbering for each `user_id` because of `PARTITION BY user_id`. Within one user, later dates sort first because `event_date` is descending. Therefore, the latest event receives row number one.

The second ordering key, `event_id DESC`, handles multiple events for the same user on the same date. Among those tied dates, the event with the greater identifier comes first. This is important for determinism: ordering only by date could let the database choose either tied row, potentially changing the reported current plan or whether the customer is considered canceled.

This CTE does not collapse rows. It preserves the original row values and merely labels their recency. That preservation lets the later `latest_event` CTE take the event type, plan, and monthly amount from one coherent record.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first common table expression, `user_with_last_event`, s... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregate all historical evidence once per user

The `user_history` CTE groups the original `subscription_events` table by `user_id` and computes four facts:

- `MIN(event_date) AS start_date` is the date of the earliest recorded event.
- `MAX(event_date) AS last_event_date` is the date of the latest recorded event.
- `MAX(monthly_amount) AS max_historical_amount` is the highest monthly amount found anywhere in the user's history.
- `downgrade_count` is the number of rows whose `event_type` is `'downgrade'`.

The downgrade count uses a conditional sum. Each downgrade row contributes one, and every other event contributes zero. The final filter needs only to know whether the count is at least one, but storing the count is a clear and portable way to express that history requirement.

The maximum amount is intentionally computed over all event rows, not merely downgrade rows and not merely the current row. The churn-risk rule compares the present amount with the greatest historical amount, so an earlier high-priced plan must remain part of the comparison even if several later changes occurred.

Likewise, the duration endpoints come from the full history. `start_date` and `last_event_date` describe the span between the user's first and latest recorded events.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "current_plan", "current_monthly_amount", "max_historical_amount", "days_as_subscriber"], "rows": [[501, "basic", 9.99, 29.99, 79], [502, "basic", 9.99, 29.99, 70]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"subscription_events": [{"event_id": 1, "user_id": 501, "event_date": "2024-01-01", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 2, "user_id": 501, "event_date": "2024-02-15", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 3, "user_id": 501, "event_date": "2024-03-20", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 4, "user_id": 502, "event_date": "2024-01-05", "event_type": "start", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 5, "user_id": 502, "event_date": "2024-02-10", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 6, "user_id": 502, "event_date": "2024-03-15", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 7, "user_id": 503, "event_date": "2024-01-10", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 8, "user_id": 503, "event_date": "2024-02-20", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 9, "user_id": 503, "event_date": "2024-03-25", "event_type": "upgrade", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 10, "user_id": 504, "event_date": "2024-01-15", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 11, "user_id": 504, "event_date": "2024-03-01", "event_type": "downgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 12, "user_id": 504, "event_date": "2024-03-30", "event_type": "cancel", "plan_name": null, "monthly_amount": 0}, {"event_id": 13, "user_id": 505, "event_date": "2024-02-01", "event_type": "start", "plan_name": "basic", "monthly_amount": 9.99}, {"event_id": 14, "user_id": 505, "event_date": "2024-02-28", "event_type": "upgrade", "plan_name": "standard", "monthly_amount": 19.99}, {"event_id": 15, "user_id": 506, "event_date": "2024-01-20", "event_type": "start", "plan_name": "premium", "monthly_amount": 29.99}, {"event_id": 16, "user_id": 506, "event_date": "2024-03-10", "event_type": "downgrade", "plan_name": "basic", "monthly_amount": 9.99}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "current_plan", "current_monthly_amount", "max_historical_amount", "days_as_subscriber"], "rows": [[501, "basic", 9.99, 29.99, 79], [502, "basic", 9.99, 29.99, 70]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated latest-event subquery:** A subquery:** - **Correlated latest-event subquery:** A subquery can search for the maximum date and event identifier for every user, but it may repeat work and becomes cumbersome when several current columns must come from the same row. `ROW_NUMBER` selects that row once and keeps its columns aligned.
- **Aggregate current columns with `MAX`:** Taking `MAX(plan_name)` or `MAX(monthly_amount)` does not mean “value from the latest event.” Different aggregates could even come from different historical rows, so this shortcut breaks the current-state semantics.
- **Join on maximum date alone:** If a user has two events on the latest date, this can return duplicate rows or choose no unique current state. The descending `event_id` tie-breaker provides the required single row.
- **Use `LAG` to detect a downgrade:** A downgrade is already represented by `event_type = 'downgrade'`. Counting those rows directly is simpler and matches the stated condition; inferring price movement could disagree with the event label.
- **Use `HAVING` for every filter:** Historical aggregate predicates can be expressed in `HAVING`, but the latest-row predicates still require a correctly selected row. Keeping history and current state in separate CTEs makes their data sources visible.
- **Exactly half of the maximum amount:** A current amount equal to `0.5 * max_historical_amount` is excluded. Changing the strict comparison to `<=` would alter the requirement.
- **A previous cancellation followed by a later event:** Only `last_event_type` determines active status. The historical presence of a cancellation is not itself an exclusion when a more recent row establishes a different current state.
- **A downgrade that is not the latest event:** It still counts because `downgrade_count` covers the entire history. The user can later upgrade or change plans and still satisfy the “has downgraded” condition.
- **Several downgrades:** Their exact number beyond one does not change qualification. The sum remains useful because `>= 1` cleanly expresses existence.
- **Multiple highest historical amounts:** `MAX` needs only the amount, not which row supplied it. Ties therefore cause no ambiguity.
- **One event only:** The duration is zero and the user cannot have a 60-day span between first and latest event, so the row is excluded naturally.
- **Events exactly 60 days apart:** `DATEDIFF` returns 60, and `>= 60` includes the user if all other conditions pass.
- **Ties in `days_as_subscriber`:** The ascending user-id key determines the requested order and prevents database-dependent tie ordering.
- **Null values:** The query follows ordinary SQL three-valued logic: comparisons involving `NULL` do not evaluate to true. The stated schema and problem contract are expected to provide the required non-null event fields; adding `COALESCE` would invent semantics not present in the exact Optimal source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R + U log U)$. Let `R` be the number of rows in `subscription_events` and `U` be the number of distinct users.
- **Auxiliary Space Complexity:** $O(R + U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
