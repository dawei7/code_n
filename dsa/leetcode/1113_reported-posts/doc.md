# Reported Posts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1113 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/reported-posts/) |

## Problem Description

### Goal

The `Actions` table records user activity on social-media posts. An action can be `view`, `like`, `reaction`, `comment`, `report`, or `share`. For a `report` row, `extra` contains the reason supplied for the report; for other action types it may be null.

For `2019-07-04`, find how many distinct posts were reported for each report reason. Several users may report the same post for the same reason, but that post contributes only once to that reason's count. Return `report_reason` and `report_count`; result order is unrestricted.

### Function Contract

**Inputs**

- `Actions(user_id, post_id, action_date, action, extra)`: $R$ user-action rows; `extra` stores the reason when `action = 'report'`.

**Return value**

- One row for every report reason present on `2019-07-04`.
- `report_reason` is the reason from `extra`, and `report_count` is the number of distinct reported `post_id` values for that reason.
- The local reference orders reasons ascending for deterministic validation.

### Examples

**Example 1**

`Actions`

| user_id | post_id | action_date | action | extra |
|---:|---:|---|---|---|
| 2 | 4 | 2019-07-04 | view | null |
| 2 | 4 | 2019-07-04 | report | spam |
| 3 | 4 | 2019-07-04 | report | spam |
| 4 | 3 | 2019-07-02 | report | spam |
| 5 | 2 | 2019-07-04 | report | racism |
| 5 | 5 | 2019-07-04 | report | racism |

Output:

| report_reason | report_count |
|---|---:|
| racism | 2 |
| spam | 1 |

Post `4` is counted once for `spam` despite two reporters. The earlier report of post `3` is outside the requested date.
