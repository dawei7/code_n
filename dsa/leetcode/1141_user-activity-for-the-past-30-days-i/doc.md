# User Activity for the Past 30 Days I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1141 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) |

## Problem Description

### Goal

The `Activity` table records events on a social-media website and may contain duplicate rows. Each session belongs to exactly one user. Every recorded `activity_type`—`open_session`, `end_session`, `scroll_down`, or `send_message`—qualifies as activity.

For the 30-day period ending on `2019-07-27`, inclusive, report the number of distinct active users on each date. A user is active on a date after performing at least one activity that day, regardless of the number of sessions or events. Include only dates having at least one active user, and return the rows in any order.

### Function Contract

**Input table**

- `Activity(user_id, session_id, activity_date, activity_type)`: activity events; no primary key is defined and duplicate rows may occur.

Let $R$ be the number of rows in `Activity`.

**Return value**

A table with columns `day` and `active_users`, containing one row per qualifying date from `2019-06-28` through `2019-07-27`, where `active_users` is the number of distinct users active that day. Dates with zero activity are absent.

### Examples

**Example 1**

On `2019-07-20`, user `1` performs several activities and user `2` opens a session, so there are two distinct active users. On `2019-07-21`, users `2` and `3` perform activities, again producing two:

| day | active_users |
|---|---:|
| 2019-07-20 | 2 |
| 2019-07-21 | 2 |

Rows dated before `2019-06-28`, including `2019-06-25`, do not participate.
