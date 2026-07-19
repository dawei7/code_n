# Create a Session Bar Chart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1435 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/create-a-session-bar-chart/) |

## Problem Description

### Goal

The `Sessions` table stores the duration of each session in seconds. Build a four-row bar-chart summary that counts sessions lasting less than 5 minutes, from 5 minutes through less than 10 minutes, from 10 minutes through less than 15 minutes, and at least 15 minutes.

Return every prescribed bin even when its count is zero. The output labels must be exactly `[0-5>`, `[5-10>`, `[10-15>`, and `15 or more`. The bracket notation denotes half-open minute intervals, so a duration exactly on a 5-, 10-, or 15-minute boundary belongs to the bin beginning at that boundary.

### Function Contract

**Inputs**

- `Sessions(session_id, duration)`: one row per session.
- `session_id` uniquely identifies a session.
- `duration` is the session length in seconds.

**Return value**

- A relation with columns `bin` and `total` containing exactly the four required labels and the number of sessions in each interval.

### Examples

**Example 1**

- Input: `Sessions = [(1,30),(2,199),(3,299),(4,580),(5,1000)]`
- Output: `[("[0-5>",3),("[5-10>",1),("[10-15>",0),("15 or more",1)]`

**Example 2**

- Input: `Sessions = [(1,299),(2,300),(3,599),(4,600),(5,899),(6,900)]`
- Output: `[("[0-5>",1),("[5-10>",2),("[10-15>",2),("15 or more",1)]`

**Example 3**

- Input: `Sessions = [(1,42),(2,120)]`
- Output: `[("[0-5>",2),("[5-10>",0),("[10-15>",0),("15 or more",0)]`
