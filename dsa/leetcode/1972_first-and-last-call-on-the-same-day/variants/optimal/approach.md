## General

**Turn every call into each participant's point of view**

The table stores a call asymmetrically: one user appears in `caller_id` and the other appears in `recipient_id`. The question is symmetric, however. A user's call counts whether that user placed or received it. Trying to analyze only the original `caller_id` column would therefore miss every received call.

The first common table expression, `s`, normalizes this mismatch. Its first query keeps each original row as

`(caller_id, recipient_id, call_time)`.

Its second query reverses the two participant columns and keeps the same time:

`(recipient_id, caller_id, call_time)`.

Because the columns inherit the names from the first query, every row of `s` can now be read uniformly: `caller_id` is the user being analyzed, while `recipient_id` is the other person in that call. One physical call normally contributes two logical rows, one for each participant.

The query deliberately uses `UNION ALL`. It does not need the database to spend work removing duplicates, because the two perspectives are meaningful records for the later per-user analysis. If self-calls are possible, the two perspectives are identical, but their duplication still does not change the first or last partner.

**Separate one user's days**

First and last are not global properties of a user. They must be recomputed for every calendar day. Both window expressions therefore partition by two keys:

- `caller_id`, which now means the user whose perspective this row represents;
- `DATE_FORMAT(call_time, '%Y-%m-%d')`, which discards the clock portion and retains the day.

All calls made or received by the same user on the same date belong to one window partition. Calls by another user, or calls by the same user on another date, cannot affect that partition.

**Find both boundary partners with window functions**

Within each user-day partition, the first `FIRST_VALUE(recipient_id)` orders rows by `call_time ASC`. The first row in that ordering is the earliest call, so the expression writes that earliest partner into the `first` column of every row in the partition.

The second expression uses the same partition but orders by `call_time DESC`. The first row of the reversed order is the chronologically latest call, so this value becomes `last`.

This is an important window-function idea: the query does not collapse the partition into one row as `GROUP BY` would. It annotates each existing logical call row with the two boundary answers for its user and day. Consequently, every row in one user-day partition receives the same relevant `first` and `last` values.

For example, suppose user 8 has calls on one day with user 4 at 09:00, user 3 at 12:00, and user 4 at 18:00. Ascending order selects 4, and descending order also selects 4. All three annotated rows therefore satisfy `first = last`. The middle call is irrelevant to the required condition; it is allowed to involve anyone.

If a user has exactly one call on a day, that same row is simultaneously earliest and latest. Its partner is therefore equal in both columns, which correctly qualifies the user for that day.

**Keep users who qualify on at least one day**

The final `WHERE first = last` retains rows belonging to a qualifying user-day partition. The requirement says "on any day," so a single qualifying day is sufficient even if the same user has other days whose boundary partners differ.

Because a qualifying partition can still contain several rows, and because one user can qualify on several dates, the final projection uses `SELECT DISTINCT user_id`. This reduces all such evidence to the requested set of user IDs. No date or partner column belongs in the result.

**Why this is correct**

The normalization step represents every original call exactly from the perspective of each participant. Therefore, for a fixed user and date, its partition contains all and only that user's calls on that date.

Ascending chronological order identifies the partner in the first call, and descending chronological order identifies the partner in the last call. The equality filter is true exactly when these partners are the same. Finally, `DISTINCT` implements the existential phrase "any day": it reports a user once if at least one of the user's partitions passes. These facts match every part of the requested condition.

**A timestamp-tie caveat in the exact query**

The window `ORDER BY` contains only `call_time`. If the same user can participate in calls with different people at exactly the same timestamp, SQL is free to choose either tied row as the first value because no secondary tie-breaker is supplied. The local schema says the three-column combination is unique, but that alone does not forbid such a per-user time tie with different partners.

The exact solution therefore relies on first and last calls being unambiguous under the data's time semantics. Adding a participant ID as a tie-breaker would make the choice deterministic, but it would invent an ordering between simultaneous calls rather than define what "first" means for the problem. This is a contract ambiguity to recognize, not something to silently change in the query.

## Complexity detail

Let $R$ be the number of rows in `Calls`. The normalized CTE has up to $2R$ rows. Producing it is linear, while the two window orderings may sort rows within user-day partitions. Across the data, the usual upper bound is $O(R\log R)$ time. The final filter and duplicate removal add linear work or hashing/sorting that remains within that bound.

The logical intermediate data and window processing require $O(R)$ space. A real database engine may spill a sort to disk, build temporary indexes, or exploit an existing index, but the manifest's algorithmic auxiliary bound is $O(R)$.

## Alternatives and edge cases

- **Conditional aggregation after ranking:** Rank earliest and latest rows and group by user and day, then compare conditional partner values. This is explicit but usually longer than two `FIRST_VALUE` annotations.
- **Join minimum and maximum times back to `Calls`:** It can work, but it needs both participant perspectives and careful joins; time ties can multiply rows.
- **`DENSE_RANK` plus grouping:** Keep rows ranked first in ascending or descending order, then require one distinct partner. This treats tied boundary times differently and can express a deliberate all-ties interpretation.
- **Analyze callers only:** This is incorrect because calls received by a user are part of that user's daily history.
- **One call in a day:** Its partner is both first and last, so the user qualifies.
- **Middle calls with other people:** They do not matter when the earliest and latest partners match.
- **Qualifying on only one of many days:** The user is included because the condition is existential.
- **Repeated qualifying rows:** `DISTINCT` ensures each user appears only once.
- **Calendar-day boundary:** Partitioning by the formatted date prevents a late call on one date from mixing with an early call on the next date.
- **Equal timestamps:** Without a secondary ordering key, different partners tied at a boundary make `FIRST_VALUE` nondeterministic; the exact source assumes an unambiguous boundary.
- **Self-call:** `UNION ALL` may create two identical perspective rows, but both name the same partner and do not change the equality result.
- **Result order:** No `ORDER BY` is needed because the contract allows any order.
