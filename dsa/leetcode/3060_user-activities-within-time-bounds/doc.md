# User Activities within Time Bounds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3060 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/user-activities-within-time-bounds/) |

## Problem Description

### Goal

Each session belongs to a user and is classified as either `Viewer` or
`Streamer`. A user qualifies when two distinct sessions of the same type are
close enough in time; sessions of different types cannot form a qualifying
pair.

Find every user for whom a later session starts no more than twelve hours after
an earlier same-type session ends. The two sessions need not be adjacent in the
table or in the user's complete mixed-type history. The twelve-hour boundary
is inclusive. Return each qualifying user once, ordered by `user_id` ascending.

### Function Contract

**Inputs**

- `Sessions(user_id, session_start, session_end, session_id, session_type)`:
  `session_id` is unique, and `session_type` is either `Viewer` or `Streamer`.

Let $n$ be the number of session rows and $u$ the number of qualifying users.

**Return value**

- An ordered one-column table of distinct `user_id` values having a qualifying
  same-type session pair.

### Examples

**Example 1**

User `102` has two `Viewer` sessions separated by one hour. User `103` has two
`Viewer` sessions separated by ten hours. User `101` has no same-type pair
within twelve hours, so the result is `102`, then `103`.

**Example 2**

If one session ends at midnight and a later same-type session starts exactly at
noon, their twelve-hour gap qualifies.

**Example 3**

Two nearby sessions with different types do not qualify a user, because the
type must match as well as the time bound.
