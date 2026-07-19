## General
**Restrict events before counting.** Filter `activity_date` to the inclusive interval from `2019-06-28` through `2019-07-27`. A session represented only by rows outside that interval must not enter any user's count.

**Establish one count per active user.** Group the retained rows by `user_id` and calculate `COUNT(DISTINCT session_id)` for each group. Distinct counting neutralizes duplicate rows and multiple event types within a session. The source guarantee that a session belongs to exactly one user keeps these groups unambiguous.

**Average the user-level results.** Apply `AVG` to the per-user session counts in an outer query and round the final value to two decimal places. `COALESCE` or `IFNULL` converts the `NULL` average of an empty subquery into `0`. Averaging after grouping gives every active user equal weight rather than weighting users by their number of event rows.

## Complexity detail
Filtering scans up to $R$ rows, while grouping and distinct-session counting can sort or hash the qualifying rows. A conservative logical bound is $O(R\log R)$ time and $O(R)$ grouping space. Indexes and hash aggregation may improve the physical execution plan.

## Alternatives and edge cases
- **Global distinct-session ratio:** Because each session belongs to one user, dividing the number of distinct qualifying sessions by the number of distinct qualifying users is equivalent, but the grouped form exposes the requested per-user grain.
- **Same-user self-join:** Joining qualifying activity rows to one another by user before deduplication remains correct but can generate $O(R^2)$ pairs for a heavily active user.
- **Duplicate session events:** Repeated rows and different activity types for one session count only once.
- **Sessions spanning dates:** A session qualifies when it has at least one event inside the window; outside events do not create another session.
- **Inactive users:** Users without a qualifying event are absent from the average.
- **Empty window:** Return `0`, not `NULL` and not an absent row.
