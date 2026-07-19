# Ad-Free Sessions

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/ad-free-sessions/) |
| Frontend ID | 1809 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Playback` table records viewing sessions. Each `session_id` is unique, and every row identifies the customer plus the session's `start_time` and `end_time`. A session includes both endpoints of this interval. Sessions belonging to the same customer never overlap.

The `Ads` table records individual advertisements, including the customer who saw each ad and its `timestamp`. Report every playback session during which its customer saw no ad. An ad affects a session only when both the customer identifiers match and the timestamp lies within that session's inclusive interval. Return the qualifying `session_id` values in any order.

### Function Contract

**Inputs**

- `Playback(session_id, customer_id, start_time, end_time)`: one row per session. `session_id` is unique, `start_time <= end_time`, and sessions of one customer do not intersect.
- `Ads(ad_id, customer_id, timestamp)`: one row per shown ad. `ad_id` is unique.
- Let $P$ be the number of playback rows and $A$ the number of ad rows.

**Return value**

- Return one column named `session_id`.
- Include a session exactly when no row in `Ads` has the same `customer_id` and a `timestamp` from `start_time` through `end_time`, inclusive.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: sessions `(1,1,1,5)`, `(2,1,15,23)`, `(3,2,10,12)`, `(4,2,17,28)`, `(5,2,2,8)`; ads `(1,1,5)`, `(2,2,15)`, `(3,2,20)`
- Output: `[[2],[3],[5]]`

The ad at time `5` belongs to session `1`, and the ad at time `20` belongs to session `4`. The remaining sessions are ad-free.

**Example 2**

- Input: `Playback = [[7,3,10,20]]`, `Ads = [[1,3,10]]`
- Output: `[]`

An ad at the inclusive start boundary makes the session ineligible.

**Example 3**

- Input: `Playback = [[8,4,10,20]]`, `Ads = [[1,9,15]]`
- Output: `[[8]]`

An ad at the right time but for a different customer does not affect the session.
