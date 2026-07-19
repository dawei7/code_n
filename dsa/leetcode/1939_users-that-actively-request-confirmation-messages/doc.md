# Users That Actively Request Confirmation Messages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1939 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/users-that-actively-request-confirmation-messages/) |

## Problem Description
### Goal
The `Signups` table records registered users. The `Confirmations` table records
each confirmation-message request, including its user, request timestamp, and
whether the request was confirmed or timed out.

Find every user who made at least two confirmation requests no more than 24
hours apart. A separation of exactly 24 hours qualifies. The request actions
do not affect eligibility; only timestamps belonging to the same user matter.
Return the qualifying user IDs in any order.

### Function Contract
**Inputs**

- `Signups(user_id, time_stamp)`: one row per user, with unique `user_id`.
- `Confirmations(user_id, time_stamp, action)`: request rows whose composite
  key is `(user_id, time_stamp)`. `user_id` references `Signups`, and `action`
  is either `"confirmed"` or `"timeout"`.

Let $C$ be the number of `Confirmations` rows.

**Return value**

- A one-column table named `user_id` containing each user who has some pair of
  confirmation requests separated by at most 24 hours.
- Emit each qualifying user once. Row order is unrestricted.

### Examples
**Example 1**

Requests for users `2`, `3`, and `6` contain pairs separated by exactly 24
hours, 6 minutes 59 seconds, and 23 hours 59 minutes 59 seconds respectively.
User `7` has two requests 24 hours and one second apart.

- Output: users `2`, `3`, and `6`.

**Example 2**

- A user's two requests occur exactly 24 hours apart.
- Output: that user.

**Example 3**

- A user has only one request.
- Output: no rows.
