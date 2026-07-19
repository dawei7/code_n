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
