## General
**Filter the exact inclusive window.** Keep rows whose `activity_date` is between `2019-06-28` and `2019-07-27`. The lower endpoint is 29 days before the ending date, so the inclusive interval contains exactly 30 calendar dates. Filtering both endpoints also prevents later activity from entering the result.

**Group at the required reporting grain.** Group the retained rows by `activity_date` and expose that value as `day`. Because only dates represented by input rows form groups, dates with no active user are omitted automatically.

**Deduplicate users within each date.** Apply `COUNT(DISTINCT user_id)` inside every date group and name it `active_users`. This collapses duplicate rows, multiple activity types, and multiple sessions belonging to the same user on the same date. The same user may still contribute once on each of several dates, which matches daily activity semantics.

## Complexity detail
The logical query scans $R$ rows and groups the qualifying subset by date while maintaining distinct users. A conservative sort-based bound is $O(R\log R)$ time and $O(R)$ grouping space. A database engine may use hashing or suitable indexes for a lower physical cost, but the result semantics do not depend on its chosen plan.

## Alternatives and edge cases
- **Pre-deduplicated subquery:** Select distinct `(activity_date, user_id)` pairs first and then use `COUNT(*)`; this is equivalent and makes the counting unit explicit.
- **Same-day self-join:** Joining the activity table to itself by date before counting distinct users remains correct, but can materialize $O(R^2)$ row pairs for a busy day.
- **Duplicate events:** Repeated identical rows count the user only once for that date.
- **Multiple sessions or types:** They establish activity but do not increase a user's daily contribution beyond one.
- **Window endpoints:** Both `2019-06-28` and `2019-07-27` are included; adjacent dates outside that interval are excluded.
- **Inactive dates:** Do not synthesize rows with a zero count.
