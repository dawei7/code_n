# Second Day Verification

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3172 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/second-day-verification/) |

## Problem Description

### Goal

The `emails` table records an email identifier, its user, and the datetime when that user signed up. The `texts` table records messages associated with email identifiers, whether each message reports a verified or unverified signup, and the datetime of that action.

Find the users who have a `Verified` text whose action date is the calendar day immediately after the corresponding signup date. A user should appear only once even if several qualifying records exist.

Return the qualifying `user_id` values in ascending order.

### Function Contract

**Input tables**

- `emails(email_id, user_id, signup_date)`: Signup records. The composite primary key is `(email_id, user_id)`.
- `texts(text_id, email_id, signup_action, action_date)`: Text actions. The composite primary key is `(text_id, email_id)`, and `signup_action` is either `Verified` or `Not Verified`.

**Return value**

- An ordered table with one column, `user_id`, containing each qualifying user once and sorted in ascending order.

Let $e$ and $t$ denote the numbers of rows in `emails` and `texts`, and let $r = e + t$.

### Examples

#### Example 1

Input `emails`:

| email_id | user_id | signup_date |
|---:|---:|---|
| 125 | 7771 | `2022-06-14 09:30:00` |
| 433 | 1052 | `2022-07-09 08:15:00` |
| 234 | 7005 | `2022-08-20 10:00:00` |

Input `texts`:

| text_id | email_id | signup_action | action_date |
|---:|---:|---|---|
| 1 | 125 | `Verified` | `2022-06-15 08:30:00` |
| 2 | 433 | `Not Verified` | `2022-07-10 10:45:00` |
| 4 | 234 | `Verified` | `2022-08-21 09:30:00` |

- **Output:** 

| user_id |
|---:|
| 7005 |
| 7771 |

Users `7005` and `7771` have verified actions on the calendar day following signup. User `1052` does not qualify because the action is `Not Verified`.
