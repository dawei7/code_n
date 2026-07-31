## Function Contract

**Inputs**

- `activity`: The activity table described above.

Let $R$ denote the number of rows in `activity`. A calendar date is eligible for a user's streak only when exactly one table row exists for that (`user_id`, `action_date`) pair. A date with two or more distinct actions is ineligible and separates runs on either side of it.

Consecutive means adjacent calendar dates, not merely adjacent records after sorting. A change in `action`, a missing date, or an ineligible multi-action date ends the current run.

**Return value**

Return an ordered table with columns:

- `user_id`
- `action`
- `streak_length`
- `start_date`
- `end_date`

Only users whose selected maximum run has length at least five appear. The primary order is `streak_length` descending and the secondary order is `user_id` ascending.
