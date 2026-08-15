# Analyze Subscription Conversion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3497 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/analyze-subscription-conversion/) |

## Problem Description

### Goal

The `UserActivity` table records how many minutes each user spent on the service on a particular date and labels that day as `free_trial`, `paid`, or `cancelled`. The service wants to analyze only users who have activity in both the free-trial stage and the paid-subscription stage; a user who never records either one of those stages has not converted for this report.

For every converted user, calculate the average daily activity duration across that user's `free_trial` rows and separately across their `paid` rows. Round both averages to two decimal places. Ignore cancelled rows when computing either average, return one row per qualifying user, and order the result by `user_id` in ascending order.

### Function Contract

**Inputs**

- `UserActivity(user_id, activity_date, activity_type, activity_duration)`: One row per unique combination of user, date, and activity type. `activity_type` is one of `free_trial`, `paid`, or `cancelled`, and `activity_duration` is the number of minutes recorded that day.

**Return value**

Return columns `user_id`, `trial_avg_duration`, and `paid_avg_duration`, ordered by increasing `user_id`. Include only users with at least one free-trial row and at least one paid row.

### Examples

#### Example 1

- **Input:** User 1 has free-trial durations `45`, `30`, and `60`, followed by paid durations `75`, `90`, and `65`. User 2 has free-trial and cancelled activity but no paid row.
- **Output:** User 1 appears with `trial_avg_duration = 45.00` and `paid_avg_duration = 76.67`; user 2 is excluded.

#### Example 2

- **Input:** A user has free-trial durations `40` and `35`, one paid duration `45`, and a later cancelled row.
- **Output:** The user appears with `trial_avg_duration = 37.50` and `paid_avg_duration = 45.00`; cancellation does not remove a prior conversion or affect either average.
