## General

**Aggregate all behavior at the session level**

Every zombie criterion describes a complete session rather than one event:

- Duration depends on the earliest and latest timestamps.
- Scroll and click requirements depend on event counts.
- Purchase absence depends on whether any purchase row exists.

The source groups all rows by `session_id`. One output group then contains every event used to calculate that session’s metrics.

It also selects `user_id` without including it in `GROUP BY`. This relies on the stated data model that a session belongs to one user, making `user_id` functionally dependent on `session_id`. In MySQL, that dependency allows the selected value when the schema or mode recognizes it. Listing both columns in `GROUP BY` would make the assumption explicit and more portable.

**Calculate duration from the timestamp endpoints**

`MIN(event_timestamp)` is the first event and `MAX(event_timestamp)` is the last.

The source computes

`TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp))`

and exposes it as `session_duration_minutes`.

MySQL `TIMESTAMPDIFF(MINUTE, ...)` returns the number of complete minute boundaries, truncating any leftover seconds. A duration of 35 minutes and 40 seconds is displayed as 35.

This is an appropriate integer output column for the example, but its use in filtering needs careful boundary handling.

**Count event types with MySQL Boolean sums**

In MySQL numeric context, a true comparison is one and a false comparison is zero.

Therefore:

- `SUM(event_type = 'scroll')` counts scroll events.
- `SUM(event_type = 'click')` counts click events.
- `SUM(event_type = 'purchase')` counts purchases.

The selected `scroll_count` is the first expression above.

The source requires at least five scrolls, no purchases, and

`click_count / scroll_count < 0.2`.

Because qualifying groups must have at least five scrolls, the intended denominator is positive. MySQL may evaluate the division expression for a zero-scroll group before the separate `HAVING` condition; division by zero yields `NULL` rather than a qualifying true comparison, but using `NULLIF(scroll_count, 0)` would express the safety explicitly.

**Why the ratio comparison is strict**

A ratio equal to 0.20 is not less than 0.20. Session S003 has one click and five scrolls, giving exactly one fifth, so it must fail.

The source correctly uses `< 0.2` rather than `<= 0.2` and compares the unrounded quotient. It does not round the rate before filtering, so values close to the threshold are judged using their actual division result.

An exact integer comparison such as

`5 * click_count < scroll_count`

would avoid decimal representation entirely, but the source uses division.

**Apply aggregate criteria with `HAVING`**

`WHERE` would filter individual event rows before session metrics are computed. Removing clicks or purchases there would corrupt the very counts being tested.

`HAVING` runs after grouping and can use complete aggregates and the selected duration alias. The source combines all four conditions with `AND`, so a session must satisfy every one.

**The duration condition has a boundary defect**

The statement requires a duration **more than** 30 minutes. The exact source uses

`session_duration_minutes >= 30`.

That admits a session lasting exactly 30 minutes, which violates the strict requirement.

Changing the alias comparison to `> 30` is not fully precise either because the alias is truncated to whole minutes. A duration of 30 minutes and 30 seconds is more than 30 minutes but still has `TIMESTAMPDIFF(MINUTE) = 30` and would be rejected by `> 30`.

A contract-accurate filter should compare at finer resolution, for example:

`TIMESTAMPDIFF(SECOND, MIN(event_timestamp), MAX(event_timestamp)) > 1800`.

The displayed whole-minute alias can remain unchanged if that is the requested output representation. This is a genuine semantic defect in the stored query, not merely a stylistic difference.

**Order the qualifying sessions**

`ORDER BY scroll_count DESC, session_id` first places sessions with more scroll activity earlier. The default ordering for `session_id` is ascending, satisfying the tie rule.

SQL group order is not guaranteed, so the explicit order clause is necessary even if a particular execution plan happens to emit grouped IDs predictably.

**Trace the example**

S001 spans 35 whole minutes, has six scrolls, zero clicks, and zero purchases. Its ratio is zero and every source condition passes.

S002 fails duration and purchase absence. S003 has sufficient duration and scrolls but ratio exactly 0.20, so the strict ratio rejects it. S004 is too short and has too few scrolls.

Only S001 remains.

**Why one grouped scan is the right logical plan**

The database needs constant aggregate state per session: first timestamp, last timestamp, scroll count, click count, and purchase count.

Each event updates that state once. Afterward, `HAVING` evaluates the metrics and the result sort orders only qualifying groups. No self-join, event ranking, or correlated subquery is required.

## Complexity detail

Let `N` be the number of event rows and `S` the number of distinct sessions.

With hash aggregation, grouping can take expected `O(N)` time and `O(S)` aggregate-state space. Sorting qualifying sessions costs `O(S log S)` in the worst case.

A sort-based grouping plan may sort the input by session and cost `O(N log N)` time with up to `O(N)` temporary storage. The manifest’s `O(N log N + S log S)` time and `O(N + S)` space are conservative physical-plan bounds.

An index beginning with `session_id` may let MySQL stream groups, while an index supporting the output order may reduce sorting. Actual SQL complexity depends on the optimizer and indexes, but the logical work is one aggregation followed by one result ordering.

## Alternatives and edge cases

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
