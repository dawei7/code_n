# Confirmation Rate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1934 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/confirmation-rate/) |

## Problem Description
### Goal
The `Signups` table contains one row for every registered user. The
`Confirmations` table records confirmation-message requests: each row belongs
to a signed-up user and has action `"confirmed"` when the request succeeded or
`"timeout"` when it expired.

For every user in `Signups`, compute the number of confirmed requests divided
by that user's total number of confirmation requests. A user with no requests
has rate zero. Round every rate to two decimal places and return one result row
per signed-up user in any order.

### Function Contract
**Inputs**

- `Signups(user_id, time_stamp)`: `user_id` is unique and `time_stamp` records
  when that user signed up.
- `Confirmations(user_id, time_stamp, action)`: `(user_id, time_stamp)` is
  unique, `user_id` references `Signups`, and `action` is either
  `"confirmed"` or `"timeout"`.

Let $S$ be the number of `Signups` rows and $C$ the number of
`Confirmations` rows.

**Return value**

- A table with columns `user_id` and `confirmation_rate`, containing every
  signed-up user exactly once.
- `confirmation_rate` is the user's confirmed-request count divided by total
  requests, rounded to two decimal places, or `0` when the user has no
  requests. Row order is unrestricted.

### Examples
**Example 1**

Given signup users `3`, `7`, `2`, and `6`, with two timeouts for user `3`,
three confirmations for user `7`, one confirmation and one timeout for user
`2`, and no requests for user `6`, the result is:

| user_id | confirmation_rate |
|---:|---:|
| 3 | 0.00 |
| 7 | 1.00 |
| 2 | 0.50 |
| 6 | 0.00 |

**Example 2**

- One user has one confirmed request.
- Output: that user's confirmation rate is `1.00`.

**Example 3**

- Two users have no confirmation rows.
- Output: both users appear with confirmation rate `0.00`.

### Required Complexity
- **Time:** $O(S+C)$
- **Space:** $O(S+C)$

<details>
<summary>Approach</summary>

#### General

**Preserve users without requests**

Start from `Signups` and left join `Confirmations` on `user_id`. An inner join
would remove users who never requested a confirmation, even though the result
must include them with rate zero.

**Turn actions into numeric contributions**

For joined confirmation rows, map `"confirmed"` to `1.0` and `"timeout"` to
`0.0`. The average of these values is precisely confirmed requests divided by
all requests. Leave the synthetic null row from an unmatched left join as
`NULL`, so it does not masquerade as a real request.

**Aggregate and round**

Group by the signup user's ID. `AVG` returns `NULL` for a group with no actual
actions, so replace that result with zero, then round to two decimal places.
Every signup row enters exactly one group, each real request contributes once,
and the conditional values have the same numerator and denominator as the
required rate.

#### Complexity detail

With an indexed or hash equality join, reading the two tables and associating
confirmation rows with users takes $O(S+C)$ expected time. Grouping retains
one aggregate state per user. Join indexes, hash state, and grouping state use
at most $O(S+C)$ space; a database may use less when suitable persistent
indexes already exist.

#### Alternatives and edge cases

- **Correlated aggregate per signup:** A scalar subquery can compute the right
  result, but without a supporting index it may rescan all $C$ confirmation
  rows for each of $S$ users and take $O(SC)$ time.
- **Inner join:** This incorrectly omits users with no requests.
- **Count only confirmed rows after filtering:** Filtering before aggregation
  loses timeout rows from the denominator and can also remove zero-rate users.
- A user with no confirmation requests must still appear with rate zero.
- A user with only timeouts has rate zero, while a user with only confirmations
  has rate one.
- Mixed outcomes use every request in the denominator and are rounded, not
  truncated, to two decimal places.
- Signup and confirmation timestamps identify rows but do not affect the rate.

</details>
