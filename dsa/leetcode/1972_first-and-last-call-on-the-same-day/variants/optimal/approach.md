## General
**Normalize each call from both users' perspectives**

Expand every source row into two rows with columns `user_id`, `other_id`, and
`call_time`. The caller-oriented row names the recipient as `other_id`; the
recipient-oriented row names the caller. This `UNION ALL` is necessary because
each physical call must count once for each participant, including two calls
between the same pair in opposite stored directions.

**Compare the daily chronological endpoints**

Partition the normalized rows by `user_id` and `DATE(call_time)`.
`FIRST_VALUE(other_id)` under ascending timestamp order identifies the first
person called that day, while the same window function under descending order
identifies the last person. Keep rows whose two window values are equal, then
select distinct user IDs.

Every user-day row receives the same two endpoint values for its partition.
Equality therefore selects exactly the days demanded by the contract.
`DISTINCT` collapses the several normalized rows of one qualifying day and
also collapses users who qualify on multiple days.

## Complexity detail
Normalization creates $2R$ rows. Sorting them for the two per-user/day window
orders takes $O(R\log R)$ time in the general case; the window evaluation and
final filtering are linear after ordering. The normalized relation, window
state, sorting workspace, and result may use $O(R)$ space. A database optimizer
may exploit suitable indexes without changing these asymptotic upper bounds.

## Alternatives and edge cases
- **Aggregate endpoints and join back:** Compute each user's daily minimum and
  maximum timestamps, join both endpoint rows, and compare their partners.
  This is correct but requires careful handling of both call directions.
- **Correlated ordered subqueries:** Look up the first and last partner for
  every normalized row. This is concise, but repeated partition scans can take
  $O(R^2\log R)$ time.
- A single call is both the first and last call for each participant, so both
  users qualify.
- Intermediate calls may involve anyone; only the first and last partners of
  a user-day determine qualification.
- Calls on different calendar dates belong to different partitions even when
  their timestamps are only seconds apart around midnight.
- A user needs only one qualifying day and appears once even if several days
  satisfy the condition.
