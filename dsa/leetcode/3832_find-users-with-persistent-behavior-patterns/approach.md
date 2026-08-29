## General

**First decide which user-days are eligible**

The primary key is `(user_id, action_date, action)`. It prevents duplicate copies of the same action on one day, but it still allows one user to have several different actions on that date.

A streak day is valid only when the user performed exactly one action that day. The first common table expression, `daily_counts`, keeps every original row and attaches

`COUNT(*) OVER (PARTITION BY user_id, action_date) AS cnt`.

All rows for the same user and calendar date receive the same count. A date with one row receives 1. A date containing two distinct actions produces two rows, both marked 2.

`filtered_activity` retains only `cnt = 1`. After this filter:

- every remaining `(user_id, action_date)` occurs exactly once;
- its `action` is the user's sole action for that day;
- a multi-action day contributes no row at all.

Removing every row of an ineligible date is important. That date must not belong to a streak, and it must separate otherwise similar activity on the days around it.

**Convert consecutive dates into an island key**

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

**Why an action change breaks the run**

Consider user activity `login` on January 1, `logout` on January 2, and `login` on January 3. The two login rows belong to the same `(user_id, action)` window, but their dates differ by two days while their row numbers differ by one. Their shifted `grp` dates differ, so they form separate login runs.

The logout row belongs to another action partition. Thus an intervening different action breaks the original-action island even though the island calculation does not explicitly call `LAG(action)`.

This relies on the single-action-day filter. Each eligible calendar day has one action, so any date occupied by another action appears as a missing date in the first action's partition.

**Summarize each maximal island**

`streak_summary` groups the island rows by `user_id, action, grp`.

Because filtered activity contains one row per eligible user-day:

- `COUNT(*)` is the streak length in days;
- `MIN(action_date)` is the first date;
- `MAX(action_date)` is the last date.

`HAVING streak_length >= 5` removes every island shorter than the minimum before final user selection.

For a truly consecutive island, the endpoints and length also satisfy

$$
\texttt{end\_date}-\texttt{start\_date}+1
=
\texttt{streak\_length}.
$$

Counting rows is safe because the island construction already established daily adjacency.

**Rank qualifying runs within each user**

A user can have multiple qualifying islands, possibly for different actions or separated date ranges. The window expression

`ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) AS rnk`

orders that user's summarized islands by decreasing length. Rank 1 is one of the maximum-length qualifying runs.

The final query keeps `rnk = 1`, producing at most one row per user. It then orders users by `streak_length DESC` and `user_id ASC` as required.

Filtering to length at least five before ranking does not hide a longer nonqualifying run: any run longer than a qualifying run is itself at least five and would also survive. If no run reaches five, the user has no summary row and is excluded.

**Trace the example through the stages**

Each example date has one row, so all rows pass `filtered_activity`.

For user 1 and action `login`, January 1 through January 5 produce one constant island key and summarize to length 5 with those endpoints. The January 6 `logout` belongs to another action and does not extend the login island.

User 2's four `click` dates form one island of length 4, which `HAVING` removes.

User 3's seven `view` dates form one island of length 7. Final ordering places user 3 before user 1 because 7 is greater than 5.

**Equal maximum lengths are not deterministically resolved**

The ranking orders only by `COUNT(*) DESC`. If one user has two distinct qualifying runs with exactly the same maximum length, their ordering is tied. MySQL may assign rank 1 to either run because no secondary key is supplied.

The contract says to consider only a maximum-length sequence but does not state which action or date range to return when several sequences share that maximum. The exact source returns one tied maximum nondeterministically. Its length is still correct, but the accompanying `action`, `start_date`, and `end_date` are not stable across execution plans.

If deterministic output is desired, the window order must add an explicit rule, such as earliest `start_date` and then `action`. Such a rule would be an added policy, not one specified by the local description.

**Why each selected row represents valid behavior**

Every source row in an island passed the exactly-one-action daily filter. Partitioning by action gives a common action. The shifted-date key proves every adjacent date in the group is one calendar day apart. The summary's count proves at least five such dates. Hence every returned row is a valid stable sequence.

Conversely, take any valid sequence. Its dates each have one row and survive the first filter. They share a user and action, and consecutive dates yield the same shifted key, so they lie in one grouped island. A maximal valid sequence is represented by that island's complete summary. Ranking retains a maximum-length qualifying island for the user.

## Complexity detail

Let $R$ be the number of rows in `activity` and $U$ the number of returned users. The window count may require ordering or hashing rows by user and date. The streak row numbers require ordering by `user_id, action, action_date`. Grouping islands, ranking summaries, and final output ordering add further database operations.

Under a comparison-sort execution model, these stages are bounded by $O(R\log R)$ time. There are several sorts, but a constant number of $R\log R$ terms remains the same asymptotic bound. The final $O(U\log U)$ ordering is covered because $U\le R$.

The common table expressions and window operations may materialize or buffer up to $O(R)$ rows. Group summaries and final results cannot exceed that scale, so auxiliary database working space is $O(R)$. Actual MySQL plans may use indexes, streaming, temporary tables, or disk spills; the bounds describe logical data scale rather than one guaranteed physical plan.

## Alternatives and edge cases

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
