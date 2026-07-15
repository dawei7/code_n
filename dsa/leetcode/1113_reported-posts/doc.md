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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Select only reports from the target day:** Filter with both `action_date = '2019-07-04'` and `action = 'report'`. A view on the target day and a report on another day must not affect the result.

**Group by the stored reason:** For report rows, `extra` is the semantic reason, so group by that column and expose it as `report_reason`.

**Count posts rather than report rows:** Apply `COUNT(DISTINCT post_id)` within each reason group. This deduplicates multiple users reporting the same post for the same reason while still counting different posts separately. Each output group therefore contains exactly the target-day report rows for one reason, and its distinct count is precisely the requested number.

#### Complexity detail

Without indexes or engine-specific assumptions, filtering and sort-based grouping of $R$ rows costs $O(R \log R)$ time and up to $O(R)$ execution space. Hash grouping can provide expected $O(R)$ time, while an index on the filter and grouping columns may change the physical plan.

#### Alternatives and edge cases

- **Pre-deduplicate reason-post pairs:** Select distinct `extra, post_id`, then group and count. It is correct and makes the two aggregation stages explicit.
- **Correlated distinct count:** Compute the count for each qualifying outer row and deduplicate afterward. It returns the same values but can rescan all $R$ rows repeatedly and take $O(R^2)$ time.
- **`COUNT(*)`:** It overcounts when several users report the same post for one reason.
- **Non-report activity:** Its `extra` value is irrelevant and the row must be filtered out.
- **Reports on other dates:** They do not contribute even if their reasons match target-day reports.
- **Same post, same reason, many users:** It contributes one distinct post.
- **Same post, different reasons:** It contributes once to each separate reason group.
- **No target-day reports:** The query returns no rows.

</details>
