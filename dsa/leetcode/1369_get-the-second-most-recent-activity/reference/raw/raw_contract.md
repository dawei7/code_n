## Function Contract

**Input**

- `UserActivity`: the possibly duplicate activity-history rows described above.

Let $A$ be the number of stored rows and $U$ the number of distinct users.

**Return value**

Return one row per user with these columns:

- `username`: the activity owner.
- `activity`: the selected activity name.
- `startDate`: the selected period's start date.
- `endDate`: the selected period's end date.

For a user with at least two distinct activity periods, select the second period in descending chronological order. For a user with one distinct period, select that period. Identical stored rows describe one logical period, and the result order is unrestricted.
