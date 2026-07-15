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

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Restrict events before counting.** Filter `activity_date` to the inclusive interval from `2019-06-28` through `2019-07-27`. A session represented only by rows outside that interval must not enter any user's count.

**Establish one count per active user.** Group the retained rows by `user_id` and calculate `COUNT(DISTINCT session_id)` for each group. Distinct counting neutralizes duplicate rows and multiple event types within a session. The source guarantee that a session belongs to exactly one user keeps these groups unambiguous.

**Average the user-level results.** Apply `AVG` to the per-user session counts in an outer query and round the final value to two decimal places. `COALESCE` or `IFNULL` converts the `NULL` average of an empty subquery into `0`. Averaging after grouping gives every active user equal weight rather than weighting users by their number of event rows.

#### Complexity detail

Filtering scans up to $R$ rows, while grouping and distinct-session counting can sort or hash the qualifying rows. A conservative logical bound is $O(R\log R)$ time and $O(R)$ grouping space. Indexes and hash aggregation may improve the physical execution plan.

#### Alternatives and edge cases

- **Global distinct-session ratio:** Because each session belongs to one user, dividing the number of distinct qualifying sessions by the number of distinct qualifying users is equivalent, but the grouped form exposes the requested per-user grain.
- **Same-user self-join:** Joining qualifying activity rows to one another by user before deduplication remains correct but can generate $O(R^2)$ pairs for a heavily active user.
- **Duplicate session events:** Repeated rows and different activity types for one session count only once.
- **Sessions spanning dates:** A session qualifies when it has at least one event inside the window; outside events do not create another session.
- **Inactive users:** Users without a qualifying event are absent from the average.
- **Empty window:** Return `0`, not `NULL` and not an absent row.

</details>
