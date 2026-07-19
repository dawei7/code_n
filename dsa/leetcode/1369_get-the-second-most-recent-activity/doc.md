# Get the Second Most Recent Activity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1369 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/get-the-second-most-recent-activity/) |

## Problem Description

### Goal

The `UserActivity` table records named activities performed by users, together with each activity's start and end dates. A user's recorded activity periods do not overlap, so their chronological order is unambiguous.

For every user, return the second most recent activity. If that user has only one recorded activity, return the single activity instead. Preserve the activity name and both dates from the selected source row, producing one result row per user.

### Function Contract

**Inputs**

- `UserActivity(username, activity, startDate, endDate)`.
- Let $A$ be the number of activity rows.

**Return value**

- Columns `username`, `activity`, `startDate`, and `endDate`.
- For each user with multiple rows, the second row in descending chronological order.
- For each user with one row, that sole activity.

### Examples

**Example 1**

- Alice has January, February, and March activities.
- Output Alice's February activity, the second most recent.

**Example 2**

- Bob has only one activity.
- Output Bob's existing row unchanged.

**Example 3**

- A user with exactly two activities receives the older one, because it is second when ordered newest-first.
