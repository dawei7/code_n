## General
**Determine newness before applying the reporting window:** Restrict the source rows to `activity = 'login'`, group them by `user_id`, and compute `MIN(activity_date)`. This produces exactly one first-login date for every user who has ever logged in. Filtering to the 90-day period earlier would incorrectly make an established user appear new when that user's first in-window login is not the first login overall.

**Filter the derived first-login relation:** The period ends on `2019-06-30`, and subtracting 90 days gives the inclusive lower boundary `2019-04-01`. Keep only derived dates in that closed interval. Non-login activities never enter the minimum, so a homepage visit before a user's first login does not disqualify the later login.

**Aggregate users by first-login date:** Group the remaining one-row-per-user relation by `login_date` and count its rows. Each counted row represents a distinct user, so `COUNT(*)` gives the daily new-user total without another distinct operation. Ordering is added only to make local results stable.

Every returned user belongs to the group for that user's minimum login date, which is inside the required interval, so every count is valid. Conversely, any user whose first login falls inside the interval survives the filter exactly once and is counted in the corresponding date group, so no qualifying user is omitted or counted twice.

## Complexity detail
A sort-based plan groups $N$ activity rows in $O(N \log N)$ time and stores at most one derived row for each of the $U$ users, using $O(U)$ execution space. A database engine may use hash aggregation for expected $O(N)$ time, and suitable indexes can change the physical plan, but those improvements are not assumed by the stated bound.

## Alternatives and edge cases
- **Correlated minimum per login row:** Compare every login with a correlated `MIN(activity_date)` for the same user. It is correct, but without an index it can rescan the table for each candidate and require $O(N^2)$ time.
- **Self anti-join:** Keep a login only when no earlier login exists for the same user, then aggregate. This expresses the definition directly but can create many intermediate pairs and needs careful deduplication if identical rows are possible.
- **Window function:** Assign `ROW_NUMBER()` within each user ordered by `activity_date`, keep rank one, then group. It is valid but does more ordering work than the direct grouped minimum.
- **Lower boundary:** A first login on `2019-04-01` is included because the 90-day difference from `2019-06-30` is allowed.
- **Earlier login:** A user first seen before `2019-04-01` remains excluded even after logging in during the reporting period.
- **Earlier non-login activity:** It does not affect the first-login date because only `login` rows define new users.
- **Repeated login rows:** Grouping by user produces one first-login record, so a user contributes at most once.
- **No qualifying users:** The result is empty rather than containing calendar dates with zero counts.
