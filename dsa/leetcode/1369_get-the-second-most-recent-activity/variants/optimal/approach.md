## General

**Normalize duplicate storage rows first.** `UserActivity` may contain exact duplicates, but a repeated copy carries the same username, activity, and period and cannot represent another simultaneous activity under the nonoverlap guarantee. The `activities` CTE uses `DISTINCT` across all four source columns so one logical period advances recency exactly once.

**Annotate every user's logical timeline.** Over the normalized rows, `ROW_NUMBER()` partitions by `username` and orders `startDate` descending. Rank one is the most recent period and rank two is the second most recent. A partition `COUNT(*)` simultaneously identifies users who need the one-activity fallback.

**Apply the two selection rules.** Keep rank two for every user with multiple logical periods; for a one-period user, keep rank one through `activity_count = 1`. Nonoverlap makes descending start dates an unambiguous chronological order after duplicate normalization. The rank and count conditions are mutually appropriate to the two partition sizes, so exactly one correct source row survives per user. The contract permits any output order, so no final sort is required.

## Complexity detail

Let $A$ be the number of stored rows. Deduplicating, partitioning, and ordering take $O(A\log A)$ time in the general comparison-based database model. The normalized relation, window partitions, and sort state require $O(A)$ working space. Indexes or hash-based duplicate elimination may improve constants or individual stages.

## Alternatives and edge cases

- **Rank raw storage rows:** This is shorter, but duplicate copies of the newest activity can occupy ranks one and two and incorrectly displace the preceding logical period.
- **Correlated later-period counts:** Counting newer distinct periods for each row is correct with a deduplication layer, but can take $O(A^2)$ time without indexes.
- **Aggregate maximum twice:** Excluding each user's latest period and taking another maximum works, but requires extra joins to recover the complete selected row and a separate one-period fallback.
- **Only one activity:** Return the normalized rank-one row rather than no row.
- **Exactly two activities:** Rank two is the older period.
- **Duplicate rows:** Exact copies collapse to one logical activity; duplicates must not alter the selected chronology.
- **Input and output order:** Physical input order is irrelevant, and the result order is unrestricted.
- **Several users:** Window partitions prevent one user's dates from affecting another user's ranks.
- **Source-row integrity:** Return the activity and both dates from the same ranked row; do not combine independent aggregates.
