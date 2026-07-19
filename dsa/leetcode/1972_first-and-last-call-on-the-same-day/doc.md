# First and Last Call On the Same Day

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1972 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/first-and-last-call-on-the-same-day/) |

## Problem Description
### Goal
The `Calls` table records phone calls with a caller, a recipient, and a
timestamp. For every user and calendar day on which that user participated in
at least one call, consider the other person in the user's chronologically
first call and the other person in the user's chronologically last call.

Report each user who has at least one day where those two people are the same.
A call counts for both participants regardless of which one is stored as the
caller. Return each qualifying user ID once, in any order.

### Function Contract
**Inputs**

- `Calls(caller_id, recipient_id, call_time)`: $R$ call rows.
- `(caller_id, recipient_id, call_time)` is the composite primary key.
- `call_time` is a datetime value whose date determines the calendar-day
  partition and whose full value determines chronological order.

**Return value**

- A one-column table named `user_id`.
- Include a user when their first and last calls match the same other person
  on at least one calendar day.
- Return no duplicate user IDs; row order is unrestricted.

### Examples
**Example 1**

For the public sample, users 8 and 4 call each other first and last on
2021-08-24, while users 5 and 1 have one call with each other on 2021-08-11.

- Output rows: `(1)`, `(4)`, `(5)`, and `(8)`.

**Example 2**

User 1 calls user 2 once on a day.

- Output rows: `(1)` and `(2)`.

**Example 3**

User 1 first calls user 2 and later calls user 3 on the same day.

- Output rows: `(2)` and `(3)`; user 1 does not qualify from that day.

### Required Complexity
- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Normalization creates $2R$ rows. Sorting them for the two per-user/day window
orders takes $O(R\log R)$ time in the general case; the window evaluation and
final filtering are linear after ordering. The normalized relation, window
state, sorting workspace, and result may use $O(R)$ space. A database optimizer
may exploit suitable indexes without changing these asymptotic upper bounds.

#### Alternatives and edge cases

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

</details>
