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

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Filter the exact inclusive window.** Keep rows whose `activity_date` is between `2019-06-28` and `2019-07-27`. The lower endpoint is 29 days before the ending date, so the inclusive interval contains exactly 30 calendar dates. Filtering both endpoints also prevents later activity from entering the result.

**Group at the required reporting grain.** Group the retained rows by `activity_date` and expose that value as `day`. Because only dates represented by input rows form groups, dates with no active user are omitted automatically.

**Deduplicate users within each date.** Apply `COUNT(DISTINCT user_id)` inside every date group and name it `active_users`. This collapses duplicate rows, multiple activity types, and multiple sessions belonging to the same user on the same date. The same user may still contribute once on each of several dates, which matches daily activity semantics.

#### Complexity detail

The logical query scans $R$ rows and groups the qualifying subset by date while maintaining distinct users. A conservative sort-based bound is $O(R\log R)$ time and $O(R)$ grouping space. A database engine may use hashing or suitable indexes for a lower physical cost, but the result semantics do not depend on its chosen plan.

#### Alternatives and edge cases

- **Pre-deduplicated subquery:** Select distinct `(activity_date, user_id)` pairs first and then use `COUNT(*)`; this is equivalent and makes the counting unit explicit.
- **Same-day self-join:** Joining the activity table to itself by date before counting distinct users remains correct, but can materialize $O(R^2)$ row pairs for a busy day.
- **Duplicate events:** Repeated identical rows count the user only once for that date.
- **Multiple sessions or types:** They establish activity but do not increase a user's daily contribution beyond one.
- **Window endpoints:** Both `2019-06-28` and `2019-07-27` are included; adjacent dates outside that interval are excluded.
- **Inactive dates:** Do not synthesize rows with a zero count.

</details>
