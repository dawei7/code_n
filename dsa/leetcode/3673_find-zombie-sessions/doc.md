# Find Zombie Sessions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3673 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-zombie-sessions/) |

## Problem Description

### Goal

The `app_events` table records actions performed during application sessions. Every row belongs to a user and a session, has a timestamp and event type, and may carry a value for a purchase or scroll. Use the complete event history of each session to find users who appear active for a long time but exhibit the abnormal pattern of a zombie session.

A session is a zombie session only when all four conditions hold: its last event occurs more than 30 minutes after its first event; it contains at least five `scroll` events; the number of `click` events divided by the number of `scroll` events is strictly less than $0.20$; and it contains no `purchase` event. The strict comparisons matter: a 30-minute duration or a click-to-scroll ratio exactly equal to $0.20$ does not qualify.

For every qualifying session, report its identifier, user, duration in whole minutes, and scroll count. Order the result by `scroll_count` in descending order, breaking ties by `session_id` in ascending order.

### Function Contract

**Inputs**

- `app_events`: rows with a unique `event_id`, `user_id`, `event_timestamp`, `event_type`, `session_id`, and nullable `event_value`.

The permitted event types are `app_open`, `click`, `scroll`, `purchase`, and `app_close`. A purchase value is an amount in dollars, a scroll value is a pixel count, and values on the other event types are `NULL`; event values do not affect the zombie criteria. Let $N$ be the number of event rows and $S$ the number of distinct `(session_id, user_id)` groups.

**Return value**

Return an ordered table with columns `session_id`, `user_id`, `session_duration_minutes`, and `scroll_count`. Include exactly the session groups satisfying every zombie-session condition.

### Examples

#### Example 1

A session running from `10:00` through `10:35`, with six scrolls, no clicks, and no purchases, is returned with duration `35` and scroll count `6`.

#### Example 2

A 60-minute session with five scrolls and one click is excluded: its click-to-scroll ratio is exactly $1/5=0.20$, while the required bound is strict.

#### Example 3

A long session with many scrolls is still excluded when even one event is a purchase, because all four conditions must hold simultaneously.
