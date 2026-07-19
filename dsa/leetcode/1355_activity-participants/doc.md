# Activity Participants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1355 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/activity-participants/) |

## Problem Description

### Goal

The `Activities` table lists the available activities, each with an ID and unique name. Every row in `Friends` identifies a friend and records the activity that friend participates in. An activity's participant count is the number of friend rows naming it.

Return the names of all activities whose participant count is neither the maximum nor the minimum among the listed activities. Activities tied at either extreme are excluded. The result may be returned in any order.

### Function Contract

**Inputs**

- `Activities(id, name)`: the catalog of activities.
- `Friends(id, name, activity)`: friends and the activity name chosen by each friend.
- Let $A$ and $F$ be the table row counts, and let $N = A + F$.

**Return value**

- Return one column named `activity` containing every activity whose participant count is strictly between the global minimum and maximum counts.

### Examples

**Example 1**

- Participant counts: Eating has `3`, Singing has `2`, and Horse Riding has `1`.
- Output: `Singing`.

**Example 2**

- Participant counts: A has `1`, B has `1`, and C has `1`.
- Output: no rows, because every activity is tied for both extremes.

**Example 3**

- Participant counts: A has `0`, B has `2`, C has `3`, and D has `3`.
- Output: `B`.
