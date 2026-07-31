# Viewers Turned Streamers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2995 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/viewers-turned-streamers/) |

## Problem Description
### Goal
The `Sessions` table records each uniquely identified session's user, start and
end times, and type, which is either `Viewer` or `Streamer`.

For each user whose chronologically first session was as a Viewer, count all of
that user's Streamer sessions. Return only users with at least one streaming
session. Sort by `sessions_count` descending and then by `user_id` descending.

Determine the first session independently for each user from the session start
time. Viewer sessions after that first event do not contribute to the count;
only sessions whose type is `Streamer` are counted.

### Function Contract
**Inputs**

- `Sessions(user_id, session_start, session_end, session_id, session_type)`: uniquely identified viewing or streaming sessions

Let $R$ be the number of session rows.

**Return value**

Return qualifying `user_id` values with their Streamer-session counts in the
required descending order.

### Examples
**Example 1**

- Input: User `101` first views and later streams twice; other users either stream first or never stream.
- Output: `(101,2)`

**Example 2**

- Input: A user begins as Viewer but has no Streamer session.
- Output: No row for that user.

**Example 3**

- Input: Two qualifying users with equal counts.
- Output: The larger user ID appears first.
