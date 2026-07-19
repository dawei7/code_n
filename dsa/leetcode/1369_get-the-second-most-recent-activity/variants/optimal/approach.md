## General
**Annotate every user's timeline.** In a common table expression, use `ROW_NUMBER()` partitioned by `username` and ordered by `startDate DESC`. Rank one is most recent and rank two is second most recent. In the same partition, `COUNT(*)` records whether a fallback is necessary.

**Apply the two selection rules.** Retain rank two for partitions containing at least two activities. For a one-row partition, retain rank one. The conditions can be written together as `activity_rank = 2 OR activity_count = 1`.

Nonoverlapping periods make descending start dates the chronological activity order. Row numbering assigns exactly one second row to every multi-activity user, while the partition count identifies exactly the single-row users. Thus the filter returns one and only one contractually correct row per user.

## Complexity detail
Partitioning and ordering the activity rows takes $O(A\log A)$ time in the general comparison-based database model. Window state and sorted partitions use $O(A)$ working space. An indexed engine may improve constants or exploit existing order.

## Alternatives and edge cases
- **Correlated later-row counts:** For each activity, count how many rows of the same user start later and retain count one, with a special single-row case. This is correct but can take $O(A^2)$ time without indexes.
- **Aggregate maximum twice:** Find each user's latest date, exclude it, and aggregate again. This works but needs a separate fallback for users with one row and additional joins to recover complete rows.
- **Only one activity:** Select rank one rather than returning no row.
- **Exactly two activities:** Rank two is the older activity.
- **Input row order:** Chronology comes from the dates, not physical table order.
- **Several users:** Window partitions prevent one user's dates from affecting another's rank.
- **Source columns:** Return the activity and dates from the same selected row; do not combine independent aggregates.
