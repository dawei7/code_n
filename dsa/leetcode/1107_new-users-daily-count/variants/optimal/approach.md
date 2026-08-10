## General

**Discard non-login activity before finding first login**

Install or new-user status depends only on login rows. The CTE first applies `WHERE activity = 'login'`, so homepage, logout, jobs, and groups events cannot become a user’s first login.

For each remaining row, `MIN(activity_date) OVER (PARTITION BY user_id)` computes the earliest login date across that user’s complete login history. A window function preserves every login row while attaching the same `login_date` to all of them.

This order is essential. Filtering the final date range before computing the minimum would incorrectly classify a returning user as new if their real first login occurred earlier than the reporting window.

**Collapse repeated rows and later logins by distinct user**

The CTE may contain several rows for one user: later login dates, repeated login records, or exact duplicates are all permitted by the table. In the outer grouping, `COUNT(DISTINCT user_id)` ensures that the user contributes once to the cohort identified by their true first-login date.

`GROUP BY 1` groups by the first selected expression, `login_date`. Each produced row therefore represents one date with at least one qualifying user. Dates with zero users never form a group, as required.

**Apply the exact protected date predicate**

`DATEDIFF('2019-06-30', login_date)` measures how many calendar days the first login precedes the assumed current date. The query retains values no greater than 90. First login on June 30 has difference zero and qualifies; April 1 has difference 90 and also qualifies; March 31 has difference 91 and is excluded.

However, the exact predicate has no lower bound. A future login produces a negative difference, and every negative number is also `<= 90`. Therefore, the protected query assumes no future first-login dates, or else it would include them.

The local Reference contract explicitly defines the closed interval April 1 through June 30 and says future dates do not qualify. To implement that broader contract independently of source-data assumptions, the outer filter must require the difference to be between zero and ninety inclusive.

**Why the cohort counts are correct under that assumption**

Every login-capable user receives their true minimum login date because the window considers all login rows. The range filter retains eligible cohort dates only. Grouping gathers users with the same minimum, and distinct counting neutralizes both duplicates and later login records. Consequently, each eligible user is counted exactly once on exactly their first-login date.

Result order is unrestricted, so no `ORDER BY` is necessary. If no login exists or no first-login date passes the predicate, the CTE or filtered result forms no groups and the output is empty.

The other activity categories are irrelevant even when they precede every login. “New user” in this problem means first login, not first appearance anywhere in Traffic. Filtering to login rows before the window minimum therefore follows the definition rather than losing meaningful history.

## Complexity detail

Let $N$ be the number of Traffic rows and $U$ the number of distinct users. Filtering scans $N$ rows. A typical window implementation sorts or partitions login rows by user, leading to $O(N\log N)$ time, followed by another grouping pass. This matches the manifest’s time bound.

The manifest records $O(U)$ space, corresponding to retaining one first-login aggregate per user. The exact window CTE logically preserves every login row and a physical engine may materialize $O(N)$ rows or sort storage. A grouped CTE using `MIN` would more directly realize $O(U)$ logical state. Actual database memory depends on indexes and the optimizer.

The final result contains at most $U$ cohort rows, usually far fewer because many users share dates.

## Alternatives and edge cases

- **Grouped CTE:** Select `user_id, MIN(activity_date)` from login rows grouped by user, then filter and group those one-row-per-user results. This eliminates the need for outer `DISTINCT` and aligns directly with $O(U)$ intermediate state.
- **Correlated minimum:** Test each login against the minimum for its user. It is correct with proper indexing but usually less clear than a grouped or window calculation.
- **Filter date before minimum:** Incorrect because it can hide an older first login and count an existing user as new.
- **Duplicate login rows:** Window output repeats them, but `COUNT(DISTINCT user_id)` prevents inflated counts.
- **Several later logins:** They carry the same first date and still count the user once.
- **No login activity:** A user with only other activity is absent from the CTE and is not counted.
- **April 1, 2019:** Difference is exactly 90, so it qualifies.
- **March 31, 2019:** Difference is 91, so it is excluded.
- **June 30, 2019:** Difference is zero, so it qualifies.
- **Future first login:** The exact query incorrectly admits it unless the source guarantees no future dates; adding a nonnegative condition fixes this.
- **Dates with zero users:** SQL grouping emits no synthetic rows, matching the requirement to omit them.
- **Any result order:** The missing `ORDER BY` is intentional and valid.
