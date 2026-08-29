## General

**Separate “what happened over the whole history” from “what is true now”**

Each output condition depends on one of two different views of a user's subscription events:

- Historical facts use all of the user's rows: the first and last event dates, the highest monthly amount ever recorded, and whether any downgrade occurred.
- Current facts must come from one specific row: the user's latest event, including its event type, plan name, and monthly amount.

Trying to obtain both views in one ordinary `GROUP BY user_id` query is unsafe. Aggregates such as `MIN`, `MAX`, and `SUM` summarize many rows, but `plan_name` and `event_type` must remain tied to the same latest row. Selecting an arbitrary plan beside aggregated values could describe a plan the user no longer has. The Optimal query therefore builds the two views independently and joins them only after each has the correct meaning.

**Rank each user's events to identify one deterministic latest row**

The first common table expression, `user_with_last_event`, selects every event and adds:

`ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_date DESC, event_id DESC) AS rn`.

The window function restarts numbering for each `user_id` because of `PARTITION BY user_id`. Within one user, later dates sort first because `event_date` is descending. Therefore, the latest event receives row number one.

The second ordering key, `event_id DESC`, handles multiple events for the same user on the same date. Among those tied dates, the event with the greater identifier comes first. This is important for determinism: ordering only by date could let the database choose either tied row, potentially changing the reported current plan or whether the customer is considered canceled.

This CTE does not collapse rows. It preserves the original row values and merely labels their recency. That preservation lets the later `latest_event` CTE take the event type, plan, and monthly amount from one coherent record.

**Aggregate all historical evidence once per user**

The `user_history` CTE groups the original `subscription_events` table by `user_id` and computes four facts:

- `MIN(event_date) AS start_date` is the date of the earliest recorded event.
- `MAX(event_date) AS last_event_date` is the date of the latest recorded event.
- `MAX(monthly_amount) AS max_historical_amount` is the highest monthly amount found anywhere in the user's history.
- `downgrade_count` is the number of rows whose `event_type` is `'downgrade'`.

The downgrade count uses a conditional sum. Each downgrade row contributes one, and every other event contributes zero. The final filter needs only to know whether the count is at least one, but storing the count is a clear and portable way to express that history requirement.

The maximum amount is intentionally computed over all event rows, not merely downgrade rows and not merely the current row. The churn-risk rule compares the present amount with the greatest historical amount, so an earlier high-priced plan must remain part of the comparison even if several later changes occurred.

Likewise, the duration endpoints come from the full history. `start_date` and `last_event_date` describe the span between the user's first and latest recorded events.

**Project the current state from exactly the rank-one row**

The `latest_event` CTE reads from `user_with_last_event` and keeps only `rn = 1`. It renames the selected values to make their later role explicit:

- `event_type` becomes `last_event_type`.
- `plan_name` becomes `current_plan`.
- `monthly_amount` becomes `current_monthly_amount`.

Because all three columns come from the same row, the current plan and amount correspond to the event used to decide whether the latest state is canceled. No independent maximum or arbitrary grouping can detach them from one another.

**Join the two views and apply every churn-risk condition**

The final query joins `latest_event l` with `user_history h` on `user_id`. Both CTEs contain one row per user at this stage, so the join produces one candidate output row per user.

The `WHERE` clause then enforces four independent requirements:

1. `l.last_event_type <> 'cancel'` keeps active users. A user with an old cancellation followed by a later active event is judged by the later event; a user whose latest event is cancellation is excluded.
2. `h.downgrade_count >= 1` requires at least one downgrade anywhere in the history.
3. `l.current_monthly_amount < 0.5 * h.max_historical_amount` requires the current amount to be strictly less than half of the user's historical maximum. Equality to exactly half does not pass because the operator is `<`, not `<=`.
4. `DATEDIFF(h.last_event_date, h.start_date) >= 60` requires a historical span of at least 60 days.

In MySQL, `DATEDIFF(later_date, earlier_date)` returns the number of date boundaries between the two dates. It is not an inclusive count of calendar dates. For example, dates exactly 60 days apart produce 60 and satisfy the condition.

The same date difference is selected as `days_as_subscriber`. Reusing the same expression ensures that the displayed duration has exactly the interpretation used for filtering.

**Produce the requested columns and stable ordering**

The result returns `user_id`, the latest row's current plan and monthly amount, the historical maximum amount, and the computed duration. It does not expose helper values such as `downgrade_count` or `last_event_type` because those are needed only to qualify rows.

Finally, `ORDER BY days_as_subscriber DESC, l.user_id ASC` places longer subscription histories first. Users with equal durations are ordered by increasing user identifier. This second key makes the order stable and exactly resolves duration ties.

The query is exact because each historical predicate is evaluated from a complete per-user aggregation, each current predicate and current output value comes from the deterministically selected latest row, and the final join combines those two records for the same user.

## Complexity detail

Let `R` be the number of rows in `subscription_events` and `U` be the number of distinct users.

The window function must arrange each user's events by descending date and event identifier. A conventional execution uses a sort and costs $O(R \log R)$ time in the worst case, although an appropriate index may let a database reduce or avoid explicit sorting. The grouped historical aggregation scans all rows and uses expected $O(R)$ work with hash aggregation, or sorting work under a sort-based aggregation plan. Filtering `rn = 1` and joining the two one-row-per-user CTE results require $O(R)$ and expected $O(U)$ work respectively in a typical plan.

The final ordering of at most `U` qualified users costs $O(U \log U)$. A useful high-level bound for the shown query is therefore $O(R \log R + U \log U)$ time. SQL execution is optimizer-dependent, so this describes the standard logical cost rather than promising one physical plan.

The ranked intermediate can contain `R` rows, and the grouped, latest, joined, and sorted user-level intermediates contain up to `U` rows. The high-level auxiliary-space bound is $O(R + U)$. A production database may spill sorts to disk, stream indexed rows, inline CTEs, or materialize them, changing the memory/disk split without changing the query's result.

## Alternatives and edge cases

- **Correlated latest-event subquery:** A subquery can search for the maximum date and event identifier for every user, but it may repeat work and becomes cumbersome when several current columns must come from the same row. `ROW_NUMBER` selects that row once and keeps its columns aligned.
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
