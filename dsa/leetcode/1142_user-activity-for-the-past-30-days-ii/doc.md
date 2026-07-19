# User Activity for the Past 30 Days II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1142 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) |

## Problem Description

### Goal

The `Activity` table records events on a social-media website, may contain duplicate rows, and guarantees that each session belongs to exactly one user. Several events can therefore describe the same session without representing additional sessions.

For the 30-day period ending on `2019-07-27`, inclusive, count the distinct sessions belonging to each user who was active in that window. Return the average of those per-user session counts rounded to two decimal places. Activity outside the window does not contribute; when the window has no active user, report `0`.

### Function Contract

**Input table**

- `Activity(user_id, session_id, activity_date, activity_type)`: activity events with possible duplicate rows; `activity_type` is one of `open_session`, `end_session`, `scroll_down`, or `send_message`.

Let $R$ be the number of rows in `Activity`.

**Return value**

A one-row, one-column table named `average_sessions_per_user`, containing the average number of distinct qualifying sessions per active user, rounded to two decimal places, or `0` when no row falls in the window from `2019-06-28` through `2019-07-27`.

### Examples

**Example 1**

Suppose users `1` and `2` each have one distinct session in the window and user `3` has two. The per-user counts are `1`, `1`, and `2`, so the result is:

| average_sessions_per_user |
|---:|
| 1.33 |

Multiple activity events from the same session do not increase its user's session count.
