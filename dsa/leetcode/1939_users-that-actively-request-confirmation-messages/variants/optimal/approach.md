## General
**Order requests within each user**

Partition `Confirmations` by `user_id` and sort each partition by
`time_stamp`. Use `LAG` to attach the immediately preceding request time to
every row.

**Why adjacent requests are sufficient**

If any two requests for one user lie within 24 hours, every chronological
request between them splits that interval into smaller non-negative gaps.
At least one adjacent pair is therefore also within 24 hours. Conversely, an
adjacent qualifying pair is directly a valid pair. Testing consecutive
requests loses no eligible user and avoids generating every pair.

**Filter the inclusive boundary**

Keep rows whose current time is no later than 24 hours after `previous_time`.
The comparison is inclusive, so exactly 24 hours qualifies. Rows without a
previous request cannot establish a pair. Finally select distinct user IDs,
because one user may have several qualifying adjacent pairs. The `action`
column is intentionally unused.

## Complexity detail
Ordering the $C$ confirmation rows by user and timestamp takes
$O(C\log C)$ worst-case time, after which the window calculation and filter
are linear. The sort and window result may require $O(C)$ working space.
A database can improve the sort cost when an index already provides the
required `(user_id, time_stamp)` order.

## Alternatives and edge cases
- **Self-join every request pair:** Match rows of the same user and compare
  timestamps directly. This is correct but can generate $O(C^2)$ candidate
  pairs.
- **Compare only each user's earliest and latest request:** This is incorrect;
  those endpoints may be far apart while two middle requests are close.
- Exactly 24 hours is inside the window, while 24 hours and one second is not.
- A single request never qualifies its user.
- Confirmation and timeout actions are treated identically.
- Users with several qualifying pairs appear only once.
- Request rows need not arrive in chronological storage order because the
  window explicitly orders them.
- Requests from different users can never form a qualifying pair.
