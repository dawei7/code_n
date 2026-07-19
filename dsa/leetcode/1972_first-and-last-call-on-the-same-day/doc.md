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
